''' Q3. A. How can you print a number between 55 and 75.
        B. How can you print a number which is either below 55 or above 75.'''

# A.

import random
n = random.randint(55,75)
print(n)

  
# B.
  
a=int(input(random.randint(0, 100)))
if a<55 or a>75:
    print(a)
else:
    print("Try again")
    
