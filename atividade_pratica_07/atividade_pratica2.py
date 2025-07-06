"""
Atividade Prática 07
Aluna: Airan Rejane
Escola da Nuvem - Aulas técnicas do curso Fundamentos de AWS


Atividade 2

Crie um script em Python que escreva dados em um arquivo CSV. O arquivo CSV deve conter informações de pessoas,
com colunas Nome, Idade e Cidade.​
​"""

import csv

def escrever_csv():
    pessoas = [
        {"Nome": "Ana", "Idade": 30, "Cidade": "São Paulo"},
        {"Nome": "Carlos", "Idade": 25, "Cidade": "Rio de Janeiro"},
        {"Nome": "Maria", "Idade": 40, "Cidade": "Belo Horizonte"}
    ]

    with open("pessoas.csv", "w", newline="", encoding="utf-8") as f:
        campos = ["Nome", "Idade", "Cidade"]
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(pessoas)

    print("Arquivo CSV criado com sucesso!")

escrever_csv()
