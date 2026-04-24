import json
import re
import streamlit as st
import google.generativeai as genai


genai.configure(api_key="AIzaSyBzlSFKAGZ1s-KN3U7yRVaDdBdLM8l4r1Y")

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("AI Support Ticket Classifier (Batch Mode)")

st.write("Enter messages in JSON array format")

# 🔹 Input
user_input = st.text_area(
    "Enter messages",
    placeholder='["message 1", "message 2", "message 3"]'
)


def classify_messages(messages):
    prompt = f"""
You are a support ticket classifier.

For each message, return a JSON array where each object contains:
- message
- category: Billing, Technical Issue, Account, General Inquiry
- priority: High, Medium, Low

Return ONLY valid JSON array.

Messages:
{json.dumps(messages)}
"""

    try:
        response = model.generate_content(prompt)
        result = response.text.strip()

        # Extract JSON array safely
        match = re.search(r'\[.*\]', result, re.DOTALL)

        if match:
            return json.loads(match.group())
        else:
            return [{
                "error": "Invalid model response",
                "raw_output": result
            }]

    except Exception as e:
        return [{
            "error": str(e)
        }]



if st.button("Classify"):
    if user_input:
        try:
            messages = json.loads(user_input)

            
            results = classify_messages(messages)

            st.subheader("Final Output")

           
            st.code(
                json.dumps(results, indent=2),
                language="json"
            )

        except Exception as e:
            st.error(f"Invalid JSON input: {str(e)}")

    else:
        st.warning("Please enter messages")
