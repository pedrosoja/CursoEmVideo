#####################################################
##Curso em Vídeo
##Aula 013 - Reajuste Salarial
##https://youtu.be/cTkivN8XcJ0
#####################################################
print('Calculando o reajuste salarial de um funcionário')
salario_atual = float(input('Qual é o salário do funcionário? R$ '))
aumento_percentual = 15 / 100 #Representação matemática de 15%
salario_novo = salario_atual * (1 + aumento_percentual)
print('Um funcionário que ganhava R$ {:.2f}, com 15% de aumento, passa a receber R$ {:.2f}'.format(salario_atual, salario_novo))