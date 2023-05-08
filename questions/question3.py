import pandas as pd
import matplotlib.pyplot as plt

def execute(df):
    print("Question 3: What were the top 5 most/least popular dates? Are these considered special in some way? (Holidays, Events)")

    # Grouping data into individual days
    df['date'] = pd.to_datetime(df['date'])
    df = df.groupby(df['date'])['count'].sum().sort_values(ascending=False)
    
    # Printing the DataFrame to show results
    print("Top 5 most and least popular dates in 2020")
    print(df)
