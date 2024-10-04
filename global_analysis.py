"""
    Perform cleaning, analyse data, 
    In analysing data:
        1. Get countries with higher and Low AQI value  
"""

import pandas as pd
from IPython.display import display
import matplotlib.pyplot as plt

#load data
data_df = pd.read_csv("./data/global_air_pollution_data.csv")

print(data_df.head(10)) # 23463 rows and 12 columns
print(f"Shape of the dataframe is : {data_df.shape}")
print(f"Get info on global_air_pollution_data is : \n {data_df.info()}")



# print only the column names
columnNames = [col for col in data_df.columns]
# print(columnNames)

# for item in columnNames:
#     print(item)

#check for any missing type data
print("Checkig for missing data:")
print(data_df.isna().sum())

#check the overall aqi value for the first 10 lines
print(data_df.aqi_value.head(10))

# accessing the rows of the data
print(f"the lenght of the rows are {len(data_df['country_name'])}") #23463
# missing values
nan_rows = data_df[data_df["country_name"].isna()]
print(nan_rows)
print(nan_rows.city_name.isna().sum())
print(f"Missing rows len is {len(nan_rows)}") # 472 rows of missing with country names


#get new csv file with missing countries 
new_country_missing_df = pd.read_csv("./data/country_cities_names.csv")
print(new_country_missing_df)


# drop the columns
data_df = data_df.dropna(axis=0)
print(data_df.isna().sum())
print(data_df.info())


# STEP 1:
# get country with the highest aqi_value
print(f"Highest value of aqi_index : {data_df['aqi_value'].max()}")
print(f"Lowest value of aqi_index : {data_df['aqi_value'].min()}")


#countries with aqi_value of above 151 == unhealthy
country_unhealthy_df = data_df[data_df["aqi_value"] > 151]
print(f"Country which are unhealthy > 151 aqi_value are : \n {country_unhealthy_df}")
# create dataset of unhealthy countries
country_unhealthy_df.to_csv("./data/country_unhealthy_condition.csv")


# use value counts to check wich country has the most appearance in the unhealthy
print(country_unhealthy_df.country_name.value_counts()) 

# assign to value_count variable for assigment(series object)
country_unhealthy_series = country_unhealthy_df.country_name.value_counts()
print(f"The type of country_unhealthy_series is {type(country_unhealthy_series)}")

# select the top 50 countries which have been repeated
country_unhealthy_series = country_unhealthy_series[country_unhealthy_series > 10]

#plot the data using bar
country_unhealthy_series.plot.bar(width=0.3)
plt.xlabel("countries")
plt.ylabel("aqi_value")
plt.xticks(rotation=45)
plt.title("Countries  with the most cities with unhealthy Air Quality Index(AQI)")
plt.show()

#plot the data using pie chart
plt.pie(country_unhealthy_series, labels=country_unhealthy_series.index, autopct="%1.1f%%")
plt.title("Countries  with the most cities with unhealthy Air Quality Index(AQI)")
plt.show()


# print(country_unhealthy_df.country_name.value_counts())
# print(f"Number of times country appears on unhealthy aqi_value : \n {country_unhealthy_value_counts}")

# plt.bar(country_unhealthy_df, height=10, width=0.5)

# country with the hihest aqi_value
country_highest_aqi = data_df['aqi_value'].max() # get value of highest air quality index == 500
max_row = data_df.nlargest(n = 20, columns="aqi_value") # return rows with highest aqi_value
print(max_row)
 
# get dataframe which has countries with highest aqi_value == 500
high_aqi_value_df = data_df[data_df["aqi_value"]==500]
print("dataframe with higherst aqi value equal to 500 is :")
print(high_aqi_value_df )

# use counts to check which country is repeated more
print(high_aqi_value_df["country_name"].value_counts())
country_count = high_aqi_value_df["country_name"].value_counts()

#plot the data is a series object
plt.pie(country_count, labels=country_count.index, autopct="%1.1f%%")
plt.title("Country Highest Aqi Value")
plt.show()

#  autopct="%1.1f%%"  startangle=140

# get cities with the highest aqi value
print("\n")
print(data_df)
print(data_df.info())
cities_high_aqi_df = data_df[data_df["aqi_value"] == 500] # 103 rows of data
print(cities_high_aqi_df["city_name"].value_counts()) # 
city_counts = cities_high_aqi_df["city_name"].value_counts()
print(type(city_counts))
print(city_counts.index)
print(city_counts.values)

# check which values have been repeated
repeated_values = city_counts.values > 1
print(f"Repeated values are : \n {repeated_values}") # no city is repeated & hence no need for plotting
# plt.pie(city_counts, labels=city_counts.index)
# plt.title("City with highest aqi_values")
# plt.show()
