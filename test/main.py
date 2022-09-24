# import secondary
# from secondary import var2
# from secondary import * #don't do this
# from example import * #don't do this

from secondary import var2
from example import var2 as value2

var1 = 10

def func1():
    print('Привет, мир!')


print(var2)

print(value2)

