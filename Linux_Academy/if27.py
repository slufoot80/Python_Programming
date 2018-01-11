import platform
import random
platform.linux_distribution()
sys_info = ' '.join(platform.linux_distribution())
print(sys_info)

if "openSUSE" in sys_info:
    print("You are running OpenSuse Leap 42.2 x86 64bit")
elif "Ubuntu" in sys_info:
    print "Debian OS"
else:
    print "Unknown OS"


test_score = random.randint(59,100)
if test_score >= 97:
    print "A+"
elif test_score >= 93 and test_score <= 96:
    print "A"
elif test_score >= 90 and test_score <= 92:
    print "A-"
elif test_score >= 87 and test_score <= 89:
    print "B+"
elif test_score >= 83 and test_score <= 86:
    print "B"
elif test_score >= 80 and test_score <= 82:
    print "B-"
elif test_score >= 77 and test_score <= 79:
    print "C+"
elif test_score >= 73 and test_score <= 76:
    print "C"
elif test_score >= 70 and test_score <= 72:
    print "C-"
elif test_score >= 67 and test_score <= 69:
    print "D+"
elif test_score >= 63 and test_score <= 66:
    print "D"
elif test_score >= 60 and test_score <= 62:
    print "D-"
else:
    print "Failed"
print(test_score)
