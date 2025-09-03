# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a Python educational repository containing a comprehensive tutorial file (`python-cheat-sheet.py`) that demonstrates Python concepts from basics to advanced features, including the latest Python 3.13 and 3.14 features.

## Common Development Commands

### Running Code
```bash
# Execute the full tutorial
python3 python-cheat-sheet.py

# Run Python interpreter (Python 3.13.6 installed)
python3
```

### Version Control
```bash
# View status and recent changes
git status
git log --oneline -10

# Commit changes with descriptive messages
git add .
git commit -m "Add Python 3.x examples: [specific feature]"
git push origin main
```

## Code Architecture and Structure

The repository contains a single comprehensive tutorial file (`python-cheat-sheet.py`, 2238 lines) organized into five main sections:

1. **Basic Python Concepts** - Variables, control flow, functions, data structures, file I/O
2. **Intermediate Python Concepts** - OOP, inheritance, exceptions, modules, decorators
3. **Advanced Python Concepts** - Threading, asyncio, type hints, generators, functional programming
4. **Modern Python Features** - Coverage of Python 3.10 through 3.14 features
5. **Pydantic and Pydantic AI** - Modern data validation and AI integration

Each section contains executable examples with detailed inline comments explaining outputs and behaviors.

## Development Guidelines

### When Adding New Content
- Maintain the educational structure with clear section headers
- Include comprehensive inline comments explaining each concept
- Show expected output as comments (e.g., `# Output: ...`)
- Mark version-specific features clearly (e.g., `# Python 3.13+ only`)
- Ensure all examples are self-contained and runnable

### Code Style
- Use 4-space indentation
- Use descriptive variable names for clarity
- Prefer f-strings for formatting
- Add type hints in advanced sections
- Follow the existing pattern of progressing from simple to complex examples

### Testing
Since there's no formal testing framework:
- Verify new code by running: `python3 python-cheat-sheet.py`
- Ensure no syntax errors or runtime exceptions
- Check that examples produce their documented outputs

## Important Context

- **No external dependencies**: The tutorial is self-contained with no pip packages required
- **Target Python version**: 3.13+ (system has Python 3.13.6)
- **Educational focus**: Code should prioritize clarity and learning over optimization
- **Progressive learning**: Examples build on previous concepts