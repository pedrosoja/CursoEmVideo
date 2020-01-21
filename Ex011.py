#####################################################
##Curso em Vídeo
##Aula 011 - Pintando Parede
##https://youtu.be/mzSJpn9ldt4
#####################################################
print('Qual a metragem quadrada da parede?')
largura = float(input('Informe a largura da parede: '))
altura = float(input('Informe a altura da parede: '))
área = largura*altura
print('Sua parede tem a dimensão de {:.2f}x{:.2f} e sua área é de {:.2f}m2.'.format(largura, altura, área))
tinta = área / 2
print('Para pintar essa parede, será necessário {}l de tinta.'.format(tinta))