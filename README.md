# AI Post-Mortem Generator

Generate structured SRE post-mortems from incident descriptions using Claude API,
with automatic fallback to Amazon Bedrock.

## Usage
```bash
pip install -r requirements.txt
cp .env.example .env
python main.py "Database connection pool exhausted, 45min outage on payment service"
```

## How it works
- Sends incident description to Claude Sonnet via Anthropic API
- Falls back to Claude on Bedrock if API is unavailable
- Outputs a markdown post-mortem with root cause, timeline, and action items

## Stack
- Python, Anthropic SDK, Boto3
