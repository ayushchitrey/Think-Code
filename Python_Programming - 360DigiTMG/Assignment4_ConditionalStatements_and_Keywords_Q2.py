''' Q2.	Find the final train ticket price with the following conditions. 
    a.	If male and senior citizen, 70% of fare is applicable
    b.	If female and senior citizen, 50% of fare is applicable.
    c.	If female and normal citizen, 70% of fare is applicable
    d.	If male and normal citizen, 100% of fare is applicable
    [Hint: First check for the gender, then calculate the fare based on age factor.
     For both Male and Female, consider them as senior citizens if their age >=60] '''

gender=str(input("Enter Gender: "))
if gender=="male":
    age=int(input("Enter Age : "))
    if age<60:
        print("Normal Citizen - 100% of fare is applicable")
    elif age>=60:
        print("Senior Citizen - 70% of fare is applicable")
    else:
        print("check that your input is an integer and try again")
        
elif gender=="female":
    age=int(input("Enter Age : "))
    if age<60:
        print("Normal Citizen - 70% of fare is applicable")
    elif age>=60:
        print("Senior Citizen - 50% of fare is applicable")
    else:
        print("check that your input is an integer and try again")
    
 
