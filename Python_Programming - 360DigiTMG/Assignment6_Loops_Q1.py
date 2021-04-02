''' Q1.	Print the Palindromes (reverse of the number is itself) that are present in between 100 and 250.
    (Ex: 121,131,212,222... etc.) '''

minimum = int(input("please enter the minimum value:"))
maximum = int(input("please enter the maximum value:"))
print("palindrom Numbers between %d and %d are:"%(minimum,maximum))
for num in range (minimum,maximum+1):
    temp=num
    reverse=0
    while(temp>0):
        Reminder=temp % 10
        reverse =(reverse * 10)+Reminder
        temp=temp//10
        if(num==reverse):
            print("%d" %num,end=' ')

