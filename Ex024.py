#####################################################
##Curso em Vídeo
##Aula 024 - Verificando as primeiras letras de um texto
##https://youtu.be/QroT8cZMRnc
#####################################################
cidade = str(input('Em que cidade você nasceu? ')).strip()
#Considere se a cidade começa com SANTO
print(cidade[0:5].upper() == 'SANTO')