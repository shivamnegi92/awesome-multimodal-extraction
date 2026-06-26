"""Document -> structured Markdown/JSON with Docling.

Setup:
    pip install docling
"""
from docling.document_converter import DocumentConverter

converter = DocumentConverter()
result = converter.convert("report.pdf")

# Clean Markdown (great as LLM input for downstream field extraction)
print(result.document.export_to_markdown())

# Or structured dict
# import json; print(json.dumps(result.document.export_to_dict(), indent=2)[:500])
