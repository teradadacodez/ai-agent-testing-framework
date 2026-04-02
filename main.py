from src.llm import call_llm

# this function is replacable later with chatbot, rag systems or a multi-agent !
def run_agent(input: str) -> str :
    response = call_llm(input)
    return response