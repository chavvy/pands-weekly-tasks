#Weekly Task 04
#input a positive integer
#if the number is odd, multiply by 3 and add 1
#if the number is even, divide by 2
#output the result

while True: #looping until a positive integer is inputted
    input_number = input("Please enter a positive integer: ")
        #checking if the inputted number is a positive integer
    if not input_number.isdigit() or int(input_number) <= 0:
        print("Error: The input must be a positive integer.")
    else:
        input_number = int(input_number) #converting the input number to an integer
        break 

#collatz conjecture part, will print number until it reaches 1
while input_number != 1:
    print(input_number, end=" ")
    #checking if the number is odd or even
    if (input_number % 2) == 0:
        input_number = (input_number // 2)
    else:
        input_number = ((3*input_number) + 1)
print(1) #printing the final 1 since its not included in the above

