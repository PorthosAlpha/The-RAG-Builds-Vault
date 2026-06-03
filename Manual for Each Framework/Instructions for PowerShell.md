
Below is your **PowerShell Operating Manual** for the system you built.  
This is written as a **command‑by‑command procedure**, with *no assumptions* and *no missing steps*.  
You can print this, save it as `README_POWERSHELL.md`, or follow it line‑by‑line.

This manual answers **only three things**, exactly as you requested:

1. How to **start the engine**
2. How to **shut it down**
3. How to **start it back up again safely**

Nothing more is needed.

---

# PowerShell Operating Manual  
## Extractive Evidence RAG Architecture (EERA)

---

## SECTION 1 — PREREQUISITES (ONE‑TIME ONLY)

> You do **not** repeat this section unless you move machines.

### 1. Confirm Python Is Available
```powershell
python --version
```
✅ Expected: Python 3.9+  
❌ If not present: install Python from python.org and restart PowerShell.

---

### 2. Navigate to Your Project Root
```powershell
cd C:\path\to\eera
```

> This is the directory that contains:
- `eera_ingest`
- `app`
- `corpus`
- `venv / eera`

---

## SECTION 2 — ACTIVATING THE ENGINE (STARTUP)

This system has **two engines**.  
You start them **separately**, in **two PowerShell windows**.

---

# ENGINE 1 — Evidence Authority Server (Uvicorn)

> This server **ingests, stores, and retrieves evidence**.  
> It must be running **before** synthesis operates.

---

## STEP 1 — Open PowerShell Window #1

---

## STEP 2 — Activate Virtual Environment
```powershell
.\eera\Scripts\Activate.ps1
```

✅ Prompt changes to show `(eera)`

---

## STEP 3 — Navigate to Ingest Service
```powershell
cd eera_ingest
```

---

## STEP 4 — Start the Uvicorn Server
```powershell
uvicorn app.main:app --host 127.0.0.1 --port 8000
```

✅ You should see output similar to:
```
Uvicorn running on http://127.0.0.1:8000
```

✅ **Engine 1 is now running**

Do **not close this window**.

---

### Verification (Optional but Recommended)
Open a browser and go to:
```
http://127.0.0.1:8000/docs
```

If the docs page loads, ingestion is live.

---

# ENGINE 2 — Extractive Synthesis Server (Hypercorn)

> This server **assembles verbatim evidence**.  
> It does **not** ingest or modify text.

---

## STEP 1 — Open PowerShell Window #2

---

## STEP 2 — Activate the Same Virtual Environment
```powershell
.\eera\Scripts\Activate.ps1
```

✅ Prompt shows `(eera)`

---

## STEP 3 — Navigate to Synthesis Service
```powershell
cd eera_ingest
```

*(Same root, different engine)*

---

## STEP 4 — Start Hypercorn
```powershell
hypercorn app.main:app --bind 127.0.0.1:9000
```

✅ Expected output:
```
Running on http://127.0.0.1:9000
```

✅ **Engine 2 is now running**

---

### Verification
Open:
```
http://127.0.0.1:9000/docs
```

If visible, extractive synthesis is live.

---

## ✅ SYSTEM STATUS: FULLY OPERATIONAL

At this point:

| Component | Status |
|--------|------|
| Evidence Ingestion | ✅ Running |
| Retrieval | ✅ Running |
| Extractive Synthesis | ✅ Running |
| Exact‑wording enforcement | ✅ Active |

You may now ingest files, retrieve evidence, and generate matrices.

---

## SECTION 3 — SHUTTING THE SYSTEM DOWN (SAFE STOP)

> Always shut down **gracefully**.  
> Never kill the PowerShell window abruptly if possible.

---

### STEP 1 — Stop Hypercorn (PowerShell Window #2)
Press:
```text
CTRL + C
```

✅ You will see:
```
Stopping server
```

---

### STEP 2 — Stop Uvicorn (PowerShell Window #1)
Press:
```text
CTRL + C
```

✅ Both servers are now offline.

---

## ✅ SAFE SHUTDOWN COMPLETE

Nothing is lost.  
No evidence is modified.  
All data remains immutable.

---

## SECTION 4 — STARTING THE SYSTEM BACK UP

This is the **most important rule**:

> **Always start Uvicorn first, Hypercorn second**

---

### Restart Checklist (In Order)

1. Open two PowerShell windows  
2. Activate environment in both:
```powershell
.\eera\Scripts\Activate.ps1
```

3. Start **Uvicorn**:
```powershell
uvicorn app.main:app --host 127.0.0.1 --port 8000
```

4. Start **Hypercorn**:
```powershell
hypercorn app.main:app --bind 127.0.0.1:9000
```

✅ System restored.

---

## SECTION 5 — COMMON OPERATING MISTAKES (AVOID THESE)

❌ Starting Hypercorn without Uvicorn  
❌ Running servers outside the virtual environment  
❌ Editing files inside `corpus/markdown`  
❌ Expecting the system to “write” findings  

✅ The system **assists analysis**, not authorship.

---

## SECTION 6 — DAILY USE PATTERN (MENTAL MODEL)

1. **Start engines**
2. **Ingest notes**
3. **Retrieve evidence**
4. **Assemble matrices / maps**
5. **Shut down**
6. **Write as a human**

That is the intended life cycle.

---

## FINAL CLOSING NOTE

If you can:
- Turn it on
- Use it
- Turn it off

Then the system is **complete**.

You now have:
- A stable research engine
- A repeatable workflow
- A defensible methodology
- A system that will not betray your scholarship

Nothing further is required.

Manual complete.