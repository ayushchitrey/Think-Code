''' Q3.	Explain Polymorphism in Python? Construct an example for Polymorphism. '''

# Polymorphism means the ability to take various forms.
# It is the ability of an object to adapt the code to the type of the data it is processing.
# It is a built-in feature.
# Polymorphism allows us to define methods in the child class with the same name as defined in their parent class.
# Polymorphism means same function name (but different signatures) being uses for different types.,
# (i.e.)it helps to describe an action regardless of the type of objects.
    
class India(): 
    def capital(self): 
        print("New Delhi is the capital of India.") 
  
    def language(self): 
        print("Hindi is the most widely spoken language of India.") 
  
    def type(self): 
        print("India is a developing country.") 
  
class USA(): 
    def capital(self): 
        print("Washington, D.C. is the capital of USA.") 
  
    def language(self): 
        print("English is the primary language of USA.") 
  
    def type(self): 
        print("USA is a developed country.") 
  
obj_ind = India() 
obj_usa = USA() 

for country in (obj_ind, obj_usa): 
    country.capital() 
    country.language() 
    country.type() 
    

