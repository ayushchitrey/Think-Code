''' Q1.	A. Write an equation which relates   399, 543 and 12345.
    B.  “When I divide 5 with 3, I got 1. But when I divide -5 with 3, I got -2”
    —How would you justify it.'''
    
# A.

x = 12345
y = 543
z = 399
# Equation : x+22y+z = 0
equation = 22*y + z
if equation == x:
    print('it is a valid relation')
else:
    print('It is not a valid relation')
   
    
# B.

a=5
b=-5
c=3
print(a/c)
print(b/c)
print(a//c)
print(b//c) # gets rounded off towards the left side, so -2 is the answer
# / - Divide left operand by the right one (always results into float)
# // - Floor division - division that results into whole number adjusted to the left in the number line

