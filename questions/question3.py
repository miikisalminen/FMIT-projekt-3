import pandas as pd
import matplotlib.pyplot as plt

# Question 3: What were the top 5 most/least popular dates? Are these considered special in some way? (Holidays, Events)

def execute(df):
    df['date'] = pd.to_datetime(df['date'])
    df = df.groupby(df['date'])['count'].sum().sort_values(ascending=False)
    
    print("Top 5 most and least popular dates in 2020")
    print(df)