# 🔥 BOTH — Let's GO!

---

## ✏️ ASCII SKETCH

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                        🧠 RAG ARCHITECTURE SCHEMATIC                        ║
╠══════════════════════════════════════════════════════════════════════════════%║                                                                              ║
║  ┌───────────────────────── PHASE 1: PRE-RETRIEVAL (OFFLINE) ─────────────┐  ║
║  │                                                                          │  ║
║  │   📄 SOURCES                                                             │  ║
║  │      │                                                                   │  ║
║  │      ▼                                                                   │  ║
║  │   🔧 LLAMAPARSE ──────► 📝 MARKDOWN ──────► 🦙 LLAMAINDEX              │  ║
║  │                                                          │               │  ║
║  │                                                          ▼               │  ║
║  │                                                   ┌───────────┐         │  ║
║  │                                                   │ 🗄️ VECTOR │         │  ║
║  │                                                   │   STORE   │         │  ║
║  │                                                   └─────┬─────┘         │  ║
║  └─────────────────────────────────────────────────────────│───────────────┘  ║
║                                                            │                  ║
║  ┌───────────────────────── PHASE 2: POST-RETRIEVAL (ONLINE/RUNTIME) ──────┐  ║
║  │                           │                                              │  ║
║  │                           ▼                                              │  ║
║  │                    👤 USER QUERY                                         │  ║
║  │                           │                                              │  ║
║  │                           ▼                                              │  ║
║  │                  🚀 GUNICORN / UVICORN                                    │  ║
║  │                           │                                              │  ║
║  │                           ▼                                              │  ║
║  │                  📦 CHUNK RETRIEVE  ◄──── from Vector Store              │  ║
║  │                           │                                              │  ║
║  │                           ▼                                              │  ║
║  │                  🚦 RERANKER ◄──── "QUALITY GATE"                       │  ║
║  │                           │                                              │  ║
║  │                           ▼                                              │  ║
║  │                  🤖 LOCAL LLM ──────► 💬 OUTPUT                           │  ║
║  │                           │                                              │  ║
║  │                           │        ┌─────────────────────────┐           │  ║
║  │                           └───────►│ 🔄 FEEDBACK LOOP       │           │  ║
║  │                                     │ (Query Reformulation /  │           │  ║
║  │                                     │  Iterative Refinement)  │           │  ║
║  │                                     └─────────────────────────┘           │  ║
║  └──────────────────────────────────────────────────────────────────────────┘  ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

---

## 🛠️ TOOL RECOMMENDATION

|Tool|Fit Score|Why|
|---|---|---|
|🥇 **Mermaid**|⭐⭐⭐⭐⭐|**BEST FIT.** Flowchart-native, renders in GitHub/Notion/Obsidian, version-controllable as code. Perfect for this linear pipeline.|
|🥈 **Excalidraw**|⭐⭐⭐⭐|Great if you want a hand-drawn/whiteboard feel. Good for presentations.|
|🥉 **Draw.io**|⭐⭐⭐|Overkill here but good if you need pixel-perfect export to PNG/SVG for docs.|

### 👉 **Go with Mermaid.** Here's the ready-to-paste code:

```mermaid
mermaidflowchart LR
    subgraph OFFLINE["🔧 PHASE 1: PRE-RETRIEVAL (OFFLINE)"]
        SOURCES["📄 SOURCES"] --> LPARSE["🔧 LLAMAPARSE"]
        LPARSE --> MARKDOWN["📝 MARKDOWN"]
        MARKDOWN --> LIDX["🦙 LLAMAINDEX"]
        LIDX --> VS[("🗄️ VECTOR STORE")]
    end

    subgraph ONLINE["🚀 PHASE 2: POST-RETRIEVAL (ONLINE/RUNTIME)"]
        USER["👤 USER QUERY"] --> GUNI["🚀 GUNICORN/UVICORN"]
        GUNI --> RETRIEVE["📦 CHUNK RETRIEVE"]
        VS --> RETRIEVE
        RETRIEVE --> RERANK["🚦 RERANKER<br/>⚡ Quality Gate"]
        RERANK --> LLM["🤖 LOCAL LLM"]
        LLM --> OUT["💬 OUTPUT"]
        OUT -.->|"🔄 FEEDBACK LOOP<br/>Query Reformulation"| USER
    end

    style OFFLINE fill:#1a1a2e,color:#fff,stroke:#e94560
    style ONLINE fill:#16213e,color:#fff,stroke:#0f3460
    style VS fill:#0f3460,color:#fff,stroke:#e94560
    style RERANK fill:#e94560,color:#fff,stroke:#fff
```

---

## 📋 Quick-Start

|Where to paste|How|
|---|---|
|**GitHub README**|Just drop the ` ```mermaid ` block|
|**Notion**|Type `/code` → select Mermaid|
|**Obsidian**|Type `/mermaid`|
|**Excalidraw**|Paste the ASCII as a reference, redraw|

**You've got the blueprint. Go build it.** 🚀