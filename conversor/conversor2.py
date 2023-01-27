# IHHX8rCReeK5nGqU1g9akAODLop9Xvfl
import requests
with open('moedas.txt') as md:
    moedas = md.read()
    print(moedas)

moedas = moedas.replace('\n','').split(' ')


print ( moedas )

'''moeda = input (' moeda que deseja converter : ').upper()
convertor = input (' para qual : ').upper()
valor = input ('valor : ')'''

url = f"https://api.apilayer.com/currency_data/convert?to={moedas[0]}&from={moedas[2]}&amount={100}"

headers= {
  "apikey": "IHHX8rCReeK5nGqU1g9akAODLop9Xvfl"
}

response = requests.request("GET", url, headers=headers )

print (response.json()["result"])