# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# <div class="alert alert-block alert-success">
#     <h1 align="center">Mini Project1</h1>
# </div>

# <img src = "https://www.cyclonis.com/images/2020/03/googleplay.jpg" width=50%>

# !pip install jupytext

# ## Importing the essential libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import KNNImputer
import jupytext

# ## Load and Prepare Data

df = pd.read_csv("googleplaystore.csv")

# ## EDA

df.head(1)

df.dtypes

df.columns.to_list()

df.shape

missing_values_count = df.isnull().sum()
missing_values_count

sns.set_theme(style = 'white',palette = "viridis")
sns.set(rc={"figure.dpi":300, "figure.figsize":(12,9)})
sns.heatmap(df.isnull(), cbar=True)

df.head()

# ## Data Preprocessing

mean_ratings = df.groupby('Category')['Rating'].median()
df['Rating'].fillna(df['Category'].map(mean_ratings), inplace=True)

df['Android Ver'].fillna(df['Android Ver'].mode()[0], inplace=True)
df['Current Ver'].fillna(df['Current Ver'].mode()[0], inplace=True)
df['Content Rating'].fillna(df['Content Rating'].mode()[0], inplace=True)
df['Type'].fillna(df['Type'].mode()[0], inplace=True)

missing_values_count = df.isnull().sum()
print(missing_values_count) 

df["Size"].replace("." ,"", regex=False, inplace = True)
df["Size"].replace("," ,"", regex=True, inplace = True)
df["Size"].replace("M" ,"000", regex=True, inplace = True)
df["Size"].replace("k","", regex=True, inplace = True)

df.head(5)

# ## Strorytelling - Visualization



# ## Send us the Result (Maktabkhoone)

#

# # create .PY file with jupytext

import subprocess
subprocess.run(["jupytext", "--to", "py", "Mini_Project1.ipynb"])


jupytext --to py "Mini_Project1.ipynb"
