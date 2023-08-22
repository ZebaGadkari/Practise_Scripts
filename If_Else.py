#if statement
a=50
b=40
if a>40:
 print("a is greater")

#if else statement
x=4
y=5
if x >y:
  print ("x is greater")
else:
     print("y is greater")

#elif statement
a = 90
b = 30
c=a/b
if c ==1:
    print("not divisible")
elif c ==0:
    print("not divisible")
elif c==3:
    print("divisible")
    
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#else keyword
A=50
B=6
C=A-B
if C>0:
     print(C)
else:
     print("invalid")

#else with elif
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#Short Hand If
if a > b: print("a is greater than b")

#Short Hand If ... Else
a = 2
b = 330
print("A") if a > b else print("B")


#One line if else statement, with 3 conditions:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

x=48
y=48
print("x is greater") if(x>y) else print("y is greater") if(y>x) else print("x==y")

#and keyword
m = 2
n = 3
if m<n and m!=0:
 print("M is greater than 0")

#or keyword
i = 10
j = 20
k =30
if i<j or j<k:
 print("Either one condition is true")

#not keyword
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

#nested if
x = 10
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.") 
else:
    print("Below 10")

#pass statement
a = 33
b = 200
if b > a:
  pass
