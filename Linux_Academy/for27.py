for number in range(1, 11):
    if number % 2 > 0:
        print number    


for number in range(1,11):
    if number == 5:
        print "I have counted to %s" % number
        break

for number in range(1,11):
    if number == 5:
        print "I have counted to %s" % number
else:
    print "I have counted from 1 to 10"
