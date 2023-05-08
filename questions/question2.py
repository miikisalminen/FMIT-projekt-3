import pandas as pd
import matplotlib.pyplot as plt

# Question 2: Can the effects of the start of the COVID-19 pandemic be seen in the data? If so how?

def execute(df):
    df['date'] = pd.to_datetime(df['date'])
    df = df.groupby(df['date'].dt.strftime('%B'))['count'].sum().sort_values(ascending=False)
    df.plot(y='Month', x='Count', kind='barh')
    plt.show()