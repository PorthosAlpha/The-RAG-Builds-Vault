#!/usr/bin/env python3
"""
Grammarly-like CLI Tool
A command-line writing assistant that detects grammatical errors, spelling mistakes,
improves writing style, tone, clarity, fixes punctuation, and provides real-time suggestions.
Uses Ollama with the qwen3.5:9b model.
"""

import sys
import json
from typing import Optional
import ollama
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.prompt import Prompt
from rich.text import Text

# Initialize Rich console
console = Console()

# Model configuration
MODEL_NAME = "qwen3.5:9b"


class GrammarChecker:
    """Main grammar checking class using Ollama."""
    
    def __init__(self):
        self.model = MODEL_NAME
        self.check_prompts = {
            "grammar": """Analyze the following text for grammatical errors only. 
Return your response in JSON format with this exact structure:
{
    "errors": [
        {"original": "text with error", "suggestion": "corrected text", "explanation": "brief explanation"}
    ],
    "has_errors": true/false
}

Text to analyze: {text}

Respond ONLY with valid JSON, no other text.""",
            
            "spelling": """Analyze the following text for spelling mistakes only.
Return your response in JSON format with this exact structure:
{
    "errors": [
        {"original": "misspelled word", "suggestion": "correct spelling", "explanation": "brief explanation"}
    ],
    "has_errors": true/false
}

Text to analyze: {text}

Respond ONLY with valid JSON, no other text.""",
            
            "punctuation": """Analyze the following text for punctuation errors only.
Return your response in JSON format with this exact structure:
{
    "errors": [
        {"original": "text with punctuation error", "suggestion": "corrected text", "explanation": "brief explanation"}
    ],
    "has_errors": true/false
}

Text to analyze: {text}

Respond ONLY with valid JSON, no other text.""",
            
            "style": """Analyze the following text for writing style improvements (clarity, conciseness, flow, word choice).
Return your response in JSON format with this exact structure:
{
    "suggestions": [
        {"original": "original text", "suggestion": "improved version", "explanation": "why this is better", "category": "clarity|conciseness|flow|word_choice"}
    ],
    "has_suggestions": true/false
}

Text to analyze: {text}

Respond ONLY with valid JSON, no other text.""",
            
            "tone": """Analyze the following text for tone and provide suggestions to improve it for professional communication.
Return your response in JSON format with this exact structure:
{
    "current_tone": "detected tone",
    "suggestions": [
        {"original": "original text", "suggestion": "improved version", "explanation": "tone improvement reason"}
    ],
    "has_suggestions": true/false
}

Text to analyze: {text}

Respond ONLY with valid JSON, no other text.""",
            
            "comprehensive": """Perform a comprehensive analysis of the following text covering:
1. Grammatical errors
2. Spelling mistakes
3. Punctuation errors
4. Writing style improvements (clarity, conciseness, flow)
5. Tone suggestions

Return your response in JSON format with this exact structure:
{
    "grammar": {
        "errors": [{"original": "", "suggestion": "", "explanation": ""}],
        "has_errors": false
    },
    "spelling": {
        "errors": [{"original": "", "suggestion": "", "explanation": ""}],
        "has_errors": false
    },
    "punctuation": {
        "errors": [{"original": "", "suggestion": "", "explanation": ""}],
        "has_errors": false
    },
    "style": {
        "suggestions": [{"original": "", "suggestion": "", "explanation": "", "category": ""}],
        "has_suggestions": false
    },
    "tone": {
        "current_tone": "",
        "suggestions": [{"original": "", "suggestion": "", "explanation": ""}],
        "has_suggestions": false
    },
    "corrected_text": "fully corrected and improved version of the text"
}

Text to analyze: {text}

Respond ONLY with valid JSON, no other text."""
        }
    
    def _call_model(self, prompt: str) -> Optional[dict]:
        """Call the Ollama model and parse JSON response."""
        try:
            response = ollama.chat(
                model=self.model,
                messages=[{"role": "user", "content": prompt}]
            )
            content = response["message"]["content"]
            
            # Extract JSON from response (handle potential markdown code blocks)
            if "```json" in content:
                content = content.split("```json")[1].split("```")[0]
            elif "```" in content:
                content = content.split("```")[1].split("```")[0]
            
            return json.loads(content.strip())
        except Exception as e:
            console.print(f"[red]Error calling model: {e}[/red]")
            return None
    
    def check_grammar(self, text: str) -> Optional[dict]:
        """Check for grammatical errors."""
        prompt = self.check_prompts["grammar"].format(text=text)
        return self._call_model(prompt)
    
    def check_spelling(self, text: str) -> Optional[dict]:
        """Check for spelling mistakes."""
        prompt = self.check_prompts["spelling"].format(text=text)
        return self._call_model(prompt)
    
    def check_punctuation(self, text: str) -> Optional[dict]:
        """Check for punctuation errors."""
        prompt = self.check_prompts["punctuation"].format(text=text)
        return self._call_model(prompt)
    
    def check_style(self, text: str) -> Optional[dict]:
        """Check for style improvements."""
        prompt = self.check_prompts["style"].format(text=text)
        return self._call_model(prompt)
    
    def check_tone(self, text: str) -> Optional[dict]:
        """Check for tone improvements."""
        prompt = self.check_prompts["tone"].format(text=text)
        return self._call_model(prompt)
    
    def comprehensive_check(self, text: str) -> Optional[dict]:
        """Perform comprehensive analysis."""
        prompt = self.check_prompts["comprehensive"].format(text=text)
        return self._call_model(prompt)


def display_results(results: dict, check_type: str = "comprehensive"):
    """Display analysis results in a formatted way."""
    if not results:
        console.print("[red]No results to display.[/red]")
        return
    
    if check_type == "comprehensive":
        # Display comprehensive results
        console.print("\n[bold cyan]═══════════════════════════════════════════════════════[/bold cyan]")
        console.print("[bold cyan]           COMPREHENSIVE WRITING ANALYSIS              [/bold cyan]")
        console.print("[bold cyan]═══════════════════════════════════════════════════════[/bold cyan]\n")
        
        # Grammar errors
        if results.get("grammar", {}).get("has_errors"):
            console.print("[bold red]📝 GRAMMAR ERRORS:[/bold red]")
            for error in results["grammar"]["errors"]:
                console.print(f"  ❌ \"{error['original']}\" → ✅ \"{error['suggestion']}\"")
                console.print(f"     💡 {error['explanation']}\n")
        else:
            console.print("[green]✓ No grammar errors detected[/green]\n")
        
        # Spelling errors
        if results.get("spelling", {}).get("has_errors"):
            console.print("[bold red]🔤 SPELLING ERRORS:[/bold red]")
            for error in results["spelling"]["errors"]:
                console.print(f"  ❌ \"{error['original']}\" → ✅ \"{error['suggestion']}\"")
                console.print(f"     💡 {error['explanation']}\n")
        else:
            console.print("[green]✓ No spelling errors detected[/green]\n")
        
        # Punctuation errors
        if results.get("punctuation", {}).get("has_errors"):
            console.print("[bold red]📌 PUNCTUATION ERRORS:[/bold red]")
            for error in results["punctuation"]["errors"]:
                console.print(f"  ❌ \"{error['original']}\" → ✅ \"{error['suggestion']}\"")
                console.print(f"     💡 {error['explanation']}\n")
        else:
            console.print("[green]✓ No punctuation errors detected[/green]\n")
        
        # Style suggestions
        if results.get("style", {}).get("has_suggestions"):
            console.print("[bold yellow]✨ STYLE SUGGESTIONS:[/bold yellow]")
            for suggestion in results["style"]["suggestions"]:
                category = suggestion.get("category", "general").upper()
                console.print(f"  [{category}] \"{suggestion['original']}\" → \"{suggestion['suggestion']}\"")
                console.print(f"     💡 {suggestion['explanation']}\n")
        else:
            console.print("[green]✓ No style improvements needed[/green]\n")
        
        # Tone suggestions
        if results.get("tone", {}).get("has_suggestions"):
            current_tone = results["tone"].get("current_tone", "unknown")
            console.print(f"[bold blue]🎭 TONE ANALYSIS (Current: {current_tone}):[/bold blue]")
            for suggestion in results["tone"]["suggestions"]:
                console.print(f"  \"{suggestion['original']}\" → \"{suggestion['suggestion']}\"")
                console.print(f"     💡 {suggestion['explanation']}\n")
        else:
            console.print("[green]✓ Tone is appropriate[/green]\n")
        
        # Corrected text
        if results.get("corrected_text"):
            console.print("[bold green]✅ CORRECTED VERSION:[/bold green]")
            panel = Panel(
                results["corrected_text"],
                title="Improved Text",
                border_style="green"
            )
            console.print(panel)
    
    else:
        # Display specific check results
        if results.get("errors") or results.get("suggestions"):
            for item in results.get("errors", []) + results.get("suggestions", []):
                original = item.get("original", "")
                suggestion = item.get("suggestion", "")
                explanation = item.get("explanation", "")
                console.print(f"  ❌ \"{original}\" → ✅ \"{suggestion}\"")
                console.print(f"     💡 {explanation}\n")
        else:
            console.print("[green]✓ No issues found![/green]")


def interactive_mode():
    """Run the tool in interactive mode with real-time suggestions."""
    checker = GrammarChecker()
    
    console.print(Panel.fit(
        "[bold cyan]🖊️  Grammarly CLI - Interactive Mode[/bold cyan]\n\n"
        "Type your text and press ENTER to get suggestions.\n"
        "Commands:\n"
        "  • Type any text to analyze it\n"
        "  • 'quit' or 'exit' to exit\n"
        "  • 'clear' to clear screen\n"
        "  • 'mode <type>' to change check type (grammar/spelling/punctuation/style/tone/comprehensive)",
        border_style="cyan"
    ))
    
    current_mode = "comprehensive"
    buffer = []
    
    while True:
        try:
            # Get input
            user_input = Prompt.ask(
                f"\n[{current_mode.upper()}] Enter text",
                default=""
            ).strip()
            
            if not user_input:
                continue
            
            if user_input.lower() in ["quit", "exit", "q"]:
                console.print("\n[bold green]👋 Goodbye! Happy writing![/bold green]")
                break
            
            if user_input.lower() == "clear":
                console.clear()
                continue
            
            if user_input.lower().startswith("mode "):
                new_mode = user_input.split(" ")[1].lower()
                valid_modes = ["grammar", "spelling", "punctuation", "style", "tone", "comprehensive"]
                if new_mode in valid_modes:
                    current_mode = new_mode
                    console.print(f"[bold blue]✓ Mode changed to: {current_mode.upper()}[/bold blue]")
                else:
                    console.print(f"[red]Invalid mode. Choose from: {', '.join(valid_modes)}[/red]")
                continue
            
            # Add to buffer for context
            buffer.append(user_input)
            full_text = " ".join(buffer[-5:])  # Keep last 5 entries for context
            
            console.print("\n[yellow]⏳ Analyzing...[/yellow]")
            
            # Perform check based on mode
            if current_mode == "grammar":
                results = checker.check_grammar(user_input)
            elif current_mode == "spelling":
                results = checker.check_spelling(user_input)
            elif current_mode == "punctuation":
                results = checker.check_punctuation(user_input)
            elif current_mode == "style":
                results = checker.check_style(user_input)
            elif current_mode == "tone":
                results = checker.check_tone(user_input)
            else:  # comprehensive
                results = checker.comprehensive_check(user_input)
            
            if results:
                display_results(results, current_mode)
            else:
                console.print("[red]Could not analyze text. Please try again.[/red]")
        
        except KeyboardInterrupt:
            console.print("\n\n[bold yellow]Interrupted. Type 'quit' to exit.[/bold yellow]")
        except Exception as e:
            console.print(f"[red]Error: {e}[/red]")


def check_file(filepath: str, comprehensive: bool = True):
    """Check a file for writing issues."""
    checker = GrammarChecker()
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        console.print(f"[red]File not found: {filepath}[/red]")
        return
    except Exception as e:
        console.print(f"[red]Error reading file: {e}[/red]")
        return
    
    console.print(f"\n[bold cyan]Analyzing file: {filepath}[/bold cyan]\n")
    
    if comprehensive:
        results = checker.comprehensive_check(content)
        display_results(results, "comprehensive")
    else:
        # Run individual checks
        for check_name, check_func in [
            ("Grammar", checker.check_grammar),
            ("Spelling", checker.check_spelling),
            ("Punctuation", checker.check_punctuation),
            ("Style", checker.check_style),
            ("Tone", checker.check_tone)
        ]:
            console.print(f"\n[bold]{check_name} Check:[/bold]")
            results = check_func(content)
            if results:
                display_results(results, "specific")


def check_text(text: str, comprehensive: bool = True):
    """Check provided text for writing issues."""
    checker = GrammarChecker()
    
    if comprehensive:
        results = checker.comprehensive_check(text)
        display_results(results, "comprehensive")
    else:
        # Run individual checks
        for check_name, check_func in [
            ("Grammar", checker.check_grammar),
            ("Spelling", checker.check_spelling),
            ("Punctuation", checker.check_punctuation),
            ("Style", checker.check_style),
            ("Tone", checker.check_tone)
        ]:
            console.print(f"\n[bold]{check_name} Check:[/bold]")
            results = check_func(text)
            if results:
                display_results(results, "specific")


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Grammarly-like CLI Tool - AI-powered writing assistant",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --interactive                    Run in interactive mode
  %(prog)s --text "Your text here"          Check specific text
  %(prog)s --file document.txt              Check a file
  %(prog)s --text "..." --mode grammar      Check only grammar
  %(prog)s --text "..." --mode style        Check only style
        """
    )
    
    parser.add_argument(
        "-i", "--interactive",
        action="store_true",
        help="Run in interactive mode with real-time suggestions"
    )
    
    parser.add_argument(
        "-t", "--text",
        type=str,
        help="Text to analyze"
    )
    
    parser.add_argument(
        "-f", "--file",
        type=str,
        help="File path to analyze"
    )
    
    parser.add_argument(
        "-m", "--mode",
        type=str,
        choices=["grammar", "spelling", "punctuation", "style", "tone", "comprehensive"],
        default="comprehensive",
        help="Type of check to perform (default: comprehensive)"
    )
    
    args = parser.parse_args()
    
    # Show welcome message
    if not args.text and not args.file and not args.interactive:
        console.print(Panel(
            "[bold cyan]🖊️  Grammarly CLI Tool[/bold cyan]\n\n"
            "AI-powered writing assistant using Ollama (qwen3.5:9b)\n\n"
            "[bold]Features:[/bold]\n"
            "  ✓ Grammar checking\n"
            "  ✓ Spelling correction\n"
            "  ✓ Punctuation fixes\n"
            "  ✓ Style improvements\n"
            "  ✓ Tone analysis\n"
            "  ✓ Real-time suggestions\n\n"
            "[bold]Usage:[/bold]\n"
            "  Run with --interactive for real-time assistance\n"
            "  Or use --text or --file to check specific content\n\n"
            "Run 'python grammarly_cli.py --help' for more options",
            border_style="cyan"
        ))
        return
    
    # Interactive mode
    if args.interactive:
        interactive_mode()
        return
    
    # Check provided text
    if args.text:
        if args.mode == "comprehensive":
            check_text(args.text, comprehensive=True)
        else:
            checker = GrammarChecker()
            check_funcs = {
                "grammar": checker.check_grammar,
                "spelling": checker.check_spelling,
                "punctuation": checker.check_punctuation,
                "style": checker.check_style,
                "tone": checker.check_tone
            }
            results = check_funcs[args.mode](args.text)
            if results:
                display_results(results, "specific")
        return
    
    # Check file
    if args.file:
        check_file(args.file, comprehensive=(args.mode == "comprehensive"))
        return


if __name__ == "__main__":
    main()
