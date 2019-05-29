import requests

# Criar um programa que peça que o usuário
# digite o cep dele e imprima o endereço

cep = input('Digite o seu cep: ')

response = requests.get('http://viacep.com.br/ws/{}/json/'.format(cep))

#print('Status Code', response.status_code)
#print('Texto planoStatus Code', response.text)
#print('Dicionário do Python', response.text)

data = response.json()
print(response.text)
#print('Logradouro: {}'.format(data[Logradouro]))