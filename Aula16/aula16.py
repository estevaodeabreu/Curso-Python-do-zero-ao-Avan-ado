# enumerete

# gerando uma lista a partir de um texto
string = "o peito do pé do Pedro é preto, é preto o peito do pé do Pedro"

lista = string.split(' ')  # definido o método de separação dos elementos da lista

string2 = ','.join(string)  # junta em uma nova string os elementos da lista separados por ','

for valor1, valor2 in enumerate(lista):  #valor1 represente o indice e valor2 o valor real na lista
    pass

lista1 = ['Maria', 'Pedro', 'Paulo' , 'josé']

n1,n2,n3,n4 = lista1  #exemplo simples de desempacotamento de lista, cada elemento da lista agora esta

# em uma variavel e ainda esta na lista ao mesmo tempo.  Obs: o numero de variaveis deve ser o mesmo que
# de itens na lista ou vai gerar um erro

nome =input('Qual seu nome ?')
print(nome or 'você não digitou nada. ') # se nome for True vai printar o nome se não a mensagem













