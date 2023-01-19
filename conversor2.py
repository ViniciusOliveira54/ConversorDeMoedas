# IHHX8rCReeK5nGqU1g9akAODLop9Xvfl
import requests

moeda = input (' Moeda que deseja converter : ').upper()
convertor = input (' Para qual : ').upper()
valor = input ('Valor : ')

url = f"https://api.apilayer.com/currency_data/convert?to={moeda}&from={convertor}&amount={valor}"

headers= {
  "apikey": "IHHX8rCReeK5nGqU1g9akAODLop9Xvfl"
}

response = requests.request("GET", url, headers=headers )

# converte o resultado para json e acessa a propriedade result
print (response.json()["result"])
