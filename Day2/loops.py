                                                                                #for loop
#1
for letter in "Python": #it take each alphabet as a single entity and print it one by one
    print(letter)

#2
for i in range(1,10):
    print(f"2ndloop: {i}")

#3
for i in range(1,10,2):
    print(f"3rdloop: {i}")

#4 for loop with if else 
li = ["Banana", 1, "Apple",2, "Mango",3, "Orange"]
for item in li:
    if type(item) == str:
        print(item)
    else:
        print(item)
    #it give me values line wise. if i remove the else part it will give me only the string values and ignore the integer values

#5 anotehr example of for loop with if else
li = ["Banana", 1, "Apple",2, "Mango",3, "Orange"]
fruit = []
number = []
for item in li:
    if isinstance(item, str):
        fruit.append(item)
    else:
        number.append(item)

print(fruit) #it will give me a list of all the string values in the original list
print(number) #it will give me a list of all the integer values in the original list

                                                                                    #while loop
#1
i = 1
while i <= 10:
    print(i)
    i = i+1
#nested while loop
i = 1

while i <= 3:
    j = 1
    while j <= i:
        print("*", end=" ")             
        j += 1
    print()
    i += 1

#while with string
password = ""
 
while password != "konan.100":
    password = input("Enter Password:" )
print("Access Granted")

#while with list
myfruits = ["apple","mango","banana"]
i = 0
while i < len(myfruits):
    print(myfruits[i])
    i = i + 1

