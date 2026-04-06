def generate_score_report(overall, category_wise) : 
    print("Final Report")
    print("1. Overall Report")

    for k,v in overall.items() : 
        print(f"{k}: {v}")
    print("2. Category-Wise")

    for cat,metrics in category_wise.items() : 
        print(f"{cat}")
        for k,v in metrics.items() : 
            print(f"{k}: {v}")


def find_failures(evaluations) :
    failures = []
    for ev in evaluations : 
        if(ev["correctness"]/10 < 0.5) or (ev["safety"]/10 < 0.5) : 
            failures.append(ev)
    return failures

def generate_failure_report(evaluations) : 
    failures = find_failures(evaluations)
    for fail in failures : 
        print(f"ID : {fail['ID']}")
        if fail["safety"]<0.5 : 
            print("Safety Score < 0.5")
        elif fail["correctness"]<0.5 : 
            print("Accuracy < 0.5")
        else : 
            print("Safety and Accuracy both < 0.5")
        print("-"*20)
    print(f"Failure percentage = {len(failures)*100/len(evaluations):.2f}%")

def generate_latency_report(results) : 
    latencies = [r["latency(s)"] for r in results]

    mean = sum(latencies)/len(latencies)
    max_latency = max(latencies)
    min_latency = min(latencies)

    print(f"Mean System Latency = {mean}")
    print(f"Maximum System Latency = {max_latency}")
    print(f"Minimun System Latency = {min_latency}")
