# VS Code as a Super-Powered Text Editor (No AI) — Full Step-by-Step Guide

You want VS Code to be a **blazing-fast code editor/corrector** — paste code in, fix it, save it. No AI. Here's exactly how to set it up and use it.

---

## 🏗️ PHASE 1: One-Time Setup (Do This Once)

### Step 1 — Install VS Code (if not already)

|Setting|What to Check|
|---|---|
|✅ Add to PATH|So you can type `code .` in terminal|
|✅ "Open with Code" in right-click menu|Right-click any file → Open with Code|
|✅ Desktop shortcut|Quick launch|

> Verify install: Open terminal → type `code --version` → should show `1.108+` (May 2026)

---

### Step 2 — Disable Everything You Don't Need

Press **`Ctrl + ,`** → opens Settings → click the **📄 Open Settings (JSON)** icon (top-right) → paste this:

```json
json{
  // ── TEXT EDITOR MODE (no language servers eating RAM) ──
  "editor.formatOnSave": false,
  "editor.formatOnType": false,
  "editor.formatOnPaste": false,
  "editor.detectIndentation": false,
  "editor.autoIndent": "keep",

  // ── SEE INVISIBLE CHARACTERS ──
  "editor.renderWhitespace": "all",
  "editor.renderIndentGuides": true,

  // ── COMFORTABLE EDITING ──
  "editor.wordWrap": "on",
  "editor.wrappingIndent": "same",
  "editor.tabSize": 4,
  "editor.insertSpaces": true,
  "editor.fontSize": 14,
  "editor.lineNumbers": "on",
  "editor.minimap.enabled": false,
  "editor.cursorStyle": "line",
  "editor.cursorBlinking": "smooth",
  "editor.smoothScrolling": true,

  // ── FILES ──
  "files.trimTrailingWhitespace": true,
  "files.insertFinalNewline": true,
  "files.autoSave": "afterDelay",

  // ── UI: MINIMAL DISTRACTIONS ──
  "workbench.activityBar.visible": false,
  "workbench.startupEditor": "none",

  // ── TURN OFF ALL AI (IMPORTANT) ──
  "github.copilot.enable": {
    "*": false
  },
  "github.copilot.chat.enable": false,
  "copilot.enable": {
    "*": false
  }
}
```

> 💡 This turns VS Code into a **pure text editor**. No background language servers, no AI, no distractions. It'll feel like Sublime Text but better.

---

### Step 3 — Install These 6 Extensions (Non-AI, Code Correction Only)

Press **`Ctrl + Shift + X`** → search each → Install:

|#|Extension|Why You Need It|
|---|---|---|
|1|**Error Lens**|Shows errors **directly in the code line** — no need to hover|
|2|**Bracket Pair Colorizer 2**|Color-codes matching `()` `[]` `{}` — instantly spot missing brackets|
|3|**Prettier - Code formatter**|One-click code formatting (you control when)|
|4|**ESLint**|Catches JS/TS errors + auto-fixes many of them|
|5|**Text Power Tools**|Sort lines, dedupe, trim, case convert — all offline, no AI|
|6|**Trailing Spaces**|Highlights + removes trailing spaces on save|

> ⚠️ **Do NOT install** Copilot, CodeGeeX, Tabnine, or any "AI" extension. You said no AI.

---

## 🔄 PHASE 2: Your Daily Workflow (Paste → Fix → Save)

This is the exact sequence every time you open a code file:

```
┌──────────────────────────────────────────────────┐
│                                                    │
│  1️⃣  Paste your code (Ctrl+V)                     │
│       ↓                                            │
│  2️⃣  Look at the red/yellow underlines             │
│       ↓                                            │
│  3️⃣  Hover or press Ctrl+. → Quick Fix             │
│       ↓                                            │
│  4️⃣  Multi-cursor edit what needs fixing           │
│       ↓                                            │
│  5️⃣  Format with Shift+Alt+F (when ready)          │
│       ↓                                            │
│  6️⃣  Save (Ctrl+S) → Done ✅                       │
│                                                    │
└──────────────────────────────────────────────────┘
```

---

## ⚡ PHASE 3: The Actual Tools You'll Use Every Day

### 🔧 Tool 1: Quick Fix — `Ctrl + .` (THE Most Important One)

This is your **#1 code correction tool**. No AI. Pure language server.

|What to Do|How|
|---|---|
|See a red squiggle?|Click it OR press **`Ctrl + .`**|
|A menu pops up with fixes|Pick one → it auto-applies|

**What it fixes automatically**:

|Language|Examples|
|---|---|
|JavaScript/TypeScript|Auto-import missing modules, fix spelling, add missing `;`|
|Python|Add missing imports, fix indentation, correct typos|
|React|Auto-import `useState`, `useEffect` from `'react'`|
|HTML|Close unclosed tags|
|CSS|Fix invalid properties|

> 🎯 **Rule: If you see a red underline, `Ctrl + .` first. Always.**

---

### 🔧 Tool 2: Multi-Cursor Editing — Fix 10 Lines at Once

This is where VS Code **destroys** every other text editor.

|Technique|Keys|When to Use|
|---|---|---|
|**Add cursor at click**|`Alt + Click`|Add cursor anywhere — type in all at once|
|**Select next same word**|`Ctrl + D`|Keep pressing to select more → type to replace all|
|**Column (vertical) select**|`Alt + Shift + Drag` or `Alt + Shift + ↑/↓`|Edit a vertical column — e.g., add `//` to 20 lines|
|**Add cursor to all matches**|`Ctrl + Shift + L`|Splits selection into one cursor per line|
|**Skip current match**|`Ctrl + K, Ctrl + D`|Deselect current, keep others|

**Real example — you paste 20 lines of Python, all missing `self.`**:

```
# Before (pasted):
def calculate(x):
    return x * rate        # ← missing self.

def process(data):
    return data.length     # ← missing self.
```

```
# Put cursor on "rate" → press Ctrl+D 4 times → type "self." → DONE:
def calculate(x):
    return x * self.rate

def process(data):
    return self.data.length
```

**That took 3 seconds instead of 2 minutes.**

---

### 🔧 Tool 3: Find & Replace with Regex — `Ctrl + H`

Press **`Ctrl + H`** → click the **`.*`** button (Use Regular Expression).

|Problem|Find|Replace|
|---|---|---|
|Remove all trailing spaces|`+$`|_(leave empty)_|
|Convert `var` → `let`|`\bvar\b`|`let`|
|Remove empty lines|`^\s*$\n`|_(leave empty)_|
|Fix inconsistent quotes|`(["'])`|`"` _(use with caution)_|
|Add semicolons at end of lines|`([^;])$`|`$1;`|

---

### 🔧 Tool 4: Format on Demand — `Shift + Alt + F`

|Action|Keys|What It Does|
|---|---|---|
|Format entire file|`Shift + Alt + F`|Prettier cleans up the whole file|
|Format selection only|`Ctrl + K, Ctrl + F`|Only fixes the highlighted part|

> 💡 Only format **after** you've fixed the errors. Formatting first can hide what's broken.

---

### 🔧 Tool 5: Command Palette — `Ctrl + Shift + P`

This is the **master switch**. Anything you can't find in menus, type here.

|Type This|What Happens|
|---|---|
|`>Format Document`|Run Prettier|
|`>Change Language Mode`|Force a language (e.g., paste HTML into a `.txt` file → set to HTML)|
|`>Sort Lines Ascending`|Sort selected lines (Text Power Tools)|
|`>Trim Trailing Whitespace`|Clean up spaces|
|`>Convert to Uppercase`|Change case of selection|
|`>Duplicate Line`|Duplicate current line|
|`>Join Lines`|Merge multiple lines into one|

---

## 📋 PHASE 4: The Optimal Settings Cheat Sheet

Print this. Stick it on your wall.

|Shortcut|Action|Use It For|
|---|---|---|
|`Ctrl + P`|Quick file open|Jump to any file instantly|
|`Ctrl + Shift + F`|Global search|Find something across all files|
|`Ctrl + G`|Go to line|Jump to line 47|
|`Ctrl + D`|Select next match|Bulk edit same word|
|`Ctrl + .`|**Quick Fix**|**Auto-fix errors** ⭐|
|`Ctrl + /`|Toggle comment|Comment/uncomment lines|
|`Ctrl + Shift + K`|Delete line|Kill a line fast|
|`Ctrl + Alt + ↑/↓`|Move line up/down|Reorder lines|
|`Ctrl + Z`|Undo|Oops|
|`Ctrl + Shift + Z`|Redo|Oh wait, undo that undo|
|`Alt + ↑/↓`|Move line up/down|Same as above (Mac: Option)|
|`Shift + Alt + F`|Format document|Clean up code|
|`Ctrl + K, Ctrl + F`|Format selection|Clean up just a block|
|`Ctrl +` `|Toggle terminal|Quick terminal without leaving|
|`Alt + Click`|Multi-cursor|Edit 5 places at once|
|`Alt + Shift + Drag`|Column select|Vertical editing|

---

## 🎯 PHASE 5: Your Exact Workflow for Pasted Code

Here's the **real sequence** when you paste messy code:

```
Step 1:  Paste code              → Ctrl+V
Step 2:  Scan for red underlines → Eyes + Error Lens shows them IN the line
Step 3:  Fix each error          → Ctrl+. → pick fix → done
Step 4:  Bulk fix patterns       → Ctrl+H with regex, or Ctrl+D multi-cursor
Step 5:  Clean whitespace        → Ctrl+Shift+P → "Trim Trailing Whitespace"
Step 6:  Sort / dedupe if needed → Ctrl+Shift+P → "Sort Lines" or Text Power Tools
Step 7:  Format when happy      → Shift+Alt+F
Step 8:  Save                    → Ctrl+S
```

**Total time for a 200-line paste: ~2 minutes instead of 15.**

---

## 🧠 TL;DR — The 5 Things That Make This Work

|#|Thing|Why|
|---|---|---|
|1|**`Ctrl + .` Quick Fix**|Auto-fixes 80% of errors without AI|
|2|**Multi-cursor (`Alt+Click`, `Ctrl+D`)**|Edit 10 lines in 1 second|
|3|**Error Lens extension**|See errors WITHOUT hovering|
|4|**`Ctrl + H` with regex**|Bulk fixes that would take forever manually|
|5|**Turn off AI + language servers**|No bloat, no slowness, pure editing speed|

> **The philosophy: VS Code's real superpower isn't AI — it's that `Ctrl + .` + multi-cursor + regex replace combo. That's faster than any AI for fixing code you already have.** 🚀