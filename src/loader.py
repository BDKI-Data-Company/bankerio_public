# Import & read
import sys
import pandas as pd

def load_df(filepath):
    df = pd.read_csv(filepath)
    filter_options = []

    print("Are you calculating spending or income?")
    
    while True:
        filter_type = input("If spending write 's', if income write 'i': ")
        
        if filter_type.lower() == 's':  
            # Get only transactions with negative numbers (< 0)
            df_spending = df[
                (df["Transactiebedrag"] < 0)]

            return df_spending, "s", filter_options
        elif filter_type.lower() == 'i':
            # Get only transactions with positive numbers (> 0)
            df_income = df[(df["Transactiebedrag"] > 0)]

            return df_income, "i", []
        else:
         print("Looks like you selected a different operation I can't help you with :(")