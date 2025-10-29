# Translate Project

## Project Name and Description

The `translate` project is a Python-based tool designed for text translation and transformation using regex patterns and string replacements. It is modular, with key components handling regex compilation, branch management, and pattern matching.

## Technology Stack

- **Programming Language**: Python 3.14 or higher

## Project Architecture

The project is structured into the following key components:

1. **`Branch` Class (`Branch.py`)**:

   - Manages branch-specific data and operations.
   - Provides methods like `add` and `remove` for manipulating branch data.

2. **Regex and String Replacement (`trs_data.py`)**:

   - Defines and compiles regex patterns for efficient text processing.
   - Uses the `Branch` class to manage branch-specific regex patterns and replacements.

3. **Main Script (`main.py`)**:
   - Initializes and tracks the status of regex patterns and string replacements.
   - Serves as the entry point for executing the translation logic.

## Getting Started

### Prerequisites

- Python 3.14 or higher

### Installation

1. Clone this repository.

2. Ensure Python 3.14 or higher is installed.

### Running the Project

To execute the main script:

```bash
python main.py
```

## Project Structure

- `Branch.py`: Defines the `Branch` class.

- `trs_data.py`: Contains regex patterns, replacements, and branch-specific logic.

- `main.py`: Entry point for the project.

- `pyproject.toml`: Specifies Python version requirements.

## Key Features

- Modular design for regex compilation and string replacements.

- Branch-specific management of regex patterns and replacements.

- Precompiled regex patterns for efficiency.

## Development Workflow

- **Debugging**:

  - Use the `Pattern_match_status` dictionary in `main.py` to track the status of regex patterns and replacements.

## Coding Standards

- Regex patterns are precompiled with flags (`re.I | re.X | re.M`) for efficiency.

- Patterns and their replacements are managed in dictionaries (`compiledRegexPatterns`, `compiledRegexPatternsWithBranch`).

- Follow existing patterns and conventions for adding new regex patterns or string replacements.
