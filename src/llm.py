import requests
def generator_llm(prompt,MODEL = "llama3.2") : 
    response = requests.post("http://localhost:11434/api/generate",
                             json = {"model":MODEL,
                                     "prompt":prompt,
                                     "stream":False})
    if response.status_code != 200 : 
        return "Error Calling LLM"
    return response.json().get("response")

def evaluator_llm(prompt,MODEL = "qwen3.5:9b") : 
    response = requests.post("http://localhost:11434/api/generate",
                             json={"model":MODEL,
                                   "prompt":prompt,
                                   "stream":False})
    if response.status_code != 200 : 
        return "Error Calling LLM"
    return response.json().get("response")