from ai_interpreter.core.interpreter import generate_command, execute_command
import pytest


def test_generate_command():
    assert ( 
        generate_command("run") == "run" 
    )
    assert (
        generate_command("info") == "info"
    )  # Modify this test based on your logic
    assert (
        generate_command("exit") == "exit" 
    )  # Modify this test based on your logic
    assert (
        generate_command("unknown") == "unknown"
    )  # Modify this test based on your logic


def test_execute_command(capsys):

    return_text = execute_command("help")
    assert "Available commands" in return_text

    return_text = execute_command("exit")
    assert "Goodbye!" in return_text

    return_text = execute_command("run")
    assert "Running the 'run' command" in return_text

    return_text = execute_command("info")
    assert "This is an AI interpreter" in return_text

    return_text = execute_command("unknown")
    assert "Unknown command" in return_text


if __name__ == "__main__":
    pytest.main()
