import sys
from src.classifier import classify_spending_transactions

filepath = sys.argv[1]

classify_spending_transactions(filepath)
