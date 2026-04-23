 #lambda function
#with one variable
z = lambda x: x*x
print(z(2))

#with 2 varibales
add = lambda a, b: a + b
print(add(3,4))

#with list  
numbers = [1,2,3,4,5]

evens = list(filter(lambda x: x%2 == 0, numbers))
print(evens)

 
user = [
  {"name": 'Abdul', "age": 25, "active": True},
  {"name": 'Konan', "age": 27, "active": False},
  {"name": 'Deckard', "age": 24, "active": True}
 ]
print(list(filter(lambda x: x["age"] > 18, user)))


user = [
  {"name": 'Abdul', "age": 25, "active": True},
  {"name": 'Konan', "age": 27, "active": False},
  {"name": 'Deckard', "age": 24, "active": True}
 ]
result = list(
      map(lambda x: x["name"],
           filter(lambda x: x["active"], user)))

print(result)