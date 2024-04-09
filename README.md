# Medical Data Visualizer

Medical Data Visualizer is a Data Analysis with Python project from freeCodeCamp. Instructions and details can be found here: https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/medical-data-visualizer

The file medical_examinations.csv contain data with the following features: age, weight, height, systolic blood pressure, diastolic blood pressure, glucose, and other medical examination information. 

In this project, the tasks were to:

1. Append an "overweight" column (boolean). From the height and weight information, the calculated BMI is used to determine if the person is overweight (1) or not (0). 
2. Cholesterol and Glucose information were normalized (converted to boolean) with 0 being good, and 1 being bad.
3. Create side-by-side barplots detailing medical information for people with and without cardiovascular disease. Each barplot shows the value counts of different categorical features: glucose, cholesterol, smoking habit, alcohol habit, physical activity.
4. Clean the blood pressure data for erroneous measurements (diastolic pressure higher than systolic pressure), and to exlude data where a person's height or weight are less than the 2.5th percentile or more than the 97.5 percentile.
5. Create a correlation matrix for the data set. As a style requirement, the plot should only show the lower triangle.


<h3>Project Output:</h3>

Task #3 Categorical Plot showing value counts for different features. The data for people with (right) and without (left) cardiovascular disease are separated. The barplot is created using seaborn "catplot".
![image](https://github.com/jessislearning/Medical-Data-Visualizer/assets/161026755/fc19901d-c117-4738-95e0-4ce42c699da6)

Task #5
Correlation matrix created using seaborn "heatmap".
![image](https://github.com/jessislearning/Medical-Data-Visualizer/assets/161026755/3546be6f-eaa8-4ec1-9693-f5e00e750c4d)


Project Notes:
* for the categorical plot, the starter code requires the use of pandas "melt" method.





