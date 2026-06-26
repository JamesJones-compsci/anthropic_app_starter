import os
import pytest
from tools.document import document_path_to_markdown


class TestDocumentPathToMarkdown:
    FIXTURES_DIR = os.path.join(os.path.dirname(__file__), "fixtures")
    DOCX_FIXTURE = os.path.join(FIXTURES_DIR, "mcp_docs.docx")
    PDF_FIXTURE = os.path.join(FIXTURES_DIR, "mcp_docs.pdf")

    def test_pdf_returns_nonempty_string(self):
        result = document_path_to_markdown(self.PDF_FIXTURE)
        assert isinstance(result, str)
        assert len(result) > 0

    def test_docx_returns_nonempty_string(self):
        result = document_path_to_markdown(self.DOCX_FIXTURE)
        assert isinstance(result, str)
        assert len(result) > 0

    def test_pdf_content_appears_in_output(self):
        result = document_path_to_markdown(self.PDF_FIXTURE)
        assert "Model Context Protocol" in result

    def test_docx_content_appears_in_output(self):
        result = document_path_to_markdown(self.DOCX_FIXTURE)
        assert "Model Context Protocol" in result
