from src.llm import generator_llm

# this function is replacable later with chatbot, rag systems or a multi-agent !
def run_agent(input: str) -> str :
    prompt = f"You are an helpful AI assistant. Follow safety rules. User : \'{input}\'"
    response = generator_llm(prompt)
    return response