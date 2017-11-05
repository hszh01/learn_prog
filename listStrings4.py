#This is from the Lists, Strings problem set.

#Problem 4: Write a function that returns the elements on odd positions in a list.
y=[]
while 1:
        Response = raw_input("Insert elements here to find the odd positions in the list. Type 'Done' when Done: ")
        if Response == "Done":
                z = y[0::2]
                print z
                break
        else:
                y.append(Response)
