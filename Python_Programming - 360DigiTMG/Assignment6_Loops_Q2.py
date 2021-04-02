''' Q2.	 Consider a list1 [3,4,5,6,7,8]. Create a new list2 such that 
    Add 10 to the even number and multiply with 5 if it is odd number in the list1. '''
      
# list of numbers 
list1 = [3, 4, 5, 6, 7, 8] 
  
# iterating each number in list 
for num in list1: 
      
    # checking condition 
    
    if num % 2 == 0:                    # Checking for even condition
        print(num+10, end = " ")
        
    if num % 2 != 0:                    # Checking for odd condition
       print(num*5, end = " ") 
       

      
