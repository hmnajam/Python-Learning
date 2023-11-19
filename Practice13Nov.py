# Exercise 1: Calculate the multiplication and sum of two numbers
# Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

number1 = 40
number2 = 30

calculated = number1 * number2

if calculated < 1000:
    print(calculated)

else:
    print(number1+number2)








# Exercise 2: Print the sum of the current number and the previous number
# Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.
previousNo = 0
for i in range(0, 10):
    print(f'Current number: {i}. Previous number: {previousNo}. Sum is: {i+i-previousNo}')
  #  print(f'Current number: {i}. Previous number: {i-1}. Sum is: {i+i-1}')
    previousNo = i-1




def sumofTwo(range):
    previousNo = 0
    for i in range(0, 10):
        previousNo = i
    print(f'Current number: {i}. Previous number: {i-1}. Sum is: {i+i-previousNo}')



