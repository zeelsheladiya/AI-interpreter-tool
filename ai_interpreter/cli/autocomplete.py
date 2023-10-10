from ai_interpreter.cli.main_commands import main_commands

def custom_autocomplete(text, state):
    """
    Custom autocomplete function.
    Returns a list of suggestions based on the current text.
    """
    return [cmd for cmd in main_commands if cmd.startswith(text)]
