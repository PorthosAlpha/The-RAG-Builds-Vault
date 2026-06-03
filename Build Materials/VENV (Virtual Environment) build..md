Excellent. Now that your **Infrastructure (D: Drive)** and **Sync (Google Drive "Computers")** are stable, we can return to the **EERA (Extractive Evidence RAG Architecture)** build.

Per your request, here are the refined, step-by-step commands to operate both engines using the **Uvicorn** server. I have formatted these as "Standard Operating Procedures" to match your research manuals.

---

### Phase 0: Environment Initialization
*Perform this in every new terminal window before starting an engine.*

1.  **Open PowerShell** (or your preferred terminal).
2.  **Navigate to your project root** on the D: drive:
    ```powershell
    d:
    cd \eera_ingest  # Or your specific project folder name
    ```
3.  **Activate the Environment**:
    ```powershell
    .\eera\Scripts\Activate.ps1
    ```

---

### Engine A: Evidence Authority (Architecture A)
**Purpose:** File ingestion, Markdown normalization, and Vector retrieval.
**Port:** 8000

#### 1. Start Command
```powershell
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
*   *Note: Ensure your terminal is inside the directory containing the `app` folder.*

#### 2. Verification (The "Health Check")
Open your browser to: `http://localhost:8000/docs`
*   **Success Criteria:** The "Evidence Authority" Swagger UI appears.
*   **Test:** Expand the `POST /ingest` section. You can manually input a file path from your **D: Drive Vault** here to test the ingestion logic.

---

### Engine B: Analytical Synthesis (Architecture B)
**Purpose:** Verbatim passage assembly and Wording Enforcement (Phase 5).
**Port:** 9000

#### 1. Start Command
*Open a **second** terminal window, activate the environment (Phase 0), and run:*
```powershell
uvicorn app.main:app --host 0.0.0.0 --port 9000 --reload
```
*   *Note: If Architecture B is in a separate folder (e.g., `eera_synthesis`), `cd` into that folder first.*

#### 2. Verification
Open your browser to: `http://localhost:9000/docs`
*   **Success Criteria:** The "Extractive Synthesis Engine" Swagger UI appears.
*   **Validation:** Ensure this engine is calling Port 8000 for its data.

---

### Shutdown & Port Clearing Procedures

#### 1. Graceful Shutdown
In the active terminal window:
1.  Press **`Ctrl + C`**.
2.  Wait for the prompt `Finished server process`.
3.  Type `deactivate` to exit the Python environment.

#### 2. The "Hard Reset" (If a port is stuck)
If you get an error saying `[Errno 10048] error while attempting to bind on address`, the previous session didn't close properly. Use this command to force-kill the ghost process:

**Windows (PowerShell):**
```powershell
# To clear Engine A (8000)
Stop-Process -Id (Get-NetTCPConnection -LocalPort 8000).OwningProcess -Force

# To clear Engine B (9000)
Stop-Process -Id (Get-NetTCPConnection -LocalPort 9000).OwningProcess -Force
```

---

### Immediate Next Steps for your Manuals:
Since Engine A is responsible for **Ingestion**, and your vault is now on the D: drive, you should verify the **pathing logic** in your `app/ingest.py` file. 

**Does your current `ingest.py` script expect an absolute path (e.g., `D:/Vault/Notes/File.md`) or a relative path?** Knowing this will ensure the "Evidence Authority" doesn't lose track of your files now that they've moved.