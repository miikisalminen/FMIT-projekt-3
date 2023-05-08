import pandas as pd
import matplotlib.pyplot as plt

# Question 4: Which weekdays have the most rides?

def execute(df):
    df['date'] = pd.to_datetime(df['date'])
    df = df.groupby(df['date'].dt.day_name())['count'].sum().sort_values(ascending=False)
    
    df.plot(x='Weekday', y='Count', kind='barh', title="Passengers by weekday")
    plt.show()