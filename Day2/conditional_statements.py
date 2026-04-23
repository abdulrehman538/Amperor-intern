#conditional statements in python

#if-else
marks = 45
if marks >=33:
    print("Pass")
else :
  print("Fail")

#else-if
marks = 90
if marks >= 90:
    print("A grade")
elif marks >= 80:
    print("B grade")
else:
    print("C grade")

#nested if-else
age = 20
has_id = True
if age >= 18:
    if has_id:
        print("you can vote")
    else:
        print("you cant vote without id")
else: 
    print("you are not eligible to vote")