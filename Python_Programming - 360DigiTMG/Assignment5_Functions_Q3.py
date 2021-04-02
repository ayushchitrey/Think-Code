''' Q3.By using a filter function, find positive number present in a list.
         Lsit1= [2, 6, -5, 4, -8, -9, 10, 1] '''

#By using a filter function, find positive number present in a list
nums=[2, 6, -5,4,-8,-9,10,1]
print("original numbers in the list:",nums)
new_nums=list(filter(lambda x: x>0,nums))
print("positive numbers in the list:", new_nums)

