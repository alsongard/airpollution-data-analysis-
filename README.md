# AIR QUALITY DYNAMICS

## Description
This repository will be used to analyze the different levels of air pollution in different countries and   
Later on, if hospital data is given for repository diseases led from air pollution we will identify patterns and interesting relationships between the level of air pollution and repository diseases.  


## Features   
### Columns/Attributes of the data:   

| Column | Data Type |
| ---- | ---- |
| country_name | object |
| city_name |  |
| aqi_value |  integer |
| aqi_category |   |
| co_aqi_value |   |
| co_aqi_category |   |
| ozone_aqi_value |   |
| ozone_aqi_category |   |
| no2_aqi_value |   |
| no2_aqi_category |   |
| pm2.5_aqi_value |  |
| pm2.5_aqi_category | 


1. Country_name:  
Provides the name of the country.  

2. city_name:  
name of the city in the given country.

3. . Air Quality Index:   
Air Quality Index(AQI) is a numerical value indication how clean or polluted the air is for the given location. AQI ranges for 0 to 500. Higer AQI values indicate polluted air which is poses a significant risk to health. 

**AQI Categories:**   
| Category | Range | 
| ----- | ----- |
| Good | below 50|
| Moderate | 51 - 100 |
| Unhealthy  (sensitive groups such as children, eldery) | 101 - 150 |
| Unhealthy | 151 - 200 |
| Very UnHealthy | 201 - 300 |
| Hazardous | above 300 |