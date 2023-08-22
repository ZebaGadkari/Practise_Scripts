# defining a function
def my_function():
    print("Hello from a function")

#calling a function
def my_function():
    print("Hello from a function")
my_function()

#pasing arguments to function
def name(first_name):
    print("my name is",first_name)
name("soha")

def sum(a,b):
     c=a+b
     d=a-b
     print(c,d)
sum(5,6)

def sum(a,b):
     c=a+b
     d=a-b
     return c,d
m=5
n=6
o,p = sum(m,n)
print(o,p)

#pass by value
#pass by reference

#Types of function arguments
#Keyword argument
def person(name , age):
   print("name",name)
   print("age",age)
person(age=10, name="ram")
#Default srgument
#variable length argument
#Keyword variable length argument
