''' Q1.	A) Find the magnitude of (3+5j)
    B) list1 = [1,5.5, (10+20j),’data science’].. Print default functions and parameters exists in list1.
    C) How do we create a sequence of numbers in Python.
    D) Read the input from keyboard and print a sequence of numbers up to that number. '''

# A.
import numpy as np
vector=np.array([3,4])
magnitude=np.linalg.norm(vector)
print(magnitude)

# B. 
list1 = [1,5.5, (10+20j),"data science"]
list1.append(20)
print(list1)

# C.      
numbers=range(1,10)
sequence_of_numbers=[]
for number in numbers :
    if number % 5 in (1,2):
        sequence_of_numbers.append(number)
        print(sequence_of_numbers)
        
# D.
import numpy as np
a = int(input("Enter a number: "))
print(np.arange(a))

