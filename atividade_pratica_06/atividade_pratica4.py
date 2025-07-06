"""
Atividade Prática 06
Aluna: Airan Rejane
Escola da Nuvem - Aulas técnicas do curso Fundamentos de AWS


Exercício 4

Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL). 
O usuário deve informar o código da moeda desejada (ex: USD, EUR, GBP), e o programa deve exibir o valor atual, 
máximo e mínimo da cotação, além da data e hora da última atualização. Utilize a API da AwesomeAPI 
para obter os dados de cotação.​​"""


import requests

def consultar_cotacao():
    print("Cotação de moeda estrangeira para BRL\n")
    moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").strip().upper()

    try:
        url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
        response = requests.get(url)
        dados = response.json()

        chave = f"{moeda}BRL"
        if chave not in dados:
            print("Moeda não encontrada.")
            return

        info = dados[chave]
        print(f"\nMoeda: {info['name']}")
        print(f"Valor atual: R$ {info['bid']}")
        print(f"Máximo: R$ {info['high']}")
        print(f"Mínimo: R$ {info['low']}")
        print(f"Última atualização: {info['create_date']}\n")

    except Exception as e:
        print("Erro ao consultar a cotação:", e)

consultar_cotacao()
