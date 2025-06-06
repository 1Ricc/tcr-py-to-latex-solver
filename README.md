# Risolutore di Sistemi di Congruenze

Questo programma genera soluzioni dettagliate per gli esercizi riguardanti sistemi di congruenze lineari, utilizzando il Teorema Cinese del Resto. 

## Caratteristiche

- Risolve sistemi di due congruenze lineari
- Genera soluzioni passo-passo in formato LaTeX
- Include dimostrazioni dettagliate di ogni passaggio
- Calcola automaticamente MCD, MCM e coefficienti di Bézout
- Produce output LaTeX pronto per la compilazione

## Requisiti

- Python 3.8 o superiore
- pacchetti Python: `sympy`

## Installazione

1. Clona la repository:
```bash
git clone https://github.com/tuusuario/tcr-py-to-latex-solver.git
cd tcr-py-to-latex-solver
```

## Utilizzo

### Da riga di comando

1. Apri il terminale e naviga nella cartella del progetto:
```bash
cd tcr-py-to-latex-solver
```

2. Esegui il programma:
```bash
python chinese_remainder_solver/main.py
```

3. Il programma ti chiederà di inserire i dati del sistema di congruenze:
   - Nella prima riga inserire: a n
   - Nella seconda riga inserire: b m
   - Nella terza riga: INVIO (per terminare il sistema di congruenze)

4. Al prompt (pdf/tex/both) inserire il formato desiderato in output

5. Il programma genererà automaticamente un file LaTeX con la soluzione dettagliata nella cartella `output/`

6. Per compilare il file LaTeX generato, puoi usare un compilatore LaTeX come pdflatex:
```bash
cd output
pdflatex solution.tex
```

## Output

Il programma genera un documento LaTeX che include:

1. Il sistema di congruenze originale
2. Verifica della compatibilità
3. Calcolo del MCD usando l'algoritmo di Euclide
4. Calcolo dei coefficienti di Bézout
5. Determinazione di una soluzione particolare
6. Calcolo dell'insieme completo delle soluzioni

## Modalità Batch

Il programma supporta anche una modalità batch per risolvere più sistemi di congruenze contemporaneamente. Per utilizzarla:

1. Navigare al file `tcr-py-to-latex-solver/chinese_remainder_solver/examples/test_cases.json`

2. Inserire i sistemi che si desiderano risolvere

3. Esegui il programma in modalità batch:
```bash
python chinese_remainder_solver/main.py batch 
```

4. Il programma genererà un file LaTeX per ogni sistema nella cartella `output/`, con nomi progressivi (solution_1.tex, solution_2.tex, ecc.)

Questa modalità è particolarmente utile per:
- Generare più esercizi in una volta
- Verificare rapidamente più soluzioni
- Creare una raccolta di esempi risolti

## Note per i Docenti

Il programma è particolarmente utile per:
- Creare documentazione facilmente
- Verificare soluzioni degli esercizi fatti a mano
- Fornire agli studenti un modo per avere un riferimento sul come svolgere gli esercizi d'esame

## Licenza

Questo progetto è distribuito sotto la licenza MIT. Vedi il file `LICENSE` per maggiori dettagli. 