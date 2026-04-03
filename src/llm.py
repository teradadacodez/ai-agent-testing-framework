import requests
def call_llm(prompt) : 
    response = requests.post("http://localhost:11434/api/generate",
                             json = {"model":"llama3.2",
                                     "prompt":prompt,
                                     "stream":False})
    if response.status_code != 200 : 
        return "Error Calling LLM"
    return response.json().get("response")