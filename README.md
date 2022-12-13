# Data Science Fundamentals: Archaeological Site Analysis

## I Problem Statement and Motivation

Within the field of archaeology, excavation is often an integral part of studying a site. However, this process is both costly and time consuming. 
As a result, archaeologists often need to make intelligent decisions on where to excavate to answer a posed research question. Prior excavation data 
can be examined to assist in finding the most relevant areas to dig. The intention of the work done was to develop visual tools to assist archaeologists 
both in making these decisions and analyzing their findings. The project is of interest on the development side as it provides good exposure to data science 
techniques, most significantly data cleaning and visualization. 

## II Project Design

The hope was to create a set of tools which could be used to clean and visualize typical sets of archaeological data. To this end, functions were developed utilizing 
the Excavations at Polis data set from the Open Context data website. However, many archaeological data sets are structured similarly, so it should be possible to use 
this work with more than the Polis data set. The expectation for the project was the creation of tools to clean the data and sort and unorganized columns into categories for visualization. A function to_categorize was created to accomplish the data cleaning task. The function takes two inputs, a column of text data and a predefined list of categories to check for within the text data. Each entry is checked and converted to the relevant category if the associated keyword is found. From here, it’s a simple enough task to visualize the data as a pie chart or otherwise. Any of the text data with the data set can be visualized in this way. 

Something of particular note is the graph_per_context function. This function works by first applying a mask to obtain only the data for a specified context from the 
cleaned data before creating visualizations. Within archaeology, subsections of an excavated area are referred to as contexts. By breaking down the contents of a 
specific context, archaeologists can both draw conclusions about the area and know where to excavate next based on their posed research question. For example, the 
presence of charcoal, slag, and plaster within the example context graph below indicates that this area was a part of an industrial metalworking complex.

Another interesting function is the regression_line function, which creates a regression line between the counts of two material types across the site. The intention 
of a regression line is to predict a y value for a given x value, showing how much and in what direction the response variable changes based on the explanatory variable. The function itself manipulates the cleaned data into a workable format before performing and plotting a regression line. This shows how the presence of one material influences the presence of another across the site. As is expected, there is positive correlation within the example below as charcoal and slag are directly relatable materials.

The histogram function creates a histogram of the counts of a certain type of artifact across the entire site. Some initial work is done to sum up the 
individual item counts per context before generating a histogram with a user provided bin count. The normal use of a histogram is to display the frequency distribution 
of a variable across several data points. The visual produced here helps with understanding how common a given artifact is across the site, which is certainly helpful 
from a site analysis standpoint.

The final implemented function find_context works a bit differently than other functions within this project. This function takes minimum artifact count constraints 
and returns a list of contexts which satisfy all of the constraints. A short paper which was written to describe the integer linear programming problem formulated to 
tackle this issue can be read [here](https://medium.com/@panarom/selecting-an-archaeological-context-using-integer-linear-programming-8f60cf7a405d). When applied on a large scale like with the Polis data set, this function is certain to help simplify the process of determining 
the best location to continue excavation based on a posed research question.

## III Conclusion
This project successfully saw the implementation of a variety of tools for visualizing and working with archaeological data. Understanding of both data science 
techniques and archaeological principles were applied along the way to facilitate development. Through the use of the tools developed here, greater understanding 
of an excavation data set can be gleaned.



<p float="center">
  <img src="Images/Polis%20Materials%20Python.png" width="500" />
  <img src="/Images/Context%20Types%20Python.png" width="500" /> 
</p>
<p float="center">
  <img src="Images/Polis%20Histogram.png" width="500" />
  <img src="Images/Polis%20Regression%20Line.png" width="500" />
</p>
