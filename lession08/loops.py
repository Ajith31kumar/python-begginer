value = 1  # You can set the initial value to any integer

# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1



# while value <= 10:
#     value += 1
#     if value == 5:
#         continue
#     print(value)
# else:
#     print("value is now equl to" + str(value))
names = ["ajith","ashok","hari"]
# for x in names:
#       print(x)

# for x in "mississippi":
#       print(x)

# for x in names:
#     if x == "ashok":
#         break
#     print(x) 


# for x in names:
#     if x == "ashok":
#         continue
#     print(x)     

# for x in range(4):
#     print(x)


for x in range(2,4):
    print(x)

for x in range(0,101,5):
    print(x)
else:
    print("glad that\'s over")

    names = ["ajith","ashok","hari"]
    actions = ["codes","eates","sleeps"]

    # for name in names:
    #     for action in actions:
    #         print(name + " "+action+ ",")

    for action in actions:
        for name in names:
            print(name + " "+action+ ",")