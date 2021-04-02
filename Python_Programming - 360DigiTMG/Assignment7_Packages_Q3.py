''' Q3.	For the data set “Indian_cities”
    a)	Construct histogram on literates_total and comment about the inferences
    b)	Construct scatter plot between male graduates and female graduates
    c)	Construct Boxplot on total effective literacy rate and draw inferences
    d)	Find out the number of null values in each column of the dataset and delete them. '''

import pandas as pd
import matplotlib.pyplot as plt

indiancities = pd.read_csv("C:\\Users\\Malika Hafiza Pasha\\#Coding\\Data_Science\\#Python_Programming\\Indian_Cities_Dataset.csv")
indiancities

# A.
plt.hist(indiancities.literates_total)   # histogram

# B.
x = indiancities.male_graduates
y = indiancities.female_graduates
plt.scatter(x,y)    # scatterplot

# C.
plt.boxplot(indiancities.effective_literacy_rate_total)   # boxplot

# D.
details = pd.DataFrame(indiancities, columns =['name_of_city','state_code','state_name','dist_code','population_total','population_male','population_female','0-6_population_total','0-6_population_male','0-6_population_female','literates_total','literates_male','literates_female','sex_ratio','child_sex_ratio','effective_literacy_rate_total','effective_literacy_rate_male','effective_literacy_rate_female','location','total_graduates','male_graduates','female_graduates'],
                                       index =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v']) 
print(details)

# show the boolean dataframe             
print(" \nshow the boolean Dataframe : \n\n", details.isnull()) 
  
# Count total NaN at each column in a DataFrame 
print(" \nCount total NaN at each column in a DataFrame : \n\n", details.isnull().sum()) 

# Count total NaN in a DataFrame 
print(" \nCount total NaN in a DataFrame : \n\n", details.isnull().sum().sum()) 

# drop all rows with any NaN and NaT values
details1 = details.dropna()
print(details1)


