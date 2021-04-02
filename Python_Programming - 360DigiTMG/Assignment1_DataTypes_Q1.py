''' Q1. Construct 2 lists containing all the available data types (integer, float, string, complex and Boolean)
    and do the following.
a.	Create another list by concatenating above 2 lists
b.	Find the frequency of each element in the concatenated list.
c.	Print the list in reverse order.'''

list1 = [10 , 12.5 , 10+2j , "malika" , True]
list2 = [23 , 12.5 , 17+4j , "hafiza" , False]

# Creating another list by concatenating above 2 lists
list3 = list1 + list2
print("Concatenated list using + :" + str(list3))

# Finding the frequency of each element in the concatenated list

    #Array 'freq' will store frequencies of element    
freq = [None] * len(list3);    
visited = -1;    
     
for i in range(0, len(list3)):    
    count = 1;    
    for j in range(i+1, len(list3)):    
        if(list3[i] == list3[j]):    
            count = count + 1;    
            #To avoid counting same element again    
            freq[j] = visited;    
                
    if(freq[i] != visited):    
        freq[i] = count;    
     
        #Displays the frequency of each element present in array    
print("---------------------");    
print(" Element | Frequency");    
print("---------------------");    
for i in range(0, len(freq)):    
    if(freq[i] != visited):    
        print("    " + str(list3[i]) + "    |    " + str(freq[i]));    
print("---------------------");  


# Printing the list in reverse order
print ("List in the reverse order: " + str(list3[::-1]))