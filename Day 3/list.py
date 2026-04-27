                        #list
fruits = ["apples", "oranges", "bananas"]
print(fruits)
fruits.append("grapes")
print(fruits)
fruits[0] = "kiwi"
print(fruits)
fruits.remove("bananas")
print(fruits)
                                             #sets
list1 = {"apple", "banana", "orange", "apple"}
List2 = {"tomato", "cucumber", "banana", "carrot"}
print(list1 & List2)

                                            #list into set
list3 = ["apple", "banana", "orange", "apple"]
set1 = set(list3)
print(set1)
list4 = list(set1)
print(list4)