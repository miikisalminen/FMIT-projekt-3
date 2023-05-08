import pandas as pd
import matplotlib.pyplot as plt


def execute(df):
    print(
        "Question 6: What is the total number of journeys that happened during the year?")
    sum = df['count'].sum()
    print("Total number of journeys: {0}".format(sum))
