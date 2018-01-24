from os import getenv
from math import pi

digits = getenv("DIGITS") or 48 
print("%.*f" % (int(digits), pi))
