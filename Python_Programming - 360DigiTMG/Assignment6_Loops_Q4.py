''' Q4.	Create 2 lists.. one list contains 10 numbers (list1=[0,1,2,3....9]) 
    and other list contains words of those 10 numbers (list2=['zero','one','two',.... ,'nine']).
    Create a dictionary such that list2 are keys and list 1 are values. '''
    
def Convert(list):
    res_dct = {list2[i]: list1[i] for i in range(0,10)}
    return res_dct
         
# Driver code
list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = ['zero','one','two','three','four','five','six','seven','eight','nine']
print("Dictionary: ", Convert(list))

