#iterate over a list
fruits=["apple","banana","mango"]
for fruit in fruits:
   print(fruit)

#iterate over a string
message="hello world"
for char in message:
    print(char)
    
#iterate over integers
for num in range(1,6):
  print(num)      
    
student_scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
for name, score in student_scores.items():
    print(name, score)

#iterate over a dictionary
student_scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
for name, score in student_scores.items():
    print(name, score)
    
fruits={"apple":1,"banana":2,"mango":3}
for fruit,no in fruits.items():
    print(fruit,no)
    
#iterate over a list with index
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
