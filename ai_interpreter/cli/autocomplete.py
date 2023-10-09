# List of predefined commands for autocomplete
commands = ["help", "run", "exit", "info"]  # Replace with your own suggestions


def custom_autocomplete(text, state):
    """
    Custom autocomplete function.
    Returns a list of suggestions based on the current text.
    """
    return [cmd for cmd in commands if cmd.startswith(text)]
