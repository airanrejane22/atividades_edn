"""
Atividade Prática 07
Aluna: Airan Rejane
Escola da Nuvem - Aulas técnicas do curso Fundamentos de AWS


Atividade 3

Crie um script em Python que leia um arquivo CSV e exiba os dados na tela. 
O arquivo CSV deve conter informações de pessoas, com colunas Nome, Idade e Cidade.​

​"""

import csv

def ler_csv():
    try:
        with open("pessoas.csv", "r", encoding="utf-8") as f:
            leitor = csv.DictReader(f)
            for linha in leitor:
                print(f"Nome: {linha['Nome']}, Idade: {linha['Idade']}, Cidade: {linha['Cidade']}")
    except FileNotFoundError:
        print("Arquivo CSV não encontrado.")

ler_csv()