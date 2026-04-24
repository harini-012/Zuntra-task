import json
import re
import google.generativeai as genai

genai.configure(api_key="AIzaSyBugfmCt322KHTlKEQ-C23X10dfzVodeNg")

model = genai.GenerativeModel("gemini-2.5-flash")

messages = [
    "My payment got deducted but service is not activated",
    "App crashes every time I login",
    "How to change my email address?"
]


def classify_message(message):
    prompt = f"""You are a support ticket classifier.

Classify the message into:
- category: Billing, Technical Issue, Account, General Inquiry
- priority: High, Medium, Low

Return ONLY valid JSON. No explanation, no extra text.

Format:
{{
  "category": "Billing",
  "priority": "High"
}}

Message: "{message}"
"""

    try:
        response = model.generate_content(prompt)
        result = response.text.strip()

        # 🔍 Extract JSON safely (handles extra text)
        json_text = re.search(r'\{.*\}', result, re.DOTALL)
        if json_text:
            parsed = json.loads(json_text.group())
        else:
            raise ValueError("No valid JSON found")

        return {
            "message": message,
            "category": parsed.get("category", "Unknown"),
            "priority": parsed.get("priority", "Unknown")
        }

    except Exception as e:
        return {
            "message": message,
            "error": str(e)
        }


def process_messages(messages):
    return [classify_message(msg) for msg in messages]


if __name__ == "__main__":
    results = process_messages(messages)
    print(json.dumps(results, indent=2))
