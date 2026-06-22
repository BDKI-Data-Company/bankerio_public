# Classify transactions
import pandas as pd
from bankerio_public.loader import load_df


def classify_spending_transactions(filepath):
    df, filter_type, filter_options = load_df(filepath)
    
    if filter_type == "i":
        total_income = df["Transactiebedrag"].sum()
        print("Total income is: ", total_income)
        return
    elif filter_type == "s":     
        # Dict for pairs FILTER ARG: "WHAT TO FILTER BY"
        # ie: SHOPPING: "ALBERT HEIJN"
        user_categories = {}
        # Prompt user for categories to filter by
        for i in range (10):
            cat_name = input(f"Category {i + 1} name (or press Enter to stop): ")
            if not cat_name.strip():
                break
            keywords_raw = input(f"Keywords for {cat_name} (comma-separated): ")
            keywords = [k.strip() for k in keywords_raw.split(",")]
            user_categories[cat_name] = keywords

        
        total_spending = df["Transactiebedrag"].sum()

        # Extract clean merchant names
        df["merchant"] = df["Omschrijving"].str.extract(r'BEA, Betaalpas\s+(.+?),PAS')
        mask = df["merchant"].isna()
        df.loc[mask, "merchant"] = df.loc[mask, "Omschrijving"].str.extract(r'NAME/([^/]+)')[0]

        df["category"] = "unclassified"
        
        for category, keywords in user_categories.items():
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