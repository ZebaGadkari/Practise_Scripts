#creating a set
thisset = {"apple", "banana", "cherry"}
print(thisset)

#duplicate values are ignored
set1 ={1,2,3,1,2,3}
print(set1)

#True and 1 is considered the same value:
my_set = {False, True, 1, 2}
print(my_set)

#length of set
set1= {3,4,5,'hi'}
print(len(set1))

#set can be of any type
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1)
print(set2)
print(set3)

#type()
myset = {"apple", "banana", "cherry"}
print(type(myset))

# set() Constructor
thisset = set(("apple", "banana", "cherry")) 
print(thisset) 

#Access Items
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#check if item is present
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)


newset= {'one','two','three'}
if "one" in newset:
    print('one is present')

#add items ,add() method
new_set={1,2,3}
new_set.add(4)
print(new_set)

#add sets, update() method
set1={'a','b','c'}
set2={'d','e','f'}
set1.update(set2)
print(set1)
#add any iterables, tuples, lists, dictionaries etc
set1={'11','22'}
tup1=['33','44']
set1.update(tup1)
print(set1)

#remove() method, If the item to remove does not exist, remove() will raise an error.
my_set1 = {'hello','welcome','once','again'}
my_set1.remove('once')
print(my_set1)

#discard() method, If the item to remove does not exist, discard() will NOT raise an error.
set1 = {50,60,70}
set1.discard(60)
print(set1)

set1 = {50,60,70}
set1.discard(90)
print(set1)

#clear() method ,empties the set
set1={1,2,3,4,5,6,7}
set1.clear()
print(set1)

'''#del keyword
my_set1 = {'hello','welcome','once','again'}
del my_set1
print(my_set1)'''

#for loop
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#union() method
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 =set1.union(set2)
print(set3) 

#intersection_update() ,method will keep only the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

#intersection(), method will return a new set, that only contains the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z) 

#symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

#symmetric_difference, method will return a new set, that contains only the elements that are NOT present in both sets.
A={'carrot','radish'}
B={'radish','tomato'}
C= A.symmetric_difference(B)
print(C)
#True and 1 is considered the same value:
x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}
z = x.symmetric_difference(y)
print(z)

#Return a set that contains the items that only exist in set x, and not in set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z) 

#removes the items that exist in both sets. and keeps only items present in x
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple","cherry"}
x.difference_update(y)
print(x) 

#isdisjoint() ,Return True if no items in set x is present in set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)

#issubset(), Return True if all items in set x are present in set y:
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z) 

#issuperset(),Return True if all items set y are present in set x:
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)

#pop() method, Remove a random item from the set:
fruits = {"apple", "banana", "cherry"}
fruits.pop()
print(fruits) 
