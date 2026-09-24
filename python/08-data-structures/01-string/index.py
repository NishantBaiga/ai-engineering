
# access character in string
s = "ABCDEF"
print(s[0])   
print(s[4])

# string slicing
s = "ABCDEF"
print(s[1:4])    
print(s[:3])     
print(s[3:])    
print(s[::-1])

# loop
s = "ABCDEF"
for char in s:
    print(char)
    
# deleting string
s = "ABC"
del s


# updating string
s = "ABCD EF"
s1 = "H" + s[1:]                  
s2 = s.replace("ABC", "abc")  

print(s1)
print(s2)


####  common string methods

s = "GeeksforGeeks"
print(len(s))

s = "Hello World"
print(s.upper())
print(s.lower())

s = "   ABC   "
print(s.strip())  #removes leading and trailing whitespace from the string   

s = "Python is fun"
print(s.replace("fun", "awesome"))
