# map
s = ['1', '2', '3', '4']
res = map(int, s)
print(list(res))


# Converting map object to a list
def double(val):
    return val * 2

a = [1, 2, 3, 4]    
res = list(map(double, a))
print(res)

# map() with lambda
a = [1, 2, 3, 4]
res = list(map(lambda x: x ** 2, a))
print(res)

# map() with multiple iterables
a = [1, 2, 3]
b = [4, 5, 6]
res = map(lambda x, y: x + y, a, b)
print(list(res))

# Using map() with Tuples
nums = (1, 2, 3)
res = tuple(map(lambda x: x + 1, nums))
print(res)

# Converting strings to Uppercase
fruits = ['apple', 'banana', 'cherry']
res = map(str.upper, fruits)
print(list(res))