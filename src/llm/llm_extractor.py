import os
import requests
import logging

def extract_invoice_data(text, context=""):
    api_key = os.getenv("GROQ_API_KEY", "YOUR_GROQ_API_KEY")
    model = "llama3-8b-8192"

    prompt = f"""
    You are an expert invoice parser. Extract key fields from the invoice text.

    Context from past invoices:
    {context}

    Invoice text:
    {text}

    Return JSON with keys: invoice_number, invoice_date, vendor, total_amount, line_items
    """

    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": model,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0
            }
        )
        data = response.json()
        return data["choices"][0]["message"]["content"]
    except Exception as e:
        logging.error(f"LLM extraction failed: {e}")
        return "{}"
