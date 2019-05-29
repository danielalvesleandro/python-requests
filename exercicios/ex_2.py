import requests

# Criar um programa que lista todos os usuarios da api

user_id = None

API_URL = 'https://gen-net.herokuapp.com/api/users'

response = requests.get(API_URL)

users = response.json()
for u in users:
    print(u)
    
# Criar um programa que ajude o usuário a se cadastrar
# Verificar o status da requisição

response = requests.post(API_URL, json={
    'name': input('Digite o nome a cadastrar: '),
    'email': input('Digite seu e-mail: '),
    'password': input('Digite sua senha: ')
})

if response.status_code == 200:
    user_id = response.json()['id']
    print('Usuário cadastrado com sucesso. ID do usuário: {}'.format(user_id))
else:
    print('Erro ao cadastrar')

response = requests.get(API_URL) + '/{}'.format(user_id))
print(response.json())

response = requests.put(API_URL + '/{}'.format(user_id, json={
    'email': 'test_' + user_id + '@test.com'
})

if response.status_code == 200:
    print(response.json())

response = requests.post(API_URL + '/auth', {
    'email': new_email,
    'password': password
})

print(response.status_code)