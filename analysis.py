# Analysis.py
# Author: Jaime Lara Carrillo

# Import all usefull libraries fot the analysis
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


df = pd.read_csv("iris_csv.csv")    # Read a CSV file named "iris_csv" into a Pandas DataFrame named "df"

df = df.describe()                  # This outputs basic stadistic information
print(df)