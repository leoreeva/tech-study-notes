# AGENTS.md - Tech Study Notes

This document provides guidelines for AI agents and developers working on the Tech Study Notes repository, a Quarkdown-based knowledge base for software engineering and related topics.

## 🛠️ Build/Lint/Test Commands

### Build Commands

**Compile the entire knowledge base:**
```bash
quarkdown c main.qd
```

**Live preview during editing:**
```bash
quarkdown c main.qd -p -w
```

**Preview server only:**
```bash
quarkdown c main.qd -p
```

### Lint/Test Commands

**Run Python script to fix heading numbering:**
```bash
python3 fix_headings.py
```

**Check Python syntax:**
```bash
python3 -m py_compile fix_headings.py
```

**Run Ruff linter (if installed):**
```bash
ruff check fix_headings.py
```

## 📝 Code Style Guidelines

### Quarkdown File Structure

1. **File Headers**: All `.qd` files must start with:
   ```markdown
   .docname {Your Title}
   .include {docs}
   ```

2. **Content Organization**:
   - Use clear section headings with proper hierarchy
   - Start with level 2 headings (`##`) for main sections
   - Use consistent numbering format: `## 1. Section Title`

### Python Scripts

**Imports:**
- Group imports by type (standard library, third-party, local)
- Sort alphabetically within each group
- Example from `fix_headings.py`:
  ```python
  import re
  import os
  from pathlib import Path
  ```

**Formatting:**
- Use 4 spaces for indentation (PEP 8 standard)
- Limit lines to 88 characters where practical
- Use descriptive variable names
- Add docstrings for functions and modules

**Type Hints:**
- Use Python type hints for function signatures
- Example:
  ```python
  def process_file(file_path: str) -> None:
  ```

**Error Handling:**
- Use try/except blocks for file operations
- Provide meaningful error messages
- Example:
  ```python
  try:
      with open(file_path, "r", encoding="utf-8") as f:
          content = f.read()
  except FileNotFoundError:
      print(f"Error: File {file_path} not found")
      return
  ```

**Naming Conventions:**
- Functions: `snake_case` (e.g., `process_file`)
- Variables: `snake_case` (e.g., `heading_counter`)
- Constants: `UPPER_SNAKE_CASE` (if applicable)
- Classes: `PascalCase` (if used)

### Quarkdown Content Style

**Headings:**
- Use numbered headings: `## 1. Section Title`
- Maintain hierarchical structure
- Reset numbering appropriately when changing levels

**Tables:**
- Use pipe syntax for tables
- Align columns consistently
- Example:
  ```markdown
  | Pattern | One-Line Summary | Difficulty | Progress |
  |---------|------------------|------------|----------|
  | Singleton | Ensure a class has only one instance | ⭐ | ✅ |
  ```

**Code Blocks:**
- Use triple backticks with language specification
- Example:
  ```markdown
  ```python
  def example_function():
      return "Hello World"
  ```
  ```

**Admonitions:**
- Use Quarkdown admonition syntax
- Example:
  ```markdown
  > **Note**: This is an important observation
  ```

**Cross-references:**
- Use `.seealso` for related content
- Link to other documents when relevant

## 📁 File Organization

**Directory Structure:**
```
tech-study-notes/
├── computer_science_fundamentals/
├── databases/
├── software_design/
├── system_design/
├── data_engineering/
├── devops_cicd/
├── cloud_certifications/
├── osint/
├── deep_web/
├── data_visualization/
├── images/
├── output/
├── _nav.qd
├── _setup.qd
├── main.qd
└── README.md
```

**File Naming:**
- Use `snake_case` for directory names
- Use `snake_case.qd` for Quarkdown files
- Use descriptive names that indicate content

## 🔄 Version Control

**Git Best Practices:**
- Commit messages should be clear and descriptive
- Use present tense: "Add section on design patterns"
- Reference issues when applicable
- Keep commits focused on single changes

**Branch Strategy:**
- `main`: Production/stable branch
- `feature/*`: For new features
- `fix/*`: For bug fixes
- `docs/*`: For documentation improvements

## 🤖 AI Agent Specific Guidelines

**Working with Quarkdown:**
- Always maintain the `.docname` and `.include {docs}` headers
- Preserve existing heading structure and numbering
- Use the `fix_headings.py` script to renumber headings after major changes

**Content Creation:**
- Follow existing patterns in similar files
- Use consistent terminology
- Provide practical examples
- Reference sources when appropriate

**Python Scripts:**
- Follow PEP 8 style guide
- Add comprehensive docstrings
- Include error handling for file operations
- Test scripts before committing

## 🧪 Testing Approach

**Manual Testing:**
1. Compile the knowledge base: `quarkdown c main.qd`
2. Open `output/tech-study-notes/index.html` in browser
3. Verify navigation works correctly
4. Check all links and cross-references

**Automated Checks:**
- Run `python3 -m py_compile fix_headings.py` to check syntax
- Use `ruff check fix_headings.py` for linting (if available)

## 📚 Documentation Standards

**Writing Style:**
- Use clear, concise language
- Explain concepts before diving into details
- Provide practical examples
- Use consistent terminology

**Code Examples:**
- Keep examples simple and focused
- Use proper syntax highlighting
- Include expected output when relevant

**References:**
- Cite sources when using external content
- Link to official documentation when possible
- Give credit to original authors

## 🚫 Prohibited Actions

- Do NOT modify `output/` directory directly (generated content)
- Do NOT remove required headers from `.qd` files
- Do NOT use inconsistent heading numbering
- Do NOT commit large binary files
- Do NOT include sensitive information

## 🔧 Tool Configuration

**Quarkdown:**
- Version: 1.14.0+
- Document Type: Docs (wiki-style)
- Theme: Default Quarkdown theme

**Python:**
- Version: 3.14.3+
- Linter: Ruff (recommended)
- Formatter: Follow PEP 8 standards

## 📝 Contribution Workflow

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/your-feature`
3. **Make changes** following these guidelines
4. **Test your changes**: Compile and verify output
5. **Commit changes**: Use clear commit messages
6. **Push to your fork**: `git push origin feature/your-feature`
7. **Create a Pull Request** with detailed description

## 🎯 Quality Standards

- All content should be accurate and well-researched
- Code examples should be tested and working
- Documentation should be clear and helpful
- Follow existing patterns and conventions
- Maintain consistent style throughout

## 📬 Communication

For questions or issues, create a GitHub issue with:
- Clear description of the problem
- Steps to reproduce (if applicable)
- Suggested solution (if available)

This AGENTS.md file provides comprehensive guidelines for maintaining consistency and quality in the Tech Study Notes repository.