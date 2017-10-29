#This is from the Lists, Strings problem set.

#Problem 9: Write a function that concatenates two lists. [a,b,c],[1,2,3] --> [a,b,c,1,2,3]
x=[]
y=[]
while 1:
        Response = raw_input("Insert elements here for storage. Type 'Done' when Done: ")
        if Response == "Done":
                print "This is your list: " + str(y)
                break
        else:
                y.append(Response)
while 2:
        Response2 = raw_input("Insert elements here to add to your previous list. Type 'Done' when Done: ")
        if Response2 == "Done":
                print "This is your new list: " + str(y + x)
                break
        else:
                x.append(Response2)
