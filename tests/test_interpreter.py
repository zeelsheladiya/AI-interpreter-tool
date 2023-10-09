from ai_interpreter.core.interpreter import generate_command, execute_command
import pytest


def test_generate_command():
    assert generate_command("Please run the script") == "run"
    assert (
        generate_command("Give me information") == "run"
    )  # Modify this test based on your logic
    assert (
        generate_command("Exit the program") == "run"
    )  # Modify this test based on your logic
    assert (
        generate_command("Unknown command") == "run"
    )  # Modify this test based on your logic


def test_execute_command(capsys):
    execute_command("help")
    captured = capsys.readouterr()
    assert "Available commands" in captured.out

    execute_command("exit")
    captured = capsys.readouterr()
    assert "Goodbye!" in captured.out

    execute_command("run")
    captured = capsys.readouterr()
    assert "Running the 'run' command" in captured.out

    execute_command("info")
    captured = capsys.readouterr()
    assert "This is an AI interpreter" in captured.out

    execute_command("unknown")
    captured = capsys.readouterr()
    assert "Unknown command" in captured.out


if __name__ == "__main__":
    pytest.main()
