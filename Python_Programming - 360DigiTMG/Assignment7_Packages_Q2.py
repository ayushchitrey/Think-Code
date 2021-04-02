''' Q2. For the dataset “Indian_cities”, 
    a)	Find out top 10 states in female-male sex ratio
    b)	Find out top 10 cities in total number of graduates
    c)	Find out top 10 cities and their locations in respect of total effective_literacy_rate. '''

import pandas as pd

indiancities = pd.read_csv("C:\\Users\\Malika Hafiza Pasha\\#Coding\\Data_Science\\#Python_Programming\\Indian_Cities_Dataset.csv")
indiancities

# A.
print("Top 10 States in female-male sex ratio")
top10_states = indiancities.sort_values(by='state_name', ascending = False)
top10_states_sex_ratio = top10_states.head(10)
top10_states_sex_ratio

# B.
print("Top 10 cities in total number of graduates")
top10_cities = indiancities.sort_values(by='total_graduates', ascending = False)
top10_cities_total_graduates = top10_cities.head(10)
top10_cities_total_graduates

# C.
print("Top 10 cities and their locations in respect of total effective_literacy_rate")
top10_cities1 = indiancities.sort_values(by='effective_literacy_rate_total', ascending = False)
top10_cities_total_literacy = top10_cities1.head(10)
top10_cities_total_literacy



