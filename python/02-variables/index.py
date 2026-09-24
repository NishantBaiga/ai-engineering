# assign value to variable, python is dynamic language so types are automatically check 

x = 5 
name =  "alex"
print(x)
print(name)

# assiginig multiple values

x, y, z = "a", "b", "c"
print(x,y,z)

# one value to multipe variables, we use = operator
m = n = o = "apple"
print(m , n, o)

# del keyword is used to delete a variable from memory. After deletion, the variable can no longer be accessed.
#  and througha any error 

x = 10 
del x
print(x)

# swap two numbers
x,y = 10 ,20
print(x,y)
x,y = y,x
print(x,y)

# count charcter 
x= "helllo"
length = len(x)
print(length)