# Agentic Communication Workflows (Advanced Email & SMS)

A configuration-driven communication agent: reads a JSON pipeline of tasks and
executes them in order - sends templated emails with attachments, then
processes the inbox (IMAP): downloads attachments, applies conditional rules
(SMS alert via carrier email gateway, auto-reply), and writes an audit report.

## Structure

```
communication-pipeline/
|- src/
|  |- __init__.py
|  |- communication_agent.py   # Orchestrates the task pipeline
|  |- config_parser.py         # Loads and validates the JSON config
|  |- email_tasks.py           # SMTP send + IMAP search/fetch/attachments
|  |- sms_tasks.py             # SMS via carrier email-to-SMS gateways
|  |- template_renderer.py     # {placeholder} / {value:.2f} rendering
|  |- utils.py                 # Logging, env, audit helpers
|- configs/
|  |- comm_pipeline_config.json
|- data/
|  |- reports/                 # Attachments used by the pipeline
|- main.py
|- requirements.txt
```

## Setup & Run

1. `python -m venv venv`, activate it, `pip install -r requirements.txt`
2. Create a `.env` with: `SENDER_EMAIL`, `SENDER_APP_PASSWORD`, `SMTP_SERVER`,
   `SMTP_PORT`, `IMAP_SERVER`
3. `python main.py`

Outputs: emails sent per the pipeline, inbox processed per the rules, and an
audit report under `reports/audit_report_comm_<timestamp>.json`.
