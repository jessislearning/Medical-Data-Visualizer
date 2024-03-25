# This entrypoint file to be used in development. Start by reading README.md
#import medical_data_visualizer
#from unittest import main

# Test your function by calling it here
#medical_data_visualizer.draw_cat_plot()
#medical_data_visualizer.draw_heat_map()

# Run unit tests automatically
#main(module='test_module', exit=False)

#----my code----
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
# Import data
df = pd.read_csv("medical_examination.csv")

#Calculate BMI
BMI = df["weight"]/((df["height"])/100)**2

# Add 'overweight' column
df["overweight"] = (BMI > 25).astype(int)

# normalize cholesterol and gluc
df["cholesterol"] = (df["cholesterol"] > 1).astype(int)
df["gluc"] = (df["gluc"] > 1).astype(int)

print (df.head())