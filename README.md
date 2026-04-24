AI Support Ticket Classifier

Description
This project is an AI-based system that automatically classifies customer support messages into predefined categories and assigns a priority level. It helps reduce manual effort and improves response efficiency.

Features
Classifies support messages into categories
Assigns priority levels based on urgency
Uses AI (Google Gemini) for intelligent understanding
Returns structured JSON output
Includes error handling

Categories
Billing
Technical Issue
Account
General Inquiry

Priority Levels
High: Urgent or blocking issues
Medium: Moderate issues
Low: General or informational queries

Input Example
"My payment got deducted but service is not activated"
"App crashes every time I login"
"How to change my email address?"

Output Example
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

Technologies Used
Python
Google Gemini API
JSON

Setup Instructions
Install Python (version 3.8 or above)
Install required library: pip install google-generativeai
Add your Gemini API key inside the code
Run the program: python app.py

Project Structure
app.py – Main script
README.md – Documentation

How It Works
Takes a list of messages
Sends them to AI
AI classifies category and priority
Returns JSON output

Notes
Do not upload your API key to GitHub
Ensure your API key is valid

Future Improvements
Add frontend interface
Store results in database
Improve accuracy

Author
Harini R
