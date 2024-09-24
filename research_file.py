import pandas as pd
import streamlit as st

data_df = pd.read_csv("./data/global_air_pollution_data.csv")

st.write(f"size of the dataframe before cleaning {data_df.shape} ") # to view original data set/ lines of dataset



# drop some columns
data_df = data_df.dropna(axis=0)
st.write("Cleaned data: ")
st.write(f"size of the dataframe after cleaning {data_df.shape} ") # to view original data set/ lines of dataset

data_df

# print(data_df.info())

st.write("# Co_aqi_value")
data_df["co_aqi_value"]




# check on values in the co_aqi_value column
co_aqi_value_counts = data_df["co_aqi_value"].value_counts()
"Values in the co_aqi_value are :"
co_aqi_value_counts

# grap the values
sum = 0
for item in co_aqi_value_counts.values:
    sum += item
st.write(f"Sum is {sum}")


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

