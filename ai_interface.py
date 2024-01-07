""" 
Accesses OpenAI 
"""
from openai import OpenAI
from datastructures import Analysis

def analyze_report(text):
    """ Creates an Analysis object from the given text """
    system_prompt = """
    You are an analysis engine for post-mortem events. Your purpose is to evaluate post-mortem reports and provide valuable information
    to ensure they do not occur again. You respond only in json documents with the following keys:
        "title": This is the title of the document
        "summary": Produce a text summary of the entire document
        "keywords": Produce a list of 10 key words from the document text
        "key_ideas": Produce a list of 3-5 short ideas from the document
    """
    temperature = 3
    model = "gpt-3.5-turbo-16k"
    client = OpenAI()
    chat_completion = client.chat.completions.create(
        messages = [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": "The following is a post-mortem report. Create a json document with the title, summary, keywords, and key ideas"
            }
        ],
        model = model,
    )
    return chat_completion