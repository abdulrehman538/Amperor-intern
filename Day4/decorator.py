















# This function will ADD extra behavior
def alpha(beta):
    # This function replaces the original one
    def new_function():
        print("🔵 Before running function")
        beta()   # run original work
        print("🟢 After running function")
    return new_function
# This is the MAIN function
def say_hello():
    print("Hello, Abdul!")

# We are "decorating" the function manually
say_hello = alpha(say_hello)
# Call the function
say_hello()

def shownumber(no):
    def new_func():
        print("i am first")
        no()
        print("i am third")
    return new_func

def showmissingnum():
    print("i am second")

showmissingnum = shownumber(showmissingnum)
showmissingnum()
    