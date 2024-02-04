# string data type

# literal assignment
import math
first = "ajith"
last  = "kumar"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# constructor finction
# pizza= str("pepperoni")
# print(type(pizza))
# print(type(pizza)== str)
# print(isinstance(pizza, str))

# concatenation

fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

#castinga number to a string
decade = str(1999)
print(type(decade))
print(decade)

statement = "i like rock music from " + decade + "s."
print(statement)

#mutiline lines

mutiline = '''
her, how are you

i was checket in  
                                          all good?

   '''
print(mutiline)     

#escaping special characters
sentence = 'I\'m back at work!\they!\n\nwhere\'s this at\\located?'
print(sentence)

#string method

print(first)
print(first.lower())
print(first.upper())

print(mutiline.title())
print(mutiline.replace("good","ok"))
print(mutiline)

print(len(mutiline))
mutiline += "                         "
mutiline = "               " + mutiline
print(len(mutiline))

print(len(mutiline.strip()))
print(len(mutiline.lstrip()))
print(len(mutiline.rstrip()))

#build a menu
title = "menu".upper()
print(title.center(200,"="))
print("cofee".ljust(16,".") + "$1".rjust(4))
print("muffin".ljust(16,".") + "$2".rjust(4))
print("cheesecake".ljust(16,".") + "$4".rjust(4))

print("")

#string index values
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

#some method return boolean data
print(first.startswith('a'))
print(first.endswith('h'))

#Boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue,bool))

#numeric data type


import math

# Print the value of pi
print(math.pi)

# Calculate the square root of 64
print(math.sqrt(64))

# Assuming gpa is a variable, round up to the nearest integer
gpa = 3.7
print(math.ceil(gpa))

# Round down to the nearest integer
print(math.floor(gpa))


#casting a string to a number
