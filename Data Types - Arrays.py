# bytes - any positive integer between 0-255
byte_list = [13, 20, 24, 29, 30]
print(type(byte_list))
byte_num = bytes(byte_list)
print(type(byte_num))
# Lists - square brackets, values separated with comma, can have any values inside
letters = ["a", "b", "c", "d", "e"]
# lists in lists
matrix = [[0, 1], [2, 3]]
# if you need multiple of same values in the list you can use this
zeros = ["t"] * 30
print(zeros)
# you can concatenate lists as well
combined = zeros + letters
print(combined)
# list() function accepts iterables
# range function gives range up to mentioned number (but not included)
numbers = list(range(20))
print(numbers)
# lists are also iterable so you can use it in list function as well
characters = list('Hello World')
print(characters)
# to see how many chars are there
print(len(characters))
# using square brackets you can call certain values in lists as well as modify them

letters = ["a", "b", "c", "d", "e"]
# print first value
print(letters[0])
# and the last value
print(letters[-1])
# replace values using index
letters[0] = 'A'
print(letters)
# slicing leaves original list intact but returns only part of it, 0 is assumed by default
# up to but included 3
print(letters[:3])
# from pre last to NOT included 4
print(letters[-2:4])
# you can specify steps as well
print(letters[::2])
numbers = list(range(20))
# will print every third value including first one
print(numbers[::3])
# step -1 means return all but in reverse order
print(numbers[::-1])

# list unpacking creates values with mentioned var names one by one using given list
# number of vars should be equal to amount of values

nums = [1, 2, 3]
first, second, third = nums
print(first, second, third)
# sometimes you don't need all the values from list except few
more_nums = [1, 2, 3, 4, 4, 4, 4]
first, second, *others = more_nums
print(first, second, others)
# note that class of others is still a list
print(type(first))
print(type(others))
# in general when we prefix asterisk in start of parameter python will take arbitrary number of args and pack into list
# we can use *others in other places as well:
more_nums = [1, 2, 3, 4, 4, 4, 9]
first, *others, last = more_nums
print(first, last, others)

# Looping over lists
# enumerate just gives index numbers for each value in lists
letters = ["a", "b", "c", "d", "e"]
for letter in enumerate(letters):
    print(letter)
    # to get the indexes themselves
    print(letter[0], letters[1])

# more elegant way of getting and printing indexes using unpacking
letters = ["a", "b", "c"]
# as enumerate adds another value, we can use unpacking to show index and letter without adding []
for index, letter in enumerate(letters):
    print(index, letter)
# adding items
# everything in python is an object & you can use individual functions or methods to add or remove items to that object
# when the function is part of an object it is called method
# insert method has index position as well

letters.append("d")
letters.insert(0, "_")
print(letters)

# removal
# without index mentioned pop will remove and return the last one
letters.pop()
print(letters)

# if you don't know the index, but know the value use remove, which will remove first appearance of mentioned b
letters.remove("b")
print(letters)

# you can also delete items using delete statement, which accepts ranges as well:
del letters[0:3]
print(letters)
# finding index in list
letters = ["a", "b", "c"]
print(letters.index("a"))
# when you trying to get non existent value in list it return error unlike C based languages where you get -1
# print(letters.index("d"))
# you can avoid error using the if statement
if "d" in letters:
    print(letters.index("d"))
# counting matched items in list
print(letters.count("d"))

# Tuples
# read only lists, with parenthesis (), immutable
coordinates = (4, 5)
# indexes work in the same way as for lists, you just can't change it's values
print(coordinates[0])
# coordinates[0] = '8' will return Tuples do not support item assignment

# Dictionaries are key value pairs key is the identifier for data and value is the data itself
# keys should be immutable type(usually int or str), values can be anything
# if you call a non-existing key, it will not give any error, but will not read code after
# uses {}

student = {"name": "John", "Age": 18, "courses": ["math", "french"], 1: "for int key"}
print(student["name"])
print(student["courses"])
print(student[1])

# if you want none in return for non existent ones, use get method
print(student.get('phone'))
# or you can specify what to return if not found after comma
print(student.get('phone', "not found"))
# you can add value to dict if you want:
student["phone"] = '555-55555'
print(student.get('phone'))
# if key is already there, value will be updated:
student["phone"] = '666-55555'
print(student.get('phone'))
# same can be done using update, even for multiple values at a time. Update method takes dict as an argument
print(student)
student.update({'name': 'Sins', "Age": 20, "middle name": "Carlton"})
print(student)
# you can remove the values using del
del student["Age"]
print(student)
# pop method removes value and returns it
middle_name = student.pop('middle name')
print(middle_name)
# get the amount of items in dict
print(len(student))
# get only keys, values, items
print(student.keys())
print(student.values())
print(student.items())
# without specifying method, loop will go through keys only, so if you want all of the values as well use items method
for key, value in student.items():
    print(key, value)
# Sets is collection with no duplicates, uses curly braces, Sets are unordered so you can't use indexes
# you can remove duplicates from list converting it to set
nums = [1, 2, 3, 4, 4, 4, 4]
uniques = set(nums)
print(nums)
print(uniques)
nums2 = {1, 2, 3}
nums2.add(4)
nums2.remove(2)
len(nums2)
print(nums2)

nums1 = {1, 2, 3, 4, 5}
nums2 = {5, 6, 7, 8}
# we can unite multiple sets and show all the items there are either in 1 or another set. Not that 5 is shown once only
print(nums1 | nums2)
# you can return all values in all sets with & operator
print(nums1 & nums2)
# get the difference between 2 or more sets
print(nums1 - nums2)
# get values that have no duplicates in all sets
print(nums1 ^ nums2)

# Range provides mentioned range up to but not included, by default step is 1
# ranges work only with int and not with floats
results = range(0, 11)
# by default range return object that is class range object
print(type(results))
# if you want to see values in list you should use function list
print(list(results))

# ranges can be used without start parameter. python assumes it's 0 in those cases
results2 = range(11)
print(list(results2))
# you can change the step as well
results3 = range(1, 11, 3)
print(list(results3))
# we can use negative numbers, and step -1 goes backwards
results4 = range(5, -6, -1)
print(list(results4))
# task - print 3, 6, 9, 12, 15, 18, 21, 24, 27, 30
task = range(3, 31, 3)
print(list(task))