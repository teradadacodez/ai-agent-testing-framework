from src.evaluator import llm_judge
import json

def load_results(path = "data/results.json") : 
    with open(path,encoding="utf-8") as f :
        return json.load(f)
    
res = load_results()

judgement_list = []
for r in res : 
    judgement = json.loads(llm_judge(r["id"],r["input"],r["output"],r["expected"]))
    judgement_list.append(judgement)
    

with open("data/judgements.json","w",encoding="utf-8") as f :
    json.dump(judgement_list,f,indent=4)
