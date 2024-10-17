import pandas as pd
import matplotlib.pyplot as plt
from sklearn  import tree # depreated feature
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import streamlit as st
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

data_df = pd.read_csv("./data/global_air_pollution_data.csv")

print(data_df)

# perform cleaning
data_df = data_df.dropna(axis=0)

print(data_df.isna().sum())


# convert the column aqi_category to numerical values  to be used as target for decision tree

#get values in aqi_category
print(data_df["aqi_category"].value_counts())

# convert Good, Moderate, Unhealthy, Unhealthy for sensitive People, Hazardous
category = {
    "Good" : 1,
    "Moderate": 2,
    "Unhealthy": 3,
    "Unhealthy for Sensitive Groups": 4,
    "Very Unhealthy": 5,
    "Hazardous": 6
}

data_df["aqi_category"] = data_df["aqi_category"].map(category)
# checking data
print(data_df["aqi_category"].value_counts())

# get countries with high aqi value
print(f"Countries with higher aqi value are : \n{data_df[data_df["aqi_value"] > 300]}")

print("\n")

# get feature and target for our decision tree
Y_target = data_df["aqi_category"]
print(f"The target to be used for our decision tree : \n {Y_target}")
features = ["co_aqi_value","ozone_aqi_value", "no2_aqi_value", "pm2.5_aqi_value"]
X_independent = data_df[features]
print(f"The featurs to be used for decision tree are : \n {X_independent}")


X_train, X_test, Y_train, Y_test = train_test_split(X_independent, Y_target, test_size=0.3, random_state=42)


# lets check each var above
print(f" X_train shape is :  {X_train.shape} data type is {type(X_train)} and data is \n {X_train}")
print(f" X_test shape is : {X_test.shape} data type is {type(X_test)} and data is \n {X_test}")
print(f" Y_train shape is : {Y_train.shape} data type is {type(Y_train)}  and data is \n {Y_train}")
print(f" Y_test shape is : {Y_test.shape} data type is {type(Y_test)}  and data is \n {Y_test}")


# Apply decision tree
dtree = DecisionTreeClassifier()
air_pollution_tree =  dtree.fit(X_train, Y_train)
plt.figure(figsize=(12,12))
tree.plot_tree(air_pollution_tree, filled=True, feature_names=features, max_depth=3,node_ids=True,  fontsize=10)
plt.show()


X_test_pred_result = air_pollution_tree.predict(X_test)
print(f"accuracy of the prediction model : {accuracy_score(X_test_pred_result, Y_test)}")

print(f"The classification report : \n {classification_report(X_test_pred_result, Y_test)}")

