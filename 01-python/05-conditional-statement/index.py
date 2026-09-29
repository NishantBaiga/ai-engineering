# if statement
age = 20
if age >= 18:
    print("Eligible to vote.")
    
# shorthand
age = 19
if age > 18: print("Eligible to Vote.")
    
    
# if else statement
age = 10
if age <= 12:
    print("Travel for free.")
else:
    print("Pay for ticket.")
    
#  if elif-else
age = 25

if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")
    
# ternary operator
age = 20
s = "Adult" if age >= 18 else "Minor"
print(s)

# match case 
number = 2

match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other number")