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
- Pacchetti Python: `sympy`
- (Opzionale) Distribuzione LaTeX per compilare i file generati

## Installazione

### Windows

#### 1. Installazione di Python
1. Scarica Python dal [sito ufficiale](https://www.python.org/downloads/windows/)
2. Durante l'installazione, assicurati di spuntare "Add Python to PATH"
3. Verifica l'installazione aprendo il Prompt dei Comandi (cmd) e digitando:
   ```cmd
   python --version
   ```

#### 2. Installazione del progetto
1. Apri il Prompt dei Comandi
2. Clona la repository:
   ```cmd
   git clone https://github.com/1Ricc/tcr-py-to-latex-solver.git
   cd tcr-py-to-latex-solver
   ```
3. Installa le dipendenze:
   ```cmd
   pip install sympy
   ```

#### 3. (Opzionale) Installazione LaTeX
- Scarica e installa [MiKTeX](https://miktex.org/download) per Windows
- Oppure usa [TeX Live](https://www.tug.org/texlive/)

### macOS

#### 1. Installazione di Python
**Opzione A - Homebrew (consigliata):**
1. Installa Homebrew se non ce l'hai:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2. Installa Python:
   ```bash
   brew install python
   ```

**Opzione B - Sito ufficiale:**
1. Scarica Python dal [sito ufficiale](https://www.python.org/downloads/macos/)
2. Installa seguendo le istruzioni
3. Verifica con:
   ```bash
   python3 --version
   ```

#### 2. Installazione del progetto
1. Apri il Terminale
2. Clona la repository:
   ```bash
   git clone https://github.com/1Ricc/tcr-py-to-latex-solver.git
   cd tcr-py-to-latex-solver
   ```
3. Installa le dipendenze:
   ```bash
   pip3 install sympy
   ```

#### 3. (Opzionale) Installazione LaTeX
- Installa MacTeX:
  ```bash
  brew install --cask mactex
  ```
- Oppure scarica da [MacTeX](https://www.tug.org/mactex/)

### Linux (Ubuntu/Debian)

#### 1. Installazione di Python
1. Aggiorna i pacchetti:
   ```bash
   sudo apt update
   ```
2. Installa Python e pip:
   ```bash
   sudo apt install python3 python3-pip
   ```
3. Verifica l'installazione:
   ```bash
   python3 --version
   pip3 --version
   ```

#### 2. Installazione del progetto
1. Installa git se non ce l'hai:
   ```bash
   sudo apt install git
   ```
2. Clona la repository:
   ```bash
   git clone https://github.com/1Ricc/tcr-py-to-latex-solver.git
   cd tcr-py-to-latex-solver
   ```
3. Installa le dipendenze:
   ```bash
   pip3 install sympy
   ```

#### 3. (Opzionale) Installazione LaTeX
```bash
sudo apt install texlive-full
```
Per un'installazione più leggera:
```bash
sudo apt install texlive-latex-base texlive-latex-recommended
```

### Arch Linux

#### 1. Installazione di Python
```bash
sudo pacman -S python python-pip
```

#### 2. Installazione del progetto
```bash
sudo pacman -S git
git clone https://github.com/1Ricc/tcr-py-to-latex-solver.git
cd tcr-py-to-latex-solver
pip install sympy
```

#### 3. (Opzionale) Installazione LaTeX
```bash
sudo pacman -S texlive-most
```

## Utilizzo

### Da riga di comando

1. Apri il terminale/prompt dei comandi e naviga nella cartella del progetto:
   ```bash
   cd tcr-py-to-latex-solver
   ```

2. Esegui il programma:
   **Windows:**
   ```cmd
   python chinese_remainder_solver/main.py
   ```
   **macOS/Linux:**
   ```bash
   python3 chinese_remainder_solver/main.py
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
   **Windows:**
   ```cmd
   python chinese_remainder_solver/main.py batch 
   ```
   **macOS/Linux:**
   ```bash
   python3 chinese_remainder_solver/main.py batch 
   ```

4. Il programma genererà un file LaTeX per ogni sistema nella cartella `output/`, con nomi progressivi (solution_1.tex, solution_2.tex, ecc.)

Questa modalità è particolarmente utile per:
- Generare più esercizi in una volta
- Verificare rapidamente più soluzioni
- Creare una raccolta di esempi risolti

## Risoluzione Problemi

### Python non riconosciuto
- **Windows:** Assicurati di aver spuntato "Add Python to PATH" durante l'installazione
- **macOS/Linux:** Prova `python3` invece di `python`

### Modulo sympy non trovato
```bash
pip install --user sympy    # Windows
pip3 install --user sympy   # macOS/Linux
```

### Problemi con i permessi su Linux/macOS
Se hai problemi con i permessi, usa:
```bash
pip3 install --user sympy
```

### Git non installato
- **Windows:** Scarica da [git-scm.com](https://git-scm.com/download/win)
- **macOS:** Installa con `brew install git` o Xcode Command Line Tools
- **Linux:** Usa il package manager della tua distribuzione

## Note per i Docenti

Il programma è particolarmente utile per:
- Creare documentazione facilmente
- Verificare soluzioni degli esercizi fatti a mano
- Fornire agli studenti un modo per avere un riferimento sul come svolgere gli esercizi d'esame

## Licenza

Questo progetto è distribuito sotto la licenza MIT. Vedi il file `LICENSE` per maggiori dettagli.