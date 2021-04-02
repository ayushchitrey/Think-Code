''' Q3.	Consider a list [2,3,4,5,6]. Find the total sum of cumulative products of all the numbers in the list.
    (sum= 2*3 + 2*3*4 +....) '''
    
def cumprod(lst):
    results = []
    cur = 1
    for n in lst:
        cur *= n
        results.append(cur)
    return results

lst = [2,3,4,5,6]
print (cumprod(lst))

