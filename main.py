import pandas as pd
import matplotlib.pyplot as plt
import question1

# Loading in the csv into a pandas DataFrame
print('Loading in 2020-foli.csv')
df = pd.read_csv("2020-foli.csv")
print('Done!')

# Question results in order
question1.execute(df)
