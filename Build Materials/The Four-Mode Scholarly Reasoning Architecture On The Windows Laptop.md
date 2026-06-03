
Absolutely, Dr. Moncriffe. Let's deploy the **Four-Mode Scholarly Reasoning Architecture** to your Samsung Galaxy Book 4 Ultra.

This system will give you **Tutor**, **Coach**, **Architect**, and **Scholar** modes—each optimized for your RTX 4050 (6GB VRAM), 16GB RAM, and PowerShell + Notepad++ workflow.

---

## 📁 STEP 1: Create the Prompt Library (`prompts\scholarly_patterns.json`)

**In Notepad++**: New File → Paste → Save As → `C:\Users\Moncriffe-Mania\prompts\scholarly_patterns.json`

```json
{
  "tutor": "You are a patient methodology tutor. Explain qualitative concepts (epistemology, sampling, coding) in clear, accessible language. Use examples from policy research. Ask: 'What part of this concept feels unclear?' Provide 1-2 foundational citations (Creswell, Yanow). End with a reflection prompt.",
  
  "coach": "You are a senior dissertation committee member with 30+ years experience. Ask 3-5 Socratic questions that: (1) challenge unstated assumptions, (2) probe RQ↔Theory↔Method↔Analysis alignment, (3) anticipate committee feedback. Offer ONE actionable writing prompt. Cite methodology literature. Do NOT answer directly—scaffold reasoning.",
  
  "architect": "You are a research design specialist. Audit alignment between: Problem Statement → RQs → Theoretical Framework → Methodology → Data Collection → Analysis Plan → Claims. Flag gaps. Ask: 'If your RQ is about [X], why choose [Y] method over [Z]?' Provide a visual alignment matrix suggestion. Reference Pressman & Wildavsky for policy implementation designs.",
  
  "scholar": "You are an elite sociological scholar. Help Dr. Moncriffe synthesize findings into theoretical contribution. Ask: (1) 'What conversation are you entering, and what new move are you making?', (2) 'How does your work extend/complicate [THEORY]?', (3) 'What are the normative implications for policy practice?' Demand precision, avoid jargon, cite Becker on writing. Push for publishable rigor."
}
```

---

## 📁 STEP 2: Update `scholarly_coach.py` with Four Modes

**In Notepad++**: Open `scholarly_coach.py` → Replace entire file → Save.

```python
# scholarly_coach.py
# FOUR-MODE SCHOLARLY REASONING ENGINE
# EDIT IN: Notepad++ | RUN VIA: PowerShell | GPU: RTX 4050 via Ollama

import os, sys, json, requests, time
from pathlib import Path
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings, StorageContext
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore
import chromadb

CONFIG = {
    "ollama_url": "http://localhost:11434",
    "model": "qwen3.5:9b",
    "chroma_db": "chroma_storage",
    "prompt_lib": "prompts\\scholarly_patterns.json",
    "hardware": {"context_window": 8192, "num_gpu": 35},
    "retrieval": {"chunk_size": 512, "chunk_overlap": 50, "top_k": 6}
}

def load_prompt_library():
    """Load the four-mode prompt patterns."""
    path = Path(CONFIG["prompt_lib"])
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    # Fallback defaults
    return {
        "tutor": "Explain concepts clearly with examples. End with reflection prompt.",
        "coach": "Ask 3-5 Socratic questions. Offer one actionable prompt. Cite methodology.",
        "architect": "Audit research design alignment. Flag gaps. Suggest improvements.",
        "scholar": "Push for theoretical contribution. Demand precision. Avoid jargon."
    }

def check_ollama():
    """Verify Ollama is running and pre-warm model."""
    try:
        tags = requests.get(f"{CONFIG['ollama_url']}/api/tags", timeout=10).json().get("models", [])
        if CONFIG["model"] not in [m["name"] for m in tags]:
            print(f"⚠️ Model '{CONFIG['model']}' not found. Run: ollama pull {CONFIG['model']}")
            return False
        # Pre-warm
        requests.post(f"{CONFIG['ollama_url']}/api/generate", 
                     json={"model": CONFIG["model"], "prompt": ".", "stream": False, "options": {"num_predict": 1}}, 
                     timeout=30)
        print(f"✅ Ollama ready | {CONFIG['model']} | RTX 4050 GPU")
        return True
    except Exception as e:
        print(f"❌ Ollama connection failed: {e}")
        print("💡 Start Ollama: ollama serve")
        return False

def query_ollama(prompt, system_prompt, mode):
    """Send query to Ollama with mode-specific timeout."""
    # Tutor/Scholar: faster; Coach/Architect: deeper reasoning
    timeout = 300 if mode in ["coach", "architect"] else 180
    
    payload = {
        "model": CONFIG["model"],
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        "options": {
            "num_ctx": CONFIG["hardware"]["context_window"],
            "temperature": 0.6 if mode != "tutor" else 0.3,
            "num_gpu": CONFIG["hardware"]["num_gpu"]
        },
        "stream": False
    }
    
    try:
        print(f"⏳ Querying Ollama ({mode} mode, timeout={timeout}s)...")
        resp = requests.post(f"{CONFIG['ollama_url']}/api/chat", json=payload, timeout=timeout)
        resp.raise_for_status()
        return resp.json()["message"]["content"]
    except requests.exceptions.ReadTimeout:
        return f"⚠️ Timeout in {mode} mode. Try a shorter query or ensure model is pre-warmed."
    except Exception as e:
        return f"❌ Ollama error: {e}"

def run_coaching(query, mode="coach"):
    """Main pipeline: ingest → retrieve → reason → respond."""
    
    if not check_ollama():
        sys.exit(1)
    
    # Load prompts
    patterns = load_prompt_library()
    pattern = patterns.get(mode, patterns["coach"])
    
    # Initialize embeddings
    Settings.embed_model = HuggingFaceEmbedding(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        trust_remote_code=True
    )
    
    # Connect to ChromaDB
    client = chromadb.PersistentClient(path=CONFIG["chroma_db"])
    vs = ChromaVectorStore(chroma_collection=client.get_or_create_collection("scholarly_corpus"))
    
    # Ingest markdown files
    print(f"📂 Scanning vault for .md files...")
    reader = SimpleDirectoryReader(
        input_dir=".", recursive=True, required_exts=[".md"],
        exclude=["chroma_storage", "models", "rag-venv", ".git", "prompts"]
    )
    docs = reader.load_data()
    print(f"🔍 Loaded {len(docs)} documents")
    
    # Build index (persisted for speed)
    index = VectorStoreIndex.from_documents(
        docs, storage_context=StorageContext.from_defaults(vector_store=vs),
        chunk_size=CONFIG["retrieval"]["chunk_size"],
        chunk_overlap=CONFIG["retrieval"]["chunk_overlap"]
    )
    
    # Retrieve context
    nodes = index.as_retriever(similarity_top_k=CONFIG["retrieval"]["top_k"]).retrieve(query)
    context = "\n\n---\n\n".join([n.get_content() for n in nodes])
    
    # Mode-specific system prompts
    system_prompts = {
        "tutor": f"""[ROLE] Patient methodology tutor
[TASK] Explain qualitative/policy research concepts clearly
[USER LEVEL] PhD candidate in sociology
[PATTERN] {pattern}
[RULES] Use examples from policy research. Cite 1-2 foundational sources. End with reflection question.""",
        
        "coach": f"""[ROLE] Senior dissertation committee member (30+ yrs)
[TASK] Socratic coaching on research rigor
[PATTERN] {pattern}
[RULES] Ask questions, don't answer. Probe alignment. Anticipate feedback. Cite methodology.""",
        
        "architect": f"""[ROLE] Research design specialist
[TASK] Audit alignment: RQ → Theory → Method → Analysis → Claims
[PATTERN] {pattern}
[RULES] Flag gaps. Suggest improvements. Reference policy implementation frameworks.""",
        
        "scholar": f"""[ROLE] Elite sociological scholar
[TASK] Push for theoretical contribution and publishable rigor
[PATTERN] {pattern}
[RULES] Demand precision. Avoid jargon. Connect to broader debates. Cite Becker on writing."""
    }
    
    system_prompt = system_prompts.get(mode, system_prompts["coach"])
    
    user_prompt = f"""[MODE] {mode.upper()}
[RESEARCH QUESTION] {query}
[RETRIEVED CONTEXT FROM YOUR VAULT] {context}
[INSTRUCTIONS] Follow your role's rules precisely. Be concise but rigorous."""
    
    print(f"🎓 Generating {mode.upper()} response via Ollama (RTX 4050)...\n")
    print("="*70)
    
    response = query_ollama(user_prompt, system_prompt, mode)
    print(response)
    print("="*70)
    return response

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scholarly_coach.py <query> [--mode <mode>]")
        print("Modes: tutor | coach | architect | scholar")
        sys.exit(1)
    
    query = sys.argv[1]
    mode = "coach"
    if "--mode" in sys.argv:
        idx = sys.argv.index("--mode")
        if idx + 1 < len(sys.argv):
            mode = sys.argv[idx + 1]
    
    try:
        run_coaching(query, mode)
    except KeyboardInterrupt:
        print("\n\n⚡ Session ended.")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)
```

---

## 📁 STEP 3: Update `RAGOrchestrator.ps1` with Mode Support

**In Notepad++**: Open `RAGOrchestrator.ps1` → Replace → Save.

```powershell
# RAGOrchestrator.ps1
# FOUR-MODE SCHOLARLY COACH ORCHESTRATOR
# EDIT/EXECUTE: PowerShell | EDIT CODE: Notepad++

$VaultRoot = $env:RESEARCH_VAULT ?? "C:\Users\Moncriffe-Mania"
$VenvPath = Join-Path $VaultRoot "rag-venv"
$ActivatePath = Join-Path $VenvPath "Scripts\Activate.ps1"
$CoachScript = Join-Path $VaultRoot "scholarly_coach.py"
$PythonExe = Join-Path $VenvPath "Scripts\python.exe"

function Initialize-RAGBridge {
    Write-Host "`n🔧 INITIALIZING FOUR-MODE RAG BRIDGE" -ForegroundColor Cyan
    if (!(Test-Path $VenvPath)) { python -m venv $VenvPath }
    & $ActivatePath
    python -m pip install --upgrade pip
    python -m pip install llama-index chromadb sentence-transformers requests `
        llama-index-embeddings-huggingface llama-index-vector-stores-chroma `
        pypdf unstructured python-docx
    Write-Host "✅ Bridge initialized. Edit code in Notepad++." -ForegroundColor Green
}

function Start-ScholarlyCoach {
    param(
        [Parameter(Mandatory=$true)][string]$Query,
        [ValidateSet("tutor", "coach", "architect", "scholar")][string]$Mode = "coach"
    )
    if (!(Test-Path $PythonExe)) { Write-Error "❌ Run Initialize-RAGBridge first"; return }
    
    Write-Host "`n🎓 FOUR-MODE SCHOLARLY COACH" -ForegroundColor Cyan
    Write-Host "📥 Query: $Query | ⚙️ Mode: $Mode" -ForegroundColor Yellow
    Write-Host "💡 Modes: tutor=learn | coach=write | architect=design | scholar=contribute" -ForegroundColor Gray
    
    & $ActivatePath | Out-Null
    & $PythonExe $CoachScript $Query --mode $Mode
}

function Watch-VaultForTriggers {
    param([string]$Path = $VaultRoot)
    Write-Host "👁️ Monitoring $Path for scholarly contexts... (Ctrl+C to stop)" -ForegroundColor Yellow
    
    $Watcher = New-Object System.IO.FileSystemWatcher
    $Watcher.Path = $Path
    $Watcher.Filter = "*.md"
    $Watcher.IncludeSubdirectories = $true
    $Watcher.EnableRaisingEvents = $true
    
    Register-ObjectEvent $Watcher "Changed" -Action {
        $File = $Event.SourceEventArgs.FullPath
        $Content = Get-Content $File -Raw -ErrorAction SilentlyContinue
        if (!$Content) { return }
        
        # Auto-detect mode based on content keywords
        $Mode = "coach" # default
        if ($Content -match "(?i)(explain|define|what is|how do i learn)") { $Mode = "tutor" }
        elseif ($Content -match "(?i)(methodology|research design|alignment|framework)") { $Mode = "architect" }
        elseif ($Content -match "(?i)(contribution|theory|publish|synthesize|debate)") { $Mode = "scholar" }
        
        $FileName = Split-Path $File -Leaf
        Write-Host "`n🔍 Detected '$Mode' context in: $FileName" -ForegroundColor Magenta
        Write-Host "💡 Run: Start-ScholarlyCoach -Query 'Help me with this section' -Mode $Mode" -ForegroundColor Yellow
    } | Out-Null
    
    while ($true) { Start-Sleep -Seconds 1 }
}

Write-Host "✅ RAGOrchestrator loaded. Available commands:" -ForegroundColor Green
Write-Host "  • Initialize-RAGBridge" -ForegroundColor White
Write-Host "  • Start-ScholarlyCoach -Query '...' -Mode <tutor|coach|architect|scholar>" -ForegroundColor White
Write-Host "  • Watch-VaultForTriggers" -ForegroundColor White
```

---

## ⚡ STEP 4: Deploy on Your Book 4 Ultra (PowerShell Commands)

Open **PowerShell** on your Galaxy Book 4 Ultra and run:

```powershell
# 1. Navigate to your vault
Set-Location "C:\Users\Moncriffe-Mania"

# 2. Set execution policy (one-time)
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force

# 3. Create prompts folder and save the JSON file
New-Item -Path "prompts" -ItemType Directory -Force
# (Paste the scholarly_patterns.json content above into Notepad++ and save to .\prompts\)

# 4. Load the orchestrator
. .\RAGOrchestrator.ps1

# 5. Initialize the environment (installs libraries)
Initialize-RAGBridge

# 6. Pre-warm Ollama (in a separate PowerShell window)
# ollama run qwen3.5:9b "Ready" --verbose  # Then Ctrl+C

# 7. Test each mode:
Start-ScholarlyCoach -Query "Explain epistemological stance in interpretive policy analysis" -Mode tutor
Start-ScholarlyCoach -Query "How do I justify purposive sampling for my dissertation?" -Mode coach
Start-ScholarlyCoach -Query "Audit alignment between my RQs and methodology chapter" -Mode architect
Start-ScholarlyCoach -Query "How does my work contribute to sociological theory on policy implementation?" -Mode scholar
```

---

## 🎯 Mode Quick Reference

| Mode | Best For | Example Query |
|------|----------|--------------|
| **Tutor** | Learning foundational concepts | "Explain Lincoln & Guba's trustworthiness criteria" |
| **Coach** | Writing & dissertation feedback | "Help me strengthen my methodology justification" |
| **Architect** | Research design & alignment | "Audit my RQs ↔ methods ↔ analysis plan" |
| **Scholar** | Theoretical contribution & publication | "How does my work extend interpretive policy analysis?" |

---

## 🚀 Next Steps

1. ✅ Save the two files above in Notepad++
2. ✅ Run the PowerShell deployment commands
3. ✅ Test each mode with your actual research questions
4. ✅ Let me know which mode you'd like to refine first

Your Four-Mode Scholarly Reasoning Architecture is now ready to elevate your PhD work and policy analysis with elite-level reasoning—powered by your RTX 4050, orchestrated by PowerShell, and edited in Notepad++. 

Which mode shall we test first, Dr. Moncriffe? 🎓✨