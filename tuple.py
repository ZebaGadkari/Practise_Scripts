#creating tuple
mytuple=("apple","orange")
print(mytuple)

tuple1 = (4,5,"one","two","two")
print(tuple1)

#tuple length
tup = (4.6,6,3,2,1,4,)
print(len(tup))

# tuple with single item...need to add comma after the item or else it will be a string
my_tuple =('hi',)
print(type(my_tuple))

#tuple with string,int and bool values
tuple1 =('he','is',34,'years','old','thats',True)
print(tuple1)

# type
num =(2,3.4,'hi')
print(type(num))

#tuple() constructor
tuple1=tuple(('hi','welcome'))
print(tuple1)

#access tuple items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#negative indexing
name= ('devi','neha','soha')
print(name[-1])

#range of indexes
num =(3,4,5,8)
print(num[1:3])

#returning items from index[0]
new_tuple=('one','two','three','four','five')
print(new_tuple[:4])
      
#returning items till last index
new_tuple=('one','two','three','four','five')
print(new_tuple[3:])

#range of negative indexing
thistuple = ("apple", "banana", "cherry",'orange','chikku')
print(thistuple[-3:-2])

# in keyword
num =(3,4,5,8)
if 8 in num:
 print( '8 is present')

# changing tuple values , by converting it into lists
tuple1 = ('apple','orange','mango')
new=list(tuple1)
new[2]="kiwi"
print(new)
new1= tuple(new)
print(new1)

# changing tuple values, using append() method
my_tuple= ('one','two','three')
new_list=list(my_tuple)
new_list.append('four')
print(new_list)
new=tuple(new_list)
print(new)

#adding tuple to a tuple
one_tuple=("today","is")
two_tuple=("sunday",)
one_tuple+=two_tuple
print(one_tuple)

# changing tuple values, using extend() method
one_tuple=('ten','twenty','thirty')
one_list=list(one_tuple)
next_item=("fourty",)
one_list.extend(next_item)
print(one_list)

#remove item , by convertinf into list
my_tuple =('hi','you','welcome')
my_list= list(my_tuple)
my_list.remove("you")
mynew_tuple = tuple(my_list)
print(mynew_tuple)

'''# del keyword
one=(1,2,3)
del one
print(one)'''

# unpacking ,extract the values back into variables
fruits = ('apple','orange','banana')
(red,yellow,green) = fruits
print(yellow)
print(green)
print(red)
#If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
alp =("an","the","at","if","was")
(a,b,*c)=alp
print(a)
print(b)
print(c)
#If the asterisk is added to another variable name than the last,
#Python will assign values to the variable until the number of values left matches the number of variables left.
num =(1,2,3,4,5,6,7)
(a,b,*c,d) = num
print(c)

#Loop Through a Tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#Loop Through the Index Numbers
tuple1=('apple','banana','orange','mango')
for i in range(len(tuple1)):
 print(tuple1[i])

#while loop to print items
tuple1=('pune','bombay','delhi')
i=0
while i <(len(tuple1)):
 print(tuple1[i])
 i+=1

#join two tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3) 

 #multiply tuples
tuple1 = ('9','10')
new_tuple = tuple1*3
print(new_tuple)

# count() method, returns the no of time the argument is present 
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x) 

#index() method ,Search for the first occurrence of the value 8, and return its position:
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x) 
