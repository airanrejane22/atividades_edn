"""
Atividade Prática 06
Aluna: Airan Rejane
Escola da Nuvem - Aulas técnicas do curso Fundamentos de AWS

Exercício 2

Crie um programa que gera um perfil de usuário aleatório usando a API 'Random User Generator'. 
O programa deve exibir o nome, email e país do usuário gerado."​
"""

import requests

def gerar_usuario():
    print("Gerando perfil de usuário aleatório...\n")
    
    try:
        response = requests.get("https://randomuser.me/api/")
        dados = response.json()

        user = dados['results'][0]
        nome = f"{user['name']['first']} {user['name']['last']}"
        email = user['email']
        pais = user['location']['country']

        print(f"Nome: {nome}")
        print(f"Email: {email}")
        print(f"País: {pais}\n")

    except Exception as e:
        print("Erro ao buscar dados do usuário:", e)

gerar_usuario()