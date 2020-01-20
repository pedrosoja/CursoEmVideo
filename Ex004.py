#####################################################
##Curso em Vídeo
##Aula 004 - Dissecando uma Variável
##https://youtu.be/tHYxjJxtJko
#####################################################
print('Vamos descobrir qual o tipo da variável que você está informando?')
a = input('Digite algo: ')
print('O tipo primitivo é ', type(a))
print('Tem espaço? ', a.isspace())
print('É número? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('Está em maiúsculas? ', a.isupper())
print('Está em minúsculo?', a.islower())
print('Está capitalizada? ', a.istitle())