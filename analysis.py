# Analysis.py
# Author: Jaime Lara Carrillo

# Import all usefull libraries fot the analysis
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Read a CSV file named "iris_csv" into a Pandas DataFrame named "df"
df = pd.read_csv("iris_csv.csv")                
summary = open("my_summary.txt", "w")       # Open the .txt file

# Cleaning data
print("\rDuplicate rows:\n\t",file=summary)

# Starting with data analysis

print("Stat Summary: \r",file=summary)
print(df.describe(),"\n",file=summary)             # Stat summary of 3 species

iris_setosadf=df.loc[df["class"]=="Iris-setosa"]             # Create 3 subsets of the dataset for each species
iris_versicolordf=df.loc[df["class"]=="Iris-versicolor"] 
iris_virginicadf=df.loc[df["class"]=="Iris-virginica"]

# Statistic summary of iris-setosa
print("Stat Summary setosa: \r",file=summary)
print(iris_setosadf.describe(),"\n",file=summary)

# Statistic summary of iris-versicolor
print("Stat Summary versicolor: \r",file=summary)
print(iris_versicolordf.describe(),"\n",file=summary)

# Statistic summary of iris-virginica
print("Stat Summary virginica: \r",file=summary)
print(iris_virginicadf.describe(),"\n",file=summary)

# Combine mean in one table
print("Mean Summary: \r",file=summary)
mean_df = df.groupby("class").mean().transpose()
print(mean_df,"\n",file=summary)

# Combine min in one table
print("Min Summary: \r",file=summary)
min_df = df.groupby("class").min().transpose()
print(min_df,"\n",file=summary)

# Combine max in one table
print("Max Summary: \r",file=summary)
max_df = df.groupby("class").max().transpose()
print(max_df,"\n",file=summary)

# Histogram of each variable 
sns.displot(df, x="petal_length", hue="class", palette="colorblind", kde=False)
plt.savefig("Histogram petal_length.png")
sns.displot(df, x="petal_width", hue="class", palette="colorblind", kde=False)
plt.savefig("Histogram petal_width.png")
sns.displot(df, x="sepal_length", hue="class", palette="colorblind", kde=False)
plt.savefig("Histogram sepal_length.png")
sns.displot(df, x="sepal_width", hue="class", palette="colorblind", kde=False)
plt.savefig("Histogram sepal_width.png")

# Mean summary plot
mean_df.plot(kind="bar")
plt.title("Mean Summary")
plt.xlabel("Attributes")
plt.xticks(rotation=0)          # Rotates x-tick labels to be horizontal
plt.ylabel("Mean Value")
plt.savefig("Mean summary plot.png")

# Min summary plot
min_df.plot(kind="bar")
plt.title("Min Summary")
plt.xlabel("Attributes")
plt.xticks(rotation=0)          
plt.ylabel("Mean Value")
plt.savefig("Min summary plot.png")

# Max summary plot
max_df.plot(kind="bar")
plt.title("Max Summary")
plt.xlabel("Attributes")
plt.xticks(rotation=0)          
plt.ylabel("Mean Value")
plt.savefig("Max summary plot.png")  

# Scatterplot for sepal variables
plt.figure(figsize=(4,4)) 
sns.scatterplot(x = "sepal_length", y = "sepal_width",data=df, hue="class", palette="colorblind")
plt.title("Sepal variables") 
sns.set(style="dark") 
plt.savefig("Scatterplot_sepal.png")  

# Scatterplot for petal variables
plt.figure(figsize=(4,4)) 
sns.scatterplot(x = "petal_length", y = "petal_width",data=df, hue="class", palette="colorblind")
plt.title("Petal variables") 
sns.set(style="dark") 
plt.savefig("Scatterplot_petal.png") 

plt.show()

summary.close()     # Free up system resources and avoid problems





