from openai import OpenAI
import os
import json
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

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

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": prompt}]
    )
    raw = response.choices[0].message.content.strip()
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