#Weekly Task 06
#a function that gives an approximate square root of an inputted number
#uses newton method at estimating square roots
#root = 0.5 * (x + (n / x)) where x is any guess which can be assumed to be n/2

#2 variables, x and n, x will be assumed to be = n/2 for convenience
def sqrt(n):
    x = (n/2)
    #comparing the difference between x squared and the number inputted
    while abs((x * x) - n) > 0.00001: #0.00001 is used to determine accuracy
        x = (0.5 * (x + (n / x)))
    return x

#Handling the input
while True: #looping until a positive number is inputted
    number_input = input("Please enter a positive number: ")

    try: #try/except used to handle incorrect inputs
        number = float(number_input)
        if number <= 0:
            print("Error: The input must be a positive number.")
        else:
            break
    except ValueError:
        print("Error: The input must be a positive number.")

#calling the function and outputting the result
result = sqrt(number)
print("The square root of {} is approx. {:.1f}".format(number, result))
