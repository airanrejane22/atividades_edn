"""
Atividade Prática 07
Aluna: Airan Rejane
Escola da Nuvem - Aulas técnicas do curso Fundamentos de AWS


Atividade 4

Crie um script em Python que leia e escreva dados em um arquivo JSON. O arquivo JSON deve conter informações 
de uma pessoa, com campos nome, idade e cidade.​"""

import json

def manipular_json():
    pessoa = {
        "nome": "João",
        "idade": 28,
        "cidade": "Salvador"
    }

    
    with open("pessoa.json", "w", encoding="utf-8") as f:
        json.dump(pessoa, f, indent=4)

    print("Arquivo JSON criado com sucesso.")

    
    with open("pessoa.json", "r", encoding="utf-8") as f:
        dados = json.load(f)
        print(f"Nome: {dados['nome']}, Idade: {dados['idade']}, Cidade: {dados['cidade']}")

manipular_json()
