#This is from the Lists, Strings problem set.

#Problem 5: Write a function that computes the running total of a list.
y=[]
runningTotal = 0
while 1:
        Response = raw_input("Insert elements here to find the running total of the list. Type 'Done' when Done: ")
        if Response == "Done":
                for x in range(0, len(y)):
                        runningTotal = int(runningTotal) + int(y[x])
                print runningTotal
                break
        else:
                y.append(Response)
