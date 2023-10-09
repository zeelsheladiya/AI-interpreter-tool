from rich.console import Console
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from ai_interpreter.cli import autocomplete
from ai_interpreter.core.interpreter import generate_command, execute_command


def main():
    console = Console()

    console.print("Welcome to the AI Interpreter Tool")

    completer = WordCompleter(autocomplete.commands, ignore_case=True)

    session = PromptSession(
        completer=completer,
        complete_while_typing=True,
        reserve_space_for_menu=2,
    )

    while True:
        try:
            user_input = session.prompt("Enter a command: ")
        except KeyboardInterrupt:
            continue  # Handle Ctrl+C gracefully
        except EOFError:
            console.print("\nGoodbye!", style="bold blue")
            break  # Exit on Ctrl+D or EOF

        generated_command = generate_command(user_input)
        execute_command(generated_command)


if __name__ == "__main__":
    main()
