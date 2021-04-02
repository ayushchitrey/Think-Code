''' Q2.	Construct an example for Inheritance. '''

#Inheritance allows us to define a class that inherits all the methods and properties from another class.
#Parent class is the class being inherited from, also called base class.
#Child class is the class that inherits from another class, also called derived class.

class Parent:
     def __init__(self , fname, fage):
          self.firstname = fname
          self.age = fage
     def view(self):
         print(self.firstname , self.age)
class Child(Parent):
     def __init__(self , fname , fage):
          Parent.__init__(self, fname, fage)
          self.lastname = "Pasha"
     def view(self):
          print("First Name : " , self.firstname)
          print("Last Name : " , self.lastname) 
          print("Age : ", self.age)
ob = Child("Malika Hafiza" , '26')
ob.view()



