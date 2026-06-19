# Import & read
import sys
import pandas as pd

def load_df(filepath):
    df = pd.read_csv(filepath)

    print("Are you calculating spending or income?")
    
    while True:
        filter_type = input("If spending write 's', if income write 'i': ")
        
        if filter_type.lower() == 's':  
            print("I can filter out up to 4 transaction for you if you'd like")
            print("Any string will work")
            filter_argument_1 = input("Filter option 1: ")
            filter_argument_2 = input("Filter option 2: ")
            filter_argument_3 = input("Filter option 3: ")
            filter_argument_4 = input("Filter option 4: ")
            
            # Get only transactions with negative numbers (< 0)
            df_spending = df[
                (df["Transactiebedrag"] < 0) &
                (~df["Omschrijving"].str.contains(filter_argument_1, case=False)) &
                (~df["Omschrijving"].str.contains(filter_argument_2, case=False)) &
                (~df["Omschrijving"].str.contains(filter_argument_3, case=False)) &
                (~df["Omschrijving"].str.contains(filter_argument_4, case=False))
            ]

            return df_spending, "s"
        elif filter_type.lower() == 'i':
            # Get only transactions with positive numbers (> 0)
            df_income = df[(df["Transactiebedrag"] > 0)]

            return df_income, "i"
        else:
         print("Looks like you selected a different operation I can't help you with :(")