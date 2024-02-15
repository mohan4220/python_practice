"""
Exception handling -> handling errors
"""

"""
try:
    #run this block of code

except <Exception1>:
    #run this code if error comes
 .
 .
 .
finally:
    #run this code always, with or without exceptions.
    
"""
a = 23
b = 2
c = 0

try:
    c = a / b

except ZeroDivisionError as err:
    print(err)
    c = a / 1
except TypeError as err:
    print(err)
    c = a / int(b)

finally:
    c = c + 100

print(c)
print("done")
