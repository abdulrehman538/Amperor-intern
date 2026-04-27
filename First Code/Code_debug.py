                                    #Return a list of unique active user names only.
users = [
    {"name": "Ali", "age": 20, "active": True},
    {"name": "Sara", "age": 17, "active": True},
    {"name": "John", "age": 25, "active": False},
    {"name": "Ali", "age": 20, "active": True}
]
def active_users(users):
 active = list(filter(lambda user: user["active"], users))
 active_user_names = (set(map(lambda x: x["name"], active)))
 unique_active_users = list(set(active_user_names))
 return unique_active_users
print(active_users(users))



                            #🔥 Problem 2: Filter + Transform
numbers = [1, 2, 3, 4, 5, 6]

def fls(number):
 even = list(filter(lambda x:x % 2 == 0, numbers))
 square_even = list(map(lambda x:x*x, even))
 return square_even
print(fls(numbers))
