Below is the **MacOS Terminal Operating Manual** for your system.  
It mirrors the PowerShell manual **step‑for‑step**, translated precisely into **macOS Terminal commands and conventions**.

This is an **operator’s manual**, not a tutorial.

---

# macOS Terminal Operating Manual  
## Extractive Evidence RAG Architecture (EERA)

---

## SECTION 1 — PREREQUISITES (ONE‑TIME ONLY)

> You do **not** repeat this section unless you change machines.

---

### 1. Verify Python Installation
```bash
python3 --version
```

✅ Required: **Python 3.9 or higher**  
❌ If missing: install via **Homebrew** or python.org, then reopen Terminal.

---

### 2. Navigate to the Project Root
```bash
cd /path/to/eera
```

Your root directory must contain:
- `eera/` (virtual environment)
- `eera_ingest/`
- `app/`
- `corpus/`

---

## SECTION 2 — STARTING THE SYSTEM (ENGINE STARTUP)

The system consists of **two engines**.  
They **must run simultaneously** in **two Terminal windows or tabs**.

---

# ENGINE 1 — Evidence Authority Server (Uvicorn)

**Purpose**
- File ingestion
- Canonical Markdown storage
- Evidence retrieval

This engine **must start first**.

---

### STEP 1 — Open Terminal Window #1

---

### STEP 2 — Activate the Virtual Environment
```bash
source eera/bin/activate
```

✅ Prompt changes to show:
```
(eera) yourname@machine %
```

---

### STEP 3 — Navigate to the Ingest Service
```bash
cd eera_ingest
```

---

### STEP 4 — Start Uvicorn
```bash
uvicorn app.main:app --host 127.0.0.1 --port 8000
```

✅ You should see:
```
Uvicorn running on http://127.0.0.1:8000
```

✅ **Engine 1 is live**

**Do not close this window.**

---

### Verification (Optional)
Open Safari or Chrome and visit:
```
http://127.0.0.1:8000/docs
```

If the API docs load, ingestion is active.

---

# ENGINE 2 — Extractive Synthesis Server (Hypercorn)

**Purpose**
- Verbatim evidence assembly
- Matrices, theory maps, APA outputs
- Exact‑wording enforcement

---

### STEP 1 — Open Terminal Window #2

---

### STEP 2 — Activate the SAME Virtual Environment
```bash
source eera/bin/activate
```

✅ Prompt shows `(eera)`

---

### STEP 3 — Navigate to the Same Service Root
```bash
cd eera_ingest
```

---

### STEP 4 — Start Hypercorn
```bash
hypercorn app.main:app --bind 127.0.0.1:9000
```

✅ Expected output:
```
Running on http://127.0.0.1:9000
```

✅ **Engine 2 is live**

---

### Verification
Open:
```
http://127.0.0.1:9000/docs
```

If documentation loads, extractive synthesis is active.

---

## ✅ SYSTEM STATUS: OPERATIONAL

| Component | Status |
|---------|--------|
| Evidence ingestion | ✅ Running |
| Canonical Markdown | ✅ Locked |
| Retrieval | ✅ Active |
| Verbatim synthesis | ✅ Enforced |
| Auditability | ✅ On |

---

## SECTION 3 — SAFE SHUTDOWN PROCEDURE

> Always shut down intentionally.  
> Never force‑close Terminal unless absolutely necessary.

---

### STEP 1 — Stop Hypercorn (Terminal Window #2)
Press:
```text
CTRL + C
```

✅ Terminal prints shutdown messages.

---

### STEP 2 — Stop Uvicorn (Terminal Window #1)
Press:
```text
CTRL + C
```

✅ Ingestion services stop cleanly.

---

## ✅ SYSTEM SHUTDOWN COMPLETE

- No data lost
- Evidence unchanged
- Corpus remains immutable

---

## SECTION 4 — RESTARTING THE SYSTEM

> Always restart in this order:
> **Uvicorn → Hypercorn**

---

### Restart Checklist

#### Terminal Window #1
```bash
cd /path/to/eera
source eera/bin/activate
cd eera_ingest
uvicorn app.main:app --host 127.0.0.1 --port 8000
```

#### Terminal Window #2
```bash
cd /path/to/eera
source eera/bin/activate
cd eera_ingest
hypercorn app.main:app --bind 127.0.0.1:9000
```

✅ System fully restored.

---

## SECTION 5 — NORMAL DAILY OPERATION

This is how the system is intended to be used:

1. **Start Uvicorn**
2. **Start Hypercorn**
3. **Ingest your notes**
4. **Retrieve and assemble evidence**
5. **Export matrices / tables**
6. **Shut everything down**
7. **Write as a human researcher**

---

## SECTION 6 — OPERATIONAL RULES (DO NOT BREAK THESE)

❌ Do not edit files inside `corpus/markdown`  
❌ Do not expect the system to write prose  
❌ Do not bypass the virtual environment  
❌ Do not start Hypercorn without Uvicorn  

✅ Treat outputs as **evidence artifacts**, not text drafts.

---

## FINAL STATEMENT

If you can:
- Open two Terminal windows
- Run four commands in each
- Press `CTRL + C` to stop

Then you **fully control the system**.

You are operating a:
- Research instrument
- Evidence compiler
- Methodologically defensible analytic engine

Nothing further is required.

**macOS Terminal Manual complete.**