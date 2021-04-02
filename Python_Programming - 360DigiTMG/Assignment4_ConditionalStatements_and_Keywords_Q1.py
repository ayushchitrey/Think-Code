''' Q1.	 Take a variable age which is of positive value and check the following:
    a. If age is less than 1, print 'infant'
    b. If age is between 1 to 14, print 'child'
    c. If age is between 15 to 60, print 'Adult'
    b.	If age is more than 60, print ‘senior citizens’ '''
    
age=int(input("Enter Age : "))
if age<1:
    print("INFANT")
elif age>=1 and age<=14:
    print("CHILD")
elif age>=15 and age<60:
    print("ADULT")
elif age>=60:
    print("SENIOR CITIZEN")
else:
    print("check that your input is an integer and try again")

