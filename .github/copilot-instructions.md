# Copilot Instructions for the `translate` Project

## Project Overview

The `translate` project is a Python-based tool designed for text translation and transformation using regex patterns and string replacements. The project is modular, with key components handling regex compilation, branch management, and pattern matching.

### Key Components

1. **`Branch` Class (`Branch.py`)**:

   - Manages branch-specific data and operations.
   - Provides methods like `add` and `remove` for manipulating branch data.

2. **Regex and String Replacement (`trs_date.py`)**:

   - Defines and compiles regex patterns for efficient text processing.
   - Uses the `Branch` class to manage branch-specific regex patterns and replacements.

3. **Main Script (`main.py`)**:
   - Initializes and tracks the status of regex patterns and string replacements.
   - Serves as the entry point for executing the translation logic.

## Developer Workflows

### Running the Project

- Use Python 3.14 or higher as specified in `pyproject.toml`.
- Execute the main script:
  ```bash
  python main.py
  ```

### Testing

- The project includes tasks for testing and scanning using `ast-grep`:
  - Run tests interactively:
    ```bash
    sg test --interactive
    ```
  - Scan the codebase:
    ```bash
    sg scan
    ```

### Debugging

- Use the `Pattern_match_status` dictionary in `main.py` to track the status of regex patterns and replacements during execution.

## Project-Specific Conventions

- **Regex Compilation**:

  - Regex patterns are precompiled with flags (`re.I | re.X | re.M`) for efficiency.
  - Patterns and their replacements are managed in dictionaries (`compiledRegexPatterns`, `compiledRegexPatternsWithBranch`).

- **Branch Management**:

  - The `Branch` class is used to group and manage branch-specific regex patterns and replacements.
  - Methods like `add` and `done_with_zip` are used to construct and finalize branch data.

- **String Replacement**:
  - Direct string replacements are defined in `stringReplacementMap` and `stringReplacementMapWithBranch`.

## Integration Points

- **Dependencies**:

  - The project does not currently list external dependencies in `pyproject.toml`.
  - Ensure Python 3.14 or higher is installed.

- **File Structure**:
  - `Branch.py`: Defines the `Branch` class.
  - `trs_date.py`: Contains regex patterns, replacements, and branch-specific logic.
  - `main.py`: Entry point for the project.

## Examples

- Adding a new branch-specific regex pattern:

  ```python
  branch = Branch()
  branch.add("example_branch", {r"pattern": "replacement"})
  ```

- Compiling a regex pattern:
  ```python
  import re
  pattern = re.compile(r"example_pattern", re.I | re.X | re.M)
  ```

## Notes

- Follow the existing patterns and conventions for adding new regex patterns or string replacements.
- Use the `ast-grep` tasks for testing and scanning to ensure code quality.
