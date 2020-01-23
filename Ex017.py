#####################################################
##Curso em Vídeo
##Aula 017 - Catetos e Hipotenusa
##https://youtu.be/vmPW9iWsYkY
#####################################################
from math import hypot
print('Trigonometria - Vamos calcular a hipotenusa?')
co = float(input('Informe o comprimento do cateto oposto: '))
ca = float(input('Informe o comprimento do cateto adjacente: '))
#h = pow((co**2 + ca**2), (1/2))
##h = (co**2 + ca**2) ** (1/2)
h = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(h))