#This is from the Lists, Strings problem set.

#Problem 6: Write a function that tests whether a string is a palindrome.
Response = raw_input("Insert a string to see if it is a palindrome: ")
if str(Response)[::-1] == str(Response):
        print "Yes, " + Response  + " is a palindrome."
else:
        print "No, " + Response + " is not a palindrome."
