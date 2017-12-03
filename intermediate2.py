#Problem 2 from Intermediate Problem Set

import re
days = raw_input("Insert amount of days per year: ")
a = re.split(r'\.+', days)
b = max(a[1:2])
c = float("0." + str(b))
d = 1.0/c
print str(d) + " years until the next leap year."
