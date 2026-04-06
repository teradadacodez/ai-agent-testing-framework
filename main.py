import json
from evaluation.metrics import compute_metrics, category_metrics
from report.report_generator import generate_latency_report, generate_score_report, generate_failure_report

with open("data/judgements.json") as f : 
    evaluations = json.load(f)

with open("data/results.json",encoding="utf-8") as f :
    results = json.load(f) 

# Mapping
id_to_cat = {int(r["id"]): r["category"] for r in results}

# Metrics
overall = compute_metrics(evaluations)
category_wise = category_metrics(evaluations, id_to_cat)

# Score
generate_score_report(overall,category_wise)

# Failure
generate_failure_report(evaluations)

# Latency
generate_latency_report(results)