##### Formatação de string

nome = 'Estevão'
idade = 32
altura = 1.79
run = True
peso = 92   
 
imc = peso / altura ** 2 

print(nome,'seu IMC é :', imc)                            forma mais comum de um iniciante escrever

print(nome ,'seu IMC é {} :'.format(imc))                 mantendo nome e formatando imc

print(f'{nome}'seu IMC é :'{imc:.2f})                     formatando nome e imc nas chaves

print(f'{nome}seu IMC é: {imc:.2f}')                      com format no inicio e as variaveis nas chaves

print('{} seu IMC é: {:.2f}'.format(nome,imc))            determinando o format por ordem de precedencia

print('{n} seu IMC é: {im}'.format(n=nome,im=imc))        nomeando as chaves

print('{im} seu IMC é: {n}'.format(n=nome,im=imc))        podemos inverter a ordem