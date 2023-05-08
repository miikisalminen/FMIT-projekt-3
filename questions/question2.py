import pandas as pd
import matplotlib.pyplot as plt

def execute(df):

    print("Question 2: Can the effects of the start of the COVID-19 pandemic be seen in the data? If so how?")

    # Grouping the data into months
    df['date'] = pd.to_datetime(df['date'])
    df = df.groupby(df['date'].dt.strftime('%B'))['count'].sum().sort_values(ascending=False)
    
    # Plotting the results into a horizontal bar chart with matplotlib
    print('Plotting the results.\nPlease close the graph to continue...')
    df.plot(y='Month', x='Count', kind='barh', title="Föli passengers per month (millions)")
    plt.show()