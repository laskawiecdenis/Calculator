'''Text version of calc'''
listOfOperators = ["+","-","*","/"]
#########################
def operation(n1,n2,op):
    if op == "+":
        result = n1+n2
        return result
    elif op == "-":
        result = n1-n2                      #function which calculate result
        return result
    elif op == "*":
        result = n1*n2
        return result
    elif op == "/":
        result = n1/n2
        return result


############################
while True:
    ####
    try:
        number1 = int(input("Enter a number (or a letter to exit): "))   #testing if number1 is integer type
    except ValueError:
        break
    ####
    operator = str(input("Enter an operation: "))
    while operator not in listOfOperators:              #using list to check if input contain non-valid operator
        print("Invalid Sign ¯\_ツ_/¯")
        operator = str(input("Enter an operation: "))
    ####
    number2 = input("Enter another number: ")
    while True:
        try:
            int(number2)
        except ValueError:
            #While not a valid number
            print("Its not a number")
            number2 = input("Enter another number: ")
        else:
            #While there is no errors
            break
    number2 = int(number2)
    outcome = operation(number1,number2,operator)
    print('Result: {0} \n'.format(outcome))
