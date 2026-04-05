from src.ml_model import predict
from src.rule_engine import apply_rules

def make_decision(marketing, operations, current_revenue):
    
    predicted = predict(marketing, operations)
    
    growth = ((predicted - current_revenue) / current_revenue) * 100
    
    decision = apply_rules(growth, predicted, operations)
    
    return predicted, growth, decision