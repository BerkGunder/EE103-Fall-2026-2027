fraction = float(input("Enter a fraction number "))
binary_fraction = "0."

while fraction > 0:
    fraction *= 2
    integer_part = int(fraction)
    binary_fraction += str(integer_part)
    fraction -= integer_part
    
print(binary_fraction)