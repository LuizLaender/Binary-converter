def decimal_to_binary(decimal_num):
    binary_result = ""
    
    if decimal_num == 0:
        return "0"
    
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_result = str(remainder) + binary_result
        decimal_num = decimal_num // 2
    
    return binary_result

# Example usage
decimal_number = int(input("Enter a decimal number: "))
binary_representation = decimal_to_binary(decimal_number)
print(f"The binary representation of {decimal_number} is {binary_representation}")
