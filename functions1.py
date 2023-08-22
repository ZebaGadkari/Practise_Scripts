#add number
def add_numbers(a, b):
    return a + b
result = add_numbers(5, 3)
print(result)  # Output: 8

#max number
def max(a,b):
  if(a>b):
    return a
  else:
     return b
result=max(3,4)
print (result)

#global keyword
def myfunction():
  global x
  x = "hello"
myfunction()
print(x)
