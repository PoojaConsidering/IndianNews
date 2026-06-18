import anthropic
import json
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def classify_headlines(headlines: list[str]) -> dict:
    headlines_text = "\n".join(f"- {h}" for h in headlines)

    prompt = f"""You are a news classifier. Below is a list of headlines scraped from Indian news websites.

Classify each headline as either:
- "india": if it is primarily about India (Indian politics, Indian people, Indian states, Indian sports teams, etc.)
- "global": if it is primarily about international/world news (other countries, global events, etc.)

Headlines:
{headlines_text}

Respond ONLY with a valid JSON object in this exact format, no explanation:
{{
  "india_count": <number>,
  "global_count": <number>,
  "india_headlines": ["headline1", "headline2", ...],
  "global_headlines": ["headline1", "headline2", ...]
}}"""

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4096,
        messages=[{"role": "user", "content": prompt}]
    )

    raw = message.content[0].text.strip()
    result = json.loads(raw)
    return result


if __name__ == "__main__":
    sample = [
        "PM Modi inaugurates new highway in Gujarat",
        "US and China hold trade talks in Geneva",
        "IPL 2025: Mumbai Indians win by 6 wickets",
        "Ukraine war enters third year with no end in sight",
        "Bengaluru traffic worsens due to metro work"
    ]
    result = classify_headlines(sample)
    print(result)