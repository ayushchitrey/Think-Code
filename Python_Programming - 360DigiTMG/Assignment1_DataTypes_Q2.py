''' Q2.	Create 2 Sets containing integers (numbers from 1 to 10 in one set and 5 to 15 in other set)
a.	Find the common elements in above 2 Sets.
b.	Find the elements that are not common.
c.	Remove element 7 from both the Sets.'''

list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [5,6,7,8,9,10,11,12,13,14,15]

# Setting list as a Set
list1_as_set = set(list1)
list2_as_set = set(list2)

# Finding the common elements of the sets and lists
intersection = list1_as_set.intersection(list2)
intersection_as_list = list(intersection)
print("Common Elements : ", intersection_as_list)

# Finding the elements of the sets and lists that are not in common
union = list1_as_set.union(list2)
union_as_list = list(union)
print("Union of the 2 lists : ", union_as_list)
union_as_set = set(union_as_list)

uncommon = list(union_as_set - intersection)
print("Uncommon Elements : ", uncommon)


# Removing element 7 from both the sets
list1.remove(7)
print("Element 7 removed from list 1 : ", list1)
list2.remove(7)
print("Element 7 removed from list 2 : ", list2)

