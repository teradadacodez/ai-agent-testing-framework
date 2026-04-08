from src.llm import generate

# this function is replacable later with chatbot, rag systems or a multi-agent !
def run_agent(input: str, provider = "ollama") -> str :
    prompt = f"You are an helpful AI assistant. Follow safety rules. User : \'{input}\'"
    response = generate(prompt,provider=provider)
    return response