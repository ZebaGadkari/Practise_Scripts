# Global variable
global_var = 10

def my_function():
    # Accessing the global variable
   

    # Modifying the global variable
    global global_var
    global_var = 20
    return global_var
# Accessing the global variable
print(global_var)  # Output: 10

# Modifying the global variable by calling the function
my_function()

# Accessing the modified global variable
print(global_var)  # Output: 20

#lambda function
#square
square = lambda x: x**2

result = square(5)
print(result)
#add
add= lambda a,b: a+b
r=add(4,5)
print(r)
#even
even_odd=lambda b:b%2==0
print(even_odd(4))

#reverse string
reverse=lambda s: s[: : -1]
print(reverse("hello"))

#sorting
students=[("alice",0.9),("dob",0.5),("charlie",0.3)]
sorted_students= sorted(students,key=lambda x:x[1])
print(sorted_students)

#combine names
combine_names = lambda first, last: first  +" "+ last
full_name = combine_names("John", "Doe")
print(full_name)  # Output: "John Doe"

#sort by length of string
fruits=['apple','orange','banana','mango']
sorted_fruits=sorted (fruits,key= lambda x:len(x))
print(sorted_fruits)

#sort for list

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}]
cars1=sorted(cars,key=lambda x:x['year'])
print(cars1)








