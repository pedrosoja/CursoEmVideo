#####################################################
##Curso em Vídeo
##Aula 010 - Conversor de Moedas
##https://youtu.be/xM4AX3Lp2mo
#####################################################
import requests
from datetime import datetime, timedelta
real = float(input('Quanto dinheiro você tem na carteira? : R$ '))
yesterday = datetime.strftime(datetime.now() - timedelta(1), '%m-%d-%Y')
req = requests.get("https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoMoedaDia(moeda=@moeda,dataCotacao=@dataCotacao)?@moeda='USD'&@dataCotacao='" + yesterday + "'&$top=100&$filter=tipoBoletim%20eq%20'Fechamento%20PTAX'&$format=json&$select=cotacaoVenda,dataHoraCotacao,tipoBoletim")
cotação = req.json()
cotação_valor = cotação['value']
tx_conversão = float(cotação_valor[0]['cotacaoVenda'])
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, (real*tx_conversão)))