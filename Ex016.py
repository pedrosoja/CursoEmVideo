#####################################################
##Curso em Vídeo
##Aula 016 - Quebrando um número
##https://youtu.be/-iSbDpl5Jhw
#####################################################
print('Qual a porção inteira de um número?')
n = float(input('Digite um valor: '))
#print('O valor digitado foi {} e a sua porção inteira é {}'.format(n, int(n)))
#import math
#print('O valor digitado foi {} e a sua porção inteira é {}'.format(n, math.trunc(n)))
from math import trunc
print('O valor digitado foi {} e a sua porção inteira é {}'.format(n, trunc(n)))