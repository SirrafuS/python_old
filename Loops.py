# simple for loop
for number in (range(3)):
    print("attempt", number)

# simple for loop
for number in range(1, 4):
    print("attempt", number, number * ".")

# for else
# if set to true, will not get to else block and will break, otherwise will run 4 times and go to
# else, as there was no true
successful = True
for number in range(1, 5):
    print("Attempt")
    if successful:  # means if successful equals true
        print("all is good, continuing")
        break
else:
    print("attempted 4 times and failed")

# nested loops
for x in range(5):  # Outer Loop:for each value in range up to 5 (0,1,2,3,4) run for each value in range up to 3 (1,2,3)
    for y in range(1, 4):  # Inner loop (child loop)
        print(f"({x},{y})")

# ranges, arrays, strings, custom objects are iterable

count = 0  # creating count var with initial value of 0
for number in range(1, 10):  # to get range that contains even numbers 2 4 6 8
    if number % 2 == 0:  # use modulo to determine if passing value is even
        count += 1  # add 1 each time even parameter was passed (will not be added on odds)
        print(number)
print(f"We have {count} even numbers")  # formatted text to print final message after loop is done

print()
print()
print()
# PART 2
nums = [1, 2, 3, 4]
# simple loop
for num in nums:
    print(num)

# if you want to break at certain condition during the loop:
for num in nums:
    if num == 3:  # as long as thins cond is not met, loop will not print the text and will not break
        print(f"Found the number {num}, breaking...")
        break  # replace with continue to print, but continue the loop
    print(num)

# nested loop
for num in nums:
    for letter in "abc":
        print(f"{num}, {letter}")

# using range
for i in range(1, 11):  # up to but not including 11
    print(i)

print()
# While loops will keep going until certain condition is met or got a break
# while true
# ____do x unless it's not true anymore
x = 0
while x < 10:
    print(x)
    x += 1   # increments x by 1
