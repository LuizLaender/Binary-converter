def input_usuario():
    user_input = input('Digite um numero decimal para ser convertido em binario: ')
    return user_input

while True:
    try:
        val = int(input_usuario())
        break
    except ValueError:
        print('ERRO: você não digitou um numero decimal, tente novamente.')

