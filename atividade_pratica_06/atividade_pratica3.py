"""
Atividade Prática 06
Aluna: Airan Rejane
Escola da Nuvem - Aulas técnicas do curso Fundamentos de AWS

Exercício 3

Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário, 
utilizando a API ViaCEP. O programa deve exibir o logradouro, bairro, cidade e estado correspondentes 
ao CEP consultado.​
"""

import requests

def consultar_cep():
    print("Consulta de endereço por CEP\n")

    cep = input("Digite o CEP (somente números): ").strip()

    try:
        response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        dados = response.json()

        if "erro" in dados:
            print("CEP não encontrado.")
        else:
            print(f"\nLogradouro: {dados['logradouro']}.")
            print(f"Bairro: {dados['bairro']}.")
            print(f"Cidade: {dados['localidade']}.")
            print(f"Estado: {dados['uf']}.\n")

    except Exception as e:
        print("Erro ao consultar o CEP:", e)

consultar_cep()