import json

def load_rules():
    with open("rules.json") as f:
        return json.load(f)

def apply_rules(growth, revenue, cost):
    rules = load_rules()
    
    for rule in rules:
        if rule["type"] == "growth":
            if rule["operator"] == ">" and growth > rule["value"]:
                return rule["decision"]
            elif rule["operator"] == "<=" and growth <= rule["value"]:
                return rule["decision"]
        
        if rule["type"] == "cost":
            if cost > revenue:
                return rule["decision"]
    
    return "Hold"