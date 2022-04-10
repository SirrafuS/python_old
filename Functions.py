# functions are used to "group" one part of program and call it with different arguments and values
# functions start with def keyword
# when function is called with it's name, block inside of function is executed and after that control of a program
# goes back to the function call and next statement after function call is executed
# values passed to function is called arguments
def greet(name):  # define function greet, that accepts one mandatory argument name. It can be used inside of function
    print(f"Hello {name}")
    print(f"whazzabi {name}?")

greet("artur")
print("test")

def add_numbers(n1, n2):
    result = n1 + n2
    print(f"The sum equals {result}")

number1 = 10.3
number2 = 8.4
add_numbers(number1, number2)

# Above version is working fine but it's better to just calculate inside function but print the result somewhere else
# return terminates function and control goes back to the place where function is called

def add_numbers2 (n1, n2):
    result = n1 + n2
    return result

total = add_numbers2(number1, number2)
print ("The Sum is", total)

# finding Grade based on average mark of a student

def find_av_mark(marks):
    sum_of_mark = sum(marks)
    total_items = len(marks)
    average_mark = sum_of_mark / total_items
    return average_mark

marks = [79,80,85,75,100]
average_mark = find_av_mark(marks)
print("Your average mark is: ", average_mark)

def compute_grade(average_mark):
    if average_mark >= 80:
        grade = 'A'
    elif average_mark >= 70:
        grade = 'B'
    elif average_mark >= 60:
        grade = 'C'
    else:
        grade = 'F'
    return grade

grade = compute_grade(average_mark)
print("Your grade is: ", grade)

# Task
def add_nums(n1, n2):
    result = n1 + n2
    return result
add_result = add_nums(5.9, 10.5)
print("result for addition equals ", add_result)

def multiply_nums(n1, n2):
    result = n1 * n2
    return result
mult_result = multiply_nums (5.9, 10.5)
print("result for multiplication equals ", mult_result)


# lexical scoping is a convention that sets the scope of a variable so that it may only be called
# within the block of code in which it is defined. Scopes can be nested inside another

