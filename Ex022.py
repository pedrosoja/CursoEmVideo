#####################################################
##Curso em Vídeo
##Aula 022 - Analisador de Textos
##https://youtu.be/EQQt-6QqXOs
#####################################################
nome = str(input('Digite seu nome completo: ')).strip()
separa = nome.split()
print('Analisando seu nome...')
print('Seu nome em maiúsculo é {}'.format(nome.upper()))
print('Seu nome em minúsculo é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], nome.find(' ')))