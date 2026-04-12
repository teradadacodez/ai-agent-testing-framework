# full pipeline

import json
from src.runner import run_tests
from src.evaluator import llm_judge
from report.report_generator import display_failure_report, display_score_report, display_latency_report, generate_json_report 
from evaluation.metrics import compute_overall_metrics, compute_category_metrics

with open("data/test_cases.json", encoding="utf-8") as f : 
    test_cases = json.load(f)

results = run_tests(test_cases)

with open("data/results.json","w",encoding="utf-8") as f :
    json.dump(results,f,indent=4)

judgements = [llm_judge(res) for res in results]

with open("data/judgements.json","w",encoding="utf-8") as f :
    json.dump(judgements,f,indent=4)

overall = compute_overall_metrics(judgements)
category = compute_category_metrics(judgements,results)

display_score_report(overall,category)
display_failure_report(judgements)
display_latency_report(results)

dashboard = generate_json_report(judgements,results)

with open("data/dashboard.json","w",encoding="utf-8") as f :
    json.dump(dashboard,f,indent=4)