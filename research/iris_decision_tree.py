import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split



iris_data_df = pd.read_csv("./Iris.csv")

print(iris_data_df)

# perform data cldeeaning
print(iris_data_df.isna().sum()) # none all fields are not empty

# check shape, info() and value_counts
print(f"Iris data set is of shape : {iris_data_df.shape}")
print(f"Iris data set info is : \n {iris_data_df.info()}")

#check on species to know
print(f"Iris data has the following species : {iris_data_df["Species"].value_counts()}")

