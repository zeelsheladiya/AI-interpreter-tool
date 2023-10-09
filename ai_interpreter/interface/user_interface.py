from rich.console import Console
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.styles import Style
from ai_interpreter.cli import autocomplete
from ai_interpreter.core.interpreter import generate_command, execute_command

# Define custom styles
custom_style = Style.from_dict({
    'completion-menu.completion': 'bg:#008888 #ffffff',
    'completion-menu.completion.current': 'bg:#00aaaa #000000',
    'scrollbar.background': 'bg:#88aaaa',
    'scrollbar.button': 'bg:#222222',
})


def main():

    console = Console()
    completer = WordCompleter(autocomplete.commands, ignore_case=True)

    console.print("Welcome to the AI Interpreter Tool")

    session = PromptSession(
        completer=completer,
        complete_while_typing=True,
        reserve_space_for_menu=2,
        auto_suggest=AutoSuggestFromHistory(), 
        style=custom_style
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
        console.print(execute_command(generated_command))


if __name__ == "__main__":
    main()
