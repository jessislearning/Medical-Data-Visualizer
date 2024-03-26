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

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df["cholesterol"] = (df["cholesterol"] > 1).astype(int)
df["gluc"] = (df["gluc"] > 1).astype(int)


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars="cardio", value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.groupby(["cardio", "variable"])["value"].value_counts().reset_index(name="total")  

    # Draw the catplot with 'sns.catplot()'
    catplot = sns.catplot(data=df_cat, x="variable", y="total", col="cardio", kind="bar", hue="value")

    # Get the figure for the output
    fig = catplot.fig


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df["ap_lo"] <= df["ap_hi"])
            & (df["height"] >= df["height"].quantile(0.025))
            & (df["height"] <= df["height"].quantile(0.975))
            & (df["weight"] >= df["weight"].quantile(0.025))
            & (df["weight"] <= df["weight"].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    # This removes the upper triangle across the correlation matrix (square is cut along the diagonal)
    mask = np.triu(corr)

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(10,10))

    # Draw the heatmap with 'sns.heatmap()'
    # We are plotting "corr", 
    # annot places the values of the correlation on each matrix element
    # fmt formats the annot to have 1 decimal place
    sns.heatmap(corr, annot=True, mask=mask, fmt=".1f")


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
