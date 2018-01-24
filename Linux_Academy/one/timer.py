#import time
from time import localtime, strftime, mktime

start_time = time.localtime()
print("Timer Started at %s" % time.strftime("%X", start_time))

"""Wait for user input"""
raw_input("Please press Enter to continue...")

stop_time = time.localtime()
difference = time.mktime(stop_time) - time.mktime(start_time)

print("Timer stopped at %s seconds" % time.strftime("%X",stop_time))
print("Total time: %s seconds" % difference)
