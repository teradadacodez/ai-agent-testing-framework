import time
from src.agent import run_agent

def run_tests(test_cases) : # accepts test_cases in json format !
    results = []
    for test in test_cases : 
        input_text = test["input"]
        print(f"Running test case id = {test["id"]}.") # for logging

        start_time = time.time()
        try : 
            output = run_agent(input_text)
        except Exception as e : 
            print(f"Error : {e}")
            output = "ERROR"
        llm_output = run_agent(input_text)
        end_time = time.time() 

        system_latency = end_time-start_time
        results.append({
                "id" : test["id"],
                "input" : input_text,
                "output" : llm_output,
                "expected" : test["expected_behaviour"],
                "category" : test["category"],
                "latency(s)" : int(f"{system_latency:3f}")
            })
    return results