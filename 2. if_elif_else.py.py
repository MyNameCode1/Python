"""
Wtite a Python code using If, Elif And Else statement.
where a code takes a argument and if the argument matches then code will proceed or else code will show different opuput

in this code 
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
"""
#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    
if n % 2 != 0:
    print("Weird")
    
elif n % 2 == 0 and (n > 2 and n < 5):
    print("Not Weird")
    
elif n % 2 == 0 and (n > 6 and n <= 20):
    print("Weird")
    
elif n % 2 == 0 and (n > 20):
    print("Not Weird")
