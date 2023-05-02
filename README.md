# Iris Fisher Data Set
Pands project of the programming and scripting course

## Index

1. [Description](#description)
2. [Project stages and organisation](#project-stages-and-organisation)
3. [Used tools and libraries](#used-tools-and-libraries)
4. [Data collection](#data-collection)
5. [Data analysis](#data-analysis)
6. Data visualization
7. Results
8. Conclusions of the project
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
* Png formatted images of the visualised data inside a file called images
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
___

## Data collection
To obtain the dataset we can go to the following link  
https://archive.ics.uci.edu/ml/datasets/iris  
Howeber, this presents the iris file in txt format in which the data are separated by commas.  
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






















______


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












