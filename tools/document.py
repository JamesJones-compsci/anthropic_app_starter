import os
from markitdown import MarkItDown, StreamInfo
from io import BytesIO
from pydantic import Field


def document_path_to_markdown(
    path: str = Field(description="Absolute or relative path to a PDF or DOCX file"),
) -> str:
    """Convert a document file to markdown text.

    Reads the file at the given path and converts its contents to markdown.

    When to use:
    - When you have a file path to a PDF or DOCX document and need its text content
    - When you want to extract structured text from a local document

    When NOT to use:
    - When you already have the file contents as bytes (use binary_document_to_markdown instead)

    Examples:
    >>> document_path_to_markdown("/path/to/report.pdf")
    "# Report Title\\n\\nSome content..."
    """
    extension: str = os.path.splitext(path)[1].lstrip(".")
    with open(path, "rb") as f:
        binary_data: bytes = f.read()
    return binary_document_to_markdown(binary_data, extension)


def binary_document_to_markdown(binary_data: bytes, file_type: str) -> str:
    """Converts binary document data to markdown-formatted text."""
    md = MarkItDown()
    file_obj = BytesIO(binary_data)
    stream_info = StreamInfo(extension=file_type)
    result = md.convert(file_obj, stream_info=stream_info)
    return result.text_content
