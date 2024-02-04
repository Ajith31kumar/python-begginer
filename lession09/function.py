def hello():
    print("hello world!")

hello()    

def sum(num1,num2):
    return num1 + num2

total = sum(2,4)
print(total)
    

def multiple_items(*args):
    print(args)    
    print(type(args))

multiple_items("ajith","ashok","hari")

def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))
    
mult_named_items(first = "ajith",last = "kumar")    