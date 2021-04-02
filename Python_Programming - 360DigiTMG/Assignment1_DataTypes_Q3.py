''' Q3.	Create a data dictionary of 5 states having state name as key and number of covid-19 cases as values.
a.	Print only state names from the dictionary.
b.	Update another country and it’s covid-19 cases in the dictionary.'''

dictionary={"Maharashtra":990795,"Andhra Pradesh":537687,"Tamil Nadu":486052,"Karnataka":430947,"Uttar Pradesh":292029}
print("Dictionary :" , dictionary)

#Printing only the State names from the dictionary
print ("State Names : %s" %  dictionary.keys())   # or print(dict.keys())

# Updating another key and its value in the dictionary
dictionary2={"United States":6990000}
print("Country that has to be updated in Dictionary :", dictionary2)
dictionary.update(dictionary2)
print("Dictionary after Updation of another Country & its Covid-19 cases : ", dictionary)
