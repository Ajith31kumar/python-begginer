squared = lambda num: num * num
# lambda num : num * num 

print(squared(2))

def addtwo(num):
    return num + 2
# lambda num : num +2

print(addtwo(12))

def sum_total(a,b) : return a * b
# lambda a,b : a + b

print(sum_total(2,3))

# print(sum(2,10000))

################

def funcbulider(x):
    return lambda num : num + x


addten = funcbulider(10)
addtwenty = funcbulider(20)

print(addten(7))
print(addtwenty(7))



#########################3

numbers = [3,7,12,18,20,21]
squared_numbs = map(lambda num: num * num , numbers)

print(list(squared_numbs))

###############################

odd_numbs = filter(lambda num: num % 2 != 0, numbers)

print(list(odd_numbs))

############################3



from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

total = reduce(lambda acc, curr: acc * curr, numbers)

print(total)

print(sum(numbers, 10))

names = ['ajith','kumar','dsfefgergdegvfdgdf']

char_count = reduce(lambda acc,curr : acc + len(curr),names,0)

print(char_count)
### higher order function if it receives a function as an argument or if it returns a function i've got vs
# code open ans a new