import requests

# Criar um programa que lista todos os usuarios da api

user_id = None

API_URL = 'https://gen-net.herokuapp.com/api/users'

# response = requests.get(API_URL)

# users = response.json()
# for u in users:
#     print(u)
    
# Criar um programa que ajude o usuário a se cadastrar
# Verificar o status da requisição

response = requests.put(API_URL, json={
    'name': input('Digite o nome a cadastrar: '),
    'email': input('Digite seu e-mail: '),
    'password': input('Digite sua senha: ')
})

if response.status_code == 200:
    user_id = response.json()['id']
    print('Usuário cadastrado com sucesso. ID do usuário: {}'.format(user_id))
else:
    print('Erro ao cadastrar')


