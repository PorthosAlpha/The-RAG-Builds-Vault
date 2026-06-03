Below is the **Termux Operating Manual** for your system.  
It completes the triad (PowerShell → macOS Terminal → Termux) and is written as a **precise, command‑by‑command operator guide**.

This manual assumes **no improvisation** and no prior Termux experience beyond installing the app.

---

# Termux Operating Manual  
## Extractive Evidence RAG Architecture (EERA)

> **Context warning (important):**  
> Termux is a **portable / constrained environment**.  
> The system **works correctly**, but it is best used for:
> - Reviewing evidence
> - Lightweight ingestion
> - Matrix generation
> - Inspection and verification  
>
> Primary dissertation work is still best done on macOS or Windows.

---

## SECTION 1 — ONE‑TIME SYSTEM PREPARATION (TERMUX ONLY)

You do this **once** per device.

---

### STEP 1 — Open Termux

Make sure you are using the **official F‑Droid version** (recommended).

---

### STEP 2 — Update Termux Packages
```bash
pkg update && pkg upgrade
```

---

### STEP 3 — Install Required System Packages
```bash
pkg install python git openssl libffi clang
```

✅ These are required for Python, virtual environments, and crypto libraries.

---

### STEP 4 — Verify Python
```bash
python --version
```

✅ Python 3.10+ is typical in Termux.

---

## SECTION 2 — PROJECT SETUP (ONE‑TIME IF NOT COPIED FROM DESKTOP)

> If you already copied your project folder from macOS/Windows, **skip cloning**.

---

### OPTION A — Clone from Git (If Applicable)
```bash
git clone https://your-repo-url/eera.git
cd eera
```

---

### OPTION B — Copy Project Manually
Place the `eera` project folder inside:
```
/data/data/com.termux/files/home/
```

Then:
```bash
cd eera
```

---

## SECTION 3 — CREATE / ACTIVATE VIRTUAL ENVIRONMENT

> Termux does not always auto‑activate venvs correctly.  
> Follow **exactly**.

---

### STEP 1 — Create Virtual Environment (If Not Present)
```bash
python -m venv eera
```

---

### STEP 2 — Activate Environment
```bash
source eera/bin/activate
```

✅ Prompt changes to:
```
(eera) $
```

---

### STEP 3 — Install Python Dependencies
```bash
pip install --upgrade pip
pip install fastapi uvicorn hypercorn python-docx pdfplumber \
            markdownify markdown-it-py beautifulsoup4 \
            sentence-transformers faiss-cpu
```

⚠️ This may take time on mobile. Be patient.  
If FAISS fails, use retrieval lightly or copy the built index from desktop.

---

## SECTION 4 — STARTING THE SYSTEM (TERMUX)

You will run **two sessions**, but in Termux this typically means:

- Two Termux sessions
- Or one session + background processes

### Strong Recommendation  
➡️ **Use two Termux sessions**

---

# ENGINE 1 — Evidence Authority (Uvicorn)

---

### STEP 1 — Open Termux Session #1

---

### STEP 2 — Activate Environment
```bash
cd ~/eera
source eera/bin/activate
```

---

### STEP 3 — Navigate to Ingest Service
```bash
cd eera_ingest
```

---

### STEP 4 — Start Uvicorn
```bash
uvicorn app.main:app --host 127.0.0.1 --port 8000
```

✅ Expected:
```
Uvicorn running on http://127.0.0.1:8000
```

✅ **Engine 1 is live**

Leave this session running.

---

# ENGINE 2 — Extractive Synthesis (Hypercorn)

---

### STEP 1 — Open Termux Session #2

Swipe → *New session*

---

### STEP 2 — Activate Environment
```bash
cd ~/eera
source eera/bin/activate
```

---

### STEP 3 — Navigate to Service Root
```bash
cd eera_ingest
```

---

### STEP 4 — Start Hypercorn
```bash
hypercorn app.main:app --bind 127.0.0.1:9000
```

✅ Expected:
```
Running on http://127.0.0.1:9000
```

✅ **Engine 2 is live**

---

## SECTION 5 — VERIFICATION (TERMUX)

Termux has no browser by default. Use:

- A mobile browser on the same device
- Or test with `curl`

---

### Test Uvicorn
```bash
curl http://127.0.0.1:8000/docs
```

---

### Test Hypercorn
```bash
curl http://127.0.0.1:9000/docs
```

✅ HTML output = OK

---

## SECTION 6 — SAFE SHUTDOWN (TERMUX)

---

### STEP 1 — Stop Hypercorn (Session #2)
Press:
```text
CTRL + C
```

---

### STEP 2 — Stop Uvicorn (Session #1)
Press:
```text
CTRL + C
```

✅ Both engines stopped cleanly.

---

## SECTION 7 — RESTARTING THE SYSTEM (TERMUX)

Always restart in **this order**.

---

### Session #1 (Uvicorn)
```bash
cd ~/eera
source eera/bin/activate
cd eera_ingest
uvicorn app.main:app --host 127.0.0.1 --port 8000
```

---

### Session #2 (Hypercorn)
```bash
cd ~/eera
source eera/bin/activate
cd eera_ingest
hypercorn app.main:app --bind 127.0.0.1:9000
```

✅ System fully operational again.

---

## SECTION 8 — WHAT TERMUX IS BEST USED FOR

✅ Reviewing evidence matrices  
✅ Inspecting verbatim outputs  
✅ Running theory maps  
✅ Validating audit logs  
✅ Portability and redundancy  

⚠️ Not recommended for:
- Heavy PDF ingestion
- Large embedding jobs
- Primary dissertation drafting

---

## FINAL OPERATIONAL SUMMARY

| Task | Termux |
|----|------|
| Start engine | ✅ Yes |
| Shut down cleanly | ✅ Yes |
| Retrieve exact wording | ✅ Yes |
| Build matrices | ✅ Yes |
| Heavy analysis | ⚠️ Limited |
| Portability | ✅ Excellent |

---

## CLOSING STATEMENT

Across **PowerShell**, **macOS Terminal**, and **Termux**, you now have:

- One system  
- One methodology  
- Three operating environments  
- Zero ambiguity  

You can start it.  
You can stop it.  
You can restart it at will.

Nothing further is required.

**Termux Manual complete.**