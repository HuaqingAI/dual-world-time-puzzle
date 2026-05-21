```markdown
# dual-world-time-puzzle Development Patterns

> Auto-generated skill from repository analysis

## Overview
This skill teaches you the core development patterns and conventions used in the `dual-world-time-puzzle` Python codebase. You'll learn about file naming, import/export styles, commit conventions, and how to write and organize tests. The repository is framework-agnostic and focuses on clear, maintainable Python code with a consistent structure.

## Coding Conventions

### File Naming
- **Pattern:** camelCase  
  Example:  
  ```python
  # Good
  dualWorldPuzzle.py
  timeManager.py

  # Avoid
  dual_world_puzzle.py
  DualWorldPuzzle.py
  ```

### Import Style
- **Pattern:** Relative imports  
  Example:
  ```python
  from .timeManager import TimeManager
  from .puzzleLogic import solvePuzzle
  ```

### Export Style
- **Pattern:** Named exports (explicitly specifying what is exported)  
  Example:
  ```python
  # timeManager.py
  class TimeManager:
      pass

  __all__ = ["TimeManager"]
  ```

### Commit Patterns
- **Type:** Conventional commits
- **Prefixes:** `feat`, `test`
- **Average length:** 36 characters  
  Example commit messages:
  ```
  feat: add dual world time calculation logic
  test: add unit tests for puzzle solver
  ```

## Workflows

### Adding a New Feature
**Trigger:** When you want to implement a new capability or logic.  
**Command:** `/add-feature`

1. Create a new Python file using camelCase naming.
2. Implement your feature using relative imports for dependencies.
3. Export main classes/functions using named exports.
4. Commit your changes with a `feat:` prefix and a concise description.

### Writing and Running Tests
**Trigger:** When you need to verify the correctness of your code.  
**Command:** `/run-tests`

1. Create a test file named with the pattern `*.test.*` (e.g., `timeManager.test.py`).
2. Write your test cases (framework is not specified; use standard `unittest` or your preferred method).
3. Run your tests using the Python interpreter or your chosen test runner.

### Committing Changes
**Trigger:** When you're ready to save your work in version control.  
**Command:** `/commit-changes`

1. Stage your changes.
2. Write a commit message using the conventional commit format:
   - Use `feat:` for new features.
   - Use `test:` for test-related changes.
3. Keep your commit message concise (around 36 characters).

## Testing Patterns

- **File Pattern:** Test files are named using `*.test.*` (e.g., `puzzleLogic.test.py`).
- **Framework:** Not specified; standard Python testing applies.
- **Example:**
  ```python
  # timeManager.test.py
  import unittest
  from .timeManager import TimeManager

  class TestTimeManager(unittest.TestCase):
      def test_time_sync(self):
          tm = TimeManager()
          self.assertTrue(tm.isSynced())

  if __name__ == "__main__":
      unittest.main()
  ```

## Commands
| Command         | Purpose                                      |
|-----------------|----------------------------------------------|
| /add-feature    | Start the process for adding a new feature   |
| /run-tests      | Run all test files in the codebase           |
| /commit-changes | Commit changes using conventional commits    |
```
