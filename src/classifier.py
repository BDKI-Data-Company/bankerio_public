# Classify transactions
import pandas as pd
from src.loader import load_df


def classify_spending_transactions(filepath):
    df, filter_type = load_df(filepath)
    
    if filter_type == "i":
        total_income = df["Transactiebedrag"].sum()
        print("Total income is: ", total_income)
        return
    elif filter_type == "s":     
        # Dict for pairs FILTER ARG: "WHAT TO FILTER BY"
        # ie: SHOPPING: "ALBERT HEIJN"
        user_categories = {}


        
        total_spending = df["Transactiebedrag"].sum()

        # Extract clean merchant names
        df["merchant"] = df["Omschrijving"].str.extract(r'BEA, Betaalpas\s+(.+?),PAS')
        mask = df["merchant"].isna()
        df.loc[mask, "merchant"] = df.loc[mask, "Omschrijving"].str.extract(r'NAME/([^/]+)')[0]

        df["category"] = "unclassified"
        
        all_rules = {**PARAMS_TEMPLATE}
        for category, keywords in all_rules.items():
            pattern = "|".join(keywords)
            mask = df["Omschrijving"].str.contains(pattern, case=False)
            df.loc[mask, "category"] = category

        print('Total spending is: ', abs(total_spending))

        category_total = df.groupby("category")["Transactiebedrag"].sum().abs()
        print(category_total)

        # Unclassified - now prints clean merchant name
        df_unclassified = df[df["category"] == "unclassified"][["merchant", "Transactiebedrag"]]
        for _, row in df_unclassified.iterrows():
            print(row["merchant"], abs(row["Transactiebedrag"]))