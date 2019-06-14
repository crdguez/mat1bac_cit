# -*- coding: utf-8 -*-

from sympy import init_session
from sympy.calculus.util import continuous_domain
from sympy import solve_poly_inequality, reduce_abs_inequality
from sympy.solvers.inequalities import solve_univariate_inequality, reduce_rational_inequalities

import matplotlib.pyplot as plt
from matplotlib import style

def trozos(f):
    # Función que devuelve el extremo superior de los tramos, los límites laterales, y el valor de la función
    sol = []
    for i,s  in enumerate(f.args):
        if(i<len(f.args)-1):
            extremo = f.args[i][1].as_set().sup
            #display(extremo)
            #display(s)
            #display(limit(f.args[i][0],x,extremo, dir='-'))
            #display(limit(f.args[i][0],x,extremo, dir='+'))
            #display(f.subs(x,extremo))
            sol.append((extremo, limit(f.args[i][0],x,extremo, dir='-'), limit(f.args[i+1][0],x,extremo, dir='+'),f.subs(x,extremo)))        
    return sol    

def estudio(f) :
    # Estudio en una función a trozos
    
    set = S.Reals
    conj_singular = S.EmptySet
    for j, t in enumerate(f.args) :
        #display(singularities(t[0],x))
        #conj_singular = Union(conj_singular,singularities(t[0],x))
        #display(Union(conj_singular,singularities(t[0],x)))
        #conj_singular = Union(conj_singular,Complement(S.Reals,continuous_domain(t[0],x,S.Reals)))
        #conj_singular = Union(conj_singular,Intersection(t[1].as_set(),Complement(S.Reals,continuous_domain(t[0],x,S.Reals))))
        set2 = Intersection(set,t[1].as_set())
        conj_singular = Union(conj_singular,Intersection(set2,Complement(S.Reals,continuous_domain(t[0],x,S.Reals))))
        set = Complement(S.Reals,t[1].as_set())
        
    sol = r"Singularidades de las expresiones analíticas: $"+ latex(conj_singular)+"$"  
    sol += r".\\ Posibles discontinuidades en los extremos de los trozos:"

    xs = []
    estudio = []

    for j, t in enumerate(trozos(f)) :
        xs.append(str(t[0]))
        if (t[1]==t[2]) :
            estudio.append(r"\\En {} es continua ya que hay límite y $\lim = f({})={}$".format(t[0],t[0],t[3]))
            display(r"En $x_0={}$ hay límite y f({})={}".format(t[0],t[0],t[3]))
        else :
            estudio.append(r"\\En {} no es continua porque no existe límite. Límites laterales: ${}$ y ${}$".format(t[0], latex(t[1]), latex(t[2])))
            display(r"En {} no existe límite. Límites laterales: {} y  {}".format(t[0], t[1], t[2]))

    sol+=', '.join(xs)+r"."+'. '.join(estudio)
    return(sol)
    
    
def asintotas(f) :
    # Igual usar singularities mejor: asintotas, verticales, horizontales y oblícuas (a,b) en oo y -oo
    asint = []
    asintex = r'Asíntotas:\\'
    asint.append([(i,limit(f,x,i)) for i in list(S.Reals - continuous_domain(f,x,domain=S.Reals))])
    asintex += ', '.join(r'A.V. $x='+str(i)+r'$\\' for i in list(S.Reals - continuous_domain(f,x,domain=S.Reals)))
    if abs(limit(f,x,oo)) != oo:
        asintex += r'A.H. $y='+latex(limit(f,x,oo))+r'$\\'
    if abs(limit(f,x,-oo)) != oo:
        asintex += r'A.H. $y='+latex(limit(f,x,-oo))+r'$\\'
  
    asint.append([(oo,limit(f,x,oo)), (-oo,limit(f,x,-oo))])
    oblicuas=[]
    if abs(limit(f/x,x,oo)) != oo :
        oblicuas.append((oo,limit(f/x,x,oo)*x+limit(f-limit(f/x,x,oo)*x,x,oo)))
        #display(latex(limit(f/x,x,oo)*x+limit(f-limit(f/x,x,oo)*x,x,oo)))
        asintex += r'A.O. $y='+latex(limit(f/x,x,oo)*x+limit(f-limit(f/x,x,oo)*x,x,oo))+r'$ \\'
    if abs(limit(f/x,x,-oo)) != oo :
        oblicuas.append((-oo,limit(f/x,x,-oo)*x+limit(f-limit(f/x,x,-oo)*x,x,-oo)))
        asintex += r'A.O. $y='+latex(limit(f/x,x,-oo)*x+limit(f-limit(f/x,x,-oo)*x,x,-oo))+r'$ \\'
    asint.append(oblicuas)
    return asint,asintex

def crecimiento(f) :
    #crecimiento, decrecimiento y puntos singulares
    crec = reduce_rational_inequalities([[f.diff()>0]],x,relational=False)
    decrec = reduce_rational_inequalities([[f.diff()<0]],x,relational=False)
    sing = []
    for t in solve(f.diff()) :
        if f.diff().diff().subs(x,t) < 0 :
            tipo = 'máx'
        elif f.diff().diff().subs(x,t) > 0 :
            tipo = 'mín'
        else :
            tipo = 'inflex'      
        sing.append([t,tipo])

    sol=[crec,decrec,sing]

    return sol


def mi_plot(f, nombre='sin_nombre', xmax=10) :
        plt.rcParams['figure.figsize'] = 10,10
        #p1 = plot(f,show=True, xlim=(-xmax,xmax), ylim=(-xmax,xmax))
        p1 = plot(f, xlim=(-xmax,xmax), ylim=(-xmax,xmax))
        p1.save(nombre+".png")
#        p1.save("prueba.png")
        return r"\\ \resizebox{0.4\textwidth}{!}{\includegraphics[width=1\columnwidth]{%s}}" % (nombre)

