import streamlit as st
import pandas as pd

# Using this file to analyse the decision tree 


st.write("# Comedy Decision Tree Analysis")
st.image("comedy_decision_tree.png", caption="Comedy Decision tree")
data_df = pd.read_csv("comedy.csv")
st.write(" Comedy Data Frame ")
st.write(f"Shape of dataframe is {data_df.shape}")
data_df
st.image("root_node.png", caption="root node image")
# root node of the decision tree
# any comedian with a rank of 6.5  or less than this rank will have "GO" === "No"
st.write("### Root node of the decision tree")
st.write(""" ### Analysis:  
    - any comedian with a rank of 6.5  or less than 6.5 is classified as under **True**.
    - any comedian whose rank is greater than 6.5 is classified under **False**.
    - The gini value 0.497 means that atleast 49.7\%   of the data is classified in one direction and the other 52.97 is on the other.
""")


rank_low = data_df[data_df["Rank"] <= 6.5]
st.write("Analysis on the comedian rank with a value of 6.5 or lower")
rank_low

high_rank = data_df[data_df["Rank"] > 6.5]
st.write("Analysis of the comedians whose rank is greater that 6.5")
high_rank   # one wrongly classified

# rank of 6.5 
# comedian is expected to get a "YES" === GO
st.write("""
    ### Next node of the decision tree on True part
""")
st.image("true_node_2.png", caption="Node 2 on true")
st.write('''
- from the previous node any comedian with a rank of 6.5  greater will have a "GO" === "No"
- Total number of samples are 5
- gini index of 0.0 means all samples were classified in one direction
- The value of [5, 0] shows that 5 comedians whose GO === NO
''')
rank_low = data_df[data_df["Rank"] <= 6.5]
rank_low


# Move on the False side of the tree
st.write(''' ### Level 2 of the tree : False : Move on the False side of the tree''')
st.image("root_node_2_false.png", caption="false part of root node")
st.write("""
    ### Analysis of the node:
    - if age is less than  or equal to 39.5
    - gini index is 0.219 means 21.9 percent of the values is classified in one direction
    - samples 8 : total number of samples is 8
    - value [1, 7] : means 1 is classified as G0 === NO and 7 GO === YES
""")


#  Move on the False side of the tree
st.write(''' ### Level 3 of the tree : False : Move on the False side of the tree''')
st.image("last_false_on_node_2.png", caption="False part on False Node on Level 2")
st.write("""
    ### Analysis of the node:
    - gini index is 0.0 means all samples are classified in 1 direction
    - samples = 4 : total number of samples is 4
    - value = [0, 4] :  Means all samples have a GO === YES
""")

# filter data on high_rank whose age is above 39.5, expectation GO === "YES"
high_rank_age_high = high_rank[high_rank["Age"] > 39.5]
high_rank_age_high

st.write(''' ### Level 3 of the tree : true : Move on the left side of tree ''')
st.image("true_node_level_3_age_lower.png", caption="true node on level 3 from age <= 39.5")
st.write("""
    ### Analysis of the node:
    - Age <= 35.5 : Comedians whose age is lower 35.5 or equal to go to **True** part and those Above go to **False**
    - gini index is 0.375 means that 33.75 of the samples are classified into the **True** direction and the other 62.5 is classified into the **False** direction. 
    - samples = 4 : total number of samples is 4
    - value = [1, 3] :  Means that 1 value has a GO === NO and 3  has a GO === YES
""")
high_rank_age_low =  high_rank[high_rank["Age"] <= 39.5] # Age that is low than 39.5
high_rank_age_low # Age that is low than 39.5
# from this it will be broken into 2  value = [1, 3] 2 braches Age <=35.5

# level 4 node on false
st.write(''' ### Level 4 of the tree  : false ''')
st.image("level_4_node_false.png", caption="Comedians  whose age is lower or equal to 39.5")
st.write("""
    ### Analysis of the node:
    - gini = 0.0 : A gini index of 0.0 means all samples are classified into one direction
    - samples = 3 : Total number of samples are 3
    - value [0, 3] : Comedians who have a GO === "YES"
""")

# dataframe based on these conditions
# remeber to use high_rank
left_node_value = high_rank_age_low[high_rank_age_low["Age"] <= 35.5]
left_node_value

# level 4 node on true
st.write(''' ### Level 4 of the tree  : true''')
st.image("level_4_node_true.png", caption="Comedians whose age is greater than 35.5")
st.write("""
    ### Analysis of the node:
    - gini = 0.0 : All samples are classified into one direction
    - samples = 1: Total number of samples is 1
    -  value [1, 0] = Comedian whose GO === NO
""")

righ_node_value = high_rank_age_low[high_rank_age_low["Age"] > 35.5]
righ_node_value