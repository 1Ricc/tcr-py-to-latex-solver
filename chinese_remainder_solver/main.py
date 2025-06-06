import sys
import json
from pathlib import Path
from core.crt_solver import solve_crt_system
from latex.generator import generate_latex_documentation

def input_congruence_system():
    print("Inserisci il sistema di congruenze del tipo (x ≡ a (mod n), x ≡ b (mod m)): ")
    print("Da inserire nel formato: a n [invio] b m [invio] ... (invio per terminare)")
    congruences = []
    while True:
        line = input("Congruenza (vuoto per terminare): ").strip()
        if not line:
            break
        try:
            # Parsing semplice: x ≡ a (mod m)
            parts = line.replace('x', '').replace('≡', '').replace('mod', '').replace('(', '').replace(')', '').split()
            a = int(parts[0])
            m = int(parts[1])
            congruences.append((a, m))
        except Exception as e:
            print(f"Errore di parsing: {e}")
    return congruences

def main():
    print("=== Chinese Remainder Theorem Solver ===")
    system = input_congruence_system()
    options = {
        'output_format': input("Formato output (pdf/tex/both): ").strip() or 'tex',
    }
    solution = solve_crt_system(system, options)
    latex_doc = generate_latex_documentation(solution, options)
    with open("output/solution.tex", "w") as f:
        f.write(latex_doc)
    print("File LaTeX generato in output/solution.tex")
    if options['output_format'] in ('pdf', 'both'):
        import subprocess
        subprocess.run(["pdflatex", "-output-directory", "output", "output/solution.tex"])
        print("File PDF generato in output/solution.pdf")

def batch_mode(input_file: str):
    with open(input_file, "r") as f:
        test_cases = json.load(f)
    for idx, case in enumerate(test_cases):
        system = case["system"]
        options = case.get("options", {})
        description = case.get("description", "")
        solution = solve_crt_system(system, options)
        latex_doc = generate_latex_documentation(solution, options)
        outbase = f"output/batch_{idx+1}"
        with open(f"{outbase}.tex", "w") as ftex:
            ftex.write(latex_doc)
        print(f"Test {idx+1}: {description} -> {outbase}.tex")
        if options.get("output_format") in ("pdf", "both"):
            import subprocess
            subprocess.run(["pdflatex", "-output-directory", "output", f"{outbase}.tex"])
            print(f"PDF generato: {outbase}.pdf")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "batch":
        batch_mode("chinese_remainder_solver/examples/test_cases.json")
    else:
        main() 