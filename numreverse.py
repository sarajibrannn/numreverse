# Taking user input for the number to be reversed
num = int(input("Enter a number: "))

# Initializing a variable to store the reversed number
reversed_num = 0

# Loop to reverse the number
while num > 0:
    # Extracting the last digit of the number
    digit = num % 10
    # Adding the digit to the reversed number (multiplying the current reversed number by 10 and then adding the digit)
    reversed_num = reversed_num * 10 + digit
    # Removing the last digit from the original number
    num = num // 10

# Displaying the reversed number
print("Reversed number:", reversed_num)
