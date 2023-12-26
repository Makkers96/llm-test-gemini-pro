import google.generativeai as genai
import os

key = os.getenv('google_key')
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

llm = genai.GenerativeModel('gemini-pro',
                            generation_config=generation_config,
                            safety_settings=safety_settings)


def run_llm(question):
    prompt = f"""{question}"""
    result = llm.generate_content(prompt)
    if result:
        response = result.text
    else:
        response = "Couldn't get a response from the llm."

    return response

# # pip install langchain-google-genai
# from langchain_google_genai import ChatGoogleGenerativeAI
# llm = ChatGoogleGenerativeAI(model="gemini-pro",
#                              temperature=0,
#                              google_api_key=key,
#                              safety_settings=safety_settings,
#                              max_output_tokens=2048,
#                              top_k=1,
#                              top_p=1,
#                              )
#
#
# def run_llm(question):
#     print(f"TEST: Ran the run_llm function.")
#     result = llm.invoke(question)
#     print(f"TEST2: Got result: {result}")
#     print(f"TEST3: Going to return result.content: {result.content}")
#     return result.content


# region Chat
chat = llm.start_chat(history=[])


def run_chat(input):
    chat.send_message(input)
    print(f"TEST TEST TEST: This is chat.history:")
    print(chat.history)
    return chat.history
# endregion
