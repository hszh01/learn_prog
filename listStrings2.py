#This is from the Lists, Strings problem set.

#Problem 2: Write a function that reverses a list, preferably in place.
y=[]
while 1:
        Response = raw_input("Insert elements here to reverse the order. Type 'Done' when Done: ")
        if Response == "Done":
                y.reverse()
                print y
                break
        else:
                y.append(Response)
