#####################################################
##Curso em Vídeo
##Aula 015 - Aluguel de Carros
##https://youtu.be/I4NYUeetLAc
#####################################################
print('Considerando o valor de R$ 60,00 por dia e R$ 0,15 por Km rodado')
print('Quanto custa o aluguel de carro?')
tempo = int(input('Quantos dias alugados?'))
distância = float(input('Quantos km rodado?'))
valor = (tempo * 60) + (distância * 0.15)
print('O total a pagar é de R$ {:.2f}'.format(valor))