# This function calculates exponential given an integer.
def calculateExponential(exponential):
    power =1 
    for i in range (1,exponential+1):
        power *= 2
        print(f'{i} exponential steps are equal to {power} linear steps.')


try:
    userInput = int(input('Please input a number: '))
    calculateExponential(userInput)
except:
    print('Wrong input: You were supposed to enter a number between 1 and 100. Try again.')