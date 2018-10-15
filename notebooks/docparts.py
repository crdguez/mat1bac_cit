# -*- coding: utf-8 -*-

import pandas as pd
import os
from IPython.display import Markdown as md
from IPython.display import display

def doc_ejer(title="", tipo = 'ejercicios', letra = 'A', soluciones = False):
    if tipo == 'ejercicios' :
        start=r"""
        \documentclass[spanish, 11pt]{exam}

        %These tell TeX which packages to use.
        \usepackage{array,epsfig}
        \usepackage{amsmath, textcomp}
        \usepackage{amsfonts}
        \usepackage{amssymb}
        \usepackage{amsxtra}
        \usepackage{amsthm}
        \usepackage{mathrsfs}
        \usepackage{color}
        \usepackage{multicol, xparse}
        \usepackage{verbatim}


        \usepackage[utf8]{inputenc}
        \usepackage[spanish]{babel}
        \usepackage{eurosym}

        \usepackage{graphicx}
        \graphicspath{{../img/}}



        \printanswers
        \nopointsinmargin
        \pointformat{}

        %Pagination stuff.
        %\setlength{\topmargin}{-.3 in}
        %\setlength{\oddsidemargin}{0in}
        %\setlength{\evensidemargin}{0in}
        %\setlength{\textheight}{9.in}
        %\setlength{\textwidth}{6.5in}
        %\pagestyle{empty}

        \let\multicolmulticols\multicols
        \let\endmulticolmulticols\endmulticols
        \RenewDocumentEnvironment{multicols}{mO{}}
         {%
          \ifnum#1=1
            #2%
          \else % More than 1 column
            \multicolmulticols{#1}[#2]
          \fi
         }
         {%
          \ifnum#1=1
          \else % More than 1 column
            \endmulticolmulticols
          \fi
         }
        \renewcommand{\solutiontitle}{\noindent\textbf{Sol:}\enspace}

        \newcommand{\samedir}{\mathbin{\!/\mkern-5mu/\!}}

        \newcommand{\class}{1º Bachillerato}
        \newcommand{\examdate}{\today}

        \newcommand{\tipo}{A}


        \newcommand{\timelimit}{50 minutos}



        \pagestyle{head}
        \firstpageheader{\includegraphics[width=0.2\columnwidth]{header_left}}{\textbf{Departamento de Matemáticas\linebreak \class}\linebreak \examnum}{\includegraphics[width=0.1\columnwidth]{header_right}}
        \runningheader{\class}{\examnum}{Página \thepage\ of \numpages}
        \runningheadrule

        """
        
        middle=r"""
        \begin{document}
        \begin{questions}
        """
        
    else:
        start=r"""
        \documentclass[addpoints,spanish, 12pt,a4paper]{exam}
        %\documentclass[answers, spanish, 12pt,a4paper]{exam}
        
        \pointpoints{punto}{puntos}
        \hpword{Puntos:}
        \vpword{Puntos:}
        \htword{Total}
        \vtword{Total}
        \hsword{Resultado:}
        \hqword{Ejercicio:}
        \vqword{Ejercicio:}

        \usepackage[utf8]{inputenc}
        \usepackage[spanish]{babel}
        \usepackage{eurosym}
        %\usepackage[spanish,es-lcroman, es-tabla, es-noshorthands]{babel}


        \usepackage[margin=1in]{geometry}
        \usepackage{amsmath,amssymb}
        \usepackage{multicol, xparse}

        \usepackage{yhmath}

        \usepackage{verbatim}
        %\usepackage{pstricks}


        \usepackage{graphicx}
        \graphicspath{{../img/}}




        \let\multicolmulticols\multicols
        \let\endmulticolmulticols\endmulticols
        \RenewDocumentEnvironment{multicols}{mO{}}
         {%
          \ifnum#1=1
            #2%
          \else % More than 1 column
            \multicolmulticols{#1}[#2]
          \fi
         }
         {%
          \ifnum#1=1
          \else % More than 1 column
            \endmulticolmulticols
          \fi
         }
        \renewcommand{\solutiontitle}{\noindent\textbf{Sol:}\enspace}

        \newcommand{\samedir}{\mathbin{\!/\mkern-5mu/\!}}

        \newcommand{\class}{1º Bachillerato}
        \newcommand{\examdate}{\today}

        %\newcommand{\tipo}{A}


        \newcommand{\timelimit}{50 minutos}

        \renewcommand{\solutiontitle}{\noindent\textbf{Solución:}\enspace}


        \pagestyle{head}
        \firstpageheader{\includegraphics[width=0.2\columnwidth]{header_left}}{\textbf{Departamento de Matemáticas\linebreak \class}\linebreak \examnum}{\includegraphics[width=0.1\columnwidth]{header_right}}
        \runningheader{\class}{\examnum}{Página \thepage\ of \numpages}
        \runningheadrule
        
        \pointsinrightmargin % Para poner las puntuaciones a la derecha. Se puede cambiar. Si se comenta, sale a la izquierda.
        \extrawidth{-2.4cm} %Un poquito más de margen por si ponemos textos largos.
        \marginpointname{ \emph{\points}}

        """
        
        if soluciones == True :
            start = start + r"""\printanswers
            """ + r'\newcommand{\tipo}{' + letra + '}'
        else :
            start = start + r"""%\printanswers
            """ + r'\newcommand{\tipo}{' + letra + '}'
        
        middle=r"""
        \begin{document}
        \noindent
        \begin{tabular*}{\textwidth}{l @{\extracolsep{\fill}} r @{\extracolsep{6pt}} }
        \textbf{Nombre:} \makebox[3.5in]{\hrulefill} & \textbf{Fecha:}\makebox[1in]{\hrulefill} \\
         & \\
        \textbf{Tiempo: \timelimit} & Tipo: \tipo 
        \end{tabular*}
        \rule[2ex]{\textwidth}{2pt}
        Esta prueba tiene \numquestions\ ejercicios. La puntuación máxima es de \numpoints. 
        La nota final de la prueba será la parte proporcional de la puntuación obtenida sobre la puntuación máxima. 

        \begin{center}


        \addpoints
             %\gradetable[h][questions]
            \pointtable[h][questions]
        \end{center}

        \noindent
        \rule[2ex]{\textwidth}{2pt}

        \begin{questions}
        """
    
    
    if title:
        start = start + "\\newcommand{\\examnum}{%s}" % title
    
    
   

    end=r"""
    \end{questions}
    \end{document}
    """
    return start, middle, end

def doc_parts(title="", author=""):
    start="""
    \\documentclass{article}
    \\usepackage{amsfonts}
    \\usepackage{amsmath,multicol,eso-pic}
    \\begin{document}
    """

    if title:
        start = start + "\\title{%s} \n \date{\\vspace{-5ex}} \n \maketitle" % title

    

    end="""
    \end{document}
    """
    return start, end

def exam_parts(title="", author=""):
    start="""
    \\documentclass{exam}
    \\usepackage{amsfonts}
    \\usepackage{amsmath,multicol,eso-pic}
    \\noprintanswers
    \\addpoints
    \\qformat{\\textbf{Question \\\\ \\thequestion}\\quad(\\thepoints)\\hfill}
    \\usepackage{color}
    \\definecolor{SolutionColor}{rgb}{0.8,0.9,1}
    \\shadedsolutions
    \\renewcommand{\\solutiontitle}{\\noindent\\textbf{Solution:}\\par\\noindent}

    \\begin{document}
    \\AddToShipoutPicture{
        \\AtTextUpperLeft{
        \\makebox(400,45)[lt]{
          \\footnotesize
          \\begin{tabular}{r@{\\,}l}
            Name:  & \\rule{0.5\\linewidth}{\\linethickness} \\\\[.5cm]
            Date:  & \\rule{0.5\\linewidth}{\\linethickness} \\\\
          \end{tabular}
    }}}
    \\begin{minipage}{.8\\textwidth}
    This exam includes \\numquestions\\ questions. The total number of points is \\numpoints.
    \\end{minipage}
    \\begin{questions}
    """

    end = """\end{questions}
    \end{document}
    """
    return start, end

def section_parts(title, instr="", cols = 2):
    if cols >= 2:
        section_start="""
        \\section{%s}
        %s
        \\begin{multicols}{1}
        \\begin{enumerate}
        """ % (title, instr)

        section_end="""
        \\end{enumerate}
        \\end{multicols}
        """
    else:
        section_start = """
        \\section{%s}
        %s
        \\begin{enumerate}
        """ % (title, instr)
        section_end = """
        \\end{enumerate}
        """
    return section_start, section_end


def problem(instructions, problem, solution, points=1):
    code = """
    \\question[%s]
        %s
        %s
    \\begin{solution}
        %s
    \\end{solution}
    """ % (str(points), instructions, problem, solution)
    return code

def doc_exam(title="", author=""):
    start="""
    \\documentclass[addpoints,spanish, 12pt,a4paper]{exam}
    %\\documentclass[answers, spanish, 12pt,a4paper]{exam}
    \\printanswers
    \\pointpoints{punto}{puntos}
    \\hpword{Puntos:}
    \\vpword{Puntos:}
    \\htword{Total}
    \\vtword{Total}
    \\hsword{Resultado:}
    \\hqword{Ejercicio:}
    \\vqword{Ejercicio:}

    \\usepackage[utf8]{inputenc}
    \\usepackage[spanish]{babel}
    \\usepackage{eurosym}
    %\\usepackage[spanish,es-lcroman, es-tabla, es-noshorthands]{babel}


    \\usepackage[margin=1in]{geometry}
    \\usepackage{amsmath,amssymb}
    \\usepackage{multicol}

    \\usepackage{yhmath}

    \\usepackage{verbatim}
    \\usepackage[thinlines]{easytable}
    %\\usepackage{pstricks}


    \\usepackage{graphicx}
    \\graphicspath{{../img/}}

    \\newcommand{\\class}{4º Académicas}
    \\newcommand{\\examdate}{\\today}
    \\newcommand{\\examnum}{Examen de final de trimestre}
    \\newcommand{\\tipo}{B}


    \\newcommand{\\timelimit}{50 minutos}

    \\renewcommand{\\solutiontitle}{\\noindent\\textbf{Solución:}\\enspace}


    \\pagestyle{head}
    \\firstpageheader{\\includegraphics[width=0.2\\columnwidth]{header_left}}{\\textbf{Departamento de Matemáticas\\linebreak \\class}\\linebreak \\examnum}{\\includegraphics[width=0.1\\columnwidth]{header_right}}
    \\runningheader{\\class}{\\examnum}{Página \\thepage\\ of \\numpages}
    \\runningheadrule
    \\pointsinrightmargin % Para poner las puntuaciones a la derecha. Se puede cambiar. Si se comenta, sale a la izquierda.
    \\extrawidth{-2.4cm} %Un poquito más de margen por si ponemos textos largos.
    \\marginpointname{ \\emph{\\points}}

    \\begin{document}

    \\noindent
    \\begin{tabular*}{\\textwidth}{l @{\\extracolsep{\\fill}} r @{\\extracolsep{6pt}} }
    \\textbf{Nombre:} \\makebox[3.5in]{\\hrulefill} & \\textbf{Fecha:}\\makebox[1in]{\\hrulefill} \\\\
     & \\\\
    \\textbf{Tiempo: \\timelimit} & Tipo: \\tipo
    \\end{tabular*}
    \\rule[2ex]{\\textwidth}{2pt}
    Esta prueba tiene \\numquestions\\ ejercicios. La puntuación máxima es de \\numpoints.
    La nota final de la prueba será la parte proporcional de la puntuación obtenida sobre la puntuación máxima.

    \\begin{center}


    \\addpoints
     %\\gradetable[h][questions]
    	\\pointtable[h][questions]
    \\end{center}

    \\noindent
    \\rule[2ex]{\\textwidth}{2pt}
    """

    if title:
        start = start + "\\title{%s} \\n \\date{\\vspace{-5ex}} \\n \\maketitle" % title

    end="""
    \\end{document}
    """
    return start, end

#if __name__ == "__main__":
#   print problem("test", "fasd", "asdfasd", 10)

def añadir_ejercicios(enunciado_latex, enunciado, solucion, texto = 'CCalcula:', curso = '1BC', titulo = 'sin_titulo', n_ejercicio = 'ex', dificultad = '1', n_columnas = '3' , puntos = '1') :
    encabezado = ['enunciado_latex','enunciado','solucion']
    datos = [enunciado_latex, enunciado, solucion]
    df = pd.DataFrame(dict(zip(encabezado, datos)))
    df['texto'] = texto
    df['curso'] = curso
    df['titulo'] = titulo
    df['n_ejercicio'] = n_ejercicio
    df['dificultad'] = dificultad
    df['n_columnas'] = n_columnas
    df['puntos'] = puntos
    return df


def escribir_preambulo(fichero = 'prueba3', titulo = 'Ejercicios', tipo = 'ejercicios', soluciones = False) :
    fichero = fichero + '.tex'
    f = open(fichero,'w')
    letra = f.name[-5:-4]
    f.write(doc_ejer(titulo, tipo, letra, soluciones)[0])
    f.write(doc_ejer(titulo, tipo, letra, soluciones)[1])

    f.close()


def escribir_ejercicios(df_ejercicios, fichero = 'prueba3', tipo = 'ejercicios') :
    fichero = fichero + '.tex'
    if tipo == 'ejercicios' :
        txt = df_ejercicios.iloc[0].n_ejercicio + " - " + df_ejercicios.iloc[0].texto
    else :
        txt = df_ejercicios.iloc[0].texto
    n_columnas = df_ejercicios.iloc[0].n_columnas
    f = open(fichero,'a')
    f.write(r'\question %s' % txt)
    f.write(r"""
        \begin{multicols}{%s} 
        \begin{parts}""" % n_columnas)
    
    for s in df_ejercicios.index :
        f.write(r' \part[%s]  $ %s $ '  % (str(df_ejercicios.loc[s].puntos),df_ejercicios.loc[s].enunciado_latex))
        f.write(r' \begin{solution}  $ %s $  \end{solution}'  % df_ejercicios.loc[s].solucion)

    f.write(r"""
        \end{parts}
        \end{multicols}
        """)
    
    f.close()
    
    
def escribir_fin(fichero = 'prueba3') :
    fichero = fichero
    f = open(fichero + '.tex','a')
    f.write(doc_ejer()[2])
    f.close()
    cwd = os.getcwd()
    os.system("pdflatex %s.tex" % fichero)
    os.system("pdflatex %s.tex" % fichero)
    os.rename(cwd+'/'+fichero+'.pdf','../ejercicios/build/'+fichero+'.pdf')
    os.rename(cwd+'/'+fichero+'.tex','../ejercicios/'+fichero+'.tex')
    os.remove("%s.log" % fichero)
    os.remove("%s.aux" % fichero)
    #os.remove("%s.tex" % fichero)

    
def generar_tex(df_ejercicios, fichero, titulo, tipo = 'ejercicios') :
    fichero = fichero + '.tex'
    escribir_preambulo(fichero, titulo, tipo)
    for s in df_ejercicios.groupby('n_ejercicio').count().index : 
        escribir_ejercicios(df_ejercicios[df_ejercicios.n_ejercicio == s],fichero, tipo)
    escribir_fin(fichero)
    
    
def exportar_pdf(df_ejercicios,fichero, titulo, tipo, letra = 'A', soluciones = False) : 
    # titulo = titulo + letra
    
    
    if tipo != 'ejercicios' : 
        df_ejercicios.n_columnas = 1 # para los exámenes
        fichero = fichero + letra
        
    if soluciones == True : fichero=fichero + '_sol'

    escribir_preambulo(fichero, titulo, tipo, soluciones)
    for s in df_ejercicios.groupby('n_ejercicio').count().index : 
        display(md("**Ejercicio: **" + s ))
        display(df_ejercicios[df_ejercicios.n_ejercicio == s])
        escribir_ejercicios(df_ejercicios[df_ejercicios.n_ejercicio == s],fichero, tipo)

    escribir_fin(fichero)