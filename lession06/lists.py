users = ['ajith','ashok','hari']

data = ['ajith',25,True]
emptylist = []

print("ajith" in emptylist)

print(users[2])

print(users.index('hari'))


print(users[0:2])
print(users[1:])
print(users[-3:-1])


print(len(data))

users.append('rajan')
print(users)

users += ['kumar']
print(users)

users.extend(['robert','jimmy'])
print(users)

# users.extend(data)
# print(users)

users.insert(0,'ranjith')
print(users)

users[2:2] = ['alex','eddie']
print(users)

users.remove('ajith')
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

# del data
data.clear()
print(data)

users[1:2] = ['ajith']
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [3,4,556,678,45]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums,reverse=True))
print(nums)

numscopt = nums.copy()
mynumbs = list(nums)
mycopy = nums[:]

print(numscopt)
print(mynumbs)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))
mylist = list([1,"neil",True])
print(mylist)

# tubles

mytuble = tuple(('ajith',25,True))

anothertuble = (1,2,3,4,2,2,2)

print(mytuble)
print(type(mytuble))
print(type(anothertuble))

newlist = list(mytuble)
newlist.append('ashok')
newtuple = tuple(newlist)
print(newtuple)

(one,*two, heey) = anothertuble
print(one)
print(two)
print(heey)

print(anothertuble.count(2))