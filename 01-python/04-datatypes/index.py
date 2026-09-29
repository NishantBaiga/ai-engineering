# numeric

a = 5  # integer
b = 5.5  # float 
c = 2+4j # complex number

# boolean 


# sequence :=> string, list, tuple
s = 'Welcome to the Geeks World' # string
print(s)
print(type(s))

# access string with index
print(s[1])
print(s[-1])

# list =>  ordered , mutable , multiple items 
a = [1,2,3,4,5] 

print(a)

b = ["Geeks", "For", "Geeks", 4, 5]
print(b[3])
print(b[-3])

# tuple => ordered, immutable, multiple items
t1 = (1,)
print(type(t1))

t2 = ('Geeks', 'For', 'Geeks', 1, 2)
print(t2[3])
print(t2[-3])

# set :=> unordered, mutable, unique values, can not be accessed with indexing

s1 = {"a", "a", "b", "c", "b"}
print(s1)

s2 = {"Geeks", "For", "Geeks"}
for i in s2:
    print(i)
    
# dictionary :=> key value pairs , 
d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d[1])    
print(d.get(2))
    
    