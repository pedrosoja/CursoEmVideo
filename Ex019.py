#####################################################
##Curso em Vídeo
##Aula 019 - Sorteando um item na lista
##https://youtu.be/_Nk02-mfB5I
#####################################################
from random import choice
print('Vamos escolher aleatóriamente em um grupo de quatro alunos?')
a0 = str(input('Primeiro aluno: '))
a1 = str(input('Segundo aluno: '))
a2 = str(input('Terceiro aluno: '))
a3 = str(input('Quarto aluno: '))
lista = [a0, a1, a2, a3]
escolhido = choice(lista)
print('O aluno escolhido é {}'.format(escolhido))