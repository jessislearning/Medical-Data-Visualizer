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

#pd.melt?
df_cat = pd.melt(df, id_vars="cardio", value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"])
df_cat = df_cat.groupby(["cardio", "variable"])["value"].value_counts().reset_index(name="counts")

catplot = sns.catplot(data=df_cat, x="variable", y="counts", col="cardio", kind="bar", hue="value")


# Get the figure for the output
fig = catplot.fig


# Do not modify the next two lines
fig.savefig('catplot.png')
#return fig

print (df_cat.head(20))