nome = 'Estevão'
idade = 32
altura = 1.79
run = True
peso = 92

imc = peso / altura ** 2

print(nome,'seu IMC é :', imc)

print(nome ,'seu IMC é {} :'.format(imc))

print(f'{nome}seu IMC é: {imc:.2f}')

print('{} seu IMC é: {:.2f}'.format(nome,imc))

print('{n} seu IMC é: {im}'.format(n=nome,im=imc))

print('{im} seu IMC é: {n}'.format(n=nome,im=imc))