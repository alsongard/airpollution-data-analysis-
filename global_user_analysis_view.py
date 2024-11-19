import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# What can you get from the data and what observations can you extract from these data
# 1. Get countries with high aqi value
#       * get maximum values of the attributes of each column that contribute to aqi_index
#       * Repeat these for every of the following aqi_index categories

st.write("# Air Pollution Analysis and Model Prediction based on the various Air Pollutants")
data_df = pd.read_csv("./data/global_air_pollution_data.csv")


# clean data
data_df = data_df.dropna(axis=0)
st.write(f"air pollution data frame shape is {data_df.shape}")
data_df


# step 1 : get and view the different categories of the air quality index (air pollution level s)

st.write("Air Quality Index : The Air Quality Index represents the level of Air Pollution of a location.")

"""
**AQI Categories:**   
| Category | Range | 
| ----- | ----- |
| Good | below 50|
| Moderate | 51 - 100 |
| Unhealthy  (sensitive groups such as children, eldery) | 101 - 150 |
| Unhealthy | 151 - 200 |
| Very UnHealthy | 201 - 300 |
| Hazardous | above 300 |
"""

# get location whose air quality index is above 300
high_aqi_index_df = data_df[data_df["aqi_value"] > 300]
st.subheader("Countries whose air quality index is above 300")
st.write("Countries which have a higher air quality index of 300, are considered as hazardous.")
st.write(f"The shape of high_aqi_index_df is {high_aqi_index_df.shape} ") 
high_aqi_index_df

# get countries

country_value = high_aqi_index_df["country_name"].value_counts()
country_value.index

st.write("Number of cities which have a aqi value of 300 and above in each of the above countries are :")
country_value

# plot
# country_value.plot(kind="pie")

# get characteristics

# target areas with a low air quality index

# aqi = 50 good conditions
good_aqi_data_df = data_df[data_df["aqi_value"] <= 50]
st.write("### Good Air Quality Conditions : less or equal 50 aqi_value")
good_aqi_data_df
# get the maximum value of each contributant to the aqi value
# co_aqi_value
co_aqi_maximum_value = good_aqi_data_df["co_aqi_value"].max()
co_aqi_minimum_value = good_aqi_data_df["co_aqi_value"].min()
st.write(f"For areas with good air quality index value of 50 or less the minimum co_aqi_value is {co_aqi_minimum_value} and maximum value is {co_aqi_maximum_value}")

# aqi =  50 - 100 Moderate
moderate_aqi_conditions_df = data_df[(data_df["aqi_value"] >= 51) & (data_df["aqi_value"] <= 100)]
st.write("### Moderate Air Quality Conditions : aqi_value >= 50 and <= 100")
moderate_aqi_conditions_df
# get the maximum value of each contributant to the aqi value
# co_aqi_value
moderate_co_aqi_min_value = moderate_aqi_conditions_df["co_aqi_value"].min()
moderate_co_aqi_max_value = moderate_aqi_conditions_df["co_aqi_value"].max()
st.write(f"For areas with moderate air quality index the minimum co_aqi_value is {moderate_co_aqi_min_value} and maximum value is {moderate_co_aqi_max_value}")

# aqi =  101 - 150 | Unhealthy sensitive groups such as children, eldery
unhealthy_sensitive_df = data_df[(data_df["aqi_value"] >= 101) & (data_df["aqi_value"] <= 150)]
st.write("### Unhealthy conditions for sensitive groups : aqi value range from 101 - 150")
unhealthy_sensitive_df
# get the maximum value of each contributant to the aqi value

# co_aqi_value
unhealthy_co_aqi_min_value = unhealthy_sensitive_df["co_aqi_value"].min()
unhealthy_co_aqi_max_value = unhealthy_sensitive_df["co_aqi_value"].max()
st.write(f"For areas with unhealthy conditions, minimum co_aqi_value is {unhealthy_co_aqi_min_value} and maximum value is {unhealthy_co_aqi_max_value}")


# aqi = 151 - 200 Unhealthy for every person
unhealthy_data_df = data_df[(data_df["aqi_value"] >= 151) & (data_df["aqi_value"] <= 200)]
st.write("### Unhealthy conditions for everyone : aqi value range from 151 - 200")
unhealthy_data_df
# get the maximum value of each contributant to the aqi value
# co_aqi_value
unhealthy_co_aqi_min_value = unhealthy_sensitive_df["co_aqi_value"].min()
unhealthy_co_aqi_max_value = unhealthy_sensitive_df["co_aqi_value"].max()
st.write(f"For areas with unhealthy conditions, minimum co_aqi_value is {unhealthy_co_aqi_min_value} and maximum value is {unhealthy_co_aqi_max_value}")

# aqi = 201 - 300 Very Unhealthy
very_unhealthy_df = data_df[(data_df["aqi_value"] >= 201) & (data_df["aqi_value"] <= 300)]
st.write("### Very Unhealthy Conditions : aqi value range from 201 - 300")
very_unhealthy_df
# get the maximum value of each contributant to the aqi value
# co_aqi_value
very_unhealthy_co_aqi_min_value = very_unhealthy_df["co_aqi_value"].min()
very_unhealthy_co_aqi_max_value = very_unhealthy_df["co_aqi_value"].max()
st.write(f"For areas with Very unhealthy conditions, minimum co_aqi_value is {very_unhealthy_co_aqi_min_value} and maximum value is {very_unhealthy_co_aqi_max_value}")

# aqi > 300 Hazardous
harzardous_df = data_df[data_df["aqi_value"] > 300]
st.write("### Harzardous conditions : aqi value above 300")
harzardous_df
# get the maximum value of each contributant to the aqi value
# co_aqi_value
harzardous_co_aqi_min_value = harzardous_df["co_aqi_value"].min()
harzardous_co_aqi_max_value = harzardous_df["co_aqi_value"].max()
st.write(f"For areas with Hazardous conditions, minimum co_aqi_value is {harzardous_co_aqi_min_value} and maximum value is {harzardous_co_aqi_max_value}")

# write hazardous data to excel file
harzardous_df.to_excel("hazardous_countries.xlsx")

st.write("*****")

st.write("## Accuracy of the model")

st.write("""
    The following values were used to convert the target feature into numerical values.

    | Category | Value |
    | -----    | ----  |
    | Good     |  1    |
    | Moderate |  2    |
    | Unhealthy|  3    |
    | Unhealthy for sensitive Groups | 4|
    | Very Unhealthy | 5 |
    | Hazardous | 6 |
""")


st.write("""
The  accuracy of the prediction model : 0.9986977282592968
The classification report : 

| precision  |  recall | f1-score  | support | Category |    
| -----      | -----   |    ------ | ------- | ------  |
|    1.00    |  1.00     |  1.00   |    2878 | 1 |
|    1.00    |  1.00     |  1.00   |    2768 | 2 |
|    1.00    |  1.00     |  1.00   |     614 | 3 |
|    1.00    |  1.00     |  1.00   |     502 | 4 |
|    0.93    |  0.98     |  0.95   |      83 | 5 |
|    0.97    |  0.91     |  0.94   |      66 | 6 |

    accuracy                           1.00      6911
   macro avg       0.98      0.98      0.98      6911
weighted avg       1.00      1.00      1.00      6911
""")

"""
    ### Description of the Prediction Report:
    from the above prediction report, the accuracy model is 99% (percent) meaning, the predictions based on the test data, 99% percent correct. 
    
    1. **Precision:**   
    precision measures the proportions of positive values that were actually correct.  
    In my case for values categorised in 1(Good), 2(Moderate)
    3(Unhealthy), 4 (Unhealthy for sensitive Groups) were all correct, and  for those categorised as  5 (Very Unhealthy), 93 percent were correct and for 6(Hazardous), 97 percent were correct.

    2. **Recall:**  
    Measures the proportion of actual positive samples that were correctly predicted.  
    For the test samples categorised in  1(Good), 2(Moderate) 3(Unhealthy) and 4 (Unhealthy for sensitive Groups) were all correct and for those in  5 (Very Unhealthy), 95% were correct and 
    lastly for samples in category 6, 91% were correct.

    3. **F1-score:**   
    The harmonic mean of precision and recall, providing a balanced measure of both.

    4. **Support:**   
    Indicate the number of samples in each category.

    5. **Macro Average:**  
    Calculates the average of precision, recall, and F1-score for each class without considering the class imbalance.

    6. **Weighted average:**  
     Calculates the average of precision, recall, and F1-score, taking into account the class imbalance.
"""