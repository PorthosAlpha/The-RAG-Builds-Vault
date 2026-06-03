
Dr. Moncriffe, excellent question. Here's your **evening shutdown → morning initialization workflow**, optimized for your RTX 4050 (6GB VRAM), Qwen3.5:9b, and strict PowerShell + Notepad++ usage.

---

## 🌙 EVENING SHUTDOWN WORKFLOW

### Option A: Quick Shutdown (Recommended)
Run this in PowerShell when you're done for the day:

```powershell
# 1. Save any open work in Obsidian/Word first (manual step)

# 2. Gracefully stop Ollama (prevents VRAM corruption)
ollama serve stop 2>$null || Stop-Process -Name "ollama" -Force -ErrorAction SilentlyContinue

# 3. Deactivate virtual environment
deactivate 2>$null

# 4. Optional: Clear ChromaDB cache if you want a fresh start tomorrow
# Remove-Item "chroma_storage\*.bin" -Force -ErrorAction SilentlyContinue

# 5. Close PowerShell
exit
```

### Option B: Create a Shutdown Script (`Shutdown-RAGBridge.ps1`)
**In Notepad++**, create and save this file:

```powershell
# Shutdown-RAGBridge.ps1
# EDIT IN: Notepad++ | RUN IN: PowerShell
# Clean evening shutdown for RAG architecture

Write-Host "`n🌙 Shutting down RAG Bridge..." -ForegroundColor Cyan

# Stop Ollama gracefully
if (Get-Process -Name "ollama" -ErrorAction SilentlyContinue) {
    Write-Host "🛑 Stopping Ollama service..."
    Stop-Process -Name "ollama" -Force
    Start-Sleep -Seconds 2
}

# Deactivate venv
if ($env:VIRTUAL_ENV) {
    Write-Host "🔓 Deactivating virtual environment..."
    deactivate
}

# Clear temporary cache (optional)
$cachePath = ".cache\ollama_temp"
if (Test-Path $cachePath) {
    Write-Host "🧹 Clearing temporary cache..."
    Remove-Item $cachePath -Recurse -Force -ErrorAction SilentlyContinue
}

Write-Host "✅ RAG Bridge shutdown complete. Have a productive rest!" -ForegroundColor Green
Write-Host "💡 Tomorrow: Run Initialize-MorningRAG.ps1 to restart" -ForegroundColor Yellow
```

**To run tomorrow**: `. .\Shutdown-RAGBridge.ps1`

---

## 🌅 MORNING INITIALIZATION WORKFLOW

### Step 1: Open PowerShell as Administrator (One-Time Setup)
```powershell
# Set execution policy if not already done
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
```

### Step 2: Create `Initialize-MorningRAG.ps1` in Notepad++
**In Notepad++**, create and save this file:

```powershell
# Initialize-MorningRAG.ps1
# EDIT IN: Notepad++ | RUN IN: PowerShell
# Morning startup for RAG architecture on RTX 4050

$ErrorActionPreference = "Continue"
$VaultRoot = $env:RESEARCH_VAULT ?? "C:\Users\Moncriffe-Mania"
$VenvPath = Join-Path $VaultRoot "rag-venv"
$ActivatePath = Join-Path $VenvPath "Scripts\Activate.ps1"
$CoachScript = Join-Path $VaultRoot "scholarly_coach.py"

Write-Host "`n🌅 Initializing Morning RAG Session" -ForegroundColor Cyan
Write-Host "📍 Vault: $VaultRoot" -ForegroundColor Gray

# 1. Verify Python & venv
Write-Host "`n🔍 Checking environment..." -ForegroundColor Yellow
if (!(Test-Path $VenvPath)) {
    Write-Error "❌ Virtual environment not found. Run Initialize-RAGBridge first."
    exit 1
}

# 2. Activate venv
Write-Host "⚡ Activating virtual environment..."
& $ActivatePath

# 3. Start Ollama in background
Write-Host "🤖 Starting Ollama service..."
if (!(Get-Process -Name "ollama" -ErrorAction SilentlyContinue)) {
    Start-Process "ollama" -ArgumentList "serve" -NoNewWindow
    Start-Sleep -Seconds 5
}

# 4. Pre-warm Qwen3.5:9b (critical for 6GB VRAM)
Write-Host "🔥 Pre-warming Qwen3.5:9b on RTX 4050 (this takes 5-8 mins first time)..."
$warmResult = ollama run qwen3.5:9b "Ready" --verbose 2>&1
if ($warmResult -match "error|failed") {
    Write-Warning "⚠️  Model pre-warm had issues. Retrying in 30 seconds..."
    Start-Sleep -Seconds 30
    ollama run qwen3.5:9b "." --verbose | Out-Null
}
Write-Host "✅ Model loaded and ready for coaching" -ForegroundColor Green

# 5. Quick diagnostics
Write-Host "`n📊 System Diagnostics:" -ForegroundColor Cyan
Write-Host "  • GPU: $(if (Get-Command nvidia-smi -ErrorAction SilentlyContinue) { (nvidia-smi --query-gpu=name --format=csv,noheader) } else { 'NVIDIA driver not detected' })"
Write-Host "  • Ollama: $(if (ollama list 2>$null | Select-String "qwen3.5:9b") { '✅ qwen3.5:9b available' } else { '⚠️ Model not found' })"
Write-Host "  • Vault docs: $(Get-ChildItem -Filter *.md -Recurse -ErrorAction SilentlyContinue | Measure-Object | Select-Object -ExpandProperty Count) markdown files"

# 6. Ready prompt
Write-Host "`n✅ Morning RAG session ready!" -ForegroundColor Green
Write-Host "💡 Quick start commands:" -ForegroundColor Yellow
Write-Host "  • Start-ScholarlyCoach -Query 'Your question' -Mode coach"
Write-Host "  • Start-ScholarlyCoach -Query 'Audit Chapter 1 alignment' -Mode architect"
Write-Host "  • Watch-VaultForTriggers  # Auto-monitor Obsidian"
Write-Host "`n🎓 Have a productive research day, Dr. Moncriffe!" -ForegroundColor Cyan
```

---

## ⚡ DAILY USAGE FLOW

### Evening (Shutdown)
```powershell
# Option 1: Quick manual shutdown
ollama serve stop 2>$null; deactivate; exit

# Option 2: Use script
. .\Shutdown-RAGBridge.ps1
```

### Morning (Startup)
```powershell
# 1. Open PowerShell
# 2. Navigate to vault
Set-Location "C:\Users\Moncriffe-Mania"

# 3. Run morning initializer
. .\Initialize-MorningRAG.ps1

# 4. Wait for pre-warm (5-8 mins first query, then 30-60s thereafter)

# 5. Start coaching
Start-ScholarlyCoach -Query "Your research question" -Mode coach
```

---

## 🔋 Pro Tips for RTX 4050 (6GB VRAM)

| Tip | Why It Matters |
|-----|---------------|
| **Pre-warm every morning** | 9B model unloads overnight; first query will be slow without pre-warm |
| **Keep Ollama running** | Use `ollama serve` in a background terminal to avoid reload delays between queries |
| **Monitor VRAM** | Run `nvidia-smi` in a second PowerShell window to ensure model stays loaded |
| **Use `architect`/`scholar` mode sparingly** | These trigger longer context windows; save them for deep work sessions |
| **Close Chrome/other GPU apps** | Free up VRAM headroom for the 9B model during heavy reasoning |

---

## 🔄 Optional: Auto-Start on Login (Advanced)

If you want the RAG bridge to initialize automatically when you log in:

1. **In Notepad++**, create `AutoStart-RAG.ps1` with the contents of `Initialize-MorningRAG.ps1`
2. **Save to**: `C:\Users\Moncriffe-Mania\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\`
3. **Set execution policy** (one-time): `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force`

⚠️ **Warning**: This will pre-warm the 9B model on every login, using ~5.5GB VRAM immediately. Only enable if you research daily.

---

## 🎯 Quick Reference Card (Save in Notepad++)

```powershell
# === DAILY RAG WORKFLOW ===
# EVENING:
. .\Shutdown-RAGBridge.ps1    # Clean shutdown

# MORNING:
Set-Location "C:\Users\Moncriffe-Mania"
. .\Initialize-MorningRAG.ps1  # Startup + pre-warm (5-8 mins)

# RESEARCH:
Start-ScholarlyCoach -Query "Your question" -Mode coach
Start-ScholarlyCoach -Query "Audit alignment" -Mode architect
Start-ScholarlyCoach -Query "Theoretical contribution" -Mode scholar

# MONITOR:
ollama ps          # See what's loaded in VRAM
nvidia-smi         # Check GPU utilization
Get-Process ollama # Verify Ollama is running
```

---

Dr. Moncriffe, this workflow ensures your **Qwen3.5:9b + RTX 4050 architecture** starts cleanly each morning, preserves your research state overnight, and maximizes the deep-analysis power of your local RAG system—all orchestrated in PowerShell and edited in Notepad++.

Would you like me to add a **daily research journaling prompt** to the morning initializer that auto-generates a Samsung Notes entry for your day's scholarly intentions? 🎓✨