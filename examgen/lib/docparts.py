# -*- coding: utf8 -*-

def doc_parts(title="", author=""):
    start="""
    \documentclass{article}
    \usepackage{amsfonts}
    \usepackage{amsmath,multicol,eso-pic}
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
    \\documentclass[addpoints,spanish, 12pt,a4paper]{exam}
    \\usepackage{amsfonts}
    \\usepackage{amsmath,multicol,eso-pic, eurosym, yhmath}
    \\usepackage[margin=1in]{geometry}
    \\usepackage{amssymb}
    \\usepackage{multicol}
    \\usepackage{graphicx}
    \\graphicspath{{./img/}}
    \\usepackage[utf8]{inputenc}
    \\usepackage[spanish]{babel}
    \\usepackage{eurosym}
    \\noprintanswers
    \\pointpoints{punto}{puntos}
    \\addpoints
    \\qformat{\\textbf{Pregunta\\ \\thequestion :}\\quad(\\thepoints)\\hfill}
    \\usepackage{color}
    \\definecolor{SolutionColor}{rgb}{0.8,0.9,1}
    \\shadedsolutions
    \\renewcommand{\\solutiontitle}{\\noindent\\textbf{Solución:}\\enspace}



\\hpword{Puntos:}
\\vpword{Puntos:}
\\htword{Total}
\\vtword{Total}
\\hsword{Resultado:}
\\hqword{Ejercicio:}
\\vqword{Ejercicio:}

\\newcommand{\\class}{4 Académicas}
\\newcommand{\\examdate}{\\today}
\\newcommand{\\examnum}{Recuperacion trimestre 1}
\\newcommand{\\tipo}{B}
\\newcommand{\\timelimit}{50 minutos}

\\pagestyle{head}
\\firstpageheader{\\includegraphics[width=0.2\\columnwidth]{header_left}}{\\textbf{Departamento de Matematicas\\linebreak \\class}\\linebreak \\examnum}{\\includegraphics[width=0.1\\columnwidth]{header_right}}
\\runningheader{\\class}{\\examnum}{Página \\thepage\\ of \\numpages}
\\runningheadrule


    \\begin{document}
        \\noindent
        \\begin{tabular*}{\\textwidth}{l @{\\extracolsep{\\fill}} r @{\\extracolsep{6pt}} }
        \\textbf{Nombre:} \\makebox[3.5in]{\hrulefill} & \\textbf{Fecha:}\\makebox[1in]{\\hrulefill}   \\\\
         \\ & \\ \\\\
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

if __name__ == "__main__":
    print problem("test", "fasd", "asdfasd", 10)
