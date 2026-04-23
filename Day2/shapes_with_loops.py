                                                                            #shapes Loops
for i in range(5):
    for j in range(5):
        print("*", end= " ")
    print()

for i in range(5):
    for j in range(i + 1):
        print("*", end=" ")
    print()

for i in range(5):
    for j in range(5 - i):
        print("*", end=" ")
    print()
    

for i in range(5):
    print(" " * (5 - i), end="")   # spaces
    print("* " * (i + 1))  


for i in range(5):
      print("* " * (5 - i)) 
      print(" " * (i + 1), end="")   

for i in range(5):
    print(" " * (5-i), end = "")
    print("* " *(i))
print()

row = 4
for i in range(row +1):
    print (" " * (row - i), end="")
    print("*" * i)

   
