import json
from src.runner import run_tests
def load_test_cases(path = "data/test_cases.json") : 
    with open(path, encoding="utf-8") as f : 
        return json.load(f)
    
tests = load_test_cases()

results = run_tests(tests)
with open("data/results.json","w",encoding="utf-8") as f : 
    json.dump(results,f,indent=4)

for r in results : 
    print(f"input : {r["input"]}, output : {r["output"]}, latency : {r["latency"]:.3f}")
    print("--------------------------------------")