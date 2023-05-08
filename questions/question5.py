import pandas as pd
import matplotlib.pyplot as plt

def execute(df):
    print("Question 5: During the whole year, what is the average amount of passengers per stop? What is the standard deviation?")
    
    # Adding up all passengers per stop
    df['date'] = pd.to_datetime(df['date'])
    df = df.groupby(df['stop'])['count'].sum().sort_values(ascending=False)
    
    # Calculating and printing the mean and standard deviation of passengers per stop
    print("Average amount of passengers per stop was: {0}".format(df.mean()))
    print("Standard deviation: {0}".format(df.std()))
