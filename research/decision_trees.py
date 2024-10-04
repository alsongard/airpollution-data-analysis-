
import pandas as pd
from sklearn  import tree # depreated feature
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt


data_df = pd.read_csv("./comedy.csv")
print(data_df)

# convert values of nationality, go and into numerical
nationality = {
    "UK" : 0,
    "USA" : 1,
    "N": 2
}
go_comedy = {
    "YES" : 1,
    "NO" : 0
}
data_df["Nationality"] = data_df["Nationality"].map(nationality)
data_df["Go"] = data_df["Go"].map(go_comedy)
print(data_df)

#     Age  Experience  Rank Nationality   Go
# Extract features from the data set
features = ["Age", "Experience", "Rank", "Nationality"]
X_df = data_df[features]

#Extract target from the data set
target = "Go"
Y_df = data_df[target]

print(f"Data type of X_df is {type(X_df)}")
print(f"Features are : \n {X_df}")
print(f"Dat type of Y_df is : {type(Y_df)}")
print(f"Target is : \n {Y_df}")


"""
# applying decision tree
dtree = DecisionTreeClassifier()
comedy_tree = dtree.fit(X_df, Y_df)

tree.plot_tree(comedy_tree, feature_names=features)
plt.show()
"""