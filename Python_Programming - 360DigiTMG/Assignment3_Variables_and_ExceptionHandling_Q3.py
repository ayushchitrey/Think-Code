''' Q3.	Using Exception handling, write a program to find a reciprocal of the number in a such a way that.
    a.	If reciprocal exists, it should print reciprocal of that number
    (take any integer) 
    b.	If reciprocal does not exist, it should print “reciprocal cannot be found” along with the type of error.
    (take 0). '''

import numpy as np
x=np.array([1.,2.,.2,.3])
print("original array:")
print(x)
r1=np.reciprocal(x)
r2=1/x
assert np.array_equal(r1,r2)
print("Reciprocal for all elements of the said array:", r1)

