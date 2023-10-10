from setuptools import setup, find_packages

setup(
    name="AI-INTERPRETER-TOOL",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "rich",
        "prompt_toolkit",
        "pytest",
        "black",
    ],
    entry_points={
        "console_scripts": [
            "ai_interpreter = ai_interpreter.interface.user_interface:main"
        ],
    },
)
