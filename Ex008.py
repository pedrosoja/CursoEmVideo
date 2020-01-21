#####################################################
##Curso em Vídeo
##Aula 008 - Conversor de Medidas
##https://youtu.be/KjcdG05EAZc
#####################################################
print('Convertendo distância')
medida = float(input('Informe uma distância em metros:'))
print('A medida de {:.0f}m corresponde a'.format(medida))
print('Em Km = {:.3f} Km'.format(medida/1000))
print('Em hm = {:.3f} hm'.format(medida/100))
print('Em dam = {:.3f} dam'.format(medida/10))
print('Em m = {:.3f} m'.format(medida/1))
print('Em dm = {:.3f} dm'.format(medida*10))
print('Em cm = {:.3f} cm'.format(medida*100))
print('Em mm = {:.3f} mm'.format(medida*1000))