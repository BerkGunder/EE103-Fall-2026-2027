decimal_number = int(input("Enter a decimal number "))
if decimal_number == 0:
    binary_result = "0"
else:
    remainders = ""
    while decimal_number > 0:
        remainder = decimal_number % 2
        remainders += str(remainder)
        decimal_number = decimal_number // 2
    
    binary_result = remainders[::-1]
    
print(binary_result)