"""#type 1
count = 0
def count_even_numbers(numbers):
    global count
    for number in numbers:
        if number % 2 == 0:
            count += 1
    return count,      
numbers = [2, 5, 8, 11, 14]
count_even_numbers(numbers)
print("Total even numbers:", count)
odd=len(numbers)-count
print("total odd numbers",odd)
"""




even_nos=0
odd_nos=0
def even_odd(numbers):
   global even_nos, odd_nos
   for i in numbers:
       if i % 2 == 0:
            even_nos +=1
       else:
            odd_nos +=1
   return even_nos,odd_nos

numbers=[1,34,54,23,33,2,4,4]
even_odd(numbers)
print("total even numbers are",even_nos)
print("total odd numbers are", odd_nos)














"""#using lambda
numbers = [2, 5, 8, 11, 14]
even_count = len(list(filter(lambda x: x % 2 == 0, numbers)))
odd_count = len(numbers) - even_count

print("Total even numbers:", even_count)
print("Total odd numbers:", odd_count)
"""

