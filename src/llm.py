import requests
def generator_llm(prompt,MODEL = "llama3.2:1b") : 
    response = requests.post("http://localhost:11434/api/generate",
                             json = {"model":MODEL,
                                     "prompt":prompt,
                                     "stream":False})
    print(f"Chosen Generator model is {MODEL}")
    if response.status_code != 200 : 
        return "Error Calling LLM"
    return response.json().get("response")

def evaluator_llm(prompt,MODEL = "llama3.2") : 
    response = requests.post("http://localhost:11434/api/generate",
                             json={"model":MODEL,
                                   "prompt":prompt,
                                   "stream":False,
                                   "format":"json"})
    print(f"Chosen Evaluator model is {MODEL}")
    if response.status_code != 200 : 
        return "Error Calling LLM"
    return response.json()["response"]

def list_active_models() : 
    model_list = requests.get("http://localhost:11434/api/tags").json().get("models")
    i = 1
    print("Active models are : ")
    for model in model_list : 
        print(f"{i}. {model["model"]}")
        print(f"\t-parameters = {model["details"]["parameter_size"]}")
        print(f"\t-size on disk = {model["size"]} bytes")
        i+=1

import os 
from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv())

from openai import OpenAI

hf_client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("HF_TOKEN"),
)

def hf_llm(prompt, MODEL="openai/gpt-oss-20b:fastest"):
    try:
        response = hf_client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
        )
        print(f"Chosen HF model is {MODEL}")
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"HF_ERROR: {str(e)}"

# router functions which will route the input either to ollama or to HF API
def generate(prompt, provider = "ollama") :
    if provider == "ollama" : 
        return generator_llm(prompt)
    elif provider == "hf" : 
        return hf_llm(prompt)
    else : 
        return "INVALID_PROVIDER"

def evaluate(prompt, provider = "ollama") : 
    if provider == "ollama" : 
        return evaluator_llm(prompt)
    elif provider == "hf" : 
        return hf_llm(prompt)
    else : 
        return "INVALID_PROVIDER"