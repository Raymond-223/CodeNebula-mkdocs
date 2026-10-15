from pathlib import Path
from math import sqrt, sin, cos, pi
from html import escape
root=Path(__file__).resolve().parents[1]/'docs/assets/diagrams'
def svg(name,title,parts,w=1000,h=460):
    head=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc"><title id="title">{escape(title)}</title><desc id="desc">{escape(title)}</desc><rect width="100%" height="100%" fill="#fff"/><style>text{{font-family:Arial,"Microsoft YaHei",sans-serif;fill:#172033;font-size:20px}}.title{{font-size:28px;font-weight:700}}.small{{font-size:17px;fill:#475569}}.axis{{stroke:#64748b;stroke-width:2;fill:none}}.blue{{stroke:#4f46e5;stroke-width:3;fill:none}}.pink{{stroke:#db2777;stroke-width:3;fill:none}}.dash{{stroke:#64748b;stroke-width:2;stroke-dasharray:6 5;fill:none}}.arr{{marker-end:url(#a)}}</style><defs><marker id="a" markerUnits="userSpaceOnUse" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto"><path d="M0 1L10 6L0 11Z" fill="#4f46e5"/></marker></defs>'''
    (root/name).write_text(head+f'<text x="35" y="45" class="title">{escape(title)}</text>'+''.join(parts)+'</svg>',encoding='utf-8')
def line(a,b,cls):return f'<line x1="{a[0]:.2f}" y1="{a[1]:.2f}" x2="{b[0]:.2f}" y2="{b[1]:.2f}" class="{cls}"/>'
def text(x,y,s,cls=''):return f'<text x="{x:.2f}" y="{y:.2f}" class="{cls}">{escape(s)}</text>'
def dot(p,color='#db2777'):return f'<circle cx="{p[0]:.2f}" cy="{p[1]:.2f}" r="6" fill="{color}"/>'
# Exact quadratic and its tangent: x_k=2, f=x^2-2, x_{k+1}=1.5.
xy=lambda x,y:(95+250*x,325-95*y)
parts=[line((65,325),(865,325),'axis'),line((95,75),(95,375),'axis')]
pts=' '.join(f'{xy(x/100,(x/100)**2-2)[0]:.2f},{xy(x/100,(x/100)**2-2)[1]:.2f}' for x in range(112,222))
parts+=[f'<polyline points="{pts}" class="blue"/>',line(xy(1.35,4*1.35-6),xy(2.12,4*2.12-6),'pink'),line(xy(2,0),xy(2,2),'dash'),dot(xy(2,2)),dot(xy(1.5,0)),dot(xy(sqrt(2),0),'#0891b2'),text(615,130,'(2, 2)'),text(690,95,'f(x) = x² − 2'),text(650,220,'切线 y = 4x − 6'),text(587,362,'xₖ = 2'),text(480,392,'xₖ₊₁ = 1.5'),text(335,362,'α = √2'),text(55,430,'曲线、当前点、切线斜率及横轴交点均由同一函数计算。','small')]
svg('yau-newton-tangent.svg','Newton：切线零点给出下一步',parts)
# Orthogonal projection: b = 400*u + 170*n; u dot n = 0.
u=(.96,-.28);n=(-.28,-.96);o=(150,350);p=(o[0]+400*u[0],o[1]+400*u[1]);b=(p[0]+170*n[0],p[1]+170*n[1])
parts=[line((65,374.79),(870,140),'axis'),line(o,p,'blue arr'),line(o,b,'blue arr'),line(p,b,'pink arr')]
c=(p[0]-20*u[0],p[1]-20*u[1]);d=(c[0]+20*n[0],c[1]+20*n[1]);e=(p[0]+20*n[0],p[1]+20*n[1])
parts +=[f'<polyline points="{c[0]},{c[1]} {d[0]},{d[1]} {e[0]},{e[1]}" class="axis"/>',dot(p),text(b[0]-20,b[1]-18,'b'),text(p[0]-20,p[1]+45,'Pb'),text(530,170,'b − Pb'),text(700,215,'Col(A)'),text(55,425,'b = Pb + (b − Pb)，残差与列空间垂直。','small')]
svg('yau-orthogonal-projection.svg','正交投影：垂足与残差方向',parts)
# Four distinct SVD steps, track a single vector through each transform.
parts=[];centers=[120,370,620,870];ys=225
for i,c in enumerate(centers):
    parts += [line((c-95,ys),(c+95,ys),'axis'),line((c,ys-95),(c,ys+95),'axis')]
    if i<2:parts += [f'<circle cx="{c}" cy="{ys}" r="65" fill="#eef2ff" stroke="#4f46e5" stroke-width="3"/>']
    else:parts += [f'<ellipse cx="{c}" cy="{ys}" rx="92" ry="42" transform="rotate({0 if i==2 else -35} {c} {ys})" fill="#eef2ff" stroke="#4f46e5" stroke-width="3"/>']
    angle=[pi/4,pi/4-pi/6,pi/4-pi/6,pi/4-pi/6+35*pi/180][i]
    vx,vy=(65*cos(angle),65*sin(angle)) if i<2 else (92*cos(pi/12),42*sin(pi/12))
    if i==3:vx,vy=vx*cos(35*pi/180)-vy*sin(35*pi/180),vx*sin(35*pi/180)+vy*cos(35*pi/180)
    parts += [line((c,ys),(c+vx,ys-vy),'pink'),dot((c+vx,ys-vy)),text(c-65,370,['x','Vᵀx','ΣVᵀx','UΣVᵀx = Ax'][i])]
for i,s in enumerate(['Vᵀ','Σ','U']):parts+=[line((centers[i]+105,ys),(centers[i+1]-105,ys),'blue arr'),text(centers[i]+115,195,s)]
parts += [text(35,420,'Vᵀ、U：正交变换（可含反射）；Σ：沿坐标轴伸缩。单位圆经正交变换仍是圆。','small')]
svg('yau-svd-geometry.svg','A = UΣVᵀ：逐步跟踪圆与向量',parts,h=460)
# Honest transient growth computed from B=[[.5,3],[0,.5]], e0=(0,1).
parts=[line((55,240),(440,240),'axis'),line((247,80),(247,385),'axis'),'<circle cx="247" cy="240" r="120" fill="none" stroke="#0891b2" stroke-width="3"/>',dot((307,240),'#16a34a'),text(312,225,'λ = 0.5'),text(105,408,'左：示例矩阵的全部特征值均在单位圆内','small'),text(505,95,'B = [[0.5, 3], [0, 0.5]], e₀ = (0, 1)ᵀ'),line((535,360),(960,360),'axis'),line((535,130),(535,360),'axis')]
vals=[1]+[sqrt((3*k*.5**(k-1))**2+.5**(2*k)) for k in range(1,11)]
pts=' '.join(f'{535+40*k},{360-65*v}' for k,v in enumerate(vals))
parts +=[f'<polyline points="{pts}" class="blue"/>',text(545,122,'‖Bᵏe₀‖₂'),text(960,390,'k'),text(590,415,'右：误差可先增大，随后趋于零','small')]
for k in [0,2,4,6,8,10]:parts +=[text(530+40*k,383,str(k),'small')]
svg('yau-spectral-convergence.svg','ρ(B) < 1：最终衰减与瞬态增长',parts)
# Replace an open chain incorrectly labelled closed-loop feedback.
parts=[text(55,110,'r(t)'),line((110,190),(215,190),'blue arr'),'<circle cx="240" cy="190" r="25" fill="#eef2ff" stroke="#64748b" stroke-width="2"/>',text(229,198,'Σ'),text(207,170,'+'),text(245,238,'−'),line((265,190),(355,190),'blue arr'),text(290,165,'e(t)'),line((545,190),(625,190),'blue arr'),text(562,165,'u(t)'),line((815,190),(950,190),'blue arr'),text(880,165,'y(t)'),dot((870,190),'#4f46e5'),line((870,190),(870,310),'blue'),line((870,310),(545,310),'blue arr'),line((355,310),(240,310),'blue'),line((240,310),(240,215),'blue arr')]
for x,y,w,label in [(355,140,190,'Controller'),(625,140,190,'Plant'),(355,270,190,'Sensor')]:
    parts +=[f'<rect x="{x}" y="{y}" width="{w}" height="80" rx="12" fill="#f4f7fb" stroke="#8aa0b5" stroke-width="2"/>',text(x+25,y+47,label)]
parts +=[text(55,415,'测量输出反馈至比较点，误差 e = r − y_measured 驱动控制器。','small')]
svg('feedback-loop.svg','Closed-loop feedback：负反馈闭环',parts)
print('Redrew 5 SVGs with computed geometry')
