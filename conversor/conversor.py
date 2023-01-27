

'''import requests

response = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
print ( response )'''


R = int(input (' Quantos reais você quer converter ? '))
moeda = input(str( 'converter para qual moeda ?'))
if moeda == 'dolar':
    valor = R/5.11
    print (' o valor dá : {:.2f} ' .format(valor))
elif moeda == 'euro':   
    valor = R/5.60
    print ( ' o valor dá : {:.2f}' .format(valor))
else:
    print ( ' não conheço essa moeda ainda! ')