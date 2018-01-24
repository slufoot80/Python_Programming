#!/usr/bin/python

import subprocess

try:
    output = subprocess.check_output(
            ['ls', 'frank.txt'],
            stderr=subprocess.STDOUT
            )
except OSError as err:
    print("Caught OSError")
except subprocess.CalledProcessError as err:
    print("Caught CalledProcessError")
    output = err

print(output)

