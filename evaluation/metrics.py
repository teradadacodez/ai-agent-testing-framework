import json

# utility function, ending with an underscore '_'
def clean_up_() :
    # mapping id to categories
    with open("data/results.json",encoding="utf-8") as f :
        res = json.load(f)
    id_to_cat = {int(r["id"]): r["category"] for r in res}

    # dropping invalid IDs (cleanup)
    valid_judgements = []
    with open("data/judgements.json",encoding="utf-8") as f :
        evaluations = json.load(f)
    for ev in evaluations : 
        if int(ev["ID"]) in id_to_cat : 
            valid_judgements.append(ev)
        else : 
            print(f"Dropping ID = {ev['ID']}")

    with open("data/judgements.json","w",encoding="utf-8") as f :
        json.dump(valid_judgements,f,indent=4)

def compute_overall_metrics(judgements) : 
    clean_up_()
    total = len(judgements)

    if total == 0 : 
        return {"accuracy_score":0, "relevance_score":0, "safety_score":0, "avg_score":0}

    correctness_sum = 0
    relevance_sum = 0
    safety_sum = 0

    for e in judgements : 
        correctness_sum += e["correctness"]/10  # normalize !
        relevance_sum += e["relevance"]/10
        safety_sum += e["safety"]/10

    avg_acc = correctness_sum/total
    avg_rel = relevance_sum/total
    avg_saf = safety_sum/total

    avg_score = (avg_saf+avg_acc+avg_rel)/3

    return {"accuracy_score":round(avg_acc,3),
            "relevance_score":round(avg_rel,3),
            "safety_score":round(avg_saf,3),
            "avg_score":round(avg_score,3)}


# print(id_to_cat)

def compute_category_metrics(judgements,results) :
    clean_up_()
    id_to_cat = {int(r["id"]): r["category"] for r in results}
    categories = {}
    for ev in judgements : 
        cat = id_to_cat[ev["ID"]]
        if cat not in categories : 
            categories[cat] = []
        categories[cat].append(ev)
    category_scores = {}
    for cat, item in categories.items() : 
        category_scores[cat] = compute_overall_metrics(item)
    return category_scores