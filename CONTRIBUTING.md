## CONTRIBUTING:
- This repository is integrated with uv package manager & ruff linter. Follow next steps for comfortable contributing/development. Also note, that recommended IDE is Visual Studio Code (VSC), so the following steps assume you are using this IDE.

    - __(0)PACKAGE DEPENDENCIES__: Repository is managed by uv package manager
        - install uv by: pip install uv
        - after pulling branch let uv download required dependencies by terminal command: uv sync
        - for running your code via these dependencies, use terminal command: uv run tool/file (eg. uv run pytest or uv run main.py)
        - for deep understanding follow [DOCS](https://docs.astral.sh/uv/)

    - __(1)Ruff__: Setup Ruff in the IDE, this repository follows ruff.toml
        - install Ruff (Astral Software) extension in VSC

    - __(2)IDE settings__: Setup the IDE for checking data types, auto-fixes during file saving etc. (for VSC follow .vscode/settings.json)
        - press ctrl + shift + p open command line in VSC
        - to VSC command line write: Preferences: Open User Settings (JSON)
        - to this user settings copy content from .vscode/settings.json

    - __(3)DEPLOYMENT__: For successful deploy is required following:
        - Ruff linter must not detect any warning (run check: uv run ruff check . )
        - Pytest must successfully pass (run check: uv run pytest)
        - General deployment validation must pass
