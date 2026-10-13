# Agentic Document Automation System

A config-driven "task manager" for documents: reads a JSON task list and runs
document operations via a document agent — Word report generation from a
template, PDF watermarking, PDF merging, and text extraction — with a full
audit report.

## Structure

```
agentic-document-automator/
├── src/
│   ├── __init__.py
│   ├── document_agent.py    # Orchestrates task execution
│   ├── config_parser.py     # Loads and validates the JSON config
│   ├── pdf_tasks.py         # PDF operations (watermark, merge, extract)
│   ├── word_tasks.py        # Word report generation + extraction
│   └── utils.py             # Logging + helpers
├── configs/
│   └── document_automation_config.json
├── templates/
│   └── report_template.docx
├── documents/               # Input PDFs + generated outputs
├── main.py
└── requirements.txt
```

## Setup & Run

```bash
python -m venv venv
venv\Scripts\activate          # Windows
pip install -r requirements.txt
python main.py
```

Outputs are written to `documents/`: `generated_report.docx`,
`watermarked_document.pdf`, `merged_docs.pdf`, extracted text files, and an
audit report under `documents/reports/`.

## Configuration

All behavior is defined in `configs/document_automation_config.json`:
`global_data` supplies shared placeholder values, `output_files` names the
deliverables, and `tasks` lists the operations to run in order (each task has
a `type` and its own parameters).
