#old way
name= "abdul"
age = 20
print("my name is " +name +"and my age is "+str(age))  # we have to convert the age to string to concatenate it with the other string, 
                                                       # also this way is not very readable and can be confusing when we have multiple variables to print


 #new way
name = "abdul"
age = 20
print(f"my name is {name} and my age is: {age}")   # f-string is used to format the string and print the values of variables in a readable way

#complex

#data types in python
#list
mylist = [1,2,3,4,5]
mylist[0] = 10  #lists are mutable, we can change the values of a list
print(mylist)

#tuple
mytuple = (1,2,3,4,5)
print(mytuple[3]) # tuples are immutable, we cannot change the values of a tuple

#set
myset = {1,2,3,4,5}
myset.add(6)
print(myset) #you can add values to a set but you cant add in specific positions  also sets are unordered, we cannot access the values of a set by index

#frozenset
myfrozenset = frozenset([1,2,3,4,5])
print(myfrozenset) # frozenset is immutable, we cannot change the values of a frozenset

#mapping types in python
 #dict
mydict = {"name": "abdul", "age": 20}
print(f"Age {mydict['age']}, Name {mydict['name']}") # we can access the values of a dictionary by using the keys, also dictionaries are mutable, we can change the values of a dictionary

#boolean
is_true = True
is_false = False
print(is_true, is_false)
