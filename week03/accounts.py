#Weekly Task 03
#reads 10 character account number input
#outputs only the last 4 digits with the first 6 replaced with x's
#have it give an error msg if the character count is != 10

account_number = input("Please enter a 10 digit account number: ")

#checking if the input length is exactly 10 characters long and are numbers
if len(account_number) != 10 or not account_number.isdigit():
    print("Error: Account number must 10 characters long and contain only digits.")
else:
    #replace first 6 digits with 'X' and keep last 4
    masked_account_number = 'X' * 6 + account_number[-4:]
    print(masked_account_number)