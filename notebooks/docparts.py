# -*- coding: utf-8 -*-

def doc_ejer(title="", author=""):
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
	\usepackage{multicol}
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
	
	\renewcommand{\solutiontitle}{\noindent\textbf{Sol:}\enspace}
	
	\newcommand{\samedir}{\mathbin{\!/\mkern-5mu/\!}}
	
	\newcommand{\class}{4º Académicas}
	\newcommand{\examdate}{\today}
	\newcommand{\examnum}{Geometría Analítica}
	\newcommand{\tipo}{A}
	
	
	\newcommand{\timelimit}{50 minutos}
	
	
	
	\pagestyle{head}
	\firstpageheader{\includegraphics[width=0.2\columnwidth]{header_left}}{\textbf{Departamento de Matemáticas\linebreak \class}\linebreak \examnum}{\includegraphics[width=0.1\columnwidth]{header_right}}
	\runningheader{\class}{\examnum}{Página \thepage\ of \numpages}
	\runningheadrule
	
	\begin{document}
    """

    if title:
        start = start + "\\title{%s} \n \date{\\vspace{-5ex}} \n \maketitle" % title

    

    end="""
    \end{document}
    """
    return start, end

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
