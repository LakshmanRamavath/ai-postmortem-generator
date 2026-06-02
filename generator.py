import os
import json
import anthropic
import boto3

PROMPT = """You are an SRE expert. Given this incident, generate a concise post-mortem in markdown with sections:
## Summary
## Timeline
## Root Cause
## Impact
## Resolution
## Action Items

Incident: {incident}"""

def generate_postmortem(incident: str) -> str:
    try:
        return _via_claude(incident)
    except Exception:
        return _via_bedrock(incident)

def _via_claude(incident: str) -> str:
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    msg = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=[{"role": "user", "content": PROMPT.format(incident=incident)}]
    )
    return msg.content[0].text

def _via_bedrock(incident: str) -> str:
    client = boto3.client("bedrock-runtime", region_name=os.environ.get("AWS_REGION", "us-east-1"))
    body = json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1024,
        "messages": [{"role": "user", "content": PROMPT.format(incident=incident)}]
    })
    resp = client.invoke_model(modelId="anthropic.claude-3-5-sonnet-20241022-v2:0", body=body)
    return json.loads(resp["body"].read())["content"][0]["text"]
