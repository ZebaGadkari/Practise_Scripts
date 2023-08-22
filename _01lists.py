#list
#list creation
my_list=['apple','cherry','banana']
print(my_list)

list_1=['one','three','five']
print(list_1)

#duplicate in list
fruits=['banana','orange','mango','banana','cherry']
print(fruits)

games_list=['ludo','cricket','football','ludo','volley ball','ludo']
print(games_list)

#finding length of list
N=['3','16','soha','1','neha','5']
print(len(N))

num=['one','1','two','three']
print(len(num))

#list  data types can be of any type
names_list=['dev','john','priya']
years_list=['2014','5','09']
B_list=['True','False','False']
print(names_list,years_list,B_list)

new_list=['hi','01','hello','True','05','bye','0.9']
print(new_list)

#list type
my_list=['cucumber','radish']
print(type(my_list))

#The list() constructor
months=list(('jan','feb','march'))
print(months)

#accessing list items
years=['1991','1992','1993']
print(years[2])

sum=['1+2','3+2']
print(sum[0])

#range of index
this_list=['apple','orange','banana','mango','kiwi','cherry']
print(this_list[3:5])
#prints the items from begining index[o] to index[3-1]
new_list=['rice','wheat','jawar','paddy','ragi']
print(new_list[:3])
#prints the items from index[2] to end
my_list=['bng','hyd','tel','mah']
print(my_list[2:])

#range of negative indexing
#prints the item from index[-4] to , but not including index[-1]
New=['1','2','3','4']
print(New[-3:-1])

# in keyword in list
this_list=['hi','welcome']
if "hi" in this_list:
  print('hi is present in the list')

#changing list items
thislist=['1','2','3']
thislist[1]='0'
print(thislist)
#changing a range of item values
new=['apple','banana','mango','papaya']
new[2:4]=['cherry','nuts']
print(new)
# changing one value by two new values
order=['pen','penci','eraser']
order[0:1]=['scale','gum']
print(order)
#If you insert less items than you replace, the new items will be inserted where you specified,
#and the remaining items will move accordingly:
new=['delhi','mumbai','goa','banglore']
new[1:3]=['hyderabad']
print(new)

# insert() method
flower_list=['rose','lily']
flower_list.insert(2,"lotus")
print(flower_list)

#append() method ,add item to list end
cap=['D','E','L','H']
cap.append('I')
print(cap)

# extend() method, extends the existing list
season_list=['summer','winter','rainy']
months=['may','december','july']
season_list.extend(months)
print(season_list)

#the extended list can add any iterable object (tuples, sets, dictionaries etc.).
my_list=['hi','enjoy']
my_tuple=('your','day')
my_list.extend(my_tuple)
print(my_list)

#remove() method
new_list=['one','two','five']
new_list.remove('five')
print(new_list)

#pop() method, removes last item
num=['1','2','3','4']
num.pop()
print(num)

#pop() method , using index
veg=['tomato','carrot','radish']
veg.pop(0)
print(veg)

# del keyword, using index
animal_list=['cow','cat','camel']
del animal_list[1]
print(animal_list)

"""# del keyword
num = ['5','10','15']
del num
print(num)# cause an error bcoz num list is deleted"""

# clear() method, empties the list
my_list=['today','is','friday']
my_list.clear()
print(my_list)

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#sort(method)
old_list =[1,45,3,87,6,7,90]
old_list.sort()
print(old_list)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# sort decending order
my_list= ['mom','dad','bro','sis']
my_list.sort(reverse=True)
print(my_list)

new_list=[0,8,6,5,6,7,8,5,3]
new_list.sort(reverse=True)
print(new_list)

# case insensitive sort() method,resulting in all capital letters being sorted before lower case letters:
cars =['Nissan','hyundai','Kia','TOYOTA','BMW','mahindra']
cars.sort()
print(cars)

# reverse() method
my_list = ['pen','paper',1,2,'apple','orange']
my_list.reverse()
print(my_list)

# copy() methos
this_list =['c','python','c++']
new_list= this_list.copy()
print('new list is ',new_list)

# list() method , another way to copy
my_list= ['welcome','to','python','class']
newlist=list(my_list)
print(newlist)

# + operator, join two lists
list1= ['hello']
list2=['there']
list3=list1+list2
print(list3)

# join two list using append() method
list1=[1,2]
list2=['hi' ,4]
for x in list2:
 list1.append(x)
print(list1)

# join two list using extend() method
list1=['1',2]
list2=['3','4']
for x in list2:
 list1.extend(x)
print(list1)
