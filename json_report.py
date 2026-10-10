import json

def write_json_report(page_data, filename = "report.json"):
    pages = sorted(page_data.values(), key = lambda p: p["url"])
    with open(filename, "w") as f:
        json.dump(pages, f, indent = 2)