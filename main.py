import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# key = os.getenv('google_key')
key = "AIzaSyDKUZN041lm_DsSIP-ZER5zZh-CLutu9pE"
genai.configure(api_key=key)

generation_config = {
    "temperature": 0,
    "max_output_tokens": 2048,
    "top_p": 1,
    "top_k": 1,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE"
    }
]

# text_model = genai.GenerativeModel('gemini-pro',
#                                    generation_config=generation_config,
#                                    safety_settings=safety_settings)
#
#
# def run_llm(question):
#     prompt = f"""{question}"""
#     result = text_model.generate_content(prompt)
#     print(f"TEST: This is result from run_llm b4 getting text/response: {result}")
#     if result:
#         response = result.text
#         print(f"LLM Response: {response}")
#     else:
#         response = "Couldn't get a response from the llm."
#
#     return response

llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0)


def run_llm(question):
    print(f"TEST: Ran the run_llm function.")
    result = llm.invoke(question)
    print(f"TEST2: Got result: {result}")
    print(f"TEST3: Going to return result.content: {result.content}")
    return result.content
