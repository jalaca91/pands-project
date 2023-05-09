# Iris Fisher Data Set
Pands project of the programming and scripting course

## Index

1. [Description](#description)
2. [Project stages and organisation](#project-stages-and-organisation)
3. [Used tools and libraries](#used-tools-and-libraries)
4. [Data collection](#data-collection)
5. [Data analysis](#data-analysis)
6. [Data visualization](#data-visualization)
7. [Results](#results)
8. [Conclusions of the project](#conclusions-of-the-project)
9. [References](#references)

___

 ## Description





This project consists of analysing and investigating a multivariate dataset introduced
by Ronald Fisher in his 1936 paper,_The use of multiple measurements in taxonomic problems_.
Although published by Fisher, the data was orignally collected by American botanist, Edgar Anderson,and thats why this is sometimes called Anderson's Iris data set.  
Most of the samples where collected on the same day and in the same area (two of the three species).

This famous dataset could be the ABC of machine learning and data analysis.  

The Iris dataset consists of three species of Iris flowers and 50 samples of each species, giving a sample of a total of 150 records under five attributes, which are:
1. Sepal length(in cm)
2. Sepal width(in cm)
3. Setal length(in cm)
4. Petal width(in cm)
5. Class.

The features of this sample are shown in the following image:

![image](https://user-images.githubusercontent.com/110190460/234045122-186ab79b-4fbc-4065-ac3e-017c0e1b97ee.png)

By indicating that there are no missing values, it is not necessary to perform data cleaning. 



The species are: Setosa, Versicolor and Virginica.  

![image](https://user-images.githubusercontent.com/110190460/234044887-5cf5d38c-8ac7-4846-98d3-bbc213e6f32a.png)



This makes it a multivariate data set, which means that there are two or more variable quantities.
As can be seen, despite having a similar shade of colour, these flowers have different attributes in terms
of the length of their petals and sepals, which in this project are collected in a file with .csv extension, used by the excel spreadsheet.
___
## Project stages and organisation

The steps of this project can be divided into the following tasks: 
* Show which technologies and tools will be used
* Obtain the dataset and download it
* Import the dataset to our integrated development environment (IDE) 
* Review the dataset and avoid incorrect or incomplete data
* Different statistical analyses of the data obtained
* Show graphically the result of the previous analysis
* Drawing a conclusion from the research carried out
* References used in the elaboration of the project

**The project consists of the following files**:

* A Readme file containing all the information and procedures used in the project
* An analysis.py file containing all the code used
* A text file which is the output of the Python script
* Png formatted images of the visualised data inside 3 folders: Histograms,Scatterplots and Mean,min,max plots
* Iris.csv dataset 

___

## Used tools and libraries

**The project uses the following technologies**:

* Python version 3.9.2 as programming language
* Excel spreadsheet for the imported data
* Visual Studio Code as the Integrated development environment 

**The project uses the following libraries**:

* Numpy  
Is used for numerical computation that allows you to work with large, multi-dimensional arrays and matrices of numerical data. It provides a wide range of mathematical functions to operate on these arrays, making it an essential tool for scientific computing, data analysis, and machine learning. To find out more https://numpy.org/  
`` 
import numpy as np
``  
* Matplotlib  
Is a plotting library for the Python programming language that provides a wide variety of high-quality 2D and 3D graphs and plots. More of this in https://matplotlib.org/  
``
import matplotlib.pyplot as plt
``
* Seaborn  
Is a data visualization library in Python built on top of Matplotlib.  
It provides a high-level interface for creating informative and statistical graphics. https://seaborn.pydata.org/  
``  
import seaborn as sns 
``
* Pandas  
Is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.
https://pandas.pydata.org/  
``
import pandas as pd
``  

Therefore, the totality of the libraries used is as follows:  
```
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
```

The aliases(np,plt,sns,pd) given to each library are by popular convention, however it is curious to note that seaborn conventionally uses sns and not sbn.  
  
--> It is important to note that for the script developed in analysis.py to appear in the file called my_summary.txt , you need to include in the code that includes the built-in print function the following: `` file=summary``  
This way the output of the script will appear in the txt file and not in the IDE terminal (in this case Visual Studio Code). 
___

## Data collection
To obtain the dataset we can go to the following link  
https://archive.ics.uci.edu/ml/datasets/iris  
However, this presents the iris file in txt format in which the data are separated by commas.  
In this format the 5 different characteristics are presented without a header.  
To import the data pandas can be used by the following instructions:  

``
df.columns(['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
``  

This fixed the absence of headings.  

But to simplify things and given the huge popularity of this dataset, you can find the data already with a header  
and in a different format, such as csv. An example is in the following link:  
https://datahub.io/machine-learning/iris#resource-iris  
I used the snake case before importing the data set just to gave a clearer name to the characteristics of each flower.

___

## Data analysis

#### * Import and cleaning data
Now that the data has been imported, it is important to perform a data cleansing, to remove files that may influence  
the result of our analysis, i.e. corrupted data, empty cells, duplicates, incorrect data.  
First of all, in the .py file containing our script it is necessary to import the libraries mentioned above to obtain these new functionalities.  
```
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd  
```  
Once we import the libraries, we read the file named "iris_csv" into a Pandas Dataframe named "df", to access the information it contains.  
``
df = pd.read_csv("iris_csv.csv")  
``  
To do the project we are asked to do the following: Outputs a summary of each variable to a single text file  
``  
summary = open("my_summary.txt", "w",newline='\n')
``  
This create a folder called my_summary.txt, which will contain the result of the analyses performed by the script.  

Now, it is time to clean the data,for this we are going to use several components of the Pandas module.  
First we are going to clean up the empty cells, however this step can be omitted as the table shown in the description
indicates that there are no missing values, so it also applies to wrong format.  
However, we need to check for duplicate data to do so we type the following code in the terminal:
``
print(df.duplicated())
``  

![image](https://user-images.githubusercontent.com/110190460/234237142-6325faba-25af-4832-ae94-fe0ccef3db00.png)  
This function returns True for every row that is a duplicate, othwerwise False, so we can see there is no duplicate values.

#### * Analysis

Once the data have been cleaned, you can proceed to extract information from them.
First, let's look at some basic statistical data for our dataset.  
These statistics are the following: mean, standard deviation, minimum, maximum and percentiles (25%, 50% and 75%).  
``df.describe(),"\n",file=summary``  
With this function a summary of these characteristics is opened in the .txt file created earlier.  

The explanation of these qualities is as follows:  
The mean is a measure of central tendency of a finite set of numbers: specifically, the sum of the values divided by the number of values.  
The standard deviation is a measure of the amount of variation or dispersion of a set of values.  
Min is the smallest value in the set of values.  
Max is the biggest value in the set of values.
Percentile 25% is the value at which 25% of the answers lie below that value.  
Percentile 75% lie above that value
Percentile 50%(also known as the Median). The median cuts the data set in half.  

These basic statistical data would be collected as follows:  

```
Stat Summary: 

       sepal_length  sepal_width  petal_length  petal_width
count    150.000000   150.000000    150.000000   150.000000
mean       5.843333     3.054000      3.758667     1.198667
std        0.828066     0.433594      1.764420     0.763161
min        4.300000     2.000000      1.000000     0.100000
25%        5.100000     2.800000      1.600000     0.300000
50%        5.800000     3.000000      4.350000     1.300000
75%        6.400000     3.300000      5.100000     1.800000
max        7.900000     4.400000      6.900000     2.500000   

```
This gives us an overview of the attributes of our flowers, however, it is data that aggregates all 3 flower species, so it is interesting to perform the same basic analysis for each flower variety.

For this, we will obtain 3 dataframes from the main one and each dataframe, using the DataFrame.loc  

``iris_setosadf=df.loc[df["class"]=="Iris-setosa"]``  We acces the rows where the value in the "class" column is equal to "Iris-setosa"  
``iris_versicolordf=df.loc[df["class"]=="Iris-versicolor"] ``  We acces the rows where the value in the "class" column is equal to "Iris-versicolor"  
``iris_virginicadf=df.loc[df["class"]=="Iris-virginica"]`` We acces the rows where the value in the "class" column is equal to "Iris-virginica"  

We have now the basic statistical parameters for each of the 3 classes of flowers.  

Iris-setosa  
```
Stat Summary setosa: 

       sepal_length  sepal_width  petal_length  petal_width
count      50.00000    50.000000     50.000000     50.00000
mean        5.00600     3.418000      1.464000      0.24400
std         0.35249     0.381024      0.173511      0.10721
min         4.30000     2.300000      1.000000      0.10000
25%         4.80000     3.125000      1.400000      0.20000
50%         5.00000     3.400000      1.500000      0.20000
75%         5.20000     3.675000      1.575000      0.30000
max         5.80000     4.400000      1.900000      0.60000 
```  
Iris-versicolor  
``` 
Stat Summary versicolor: 

       sepal_length  sepal_width  petal_length  petal_width
count     50.000000    50.000000     50.000000    50.000000
mean       5.936000     2.770000      4.260000     1.326000
std        0.516171     0.313798      0.469911     0.197753
min        4.900000     2.000000      3.000000     1.000000
25%        5.600000     2.525000      4.000000     1.200000
50%        5.900000     2.800000      4.350000     1.300000
75%        6.300000     3.000000      4.600000     1.500000
max        7.000000     3.400000      5.100000     1.800000 
```  
Iris-virginica  
```
Stat Summary virginica: 

       sepal_length  sepal_width  petal_length  petal_width
count      50.00000    50.000000     50.000000     50.00000
mean        6.58800     2.974000      5.552000      2.02600
std         0.63588     0.322497      0.551895      0.27465
min         4.90000     2.200000      4.500000      1.40000
25%         6.22500     2.800000      5.100000      1.80000
50%         6.50000     3.000000      5.550000      2.00000
75%         6.90000     3.175000      5.875000      2.30000
max         7.90000     3.800000      6.900000      2.50000 
``` 
After obtaining the basic statistical parameters of our 3 classes of flowers, a data that I consider interesting is to group the means
of the 3 classes of their 4 attributes(sepal_length sepal_width petal_length and petal_width), in order to facilitate the comparison of these data.  
To do this again we use a feature of the Pandas library, called dataframe groupby method()  
`` mean_df = df.groupby("class").mean().transpose() ``  

With this line of code we manage to calculate the mean of each column that has the value "class" and store it in a new variable called mean_df
where the values are transposed(they go from rows to columns).  

It allows us to compare this attribute more easily and the result looks like this:
``` 
Mean Summary: 

class         Iris-setosa  Iris-versicolor  Iris-virginica
sepal_length        5.006            5.936           6.588
sepal_width         3.418            2.770           2.974
petal_length        1.464            4.260           5.552
petal_width         0.244            1.326           2.026 
```   

To look at the size of the plant attributes in more detail, we can also group the min and max values using the same method.  

For minimum values: `` min_df = df.groupby("class").min().transpose() ``  

```
Min Summary:
class         Iris-setosa  Iris-versicolor  Iris-virginica
sepal_length          4.3              4.9             4.9
sepal_width           2.3              2.0             2.2
petal_length          1.0              3.0             4.5
petal_width           0.1              1.0             1.4 
```  

For maximum values: `` max_df = df.groupby("class").max().transpose() ``  

``` 
Max Summary:
class         Iris-setosa  Iris-versicolor  Iris-virginica
sepal_length          5.8              7.0             7.9
sepal_width           4.4              3.4             3.8
petal_length          1.9              5.1             6.9
petal_width           0.6              1.8             2.5  
```  
  
After this basic analysis, we proceed to plot the data set for a better visualisation of what the data tell us.  
___

## Data visualization  

For this part we are going to use the functionalities offered by the matplotib and seaborn libraries.  

* Histogram petal ( petal_lenght,petal_width,sepal_lenght and sepal_width)  

First of all we are going to make a histogram for each of the variables (petal_lenght,petal_width,sepal_lenght and sepal_width).  
Using the following code (in this case applied to petal_length, for the other variables it is necessary to change the input of the x):  

`` sns.displot(df, x="petal_length", hue="class", palette="colorblind", kde=False)``  

This code generates a histogram using Seaborn's displot functionusing the data set df(previously used).  
The histogram is using class to choose the 3 flower varieties and the colour palette is set to "colourblind".
The kde parameter is set to False to remove the kernel density estimation curve from the graph.  
A kernel density estimation (KDE) plot is a common way to visualize the distribution of a dataset.  
It provides a estimation of the probability density function of a continuous random variable, which can be useful to get an idea of the shape of the distribution. In this case by false state that we removed it as it did not provide additional information of interest.  

The result is as follows:  

![Histogram petal_length](https://user-images.githubusercontent.com/110190460/236702112-0c50fcbd-0924-4798-8863-5df45566069d.png)  

To view the rest of the histograms for the other 3 characteristics, see :  
[Histogram_iris](Histogram_iris)  

* Mean summary plot  

For this graph we are going to show the results obtained in the dataframe mean_df and it will show the averages of the different attributes of 
each flower class.  
We use the following code for this purpose  
```
mean_df.plot(kind="bar")  
plt.title("Mean Summary")  
plt.xlabel("Attributes")  
plt.xticks(rotation=0)  
plt.ylabel("Mean Value")  
plt.show()  
```  
With this code `` plt.xticks(rotation=0) `` We fixed the problem of having the x-axis variables vertical and moved them to horizontal for better  
visualisation and to avoid confusion.  
``plt.show()`` can be included only once at the end of the data visualisation code block, as this will cause all graphs to be displayed.

![Mean summary](https://user-images.githubusercontent.com/110190460/236702584-45544f51-8ca8-4b6a-b770-c70fa892d140.png)  

* Min summary plot  

To make a graph with the min values we use the dataframe min_df , where the code will be practically similar to the case used for mean_df.  

![Min summary](https://user-images.githubusercontent.com/110190460/236703199-7d24d1ca-4fd5-40f5-9771-b68de4b53d3b.png)  

* Max summary plot  

Finally for the max case we repeat the previous step.  

![Max summary](https://user-images.githubusercontent.com/110190460/236703225-618bc544-d82b-4a8d-9737-3573a529555c.png)  

To conclude our data visualisation section, we will construct a scatter plot for each pair of variables.  
A scatter plot is a type of graph used to show the relationship between two numerical variables.  
Each point on the graph represents a pair of values, one for each variable. The horizontal axis represents one variable, and the vertical axis represents the other variable.  

A scatter plot is commonly used to see if there is any correlation or pattern between the two variables.  
If the points on the graph form a line or pattern, this indicates a relationship between the two variables.  
On the other hand, if the points are randomly scattered, this indicates that there is no clear relationship between the two variables



* Petal Scatter plot  

We use the following code to make this graph:  
```  
plt.figure(figsize=(4,4)) 
sns.scatterplot(x = 'petal_length', y = 'petal_width',data=df, hue='class', palette='colorblind')
plt.title('Petal variables') 
sns.set(style='dark') 
plt.savefig("Scatterplot_petal.png") 
```  

The first line create a figure with 4x4 size  
``sns.scatterplot(x = 'petal_length', y = 'petal_width',data=df, hue='class', palette='colorblind')`` This line creates a scatter plot using the Seaborn library with the petal_length variable on the x-axis and the petal_width variable on the y-axis with the data contained in the Dataframe df.  
The hue parameter is set to the class variable, which allows us to color the points on the plot based on the class of iris they belong to.  
The palette parameter sets the color scheme for the plot.  
``sns.set(style='dark') `` This line sets a dark background for the plot.   

![Scatterplot petal variables](https://github.com/jalaca91/pands-project/assets/110190460/9cc8e197-5e57-410f-bccb-288199b34c0e)  

* Sepal Scatter plot  

For the case of the sepal we change the values of the previous scatter plot:  
"x" for sepal_length and "y" for sepal_width.  

![Scatterplot sepal variable](https://github.com/jalaca91/pands-project/assets/110190460/4557b461-41b6-4f95-a345-1dd0f66509e6)  

___

## Results  

After carrying out the analyses and creating graphs from these processes, we can draw the following conclusions:  

* Mean Summary
For the means of the variables:

| class          | Iris-setosa | Iris-versicolor |Iris-virginica |
|----------------|-------------|----------------|----------------|
| sepal_length   | 5.006       | 5.936          | 6.588          |
| sepal_width    | 3.418       | 2.770          | 2.974          |
| petal_length   | 1.464       | 4.260          | 5.552          |
| petal_width    | 0.244       | 1.326          | 2.026          |  

We can observe that the iris virginica variety has higher values in 3 of its attributes than the rest of the varieties, indicating a larger size.  
On the other hand, the iris setosa variety is the one with the smallest size in 3 of its four attributes.  

* Min Summary  
This table shows the average minimum values for each flower class.  

| class         | Iris-setosa | Iris-versicolor | Iris-virginica |
|---------------|-------------|----------------|-----------------|
| sepal_length  | 4.3         | 4.9            | 4.9             |
| sepal_width   | 2.3         | 2.0            | 2.2             |
| petal_length  | 1.0         | 3.0            | 4.5             |
| petal_width   | 0.1         | 1.0            | 1.4             |  

We can see that petal_width is the component with the smallest value for each class, while the sepal_length is the largest component for each iris type.  
We also see that iris setosa has 3 of the 4 smallest values, while iris virginica has 3 of the 4 highest values.  
This is consistent with the results described in the previous section(mean).  

* Max Summary  
This table shows the maximum data for each sample of 50 iris varieties.

| class         | Iris-setosa | Iris-versicolor | Iris-virginica |
|---------------|-------------|----------------|-----------------|
| sepal_length  | 5.8         | 7.0            | 7.9             |
| sepal_width   | 4.4         | 3.4            | 3.8             |
| petal_length  | 1.9         | 5.1            | 6.9             |
| petal_width   | 0.6         | 1.8            | 2.5             |

Once again we can see that the iris virginica has higher values than the other two varieties, being much larger in size.  
To see these results in a graphical form, go to section 6.  

Scatter plot..........................................









 




___

## Conclusions of the project







  















___


![loading](https://user-images.githubusercontent.com/110190460/234225693-91160e61-66d0-40b2-aa39-7045b1034ac0.gif)


## References

https://en.wikipedia.org/wiki/Iris_flower_data_set   Information about the dataset  
https://archive.ics.uci.edu/ml/datasets/iris   Dataset in format .data  
https://datahub.io/machine-learning/iris#resource-iris    Dataset used  
https://numpy.org/   
https://matplotlib.org/  
https://seaborn.pydata.org/  
https://pandas.pydata.org/  
https://stackoverflow.com/questions/41499857/why-import-seaborn-as-sns   Seaborn alias  
https://www.geeksforgeeks.org/python-pandas-dataframe-columns/   Pandas column method  
https://www.w3schools.com/python/pandas/pandas_csv.asp   Pandas Read CSV  
https://www.w3schools.com/python/python_file_write.asp  Python File Write/Create  
https://www.freecodecamp.org/news/python-new-line-and-how-to-python-print-without-a-newline/  Newline  
https://www.w3schools.com/python/pandas/pandas_cleaning_duplicates.asp  Duplicated values  
[(https://www.codigopiton.com/seleccionar-filas-de-dataframe-segun-valor-de-columnas](https://www.codigopiton.com/seleccionar-filas-de-dataframe-segun-valor-de-columnas/#:~:text=Para%20seleccionar%20filas%20de%20un,puede%20usar%20la%20funci%C3%B3n%20query%20). Pandas dataframes  
https://www.w3schools.com/python/pandas/ref_df_groupby.asp  Pandas DataFrame groupby() Method 
https://seaborn.pydata.org/generated/seaborn.histplot.html Seaborn histoplot  
https://seaborn.pydata.org/tutorial/aesthetics.html Seaborn figure aesthetics  
https://seaborn.pydata.org/tutorial/color_palettes.html Seaborn color paletes  
https://stackoverflow.com/questions/48911572/seaborn-sns-set-changing-plot-background-color/66509649#66509649  Seaborn plot color  
https://stackoverflow.com/questions/332289/how-do-i-change-the-size-of-figures-drawn-with-matplotlib  figsize parameter  
https://www.markdownguide.org/basic-syntax/  Markdown















