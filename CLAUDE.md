# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Start the MCP server
uv run main.py

# Run all tests
uv run pytest

# Run a single test file
uv run pytest tests/test_document.py

# Run a specific test by name
uv run pytest tests/test_document.py::TestBinaryDocumentToMarkdown::test_binary_document_to_markdown_with_docx
```

## Architecture

The project is an MCP server that exposes document and utility tools to AI assistants via the [FastMCP](https://github.com/jlowin/fastmcp) framework.

**Entry point:** `main.py` creates the `FastMCP` instance and registers tools by calling `mcp.tool()(function)`. Only functions explicitly registered here are exposed to MCP clients.

**Tools layer (`tools/`):** Each file contains either MCP-registered tool functions or utility helpers called by those tools. `tools/math.py` shows the canonical MCP tool pattern. `tools/document.py` shows a utility helper (`binary_document_to_markdown`) that is not itself an MCP tool but is intended to be called by tools that are.

**Tests (`tests/`):** Pytest tests call tool/utility functions directly (not through MCP). Fixtures live in `tests/fixtures/`.

## Defining MCP Tools

Tools are plain Python functions registered in `main.py` with `mcp.tool()(my_function)`. Use `Field` from pydantic for all parameter descriptions:

```python
from pydantic import Field

def my_tool(
    param1: str = Field(description="Detailed description of this parameter"),
    param2: int = Field(description="Explain what this parameter does"),
) -> ReturnType:
    """One-line summary.

    Detailed explanation of what the tool does.

    When to use:
    - Specific scenario where this tool applies
    - Another valid use case

    When NOT to use:
    - Scenario where a different tool is more appropriate

    Examples:
    >>> my_tool("foo", 42)
    "expected output"
    """
    # implementation
```

The docstring structure matters — it is surfaced to the AI assistant as the tool description. The `Field` descriptions are shown as parameter-level hints. Both should be precise enough that an AI can choose the right tool and pass correct arguments without trial and error.

After writing the function, register it in `main.py`:

```python
from tools.my_module import my_tool
mcp.tool()(my_tool)
```
