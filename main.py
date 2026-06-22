import sys
from src.classifier import classify_spending_transactions

def run():
    filepath = sys.argv[1]
    classify_spending_transactions(filepath)
