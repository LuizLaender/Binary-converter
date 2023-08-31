input_binary_number = input("Enter a binary number: ")
resulting_decimal_value = 0
counter_position = 0

for current_counter_position in reversed(input_binary_number):
    binary_digit = int(current_counter_position)
    
    resulting_decimal_value += binary_digit * (2 ** counter_position)
    
    counter_position += 1

print("Decimal equivalent: ", resulting_decimal_value)
