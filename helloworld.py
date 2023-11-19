# Problem: Calculate the Factorial
def calculate_factorial(n):
    # Your code here
    if n ==0 or n ==1:
        return 1
    else:
         return n *calculate_factorial(n-1)
    pass
# Test cases
print(calculate_factorial(0))  # Expected output: 1
print(calculate_factorial(5))  # Expected output: 120
print(calculate_factorial(7))  # Expected output: 5040




# Problem: Greeting
def greet(name):
    # Your code here
    print("Hello,", name, "!")
    pass

# Test cases
greet("Alice")  # Expected output: Hello, Alice!
greet("Bob")    # Expected output: Hello, Bob!
greet("Charlie")# Expected output: Hello, Charlie!



# Problem: Palindrome Check
def is_palindrome(word):
    # Your code here
    processedWord = "".join(word.split()).lower()
    reversedWord = processedWord[::-1]
    if reversedWord == processedWord:
        return True
    else:
        return False
    pass

# Test cases
print(is_palindrome("radar"))    # Expected output: True
print(is_palindrome("level"))    # Expected output: True
print(is_palindrome("Python"))   # Expected output: False
print(is_palindrome("A man a plan a canal Panama"))  # Expected output: True






# # Problem: Print the Multiplication Tabler

# # Get input from the user for an integer
# number = int(input("Enter an integer: "))

# # Print the multiplication table up to 10
# # Your code here
# for i in range(1,11):
#     print(f'{number} x {i} = {number * i}')







# Problem: Calculate the Sum of First N Natural Numbers
# Get input from the user for a positive integer
n = int(input("Enter a positive integer (N): "))

# Calculate the sum of the first N natural numbers
# Your code here
sum_of_natural_numbers= 0
for i in range(1, n+1):
    sum_of_natural_numbers += i
# Print the result
print(f"The sum of the first {n} natural numbers is: {sum_of_natural_numbers}")







# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old. 
name = input('Please Enter you name: ')
age = int(input('Please Enter you age: '))

toHundred = 100-age


print(f'Hello {name}. You will turn 100 years old in {toHundred} years.')