import pandas as pd
import matplotlib.pyplot as plt

from questions import question1, question2, question3, question4, question5

# Loading in the csv into a pandas DataFrame
# CSV NEEDS TO BE PRESENT IN THE PROJECT DIRECTORY
# Available at: https://data.turku.fi/6akgghfs3zbdnamay5kwat/2020-foli.csv

print('Loading in 2020-foli.csv')
df = pd.read_csv("2020-foli.csv")
print('Done!')

# Question results in order
#question1.execute(df)
#question2.execute(df)
#question3.execute(df)
#question4.execute(df)
question5.execute(df)