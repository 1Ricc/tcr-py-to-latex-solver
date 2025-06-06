import datetime
from pathlib import Path
from typing import List, Dict, Optional
from core.crt_solver import CRTSolution

# Costanti LaTeX
LATEX_HEADER = r"""
\documentclass[12pt]{article}
\usepackage[utf8]{inputenc}
\usepackage{amsmath, amssymb}
\usepackage{cancel}
\usepackage{array}
\usepackage{geometry}
\usepackage{fancyhdr}

% Imposta i margini della pagina
\geometry{
    top=2cm,
    bottom=2.5cm,
    left=2.5cm,
    right=2.5cm,
    includehead,
    includefoot
}

% Configura l'header e il footer
\pagestyle{fancy}
\fancyhf{}  % Pulisce header e footer
\renewcommand{\headrulewidth}{0pt}  % Rimuove la linea dell'header
\fancyfoot[C]{-\thepage-}  % Numero di pagina centrato nel footer

% Rimuove lo spazio extra dopo il titolo
\makeatletter
\def\@maketitle{
  \newpage
  \null
  \vskip -2em
  \begin{center}%
  \let \footnote \thanks
    {\LARGE \@title \par}%
    \vskip 1.5em%
    {\large \@date \par}%
  \end{center}%
  \par
  \vskip 1.5em
}
\makeatother
"""

LATEX_FOOTER = r"\end{document}"

def format_congruence(cong: Tuple[int, int]) -> str:
    """Formatta una congruenza in LaTeX."""
    return f"x \\equiv {cong[0]} \\pmod{{{cong[1]}}}"

def format_system(congruences: List[Tuple[int, int]]) -> str:
    """Formatta un sistema di congruenze in LaTeX."""
    return r"\begin{cases}" + r" \\".join(format_congruence(c) for c in congruences) + r"\end{cases}"

def format_euclid_table(steps: List[Tuple[str, bool]], back_subs: List[str]) -> str:
    """Formatta la tabella dell'algoritmo di Euclide in LaTeX."""
    content = [
        r"\begin{center}",
        r"\setlength{\arrayrulewidth}{0.5pt}",
        r"\begin{tabular}{|p{5cm}|p{9cm}|}",
        r"\hline",
        r"\textbf{Algoritmo di Euclide} & \textbf{Sostituzione a ritroso} \\",
        r"\hline"
    ]
    
    for (step, is_last), sub_step in zip(steps, back_subs):
        step = step.replace("·", r"\cdot ")
        sub_step = sub_step.replace("·", r"\cdot ")
        
        if is_last:
            euclide_str = r"$\cancel{" + step + r"}$"
            content.append(f"{euclide_str} & \\\\")
        else:
            euclide_str = "$" + step + "$"
            content.append(f"{euclide_str} & ${sub_step}$ \\\\")
        content.append(r"\hline")
    
    content.extend([
        r"\end{tabular}",
        r"\end{center}"
    ])
    return "\n".join(content)

def generate_latex_documentation(solution: CRTSolution, options: Optional[Dict] = None) -> str:
    """Genera la documentazione LaTeX per una soluzione di sistema di congruenze."""
    title = "Soluzione sistema di congruenze"
    date = datetime.date.today().strftime("%d/%m/%Y")
    content = []
    
    # Sezione esercizio
    content.extend([
        r"\section*{Esercizio}",
        "Si determinino tutte le soluzioni del seguente sistema di congruenze:",
        r"\[",
        format_system(solution.congruences),
        r"\]",
        r"Sia $S \subset \mathbb{Z}$ l'insieme delle soluzioni del sistema."
    ])
    
    if hasattr(solution, 'question') and getattr(solution, 'question'):
        content.append(solution.question)
    elif options and 'question' in options:
        content.append(options['question'])
    
    # Passo 1: Compatibilità
    m1, m2 = solution.congruences[0][1], solution.congruences[1][1]
    a1, a2 = solution.congruences[0][0], solution.congruences[1][0]
    content.extend([
        rf"""
\textbf{{Passo 1: Compatibilità.}} \\ 
Grazie al teorema cinese del resto, il sistema è compatibile, cioe $S \neq \emptyset$, se e solo se
$$\gcd({m1}, {m2}) \mid {a2} - {a1} = {solution.diff} \qquad (1)$$

Decomponendo in fattori primi:
$${m1} = {solution.m1_factorization}, \quad {m2} = {solution.m2_factorization}$$

Pertanto $\gcd({m1}, {m2}) = {solution.gcd_value}$.
"""
    ])
    
    if solution.compatible:
        content.extend([
            rf"Pertanto la (1) è verificata: ${solution.gcd_value} \mid {solution.diff}$. Il sistema è compatibile.\\",
            rf"Inoltre, osserviamo che $${a2} - {a1} = {(a2-a1)//solution.gcd_value} \cdot {solution.gcd_value} \qquad (2)$$"
        ])
    else:
        content.append(rf"Pertanto la (1) NON è verificata: ${solution.gcd_value} \nmid {solution.diff}$. Il sistema è incompatibile.\\")
        return assemble_latex(title, date, '\n'.join(content))
    
    # Passo 2: Euclide esteso
    content.extend([
        r"\textbf{Passo 2: Calcolo di una soluzione particolare} \\",
        rf"Determiniamo una soluzione $x_{0} \in S$.",
        rf"Iniziamo applicando l'algoritmo di Euclide con sostituzione a ritroso dei resti alla coppia ({m1}, {m2}):",
        format_euclid_table(solution.gcd_steps, solution.back_subs)
    ])
    
    if solution.expansion_steps:
        content.extend([
            r"\textbf{Espansione completa:}",
            r"\begin{align*}",
            *[step + r"\\" for step in solution.expansion_steps],
            r"\end{align*}"
        ])
    
    u, v = solution.bezout_coeffs
    content.append(rf"Otteniamo quindi: $$\gcd({m1}, {m2}) = {solution.gcd_value} = {u} \cdot {m1} + {v} \cdot {m2}$$")
    
    # Passo 3: Soluzione particolare
    content.extend([
        rf"""
Sostituendo nell'equazione (2) otteniamo:
$${a2} - {a1} = {solution.diff} = {solution.gcd_value} \cdot {solution.diff // solution.gcd_value} = {solution.diff // solution.gcd_value} \cdot ({u} \cdot {m1} + {v} \cdot {m2}) = {solution.diff // solution.gcd_value * v} \cdot {m2} - {abs(solution.diff // solution.gcd_value * u)} \cdot {m1}$$

Ricaviamo adesso una soluzione particolare partendo dalla precedente uguaglianza:
$${a2} - {a1} = {solution.diff // solution.gcd_value * v} \cdot {m2} - {abs(solution.diff // solution.gcd_value * u)} \cdot {m1} \iff {a2} - {solution.diff // solution.gcd_value * v} \cdot {m2} = {a1} + {abs(solution.diff // solution.gcd_value * u)} \cdot {m1} \iff {a2 - solution.diff // solution.gcd_value * v * m2} = {a1 + (solution.diff // solution.gcd_value * u) * m1}$$

Quindi $x_0 = {solution.particular_solution} \in S$ è una soluzione particolare del sistema.
"""
    ])
    
    # Passo 4: Insieme soluzioni
    content.extend([
        rf"""
\textbf{{Passo 3: Calcolo dell'insieme delle soluzioni}} \\ 
Grazie al Teorema Cinese del Resto sappiamo che:
$$S = [{solution.particular_solution}]_{{\mathrm{{mcm}}({m1}, {m2})}}$$
Ma
$$\mathrm{{mcm}}({{{m1}}}, {{{m2}}}) = \frac{{{{{m1}}} \cdot {{{m2}}}}}{{\gcd({{{m1}}},{{{m2}}})}} = \frac{{{{{solution.m1_factorization}}} \cdot {{{solution.m2_factorization}}}}}{{{solution.gcd_value}}} = {{{solution.period}}}$$
"""
    ])
    
    if solution.particular_solution >= 0 and solution.particular_solution < solution.period:
        content.append(rf"""Di conseguenza l'insieme delle soluzioni è:
        $$S = [{solution.particular_solution}]_{{{solution.period}}} = \{{{solution.particular_solution} + {solution.period} \cdot k : k \in \mathbb{{Z}}\}}$$
        """)
    else:
        k = (-solution.particular_solution) // solution.period + 1
        positive_sol = solution.particular_solution + k * solution.period
        content.append(rf"""Di conseguenza l'insieme delle soluzioni è:
        $$S = [{solution.particular_solution}]_{{{solution.period}}} = [{solution.particular_solution} + {k} \cdot {solution.period}]_{{{solution.period}}} = [{positive_sol}]_{{{solution.period}}} = \{{{positive_sol} + {solution.period} \cdot k : k \in \mathbb{{Z}}\}}$$
        """)
    
    return assemble_latex(title, date, '\n'.join(content))

def assemble_latex(title: str, date: str, content: str) -> str:
    """Assembla il documento LaTeX completo."""
    return f"{LATEX_HEADER}\n\\title{{{title}}}\n\\date{{{date}}}\n\\maketitle\n{content}\n{LATEX_FOOTER}" 