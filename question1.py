import pandas as pd
import matplotlib.pyplot as plt

def execute(df):
    
    # A list containing every line present in the data
    line_list = df['line'].unique()

    # Computing all the count sums for each line and storing them into a DataFrame
    print('Computing line count sums')
    line_counts_list = []
    for line in line_list:
        line_counts_list.append(int(df.loc[df['line'] == line, 'count'].sum ()))

    line_count_df = pd.DataFrame({'Line' : line_list, 'Count' : line_counts_list})
    print('Done!')

    # Plotting the result with matplotlib
    print('Plotting the top 5 most popular lines of 2020.\nPlease close the graph to continue...')
    figure, axis = plt.subplots(nrows=1, ncols=2)

    line_count_df.nlargest(5, ['Count']).plot(x='Line', y='Count', kind='bar', ax=axis[0])

    line_count_df.nsmallest(5, ['Count']).plot(x='Line', y='Count', kind='bar', ax=axis[1])

    axis[0].set_title('Top 5 most popular Föli lines in 2020')
    axis[0].set_xlabel('Line')
    axis[0].set_ylabel('Count')

    axis[1].set_title('Top 5 least popular Föli lines in 2020')
    axis[1].set_xlabel('Line')
    axis[1].set_ylabel('Count')

    plt.show()