#Requires -Version 5.1
<#
.SYNOPSIS
Automates the installation of LightRAG on Windows.
Assumes you have temporarily disabled Defender hardening (if needed).
#>

$ErrorActionPreference = "Stop"

Write-Host "LightRAG Windows Setup" -ForegroundColor Cyan
Write-Host "=======================" -ForegroundColor Cyan

# --------------------------------------------------
# 0. Warn if Defender real-time protection is still ON
# --------------------------------------------------
$mpStatus = Get-MpComputerStatus
if ($mpStatus.RealTimeProtectionEnabled) {
    Write-Host "[WARN] Real-time Defender protection is ACTIVE." -ForegroundColor Yellow
    Write-Host "       The installation may be blocked by ASR rules or Controlled Folder Access." -ForegroundColor Yellow
    Write-Host "       Consider running the 'TempDisableDefender.ps1' script first." -ForegroundColor Yellow
    Write-Host "       Press any key to continue anyway, or Ctrl+C to abort." -ForegroundColor Yellow
    $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
}

# --------------------------------------------------
# 1. Prerequisite checks & installs via winget
# --------------------------------------------------
function Test-CommandExists($cmd) {
    return [bool](Get-Command $cmd -ErrorAction SilentlyContinue)
}

function Install-WithWinget($packageId, $name) {
    if (Test-CommandExists "winget") {
        Write-Host "[INFO] Installing $name via winget..." -ForegroundColor Green
        winget install --id $packageId --accept-source-agreements --accept-package-agreements
    } else {
        Write-Host "[ERROR] winget not available. Please install $name manually." -ForegroundColor Red
        Write-Host "  Python: https://www.python.org/downloads/"
        Write-Host "  Git:    https://git-scm.com/"
        Write-Host "  Bun:    https://bun.sh/"
        exit 1
    }
}

# Python
if (-not (Test-CommandExists "python")) {
    Install-WithWinget "Python.Python.3.12" "Python 3.12"
    # Refresh PATH
    $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
}

# Git
if (-not (Test-CommandExists "git")) {
    Install-WithWinget "Git.Git" "Git"
    $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
}

# Bun (preferred) or npm
$useBun = $true
if (-not (Test-CommandExists "bun")) {
    Write-Host "[INFO] Bun not found. Attempting to install..." -ForegroundColor Yellow
    try {
        powershell -c "irm bun.sh/install.ps1 | iex"
        $env:Path += ";$env:USERPROFILE\.bun\bin"
    } catch {
        Write-Host "[WARN] Bun install failed; will fall back to npm." -ForegroundColor Yellow
        $useBun = $false
        if (-not (Test-CommandExists "npm")) {
            Install-WithWinget "OpenJS.NodeJS" "Node.js"
            $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
        }
    }
}

Write-Host "[OK] Prerequisites satisfied." -ForegroundColor Green

# --------------------------------------------------
# 2. Clone the LightRAG repository
# --------------------------------------------------
$repoUrl = "https://github.com/HKUDS/LightRAG.git"
$repoDir = Join-Path $env:USERPROFILE "LightRAG"
if (Test-Path $repoDir) {
    Write-Host "[INFO] Repository already exists. Pulling latest changes..." -ForegroundColor Yellow
    Set-Location $repoDir
    git pull
} else {
    Write-Host "[INFO] Cloning LightRAG repository..." -ForegroundColor Green
    git clone $repoUrl $repoDir
    Set-Location $repoDir
}

# --------------------------------------------------
# 3. Create Python virtual environment & install LightRAG
# --------------------------------------------------
$venvPath = Join-Path $repoDir ".venv"
if (-not (Test-Path $venvPath)) {
    Write-Host "[INFO] Creating Python virtual environment..." -ForegroundColor Green
    python -m venv $venvPath
}

# Activate virtual environment (within this script scope)
$activateScript = Join-Path $venvPath "Scripts" "Activate.ps1"
. $activateScript

Write-Host "[INFO] Upgrading pip and installing LightRAG[api]..." -ForegroundColor Green
python -m pip install --upgrade pip
pip install -e ".[api]"

# --------------------------------------------------
# 4. Build the React frontend
# --------------------------------------------------
$webuiDir = Join-Path $repoDir "lightrag_webui"
Set-Location $webuiDir

if ($useBun) {
    Write-Host "[INFO] Installing frontend dependencies with Bun..." -ForegroundColor Green
    bun install --frozen-lockfile
    Write-Host "[INFO] Building frontend..." -ForegroundColor Green
    bun run build
} else {
    Write-Host "[INFO] Installing frontend dependencies with npm..." -ForegroundColor Green
    npm install
    Write-Host "[INFO] Building frontend..." -ForegroundColor Green
    npm run build
}

Set-Location $repoDir

# --------------------------------------------------
# 5. Prepare .env configuration file
# --------------------------------------------------
$envExample = Join-Path $repoDir ".env.example"
$envFile = Join-Path $repoDir ".env"

if (-not (Test-Path $envFile)) {
    Write-Host "[INFO] Copying .env.example to .env..." -ForegroundColor Green
    Copy-Item $envExample $envFile
    Write-Host "[INFO] IMPORTANT: Please edit the .env file with your API keys:" -ForegroundColor Yellow
    Write-Host "         notepad $envFile" -ForegroundColor Yellow
} else {
    Write-Host "[INFO] .env file already exists. Skipping copy." -ForegroundColor Green
}

# --------------------------------------------------
# 6. Create a convenient start script
# --------------------------------------------------
$startScript = Join-Path $repoDir "start.ps1"
@"
# LightRAG Server Launcher
Set-Location "$repoDir"
& "$activateScript"
lightrag-server
"@ | Set-Content -Path $startScript -Encoding UTF8
Write-Host "[INFO] Created start.ps1 launcher." -ForegroundColor Green

# --------------------------------------------------
# Done
# --------------------------------------------------
Write-Host ""
Write-Host "======================================" -ForegroundColor Cyan
Write-Host " LightRAG installation completed!" -ForegroundColor Green
Write-Host " Next steps:" -ForegroundColor Cyan
Write-Host "  1. Edit $envFile and add your LLM/embedding API keys."
Write-Host "  2. Run 'start.ps1' to launch the server."
Write-Host "  3. Open http://localhost:9621 in your browser."
Write-Host "======================================" -ForegroundColor Cyan