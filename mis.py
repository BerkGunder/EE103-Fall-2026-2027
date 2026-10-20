target = 0.1
fraction = target
binary_str = "0."
current_val = 0.0
bit_value = 0.5

while abs(current_val - target) >= 0.00001:
    fraction *= 2
    bit = int(fraction)
    binary_str += str(bit)
    
    if bit == 1:
        current_val += bit_value
        
    fraction -= bit
    bit_value /= 2

print(binary_str)