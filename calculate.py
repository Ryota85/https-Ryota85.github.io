operation = input('''
Please type in math operation you would like to complete:
+ for Addition
- for substraction
* for multiplication
/ for division
''')
number_1 = int(input('Enter your first number:'))
number_2 = int(input('Enter your second number:'))
if operation== '+':
    print('{}+{}='.format(number_1,number_2))
    print(number_1+number_2)
elif operation== '-':
    print('{}-{}='.format(number_1,number_2))
    print(number_1-number_2)
elif operation== '*':
    print('{}*{}='.format(number_1,number_2))
    print(number_1*number_2)
elif operation== '/':
    print('{}/{}='.format(number_1,number_2))
    print(number_1/number_2)
else:
    print('You have not typed a valid operator, please run the program again')

def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for No.
''')
    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()

def welcome():
    print('''
Welcome to calculator
''')
welcome()
