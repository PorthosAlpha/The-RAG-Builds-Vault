The **Manual for Each Framework** consists of a triad of technical operating guides designed to manage the **Extractive Evidence RAG Architecture (EERA)** across different computing environments. These manuals ensure that your research instrument remains stable, repeatable, and methodologically defensible, whether you are working on a desktop or a mobile device.

### Overview of the Three Frameworks
The vault contains specific instructions for three primary interfaces:
1.  **[[Instructions for PowerShell]]**: For Windows-based operations.
2.  **[[Instructions for Terminal]]**: For macOS-based operations.
3.  **[[Instructions for Termux]]**: For portable/constrained operations on Android.

### Core Architecture: The Two-Engine System
Regardless of the framework used, the EERA system operates using two simultaneous "engines" that must be started in a specific order:

*   **Engine 1: Evidence Authority (Uvicorn)**
    *   **Purpose**: Ingestion, canonical Markdown storage, and evidence retrieval.
    *   **Port**: Typically runs on `http://127.0.0.1:8000`.
    *   **Rule**: This engine **must** be started first.
*   **Engine 2: Extractive Synthesis (Hypercorn)**
    *   **Purpose**: Assembles verbatim evidence, creates matrices, theory maps, and APA-compliant outputs.
    *   **Port**: Typically runs on `http://127.0.0.1:9000`.
    *   **Rule**: Enforces exact-wording to maintain scholarly integrity.

### Operational Lifecycle
The manuals define a strict "Daily Use Pattern" to ensure data integrity:
1.  **Start Engines**: Activate the virtual environment (`eera`) and launch Uvicorn, then Hypercorn.
2.  **Ingest**: Process your research notes into the system.
3.  **Retrieve & Assemble**: Use the system to find evidence and build synthesis matrices.
4.  **Shut Down**: Use `CTRL + C` to stop both engines gracefully.
5.  **Write**: Transition to human authorship using the evidence artifacts generated.

### Critical Operational Rules
To maintain the "Sovereign Core" of your research, the manuals emphasize several "Do Not" rules:
*   **Do not** edit files directly inside the `corpus/markdown` folder.
*   **Do not** expect the system to write prose; it is an evidence compiler, not an author.
*   **Do not** bypass the virtual environment.
*   **Do not** start Hypercorn without Uvicorn.

### Framework-Specific Notes
*   **Termux**: Highlighted as excellent for portability and reviewing evidence, but limited for heavy analysis or large PDF ingestion.
*   **macOS/Windows**: Recommended for primary dissertation drafting and heavy ingestion tasks.

These manuals collectively provide you with "zero ambiguity" in operating your research environment, ensuring that the technical setup never interferes with the scholarly work.