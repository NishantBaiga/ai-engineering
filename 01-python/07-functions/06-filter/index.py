def starts_a(w):
    return w.startswith("a")

li = ["apple", "banana", "avocado", "cherry", "apricot"]
res = filter(starts_a, li)
print(list(res))

#### 
def even(n):
    return n % 2 == 0

a = [1, 2, 3, 4, 5, 6]
b = filter(even, a)
print(list(b)) # Convert filter object to a list


####
a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x % 3 == 0, a)
print(list(b))

#### 
a = ["apple", "banana", "cherry", "kiwi", "grape"]
b = filter(lambda w: len(w) > 5, a)
print(list(b))

####
L = ["apple", "", None, "banana", 0, "cherry"]
A = filter(None, L)
print(list(A))