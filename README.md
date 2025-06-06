# Risolutore di Sistemi di Congruenze

Questo programma genera soluzioni dettagliate per gli esercizi riguardanti sistemi di congruenze lineari, utilizzando il Teorema Cinese del Resto. 

## Caratteristiche

- Risolve sistemi di due congruenze lineari
- Genera soluzioni passo-passo in formato LaTeX
- Include dimostrazioni dettagliate di ogni passaggio
- Calcola automaticamente MCD, MCM e coefficienti di Bézout
- Produce output LaTeX pronto per la compilazione

## Requisiti

- Python 3.6+
- pdflatex (per la generazione dei PDF)
- sympy (pacchetto Python)

## Installazione

### Windows

1. Installa Python:
   - Scarica Python da [python.org](https://www.python.org/downloads/)
   - Durante l'installazione, assicurati di selezionare "Add Python to PATH"
   - Verifica l'installazione aprendo il Prompt dei comandi e digitando:
     ```bash
     python --version
     ```

2. Installa MiKTeX (per pdflatex):
   - Scarica MiKTeX da [miktex.org](https://miktex.org/download)
   - Durante l'installazione, seleziona "Install for all users"
   - Aggiungi MiKTeX al PATH di sistema:
     - Apri le Impostazioni di Sistema
     - Vai su Variabili d'ambiente
     - Nella sezione "Variabili di sistema", trova "Path"
     - Aggiungi il percorso di MiKTeX (tipicamente `C:\Program Files\MiKTeX\miktex\bin\x64`)

3. Installa le dipendenze Python:
   ```bash
   pip install -r requirements.txt
   ```

### Linux (Ubuntu/Debian)

1. Installa Python:
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   ```

2. Installa pdflatex:
   ```bash
   sudo apt install texlive-latex-base
   ```

3. Installa le dipendenze Python:
   ```bash
   pip3 install -r requirements.txt
   ```

### macOS

1. Installa Python:
   - Usa Homebrew:
     ```bash
     brew install python
     ```
   - Oppure scarica da [python.org](https://www.python.org/downloads/)

2. Installa pdflatex:
   ```bash
   brew install mactex
   ```

3. Installa le dipendenze Python:
   ```bash
   pip3 install -r requirements.txt
   ```

## Utilizzo

### Modalità Interattiva

```bash
python -m chinese_remainder_solver.main
```

### Modalità Batch

```bash
python -m chinese_remainder_solver.main batch
```

I file di output verranno generati nella directory `output/`.

## Formato Input

### Modalità Interattiva
Inserisci le congruenze nel formato:
```
a n
b m
```
dove:
- `a` è il resto della prima congruenza
- `n` è il modulo della prima congruenza
- `b` è il resto della seconda congruenza
- `m` è il modulo della seconda congruenza

### Modalità Batch
Crea un file JSON con il seguente formato:
```json
[
  {
    "system": [[a1, m1], [a2, m2]],
    "description": "Descrizione del test case",
    "options": {
      "output_format": "pdf"
    }
  }
]
```

## Note

- Se pdflatex non è installato, il programma funzionerà solo in modalità LaTeX (senza generazione PDF)
- I file LaTeX generati possono essere compilati manualmente usando un editor LaTeX come TeXstudio o Overleaf
- Per problemi di installazione su Windows, assicurati che MiKTeX sia correttamente aggiunto al PATH di sistema

## Licenza

MIT License