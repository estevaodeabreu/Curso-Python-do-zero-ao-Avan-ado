
# Condicões:
'''
Conseito:
(não é uma tradução literal)

if ("se") usamos para que uma condição aconteça sê a condição for verdadeira
ex: if 20 > 10:

elif ("ou, se") usamos caso a função if não seja verdadeira, mas ainda seja
preciso testar uma segunda condição
ex: if 20 > 10:
    faça isso
    elif 20 < 10:
    faça aquilo

else ("se não") usamos quando nenhuma das condições anteriores forem verdadeiras
'''

x = int(input('Digite um numero entre 0 e 4: '))

if x == 1:
    print('você digitou o numero 1')
elif x == 2:
    print('Você digitou o numero 2')
elif x == 3:
    print('Você digitou o numero 3')
else:
    print('O numero digitado não está "entre" 0 e 4 ')
'''
Obs: Em python, a indenteção ira determinar o que acontece em 
cada condição, caso não tenha indentação, o programa irá dar 
erro, por não conseguir entender o que precisa ser feito como
condição.
'''