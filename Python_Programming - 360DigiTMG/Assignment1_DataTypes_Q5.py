''' Q5.	Write a program to accept the user’s first and last name and then print it in the reverse order with a
space between first name and last name'''
first_name = input("Enter your First Name : ")
last_name = input("Enter your Last Name : ")
# [::-1] It take the input entered and reverses the order
print ("Full Name in the reverse order: " + first_name[::-1] + " " + last_name[::-1])
