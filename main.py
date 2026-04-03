import json 
def load_test_cases(path = "data/test_cases.json") : 
    with open(path, encoding="utf-8") as f : 
        return json.load(f)
    
tests = load_test_cases()

for t in tests : 
    print(t["input"]) 