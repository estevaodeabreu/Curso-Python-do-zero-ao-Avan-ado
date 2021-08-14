

#### Formatando valores com modificadores:


:s -        Texto (string)

:d -        Interos (int)

:f -        Numero de ponto flutuante (float)

:.n°:f -    Quantidade de caracteres decimais (float) :.1f

:(caracter)(> ou > ou ^)(Quantidade) (tipo -s, d ou f)
> - adiciona a esquerda
< - adiciona a direita
^ - adiciona no centro

ex: nun = 1
print(f'{nun:0>10}')  

A saída será:  0000000001 
ou seja, o resultado de nun com 10 posições
incluindo o valor do proprio num e 
foi determinado que as posições seriam preenchidas por zero neste caso

Outro exemplo seria com string:

nome = 'Estevão'

print(f'{nome:*^13}') neste caso a saída sera: Estevâo com 3 * de cada lado
para que junto com as 7 letras do nome feche as 13 posições

