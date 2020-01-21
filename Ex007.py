#####################################################
##Curso em Vídeo
##Aula 007 - Média Aritmética
##https://youtu.be/_QfISzy0IKs
#####################################################
print('Vamos descobrir sua média anual?')
n1 = float(input('Insira a nota do primeiro bimestre: ')) 
n2 = float(input('Insira a nota do segundo bimestre: '))
n3 = float(input('Insira a nota do terceiro bimestre: '))
n4 = float(input('Insira a nota do último bimestre: '))
média = (n1 + n2 + n3 + n4) / 4
print('A média entre {:.1f}, {:.1f}, {:.1f} e {:.1f} é igual a {:.1f}'.format(n1, n2, n3, n4, média))