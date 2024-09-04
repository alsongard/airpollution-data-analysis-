import pandas as pd

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
print(len(nan_rows)) # 472 rows of missing with country names

# get all the cities form nan_rows
cities_missing_countries = nan_rows["city_name"]
#write to csv file
# cities_missing_countries.to_csv("./data/missing_countries.csv", index=None)


print("\n")
# after finding country names which are empty for the cities, replace/fix missing country names:
country_cities_df = pd.read_csv("./data/country_cities_names.csv")

# merging the dataframes
merged_df = pd.merge(data_df, country_cities_df, on="city_name", how="left")
print(merged_df.head(30))
print("checking empyt rows")
print(merged_df.isna().sum())
# data_df["country_name"] = merged_df["country_name"]
# print(data_df.isna().sum())

























#check for duplicates
# duplicated_cities_df = cities_missing_countries[cities_missing_countries.duplicated()]
# print(f"The number of duplicated cities are \n  {duplicated_cities_df}") # zero duplicated values