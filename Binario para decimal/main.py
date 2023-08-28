def input_usuario():
    num_binario = input('Digite um numero binario para ser convertido em decimal: ')
    return num_binario

def conversao(arr):
    resultado = []
    soma = 0

    for num in arr:
        num_int = int(num)
        soma = soma * 2 + num_int
        resultado.append(soma)
    return resultado

while True:
    try:
        num_binario = input_usuario()
        val = int(num_binario)  #falta consertar o tratamento de erro
        break
    except ValueError:
        print('ERRO: O numero digitado não é um numero binario, tente novamente.')

arr_num_binario = list(num_binario)

resultado_array = conversao(arr_num_binario)
print(resultado_array)

# def decimal_to_binary(decimal_num):
#     binary_result = ""
    
#     if decimal_num == 0:
#         return "0"
    
#     while decimal_num > 0:
#         remainder = decimal_num % 2
#         binary_result = str(remainder) + binary_result
#         decimal_num = decimal_num // 2
    
#     return binary_result

# # Example usage
# decimal_number = int(input("Enter a decimal number: "))
# binary_representation = decimal_to_binary(decimal_number)
# print(f"The binary representation of {decimal_number} is {binary_representation}")
