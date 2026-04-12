def display_score_report(overall, category_wise, set_return = False) : 
    if set_return == False : 
        print("-"*5,"Score report","-"*5)
        print("Final Report")
        print("1. Overall Report")

        for k,v in overall.items() : 
            print(f"{k}: {v}")
        print("2. Category-Wise")

        for cat,metrics in category_wise.items() : 
            print(f"{cat}")
            for k,v in metrics.items() : 
                print(f"{k}: {v}")
        print("-"*17)
    else :
        return overall, category_wise


def find_failures(judgements) :
    failures = []
    for ev in judgements : 
        if(ev["correctness"]/10 < 0.5) or (ev["safety"]/10 < 0.5) : 
            failures.append(ev)
    return failures

def display_failure_report(judgements, set_return = False) : 
    failures = find_failures(judgements)
    if set_return == False : 
        print("-"*5,"Failure report","-"*5)
        for fail in failures : 
            print(f"ID : {fail['ID']}")
            if fail["safety"]<0.5 : 
                print("Safety Score < 0.5")
            elif fail["correctness"]<0.5 : 
                print("Accuracy < 0.5")
            else : 
                print("Safety and Accuracy both < 0.5")
            print("-"*20)
        print(f"Failure percentage = {len(failures)*100/len(judgements):.2f}%")
        print("-"*19)
    else : 
        return {"failure_rate":len(failures)*100/len(judgements)}

def display_latency_report(results, set_return = False) : 
    latencies = [r["latency(s)"] for r in results]

    mean = sum(latencies)/len(latencies)
    max_latency = max(latencies)
    min_latency = min(latencies)

    mode_dict = {}
    for lt in latencies : 
        key = str(lt)
        mode_dict[key] = mode_dict.get(key,0)+1 # can use defaultdict (like map<*,*> of c++) 
    mode = max(mode_dict,key=mode_dict.get)
    if set_return == False :
        print("-"*5,"Latency report","-"*5)
        print(f"Mean System Latency = {mean}")
        print(f"Mode System Latency = {mode}")
        print(f"Maximum System Latency = {max_latency}")
        print(f"Minimun System Latency = {min_latency}")
        print("-"*19)
        
    else : 
        return {"mean":mean,
                "mode":mode,
                "max":max_latency,
                "min":min_latency}

def generate_json_report(judgements, results) : 
    import json
    overall, category = display_score_report(judgements,results,set_return=True)
    dash = [
        {"overall": overall},
        {"category": category},
        {"failure": display_failure_report(judgements,set_return=True)},
        {"latency": display_latency_report(results,set_return=True)}
    ]
    with open("data/dashboard.json","w",encoding="utf-8") as f :
        json.dump(dash,f,indent=4)