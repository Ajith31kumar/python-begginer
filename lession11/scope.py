name = "ajith"
count = 1





def another():
    color = "red"
    global count
    count += 1
    print(count)
    def greeting(name):
        
        print(color)

        print(name)

    greeting("ajith")

another()    
