# Iris Fisher Data Set
Pands project of the programming and scripting course

## Index

1. [Description](#description)
2. [Project stages and organisation](#project-stages-and-organisation)
3. [Used tools and libraries](#used-tools-and-libraries)
4. [Data collection](#data-collection)
5. Data analysis
6. Data visualization
7. Results
8. Conclusions of the project
9. References

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

___

## Used tools and libraries
**The project consists of the following files**:

* A Readme file containing all the information and procedures used in the project.  
* An analysis.py file containing all the code used
* A text file which is the output of the Python script
* Png formatted images of the visualised data

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

The aliases given to each library are by popular convention, however it is curious to note that seaborn conventionally uses sns and not sbn.  
___

## Data collection























