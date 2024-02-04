#dictionaries

band = {
    "vocals": "planet",
    "guitar": "page"
}

band2 = dict(vocals = "plant",guitar = "page")

print(band)
print(band2)
print(type(band))
print(len(band))

#access items
print(band["vocals"])
print(band.get('guitar'))

#list all keys
print(band.values())

#list of key/values paires as tuples
print(band.items())

#verfify a key exists
print("guitar" in band)
print("guitr" in band)

#change values

band['vocals'] = 'coverdale'
band.update({"bass": "jpj"})
print(band)

#remove items
print(band.pop("bass"))
print(band)

band['drums'] = 'gbjom'
print(band)

print(band.popitem()) #tuple
print(band)

#delete and clear
band['drums'] = 'gnjom'
del band["drums"]
print(band)

band2.clear()
print(band2)
del band2

#copy dictionaries

# band2 = band # create a referance
# print("bad copy!")
# print(band2)
# print(band)

# band2["drumps"] = "ajith"
# print(band)

band2 = band.copy()
band2["drumps"]= "ajith"
print(band)
print(band2)

#or use  the dict() constructor function
band3 = dict(band)
print("good copy!")
print(band3)

#nested dictionaries
member1 = {
    "name" : "plant",
    "instrument" : "vocals"
    
}
member2= {
    "name" : "page",
    "instrument" : "guitar"
    
}

band = {
    'member1' : member1,
    'member2' : member2
}

print(band)
print(band["member1"]['name'])

#sets

nums = {1,2,3,4}

nums2 = set((1,2,3,4))
print(nums)
print(nums2)
print(type(nums))
print(len(nums))

#no duplicate allowed
nums = {1,2,2,3}
print(nums)


# true is a dupe of 1, false is a dupe of zero
nums = {1,True ,2 ,False, 3, 4 ,0}
print(nums)

#check if a value is in a set 
print(2 in nums)

# but you cannot refer to an element in the set with an index position ora key


#add a new element to a set 
nums.add(8)
print(nums)

# add  element from one set to another
morenums = {5,6,7}
nums.update(morenums)
print(nums)

#you can use update with lists,tuples,and dictionaries, too .
 
 # merge two sets to create a new set
one = {1,2,3}
two = {4,5,6}

mynewset = one.union(two)
print(mynewset)

 # keep only the duolicates
one = {1,2,3}
two = {2,3,4}

one.intersection_update(two)
print(one)

 # keep everything except the duplicates
one = {1,2,3}
two = {2,3,4}

one.symmetric_difference_update(two)
print(one)
