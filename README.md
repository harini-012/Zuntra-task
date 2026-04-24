

---

# AI Support Ticket Classifier

---

## Overview

This is a Streamlit web application that uses Google Gemini AI to automatically classify customer support messages into categories and assign priority levels. It helps streamline support workflows by enabling fast and consistent ticket triaging.

---

## Live Demo

Access the deployed application here:
**https://zuntra-task-yniwpwfegmecoyfw2p3saf.streamlit.app/**

---

## Features

* Accepts multiple support messages in JSON array format

* Classifies each message into Billing, Technical Issue, Account, General Inquiry

* Assigns priority levels: High, Medium, Low

* Returns structured JSON output

* Batch processing support for multiple messages

* Clean and API-like response format

---

## Input Format

```json id="ip_01"
[
  "My payment got deducted but service is not activated",
  "App crashes every time I login",
  "How to change my email address?"
]
```

---

## Output Format

```json id="op_01"
[
  {
    "message": "My payment got deducted but service is not activated",
    "category": "Billing",
    "priority": "High"
  },
  {
    "message": "App crashes every time I login",
    "category": "Technical Issue",
    "priority": "High"
  },
  {
    "message": "How to change my email address?",
    "category": "Account",
    "priority": "Low"
  }
]
```

---

## Technology Stack

* Python

* Streamlit

* Google Generative AI (Gemini 2.5 Flash)

* JSON Processing

* Regular Expressions

---

## Installation (Local Setup)

```bash id="st_01"
git clone https://github.com/your-username/support-ticket-classifier.git

cd support-ticket-classifier

pip install -r requirements.txt

streamlit run app.py
```

---

## Configuration

Add your Gemini API key inside the application:

```python id="cfg_01"
genai.configure(api_key="YOUR_API_KEY_HERE")
```

---

## Limitations

* Free Gemini API tier has limited daily requests

* May return rate limit errors (429) under heavy usage

* Requires stable internet connection for API calls

---

## Future Improvements

* Database integration for ticket storage

* Dashboard for analytics and insights

* CSV upload support

* Auto-routing of tickets to departments

* Multi-model fallback system

---

## Purpose

This project demonstrates how AI can be used to automate customer support ticket classification and improve response efficiency.
