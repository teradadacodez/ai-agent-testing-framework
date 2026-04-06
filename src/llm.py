import requests
def generator_llm(prompt,MODEL = "llama3.2") : 
    response = requests.post("http://localhost:11434/api/generate",
                             json = {"model":MODEL,
                                     "prompt":prompt,
                                     "stream":False})
    print(f"Chosen Generator model is {MODEL}")
    if response.status_code != 200 : 
        return "Error Calling LLM"
    return response.json().get("response")

def evaluator_llm(prompt,MODEL = "qwen3.5:4b") : 
    response = requests.post("http://localhost:11434/api/generate",
                             json={"model":MODEL,
                                   "prompt":prompt,
                                   "stream":False})
    print(f"Chosen Evaluator model is {MODEL}")
    if response.status_code != 200 : 
        return "Error Calling LLM"
    return response.json().get("response")

def list_active_models() : 
    model_list = requests.get("http://localhost:11434/api/tags").json().get("models")
    i = 1
    print("Active models are : ")
    for model in model_list : 
        print(f"{i}. {model["model"]}")
        print(f"\t-parameters = {model["details"]["parameter_size"]}")
        print(f"\t-size on disk = {model["size"]} bytes")
        i+=1