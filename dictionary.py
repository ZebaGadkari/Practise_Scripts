#create and print a dictionary
my_dict={"alice":17,
                  "priya":14,
                  "neha":19
    }
print (my_dict)

#dictionary items
this_dict={"apple":1,"orange":3,"kiwi":4}
print(this_dict["kiwi"])

#duplicates not allowed
new_dict={"goat":"grass","cow":"grass","goat":"milk"}
print(new_dict)

#dictionary len
this_dict={"hi":1,"hello":2,"welcome":3}
print(len(this_dict))

#type()
this_dict={"hi":1,"hello":2,"welcome":3}
print(type(this_dict))

#The dict() Constructor
#It is also possible to use the dict() constructor to make a dictionary.
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

#get method
dict1={"neha":"girl","raj":"boy","seema":"aunt"}
x=dict1.get("seema")
print(x)

#Keys method ,returns all keys
dict2={"apple":1,"mango":20,"potata":30}
x=dict2.keys()
print(x)

#add item
my_dict={"ram":45,"jay":35,"veer":24}
a=my_dict.keys()
print(a)
my_dict["gopal"]=25
print(a)

#values method ,returns all values
dict2={"apple":1,"mango":20,"potata":30}
x=dict2.values()
print(x)

#update and see wether values get updated
dict2={"apple":1,"mango":20,"potata":30}
x=dict2.values()
print(x)
dict2["carrot"]=70
print(x)

#The items() method will return each item in a dictionary, as tuples in a list.
name={"hen":"bird","cow":"animal"}
print(name.items())

#in keyword

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary") 

#change values
dict1={"bng":"kar","mumbai":"mah","hyd":"kar"}
print(dict1)
dict1["hyd"]="TN"
print(dict1)

#Update Dictionary
#The update() method will update the dictionary with the items from the given argument.
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
thisdict.update({"year": 2020})
print(thisdict)



