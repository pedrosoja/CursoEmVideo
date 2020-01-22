#####################################################
##Curso em Vídeo
##Aula 014 - Conversor de Temperaturas
##https://youtu.be/9l_Gay8BuAw
#####################################################
print('Qual o valor da temperatura de °C em °F?')
celsius = float(input('Informe a temperatura em °C: '))
fahrenheit = (celsius * 9 / 5) + 32
print('A temperatura de {:.2f}°C corresponde a {:.2f}°F!'.format(celsius, fahrenheit))