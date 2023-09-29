# numreverse
Number reversal

1- num stores the original number provided by the user.
2- reversed_num is used to store the reversed number, initialized to 0.
3- The while loop continues until the original number (num) becomes 0.
4- In each iteration of the loop, the last digit of the original number is extracted using the modulus operator (%).
5- The extracted digit is added to the reversed_num variable after multiplying it by 10 (shifting the digits to the left) and adding the extracted digit.
6- The last digit is removed from the original number using integer division (//).
7- The loop continues until all digits are processed, and the reversed number is then printed.
