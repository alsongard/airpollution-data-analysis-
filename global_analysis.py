import pandas as pd
from IPython.display import display
import matplotlib.pyplot as plt

#load data
data_df = pd.read_csv("./data/global_air_pollution_data.csv")

print(data_df.head(10)) # 23463 rows and 12 columns
print(data_df.info())

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


# get country with the highest aqi_value

print(f"Highest value of aqi_index : {data_df['aqi_value'].max()}")
print(f"Lowest value of aqi_index : {data_df['aqi_value'].min()}")


#countries with aqi_value of above 150
countries_high_pollution_bool = data_df['aqi_value'] > 151 
print(countries_high_pollution_bool.value_counts())   #true =  2488 false = 20547
countries_high_pollution_df = data_df[countries_high_pollution_bool]
print(countries_high_pollution_df)

# country with the hihest aqi_value
# country_highest_aqi = data_df['aqi_value'].max()
# max_row = data_df.nlargest(n = 20, columns="aqi_value")
# print(max_row)

high_aqi_value_df = data_df[data_df["aqi_value"]==500]
print("dataframe with higherst aqi value equal to 500 is :")
print(high_aqi_value_df )

print(high_aqi_value_df["country_name"].value_counts())

country_count = high_aqi_value_df["country_name"].value_counts()

#plot the data
plt.pie(country_count, labels=country_count.index, autopct="%1.1f%%")
plt.title("Country Highest Aqi Value")
plt.show()

#  autopct="%1.1f%%"  startangle=140