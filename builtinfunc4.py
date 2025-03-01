#Write a Python program that invoke square 
#root function after specific milliseconds. 
# Sample Input:
# 25100
# 2123
# Sample Output:
# Square root of 25100 after 2123 miliseconds is 158.42979517754858

import time
import math

n=int(input())
mils=int(input())

time.sleep(mils/1000)
res=math.sqrt(n)


print("Square root of", n, "after", mils,"miliseconds is", res )