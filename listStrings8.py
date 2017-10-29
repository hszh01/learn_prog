#This is from the Lists, Strings problem set.

#Problem 8: Write a function on_all that applies a function to every element of a list. Use it to print the first twenty perfect squares (a natural number nn is a perfect square if it can be written as n=m*m for some other natural number mm. 1, 4, 9, 16, 25, are the first 5)

import itertools
print "This prints out the first 20 perfect squares."
y=[]
for x in itertools.count(1):
        y.append(x**2)
        if len(y) == 20:
                print str(y).strip('[]')
                break
