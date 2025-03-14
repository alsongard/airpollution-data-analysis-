# AIR QUALITY DYNAMICS

## Description
This repository will be used to analyze the different levels of air pollution in different countries and later on, if hospital data is available for repository diseases led from air pollution, i will identify patterns and interesting relationships between the level of air pollution and repository diseases.  

# Table of Contents
1. [Installation](#installation)
1. [Features](#features)


## Installation 
1. Virtual environment setup
``python3 -m venv directory name``


**Requirements**
- python
- pandas  
- matplotlib.pyplot
- streamlit 

## Features   
### Columns/Attributes of the data:   

| Column | Data Type |
| ---- | ---- |
| country_name | object |
| city_name | object  |
| aqi_value |  integer |
| aqi_category | object  |
| co_aqi_value | integer  |
| co_aqi_category | object |
| ozone_aqi_value | integer |
| ozone_aqi_category | object  |
| no2_aqi_value | integer  |
| no2_aqi_category | object |
| pm2.5_aqi_value | integer |
| pm2.5_aqi_category | object  |


1. Country_name:  
Provides the name of the country.  
2. city_name:  
name of the city in the given country.
3.  Air Quality Index:   
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
