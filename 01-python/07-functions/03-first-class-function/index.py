#  in python functions are treated as first class object 

# means they can be used just like numbes , string or any other variables 


### assigning functions to variables
def msg(name):
    return f"Hello, {name}!"

# Assigning the function to a variable
f = msg

# Calling the function using the variable
print(f("Emma"))




### passsing functions as Arguments
def msg(name):
    return f"Hello, {name}!"

def fun1(fun2, name):
    return fun2(name)

# Passing the msg function as an argument
print(fun1(msg, "Alex"))


### returning functions from other functions 
def fun1(msg):
    def fun2():
        return f"Message: {msg}"
    return fun2

# Getting the inner function
func = fun1("Hello, World!")
print(func())

###  storing functions in data structures
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

# Storing functions in a dictionary
d = {
    "add": add,
    "subtract": subtract
}

# Calling functions from the dictionary
print(d["add"](5, 3))       
print(d["subtract"](5, 3))