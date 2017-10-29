#This is from the Lists, Strings problem set.

#Problem 10: Write a function that combines two lists by alternatingly taking elements, e.g. [a,b,c],[1,2,3] --> [a,1,b,2,c,3].
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
        Response2 = raw_input("Insert elements here to add to your previous list in an alternating fashion. Type 'Done' when Done: ")
        if Response == "Done":
                z = [None]*(len(y)+len(x))
                z[0::2] = y
                z[1::2] = x
                print "This is your new list: " + str(z)
                break
        else:
                x.append(Response2)
