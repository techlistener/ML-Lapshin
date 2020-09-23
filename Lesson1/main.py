import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def read_data(file):
    data = pd.read_csv(file, delimiter=",")
    return data[["Sex", "Age"]]


data = read_data("data.csv").groupby(['Sex'], as_index=False).mean()
sns.catplot(x='Sex', y='Age', kind="bar", data=data)

plt.show()
