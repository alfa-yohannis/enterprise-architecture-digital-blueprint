"""Render diagram berlabel menjadi PNG dan SVG, tanpa TeX atau TikZ.

Pemakaian dari repo: python tools/render-diagrams.py
Data yang diedit: figures/chapter-diagrams.json
"""
from pathlib import Path
import argparse
import heapq
import io
import json
import math
import textwrap

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from matplotlib.font_manager import FontProperties
from PIL import Image

PALETTE = {
    'actor': ('#EEF1F6', '#50627D'),
    'service': ('#EAF2FB', '#3F6893'),
    'control': ('#E9F3EC', '#316B4B'),
    'data': ('#F1EDF8', '#786394'),
    'outcome': ('#E4F2EC', '#236C57'),
    'risk': ('#FCEDE7', '#B36947'),
}
GRID = .1
W, H = 3.26, 1.4


def coordinate(node):
    return (round(node['column'] * 44), round(-node['row'] * 27))


def obstacles(nodes):
    blocked = set()
    for node in nodes:
        x, y = coordinate(node)
        for a in range(x-17, x+18):
            for b in range(y-8, y+9):
                blocked.add((a,b))
    return blocked


def ports(node):
    x,y=coordinate(node)
    return [(x+18,y,'r'),(x-18,y,'l'),(x,y+9,'t'),(x,y-9,'b')]


def route(start, end, blocked, used, ymin):
    # Direction is part of the state so extra bends have an explicit cost.
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    first=(start[0],start[1],4)
    queue=[(0,0,first)]
    costs={first:0}
    previous={}
    last=None
    while queue:
        _,cost,state=heapq.heappop(queue)
        x,y,direction=state
        if cost != costs[state]:
            continue
        if (x,y)==end:
            last=state
            break
        for d,(dx,dy) in enumerate(directions):
            a,b=x+dx,y+dy
            if a < -25 or a > 113 or b < ymin or b > 19 or (a,b) in blocked:
                continue
            bend=0 if direction in [4,d] else 3.5
            penalty=used.get((a,b),0)*2.8
            candidate=cost+1+bend+penalty
            new=(a,b,d)
            if candidate < costs.get(new,1e9):
                costs[new]=candidate
                previous[new]=state
                heuristic=abs(a-end[0])+abs(b-end[1])
                heapq.heappush(queue,(candidate+heuristic,candidate,new))
    if last is None:
        return None,1e9
    path=[]
    while last != first:
        path.append((last[0],last[1]))
        last=previous[last]
    path.append(start)
    return path[::-1],costs[state]


def simplify(path):
    result=[path[0]]
    for a,b,c in zip(path,path[1:],path[2:]):
        if (b[0]-a[0],b[1]-a[1]) != (c[0]-b[0],c[1]-b[1]):
            result.append(b)
    result.append(path[-1])
    return result


def join_boundary(point, side):
    x,y=point
    adjustment={'r':(-.17,0),'l':(.17,0),'t':(0,-.2),'b':(0,.2)}[side]
    return (x*GRID+adjustment[0],y*GRID+adjustment[1])


def edge_routes(data):
    by_id={n['id']:n for n in data['nodes']}
    blocked=obstacles(data['nodes'])
    used={}
    ymin=-27*max(n['row'] for n in data['nodes'])-20
    results=[]
    # Short edges get direct lanes; long relations use the remaining channels.
    ordered=sorted(enumerate(data['edges']),key=lambda e:
        sum(abs(a-b) for a,b in zip(coordinate(by_id[e[1]['source']]),coordinate(by_id[e[1]['target']]))))
    for index,edge in ordered:
        start_node,end_node=by_id[edge['source']],by_id[edge['target']]
        best=None
        # Prioritize the sides that point at the destination, then let A* resolve obstacles.
        candidates=[]
        for s in ports(start_node):
            for t in ports(end_node):
                if edge.get('source_port') and s[2]!=edge['source_port']:
                    continue
                if edge.get('target_port') and t[2]!=edge['target_port']:
                    continue
                dist=abs(s[0]-t[0])+abs(s[1]-t[1])
                candidates.append((dist,s,t))
        candidates.sort(key=lambda x:x[0])
        for _,s,t in candidates[:6]:
            path,cost=route(s[:2],t[:2],blocked,used,ymin)
            if path and (best is None or cost < best[0]):
                best=(cost,path,s[2],t[2])
        if best is None:
            raise ValueError(f'No route for {edge}')
        _,path,side1,side2=best
        for point in path:
            used[point]=used.get(point,0)+1
        points=[(x*GRID,y*GRID) for x,y in simplify(path)]
        points=[join_boundary(path[0],side1)]+points+[join_boundary(path[-1],side2)]
        # Remove redundant collinear points, including the short port connectors.
        compact=[points[0]]
        for point in points[1:]:
            if len(compact)>1:
                a,b=compact[-2:]
                if abs((b[0]-a[0])*(point[1]-b[1])-(b[1]-a[1])*(point[0]-b[0]))<1e-7:
                    compact[-1]=point
                    continue
            compact.append(point)
        results.append((index,edge,compact))
    return sorted(results)


def rect_overlap(a,b):
    return max(0,min(a[2],b[2])-max(a[0],b[0]))*max(0,min(a[3],b[3])-max(a[1],b[1]))


def fit_words(text, font, renderer, max_pixels):
    lines=[]
    for word in text.split():
        if not lines or renderer.get_text_width_height_descent(lines[-1]+' '+word,font,False)[0]>max_pixels:
            lines.append(word)
        else:
            lines[-1]+=' '+word
    return '\n'.join(lines)


def place_label(points, label, occupied, nodes, all_routes, renderer, font, sx, sy):
    boxes=[]
    for node in nodes:
        x,y=coordinate(node); x*=GRID; y*=GRID
        boxes.append((x-W/2-.08,y-H/2-.08,x+W/2+.08,y+H/2+.08))
    choices=[]
    for a,b in zip(points,points[1:]):
        length=abs(b[0]-a[0])+abs(b[1]-a[1])
        horizontal=abs(b[1]-a[1])<1e-6
        if length < .35:
            continue
        max_width=max(.95,min(2.5,length-.08)) if horizontal else 2.5
        wrapped=fit_words(label,font,renderer,max_width*sx)
        lines=wrapped.splitlines()
        width=max(renderer.get_text_width_height_descent(t,font,False)[0] for t in lines)/sx+.08
        height=len(lines)*font.get_size_in_points()*renderer.dpi/72/sy*1.08+.04
        for fraction in [.5,.35,.65]:
            for offset in ([height/2+.09,-height/2-.09,0] if horizontal else [0,-.25,.25]):
                x=a[0]+fraction*(b[0]-a[0])
                y=a[1]+fraction*(b[1]-a[1])
                if horizontal:
                    y+=offset
                else:
                    x+=offset
                box=(x-width/2,y-height/2,x+width/2,y+height/2)
                score=sum(rect_overlap(box,k)*200 for k in boxes)
                score+=sum(rect_overlap(box,k)*90 for k in occupied)
                score+=max(0,-2.35-box[0])*100+max(0,box[2]-11.15)*100
                score+=max(0,box[3]-1.55)*100
                # A horizontal caption is better on a sufficiently long segment.
                score+=max(0,(width if horizontal else height)-length)*2
                score+=.1*abs(offset)+.03/length
                for _,_,other in all_routes:
                    if other is points:
                        continue
                    for c,d in zip(other,other[1:]):
                        if min(c[0],d[0])<=x+width/2 and max(c[0],d[0])>=x-width/2 and min(c[1],d[1])<=y+height/2 and max(c[1],d[1])>=y-height/2:
                            score+=.7
                choices.append((score,x,y,box,wrapped))
    _,x,y,box,wrapped=min(choices,key=lambda p:p[0])
    occupied.append(box)
    return x,y,wrapped


def render(data, destination, fonts, identity):
    rows=1+max(n['row'] for n in data['nodes'])
    height=6.4 if rows==2 else 8.9
    fig,ax=plt.subplots(figsize=(13.2,height),dpi=150)
    fig.patch.set_facecolor('white')
    fig.subplots_adjust(left=.018,right=.982,top=.84,bottom=.18 if rows==2 else .14)
    ax.set_aspect('auto')
    ax.set_xlim(-2.45,11.25)
    ax.set_ylim(-2.7*(rows-1)-1.75,1.65)
    ax.axis('off')
    regular=FontProperties(fname=str(fonts/'TitilliumWeb-Regular.ttf'))
    bold=FontProperties(fname=str(fonts/'TitilliumWeb-Bold.ttf'))
    fig.canvas.draw()
    renderer=fig.canvas.get_renderer()
    sx=abs(ax.transData.transform((1,0))[0]-ax.transData.transform((0,0))[0])
    sy=abs(ax.transData.transform((0,1))[1]-ax.transData.transform((0,0))[1])
    fig.text(.045,.951,identity,fontproperties=bold,fontsize=12,color='#316B4B',va='top')
    fig.text(.045,.908,data['caption'],fontproperties=bold,fontsize=21,color='#20394F',va='top')
    # Nodes are behind arrows; each box has an explicit function color.
    for node in data['nodes']:
        x,y=coordinate(node); x*=GRID; y*=GRID
        fill,stroke=PALETTE[node['role']]
        box=FancyBboxPatch((x-W/2,y-H/2),W,H,boxstyle='round,pad=0.025,rounding_size=0.10',
                           facecolor=fill,edgecolor=stroke,linewidth=1.15,zorder=3)
        ax.add_patch(box)
        title,subtitle=node['text'].split('|')
        title_font=bold.copy(); title_font.set_size(17)
        sub_font=regular.copy(); sub_font.set_size(14.5)
        title=fit_words(title,title_font,renderer,(W-.24)*sx)
        subtitle=fit_words(subtitle,sub_font,renderer,(W-.24)*sx)
        title_lines=title.count('\n')+1
        ax.text(x,y+.18+(title_lines-1)*.115,title,fontproperties=bold,fontsize=17,
                ha='center',va='center',color='#20394F',linespacing=1.05,zorder=4)
        ax.text(x,y-.28,subtitle,fontproperties=regular,fontsize=14.5,
                ha='center',va='center',color='#455264',linespacing=1.03,zorder=4)
    routes=edge_routes(data)
    for _,edge,points in routes:
        color='#5C7084' if not edge.get('dashed') else '#A15D40'
        style='--' if edge.get('dashed') else '-'
        xs,ys=zip(*points)
        ax.plot(xs,ys,color=color,linewidth=1.3,linestyle=style,zorder=1)
        arrow=FancyArrowPatch(points[-2],points[-1],arrowstyle='-|>',mutation_scale=13,
                              color=color,linewidth=1.3,linestyle=style,shrinkA=0,shrinkB=0,zorder=2)
        ax.add_patch(arrow)
    occupied=[]
    label_font=regular.copy(); label_font.set_size(13.1)
    for _,edge,points in routes:
        x,y,label=place_label(points,edge['label'],occupied,data['nodes'],routes,renderer,label_font,sx,sy)
        ax.text(x,y,label,fontproperties=regular,fontsize=13.1,color='#35485C',ha='center',va='center',
                linespacing=1.02,bbox=dict(facecolor='white',edgecolor='none',pad=1.2,alpha=.97),zorder=5)
    note='\n'.join(textwrap.wrap(data['note'],125,break_long_words=False))
    fig.text(.045,.065 if rows==2 else .052,note,fontproperties=regular,fontsize=13.4,
             color='#455264',va='bottom',linespacing=1.25)
    destination.parent.mkdir(parents=True,exist_ok=True)
    stream=io.BytesIO()
    fig.savefig(stream,format='png',dpi=150,facecolor='white')
    stream.seek(0)
    with Image.open(stream) as image:
        image.convert('RGB').save(destination.with_suffix('.png'),optimize=True)
    # Paths preserve font appearance without requiring installed fonts in vector editors.
    with matplotlib.rc_context({'svg.fonttype':'path'}):
        fig.savefig(destination.with_suffix('.svg'),format='svg',facecolor='white')
    plt.close(fig)
    if destination.with_suffix('.png').stat().st_size>512000:
        raise ValueError('PNG exceeds 500 KiB: '+str(destination))


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--repo',type=Path,default=Path(__file__).resolve().parents[1])
    parser.add_argument('--chapter',type=int,nargs='*')
    args=parser.parse_args()
    specs=json.loads((args.repo/'figures/chapter-diagrams.json').read_text(encoding='utf-8'))
    for item in specs['chapters']:
        if args.chapter and item['number'] not in args.chapter:
            continue
        render(item,args.repo/'figures'/item['filename'],args.repo/'module/fonts',
               f"{specs['code']}  /  BAB {item['number']:02}  /  DIAGRAM KONSEP")
        print(item['filename'],flush=True)


if __name__=='__main__':
    main()
