
numero =input('Digite um numero inteiro: ')

if numero.isdigit():
    numero_int = int(numero)
    resultado = numero_int % 2
    if resultado == 0:
        print(f'O numero {numero_int}, é par')
    elif resultado == 1:
        print(f'O numero {numero_int}, é impar')
else:
    print('Não foi digitado um numero inteiro.')


