import anthropic
import json
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def generate_summary(india_headlines: list[str], global_headlines: list[str]) -> dict:
    india_text = "\n".join(f"- {h}" for h in india_headlines)
    global_text = "\n".join(f"- {h}" for h in global_headlines)

    prompt = f"""You are a news analyst. Below are today's headlines from Indian news websites, split into Indian news and Global news.

INDIAN NEWS HEADLINES:
{india_text}

GLOBAL NEWS HEADLINES:
{global_text}

Do two things:
1. Write a SHORT SUMMARY (2-3 sentences) of what Indian news mainly talked about today.
2. Write a DETAILED OVERVIEW (1-2 paragraphs) covering the major themes, events, and topics from the Indian headlines.

Respond ONLY with a valid JSON object in this exact format, no explanation:
{{
  "summary": "short summary here",
  "overview": "detailed overview here"
}}"""

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}]
    )

    raw = message.content[0].text.strip()
    result = json.loads(raw)
    return result

if __name__ == "__main__":
    sample_india = [
        "PM Modi inaugurates new highway in Gujarat",
        "IPL 2025: Mumbai Indians win by 6 wickets",
        "Bengaluru traffic worsens due to metro work"
    ]
    sample_global = [
        "US and China hold trade talks in Geneva",
        "Ukraine war enters third year with no end in sight"
    ]
    result = generate_summary(sample_india, sample_global)
    print(result)