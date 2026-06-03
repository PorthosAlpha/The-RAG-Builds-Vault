# Grammarly CLI Tool

A command-line writing assistant that functions like Grammarly, using Ollama with the qwen3.5:9b model.

## Features

- ✅ **Grammar Checking** - Detects grammatical errors
- ✅ **Spelling Correction** - Finds and fixes spelling mistakes  
- ✅ **Punctuation Fixes** - Corrects punctuation errors
- ✅ **Style Improvements** - Enhances clarity, conciseness, flow, and word choice
- ✅ **Tone Analysis** - Analyzes and suggests tone improvements for professional communication
- ✅ **Real-time Suggestions** - Interactive mode for suggestions as you type

## Requirements

- Python 3.8+
- Ollama installed and running locally
- qwen3.5:9b model (will be pulled automatically when first used)

### Install Python Dependencies

```bash
pip install ollama rich
```

### Install Ollama

If you don't have Ollama installed:

```bash
# macOS
brew install ollama

# Linux
curl -fsSL https://ollama.com/install.sh | sh

# Windows
# Download from https://ollama.com/download
```

### Pull the Model

```bash
ollama pull qwen3.5:9b
```

## Usage

### Show Help

```bash
python grammarly_cli.py --help
```

### Interactive Mode (Recommended)

Run in interactive mode for real-time suggestions as you type:

```bash
python grammarly_cli.py --interactive
```

In interactive mode:
- Type any text and press ENTER to get analysis
- Use `mode <type>` to switch between check types (grammar, spelling, punctuation, style, tone, comprehensive)
- Use `clear` to clear the screen
- Use `quit` or `exit` to exit

### Check Specific Text

```bash
# Comprehensive check (all features)
python grammarly_cli.py --text "Your text here"

# Grammar only
python grammarly_cli.py --text "Your text here" --mode grammar

# Spelling only
python grammarly_cli.py --text "Your text here" --mode spelling

# Style improvements
python grammarly_cli.py --text "Your text here" --mode style

# Tone analysis
python grammarly_cli.py --text "Your text here" --mode tone
```

### Check a File

```bash
# Comprehensive check
python grammarly_cli.py --file document.txt

# Specific check
python grammarly_cli.py --file document.txt --mode grammar
```

## Examples

### Example 1: Quick Text Check

```bash
python grammarly_cli.py --text "The cat chases the mouses around the house, but their is no success."
```

### Example 2: Interactive Session

```bash
$ python grammarly_cli.py --interactive

╭─────────────────────────────────────────╮
│ 🖊️  Grammarly CLI - Interactive Mode   │
│                                         │
│ Type your text and press ENTER to get  │
│ suggestions.                            │
│ Commands:                               │
│ • Type any text to analyze it           │
│ • 'quit' or 'exit' to exit              │
│ • 'clear' to clear screen               │
│ • 'mode <type>' to change check type    │
╰─────────────────────────────────────────╯

[COMPREHENSIVE] Enter text: The team are working good on they're project.

⏳ Analyzing...

═══════════════════════════════════════════════════════
           COMPREHENSIVE WRITING ANALYSIS              
═══════════════════════════════════════════════════════

📝 GRAMMAR ERRORS:
  ❌ "The team are" → ✅ "The team is"
     💡 Subject-verb agreement: 'team' is singular

🔤 SPELLING ERRORS:
  ❌ "they're" → ✅ "their"
     💡 Wrong contraction: should be possessive form

✨ STYLE SUGGESTIONS:
  [WORD_CHOICE] "working good" → "working well"
     💡 'Well' is the correct adverb form

✅ CORRECTED VERSION:
┌─────────────────────────────────────┐
│ Improved Text                       │
├─────────────────────────────────────┤
│ The team is working well on their   │
│ project.                            │
└─────────────────────────────────────┘
```

## Architecture

The tool uses:
- **Ollama** - Local LLM runner for privacy and speed
- **qwen3.5:9b** - Advanced language model for accurate analysis
- **Rich** - Beautiful terminal output formatting
- **JSON-based prompts** - Structured analysis results

## Modes Explained

| Mode | Description |
|------|-------------|
| `comprehensive` | Full analysis covering all aspects |
| `grammar` | Grammar errors only |
| `spelling` | Spelling mistakes only |
| `punctuation` | Punctuation errors only |
| `style` | Writing style improvements |
| `tone` | Tone analysis and suggestions |

## Notes

- First run may take longer as the model is downloaded
- Requires Ollama server to be running (`ollama serve`)
- All processing happens locally for privacy
- Results are returned in structured JSON format for accuracy

## License

MIT License
