#####################################################
##Curso em Vídeo
##Aula 018 - Seno, Cosseno e Tangente
##https://youtu.be/9GvsphwW26k
#####################################################
from math import radians, sin,cos, tan
print('Trigonometria - Seno, Cosseno e Tangente?')
ang = float(input('Digite o ângulo que você deseja: '))
print('O ângulo de {:.1f} tem o SENO de {:.2f}'.format(ang, sin(radians(ang))))
print('O ângulo de {:.1f} tem o COSSENO de {:.2f}'.format(ang, cos(radians(ang))))
print('O ângulo de {:.1f} tem o TANGENTE de {:.2f}'.format(ang, tan(radians(ang))))