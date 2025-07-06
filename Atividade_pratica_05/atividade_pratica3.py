"""
Atividade Prática 05
Aluna: Airan Rejane
Escola da Nuvem - Aulas técnicas do curso Fundamentos de AWS

Atividade 3

Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de nascimento."""

def idade_dias(ano_atual:int,ano_nasc:int):
    idade = (ano_atual - ano_nasc)*365
    resultado = int(idade)
    print(f"A idade de uma pessoa em dias é: {resultado} dias.")


idade_dias(2025,2010)