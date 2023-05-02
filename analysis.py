# Analysis.py
# Author: Jaime Lara Carrillo

# Import all usefull libraries fot the analysis
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


df = pd.read_csv("iris_csv.csv")    # Read a CSV file named "iris_csv" into a Pandas DataFrame named "df"
summary = open("my_summary.txt", "w")


# Cleaning data
print('\rDuplicate rows:\n\t',file=summary)

# Starting with data analysis

print('Stat Summary: \r',file=summary)
print(df.describe(),'\n',file=summary)

summary.close()





