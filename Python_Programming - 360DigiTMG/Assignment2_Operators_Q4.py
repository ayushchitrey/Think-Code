''' Q4. A. How to check the presence of an alphabet ‘s’ in word “Data Science” .
        B. How can you obtain 64 by using numbers 4 and 3 .'''

# A.

word = "Data Science"
print("s in Data Science: ", "s" in word) # Python is case-sensitive, presence of 's' is False 
print("S in Data Science: ", "S" in word) # Python is case-sensitive, presence of 'S' is True

# B.

x = 64
y = 3
z = 4
# Equation : x+20y+z = 0
equation = 20*y+4
if equation == x:
    print('it is a valid relation')
else:
    print('It is not a valid relation')
   
