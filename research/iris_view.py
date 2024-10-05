import streamlit as st
import pandas as pd
import io

iris_data_df = pd.read_csv("./Iris.csv")


st.write("# Decision tree on Iris Dataset")

st.write("Iris dataset : ")
iris_data_df

# check shape, info() and value_counts
st.write(f"Iris data set is of shape : {iris_data_df.shape}")



st.write(f"Iris data set info is :")

"""
|    Column      | Non-Null Count | Dtype   |
|  :------       | -------------- | -----   |
|  Id            | 150 non-null   | int64   |
|  SepalLengthCm | 150 non-null   | float64 |
|  SepalWidthCm  | 150 non-null   | float64 |
|  PetalLengthCm | 150 non-null   | float64 |
|  PetalWidthCm  | 150 non-null   | float64 |
|  Species       | 150 non-null   | object  |

"""

# Exploratory Data Analysis
iris_setosa_df = iris_data_df[iris_data_df["Species"] == "Iris-setosa"] 
iris_virginica_df = iris_data_df[iris_data_df["Species"] == "Iris-versicolor"]
iris_versicolor_df = iris_data_df[iris_data_df["Species"] == "Iris-virginica"]


st.write(f"The iris_setosa_df : ")
iris_setosa_df
st.write(f"The iris_versicolor_df :")
iris_virginica_df
st.write(f"The iris_virginica_df :")
iris_versicolor_df


# getting some data from the SepalLengthCm SepalWidthCm PetalLengthCm  PetalWidthCm
# iris  setosa
iris_setosa_sepalLenghtCm_max = iris_setosa_df["SepalLengthCm"].max()
iris_setosa_SepalWidthCm_max = iris_setosa_df["SepalWidthCm"].max()
iris_setosa_PetalLengthCm_max = iris_setosa_df["PetalLengthCm"].max()
iris_setosa_PetalWidthCm_max = iris_setosa_df["PetalWidthCm"].max()
iris_setosa_sepalLenghtCm_min= iris_setosa_df["SepalLengthCm"].min()
iris_setosa_SepalWidthCm_min = iris_setosa_df["SepalWidthCm"].min()
iris_setosa_PetalLengthCm_min = iris_setosa_df["PetalLengthCm"].min()
iris_setosa_PetalWidthCm_min = iris_setosa_df["PetalWidthCm"].min()

# iris_versicolor
iris_versicolor_SepalLengthCm_max = iris_versicolor_df["SepalLengthCm"].max()
iris_versicolor_SepalWidthCm_max = iris_versicolor_df["SepalWidthCm"].max()
iris_versicolor_PetalLengthCm_max = iris_versicolor_df["PetalLengthCm"].max()
iris_versicolor_PetalWidthCm_max = iris_versicolor_df["PetalWidthCm"].max()
iris_versicolor_sepalLenghtCm_min= iris_versicolor_df["SepalLengthCm"].min()
iris_versicolor_SepalWidthCm_min = iris_versicolor_df["SepalWidthCm"].min()
iris_versicolor_PetalLengthCm_min = iris_versicolor_df["PetalLengthCm"].min()
iris_versicolor_PetalWidthCm_min = iris_versicolor_df["PetalWidthCm"].min()

# iris_virginica
iris_virginica_sepalLenghtCm_max = iris_virginica_df["SepalLengthCm"].max()
iris_virginica_SepalWidthCm_max = iris_virginica_df["SepalWidthCm"].max()
iris_virginica_PetalLengthCm_max = iris_virginica_df["PetalLengthCm"].max()
iris_virginica_PetalWidthCm_max = iris_virginica_df["PetalWidthCm"].max()
iris_virginica_sepalLenghtCm_min = iris_virginica_df["SepalLengthCm"].min()
iris_virginica_SepalWidthCm_min = iris_virginica_df["SepalWidthCm"].min()
iris_virginica_PetalLengthCm_min = iris_virginica_df["PetalLengthCm"].min()
iris_virginica_PetalWidthCm_min = iris_virginica_df["PetalWidthCm"].min()


st.write(f"""For Iris-setosa has the following characterstics: \n
    Iris-setosa SepalLengthCm_man : {iris_setosa_sepalLenghtCm_max} \n
    iris_setosa_sepalLenghtCm_min : {iris_setosa_sepalLenghtCm_min} \n
    iris_setosa_SepalWidthCm_max  : {iris_setosa_SepalWidthCm_max } \n
    iris_setosa_SepalWidthCm_min  : {iris_setosa_SepalWidthCm_min } \n
    iris_setosa_PetalLengthCm_max : {iris_setosa_PetalLengthCm_max} \n
    iris_setosa_PetalLengthCm_min : {iris_setosa_PetalLengthCm_min} \n
    iris_setosa_PetalWidthCm_max : {iris_setosa_PetalWidthCm_max} \n
    iris_setosa_PetalWidthCm_min : {iris_setosa_PetalWidthCm_min}
    """)

st.write(f"""For virginica has the following characterstics: \n
    iris_virginica_sepalLenghtCm_max : {iris_virginica_sepalLenghtCm_max} \n
    iris_virginica_sepalLenghtCm_min : {iris_virginica_sepalLenghtCm_min} \n
    iris_virginica_SepalWidthCm_max  : {iris_virginica_SepalWidthCm_max } \n
    iris_virginica_SepalWidthCm_min  : {iris_virginica_SepalWidthCm_min } \n
    iris_virginica_PetalLengthCm_max : {iris_virginica_PetalLengthCm_max} \n
    iris_virginica_PetalLengthCm_min : {iris_virginica_PetalLengthCm_min} \n
    iris_virginica_PetalWidthCm_max : {iris_virginica_PetalWidthCm_max} \n
    iris_virginica_PetalWidthCm_min : {iris_virginica_PetalWidthCm_min} 
    """)

st.write(f"""For Iris-versicolor has the following characterstics: \n
    iris_versicolor_SepalLengthCm_man : {iris_versicolor_SepalLengthCm_max}\n
    iris_versicolor_sepalLenghtCm_min : {iris_versicolor_sepalLenghtCm_min}\n
    iris_versicolor_SepalWidthCm_max  : {iris_versicolor_SepalWidthCm_max }\n
    iris_versicolor_SepalWidthCm_min  : {iris_versicolor_SepalWidthCm_min }\n
    iris_versicolor_PetalLengthCm_max : {iris_versicolor_PetalLengthCm_max}\n
    iris_versicolor_PetalWidthCm_max :  {iris_versicolor_PetalWidthCm_max }\n
    iris_versicolor_PetalLengthCm_min : {iris_versicolor_PetalLengthCm_min}\n
    iris_versicolor_PetalWidthCm_min :  {iris_versicolor_PetalWidthCm_min }
    """)


st.subheader(" Decision Tree Image:")
st.image("./iris_decision_tree_image_3.png")

st.write("Accuracy of Decision Tree-Test : 0.9555555555555556")

"""

|                |precision |recall    |f1-score  |support |
|  -------              |    -----      |   -------        |    ------     |-------      |
|Iris-setosa     |1.00      |1.00      |1.00      |  14 |
|Iris-versicolor |0.94      |0.94      |0.94      |  18 |
|Iris-virginica  |0.92      |0.92      |0.92      |  13 |
||| |
|accuracy        |0.96      |  45| |
|macro avg       |0.96      |0.96      |0.96      |  45 |
|weighted avg    |0.96      |0.96      |0.96      |  45 |
"""