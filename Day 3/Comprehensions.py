                                    #comprehensions
#old way
list = [1, 2, 3, 4, 5]
squared = []
for i in range(len(list)):
   i = i+1
   a = i*i
   squared.append(a)
print(squared)

    #new way via list comprehension 
lists = [1, 2, 3, 4, 5]
squared = [num * num for num in lists]
print(squared)

    #filter even numbers
list = [1, 2, 3, 4, 5, 6]
evens = [num for num in list if num%2 == 0]
print(evens)

  
    #dictionary comprehension
    #1
list = [1,2,3,4,5]
square = {num: num*num for num in list}
print(square)
    
    #2
users = {
    "names": ["Abdul", "Ali", "Ahmad"], 
    "ages": [25, 30, 35],
    "cities": ["Lahore", "Karachi", "Islamabad"],
    "gender": ["M", "M", "M"]
    }
user_dictx = {name: age for name, age in zip(users["names"], users["ages"])}
user_dict = {name: { age, city, gender} for name, age, city, gender in zip(users["names"], users["ages"], users["cities"], users["gender"])}
print(user_dictx)
print(f"user with age {user_dict}")
