import sys
import json
from pathlib import Path
from typing import List, Tuple, Dict, Optional
from core.crt_solver import solve_crt_system
from latex.generator import generate_latex_documentation

def parse_congruence(line: str) -> Optional[Tuple[int, int]]:
    """Parsa una riga di input in una congruenza.
    
    Args:
        line: riga di input nel formato "a n" o "x ≡ a (mod n)"
        
    Returns:
        Tupla (a, n) se il parsing ha successo, None altrimenti
    """
    try:
        # Rimuovi caratteri non necessari
        line = line.replace('x', '').replace('≡', '').replace('mod', '').replace('(', '').replace(')', '')
        parts = line.split()
        if len(parts) != 2:
            return None
        return int(parts[0]), int(parts[1])
    except (ValueError, IndexError):
        return None

def input_congruence_system() -> List[Tuple[int, int]]:
    """Richiede all'utente di inserire un sistema di congruenze.
    
    Returns:
        Lista di coppie (a, m) rappresentanti le congruenze
    """
    print("Inserisci il sistema di congruenze del tipo (x ≡ a (mod n), x ≡ b (mod m)): ")
    print("Da inserire nel formato: a n [invio] b m [invio] ... (invio per terminare)")
    congruences = []
    
    while True:
        line = input("Congruenza (vuoto per terminare): ").strip()
        if not line:
            break
            
        cong = parse_congruence(line)
        if cong is None:
            print("Formato non valido. Usa il formato 'a n' o 'x ≡ a (mod n)'")
            continue
            
        congruences.append(cong)
        
    return congruences

def get_output_format() -> str:
    """Richiede all'utente il formato di output desiderato.
    
    Returns:
        Stringa 'pdf', 'tex' o 'both'
    """
    while True:
        fmt = input("Formato output (pdf/tex/both): ").strip().lower()
        if fmt in ('pdf', 'tex', 'both'):
            return fmt
        print("Formato non valido. Scegli tra 'pdf', 'tex' o 'both'")

def compile_latex(tex_file: Path) -> None:
    """Compila un file LaTeX in PDF.
    
    Args:
        tex_file: percorso del file .tex da compilare
    """
    import subprocess
    output_dir = tex_file.parent
    subprocess.run(["pdflatex", "-output-directory", str(output_dir), str(tex_file)])

def save_solution(latex_doc: str, output_path: Path, fmt: str) -> None:
    """Salva la soluzione nel formato richiesto.
    
    Args:
        latex_doc: documento LaTeX da salvare
        output_path: percorso base per i file di output
        fmt: formato di output ('pdf', 'tex' o 'both')
    """
    # Crea la directory di output se non esiste
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Salva il file .tex
    tex_file = output_path.with_suffix('.tex')
    tex_file.write_text(latex_doc)
    print(f"File LaTeX generato in: {tex_file}")
    
    # Compila in PDF se richiesto
    if fmt in ('pdf', 'both'):
        compile_latex(tex_file)
        print(f"File PDF generato in: {output_path.with_suffix('.pdf')}")

def main() -> None:
    """Funzione principale del programma."""
    print("=== Chinese Remainder Theorem Solver ===")
    
    # Input
    system = input_congruence_system()
    if not system:
        print("Nessuna congruenza inserita. Uscita.")
        return
        
    # Opzioni
    options = {
        'output_format': get_output_format()
    }
    
    # Risoluzione
    solution = solve_crt_system(system, options)
    latex_doc = generate_latex_documentation(solution, options)
    
    # Output
    save_solution(latex_doc, Path("output/solution"), options['output_format'])

def batch_mode(input_file: str) -> None:
    """Esegue il programma in modalità batch.
    
    Args:
        input_file: percorso del file JSON con i test case
    """
    # Carica i test case
    with open(input_file, "r") as f:
        test_cases = json.load(f)
    
    # Processa ogni test case
    for idx, case in enumerate(test_cases["systems"], 1):
        # Estrai i dati
        a, n = case["a"], case["n"]
        b, m = case["b"], case["m"]
        options = case.get("options", {})
        description = case.get("description", f"Test case {idx}")
        
        # Risolvi
        solution = solve_crt_system([(a, n), (b, m)], options)
        latex_doc = generate_latex_documentation(solution, options)
        
        # Salva
        output_path = Path(f"output/batch_{idx}")
        save_solution(latex_doc, output_path, options.get("output_format", "tex"))
        print(f"Processato: {description}")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "batch":
        batch_mode("chinese_remainder_solver/examples/test_cases.json")
    else:
        main() 