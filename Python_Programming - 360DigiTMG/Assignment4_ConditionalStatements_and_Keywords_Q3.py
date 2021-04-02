''' Q3.	Check whether the given number is positive and divisible by 5 or not. '''

number = float(input("Enter a number: "))
if number > 0:
   print("Positive number")
   if(number % 5 == 0):
       print("Given Number {0} is Divisible by 5".format(number))
   else:
       print("Given Number {0} is Not Divisible by 5".format(number))
       
elif number == 0:
   print("Zero")
   if(number % 5 == 0):
       print("Given Number {0} is Divisible by 5".format(number))
   else:
       print("Given Number {0} is Not Divisible by 5".format(number))
       
else:
   print("Negative number")
   if(number % 5 == 0):
       print("Given Number {0} is Divisible by 5".format(number))
   else:
       print("Given Number {0} is Not Divisible by 5".format(number))



