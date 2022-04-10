"""
LEGB - is the order python checks vars
Local - Variables defined within the function
Enclosing - only exists in nested functions
Global - top-most scope in a python program, script or module
Built-in
"""

# global vars, within the main body of code

x = 'global_x'


def test():
    y = 'local_y'
    print(x)


test()  # will print global x as it will not find anything X locally in function test, or enclosing scope
print(x)


# also print y will return error as it's set only locally in the function, even if the print comes after functions runs
def test():
    x = 'local_x'
    print(x)


test()  # will print local x as it indeed was found when test function was called
print(x)

print()


# However if we set x as global var inside of function in both cases that one will run on print as it is defined after
# regular one
def test():
    global x
    x = 'local_x'
    print(x)


test()  # will print x inside of the function in both cases as it was set to global
print(x)


def test(z):
    x = 'local_x'
    print(z)


test("local_z")  # will work as it checks it's local z and gets value local z, but you can't print that z outside of fun

# built in ones are the ones that are pre assigned
m = min([5, 3, 2, 6, 1])
print(m)

import builtins
# to  list all attributes of the given object use dir
print(dir(builtins))

# if you set some function with matching built in name python will overwrite it and check it first because of order

# Enclosing scope - will print both inner and outer x because of LEGB
# first it checks if there is local var x to print when call inner() is executed and because there is local, it runs it
# after that in prints x from outer function which is ENCLOSING one for it (E in lEgb)
x = 'global x'
def outer():
    x = 'outer x' # if we comment this one, global one will be printed instead

    def inner():
        # nonlocal x   - if we set this and comment global one, this will run for both inner and outer
        x = 'inner x'  # if we print this one enclosing one will be printed instead
        print(x)
    inner()
    print(x)

outer()
print(x)