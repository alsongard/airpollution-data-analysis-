import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# sample data
data = {
    "Category": ["A", "B", "A", "B", "A", "B"],
    "Value" : [10,20,30,40,50,60]
        }
data_df = pd.DataFrame(data)

g = sns.FacetGrid(data_df, col="Category")

g.map(sns.barplot, "Category", "Value")

g.set_titles(col_template="Category: {col_name}")

plt.show()
