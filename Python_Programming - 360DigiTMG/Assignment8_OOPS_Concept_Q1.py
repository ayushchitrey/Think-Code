''' Q1.	Construct a class which takes in 3 arguments first name, last name and age.
    And create an instance of that class. '''

import datetime # we will use this for date objects

class Person:

    def __init__(self, name, surname, birthdate):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
     
    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1

        return age

person = Person(
    "Malika Hafiza",
    "Pasha",
    datetime.date(1995, 1, 23), # year, month, day
    
)

print("First Name : ",person.name)
print("Last Name : ",person.surname)
print("Age : ",person.age())

