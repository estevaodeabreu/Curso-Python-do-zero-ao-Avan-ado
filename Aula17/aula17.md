### Entendendo o formato de uma função

x = 2                        #variaveis usadas em funcao, devem ser de escopo global ou seja, 
y = 5                        #ser chamada de fora da funcao

def funcao(a=x,b=y):         #como neste ex: onde os parametros derivam de variaveis globais
    res = a + b              # podendo tambem ser resultados de inputs do usuario
    return res

print(funcao())
