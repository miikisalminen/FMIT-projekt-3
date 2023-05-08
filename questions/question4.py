import pandas as pd
import matplotlib.pyplot as plt

# Question 4: Which weekdays have the most rides?

def execute(df):
    print("Question 4: Which weekdays have the most rides?")

    # Grouping the data into weekdays
    df['date'] = pd.to_datetime(df['date'])
    df = df.groupby(df['date'].dt.day_name())['count'].sum().sort_values(ascending=False)
    
    # Plotting the result into a horizontal bar chart with matplotlib
    print('Plotting the results.\nPlease close the graph to continue...')
    df.plot(x='Weekday', y='Count', kind='barh', title="Passengers by weekday (millions)")
    plt.show()
