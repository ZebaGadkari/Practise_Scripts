#fibonacci
a, b = 0, 1
count= 10
fibonacci_series = []
while count >0:
    fibonacci_series.append(a)
    a, b = b, a + b
    count -= 1
print(fibonacci_series)

#factorial
n = 5
factorial = 1
while n > 0:
    factorial *= n
    n -= 1
print("Factorial:", factorial)

#reverse no
number = 12345
reversed_number = 0
while number > 0:
    digit = number % 10
    reversed_number = (reversed_number * 10) + digit
    number //= 10
print("Reversed Number:", reversed_number)
