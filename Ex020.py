#####################################################
##Curso em Vídeo
##Aula 020 - Sorteando uma ordem na lista
##https://youtu.be/OPh0nngbBSY
#####################################################
from random import shuffle
print('Vamos ordenar os alunos?')
a0 = str(input('Primeiro aluno: '))
a1 = str(input('Segundo aluno: '))
a2 = str(input('Terceiro aluno: '))
a3 = str(input('Quarto aluno: '))
lista = [a0, a1, a2, a3]
shuffle(lista)
print('A ordem de apresentação será')
print(lista)