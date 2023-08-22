str_input = "abc"
#CAPITALIZE ,capitalize first character  in a string
x = str_input.capitalize()
print(x)

#CASEFOLD , converts string to lower case
new_str= (input("enter a string"))
a=new_str.casefold()
print(a)


#LOWER, converts string to upper case
my_str = (input("Enter a string"))
x=my_str.lower()
print(x)

#CENTER, returns a centered string, center the sting with the no of character spaces provided in the argument
txt = "welcomw to python"
x= txt.center(80)
print(x)
 
#COUNT, return the no of occurence of the word
a = "well done, well keep it up "
x = a.count("well")
print(x)

#ENCODE, returns an encoded version of the string
n = "My name is Ståle"
x= n.encode()
print(x)

#FIND, returns the position of string where it is found
a= "python programming"
x= a.find("r")
print(x)


#JOIN, converts the elements of an iterable into string
a = ("john","joe","loseph")
x = "#".join(a)
y = "*".join(a)
print(x)
print(y)