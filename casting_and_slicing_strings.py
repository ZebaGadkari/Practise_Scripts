#Specifying variable type
x = int(1)
print(x)
y= int(2.8)
print(y)
z=int("3")
print(z)
x=float(5)
y=float(3.5)
z=float("4")
m=float("6.7")
print(x,y,z,m)

#Strings
print("hello")

a="welcome"
print(a)

a= """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a="welcome to python"
print(a[7])
print(a[6])

#looping through string
for x in "python":
 print(x)

#string length
a="Python Programming"
print(len(a))

#Check string
txt="that is cost effective"
print("cost" in txt)
print("out" in txt)

#Check not in string
txt="that is cost effective"
print("cost" not in txt)
print("out" not in txt)

#slicing strings
a= "hello"
print(a[2:4])
 
 #from start
print(a[:2])
 
 #upto end
print(a[2:])

#negative indexing
a="python"
print(a[-3])
print(a[-5:-2])