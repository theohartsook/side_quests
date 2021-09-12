import argparse
import random
from num2words import num2words

def findRandomNumbers(n, upper_limit, lower_limit=1):
    nums = []
    for i in range(0, n-1):
        current_limit = upper_limit - sum(nums) - 1
        nums.append(random.randint(lower_limit, current_limit))
    remainder = upper_limit - sum(nums)
    last_n = random.randint(lower_limit, remainder)
    nums.append(last_n)
    return(nums)

def generateEquationDisplay(nums, operator):
    if operator == '+':
        display_nums = [str(i) for i in nums]
        display_eq = ' + '.join(display_nums)
        return(display_eq)

def generateWrittenEquationDisplay(nums, operator, lg):
    if operator == '+':
        display_nums = [num2words(i, lang=lg) for i in nums]
        display_eq = ' + '.join(display_nums)
        return(display_eq)

def quizCalculation(n, upper_limit, operator, lg, lower_limit=1,):
    if lg == 'en':
        success = "Success :D"
        failure = "Failure :("
    elif lg == 'ja':
        success = "合格 :D"
        failure = "落第 :("
    else:
        success = ":D"
        failure = ":("

    nums = findRandomNumbers(n, upper_limit, lower_limit=lower_limit)
    solution = sum(nums)
    eq = generateWrittenEquationDisplay(nums, operator, lg)
    correct = False
    print(eq, '= ?\n')
    while correct != True:
        user_solution = input()
        if int(user_solution) == solution:
            print(success)
            correct = True
        else:
            print(failure)



# write command line argument for generating equation
# try out the goeey thing and see if I can make a desktop version
# write docstrings