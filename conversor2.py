# IHHX8rCReeK5nGqU1g9akAODLop9Xvfl
import requests

moeda = input (' moeda que deseja converter : ').upper()
convertor = input (' para qual : ').upper()
valor = input ('valor : ')

url = f"https://api.apilayer.com/currency_data/convert?to={moeda}&from={convertor}&amount={valor}"

headers= {
  "apikey": "IHHX8rCReeK5nGqU1g9akAODLop9Xvfl"
}

response = requests.request("GET", url, headers=headers )


print (response.json()["result"])
