#####################################################
##Curso em Vídeo
##Aula 012 - Calculando Descontos
##https://youtu.be/4MAmKOT9FeU
#####################################################
print('Demonstrando o valor do produto com desconto de 5%')
valor = float(input('Qual é o preço do produto? R$ '))
desconto = 0.05 #Percentual de 5% convertido para decimal
valor_com_desconto = valor * (1 - desconto)
print('O produto que custava R$ {:.2f}, na promoção com desconto de 5% vai custar R$ {:.2f}'.format(valor, valor_com_desconto))