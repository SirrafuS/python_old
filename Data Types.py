# none is like null in other programming languages
# numeric has 4 main data types:
# int
num = 2
print(type(num))
# float  2.5
num = 2.5
print(type(num))

# integers without any prefix are considered as decimal numbers
# calc https://www.rapidtables.com/convert/number/hex-dec-bin-converter.html
print(10)
# binary
print(0b10)
# octal
print(0o10)
# hexadecimal
print(0x10)
# complex
# numbers that can be expressed in the form x + yi format where a and b are real number and i is imaginary part
# which equals i² = -1. In PY j plays role of i
num = (1+3j)
print(type(num))
print(num.real)
print(num.imag)
# if we add values that are  both complex real part with add to real one and imaginary will be added to imag part
nums = (1+2j) + (2+3j)
print(nums)

# setting num to simpler number again
num = (1+3j)
print((num - 1) ** 2)
# to break this down - 1+3j-1 is 3j as 1 with -1 is 0
# now 3j**2 remains (3*j)² same as it would be for example (3*2)**2 - no difference if you multiple after or before exp.
# 3² * 2² is 9 * 4 = 36 same way as 6 * 6
# by the same logic in 3j**2 it's basically 3² which is 9 times -1 (because j is number whose sqr rt equals -1)
# so in the end we got 9*(-1) but python still keeps imaginary part as 0j that's why instead it returns 9+0j
# you can convert types as well
a = 4.3
b = int(a)
print(b)  # will return 4
c = float(b)
print(c)  # will return 4.0
e = complex(b)
print(e)    # will return 4+0j
f = complex(b, c)
print(f)    # will return 4+4j, float part is ignored
# bool only have 2 possible values either true or false
boolean = a > c
print(boolean)
# boolean is considered numeric type so if you convert true to int will get 1 and false will give 0
# strings are text types of python values. even single letter is string
string_var = 'n'
print(type(string_var))


