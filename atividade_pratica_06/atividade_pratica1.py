"""
Atividade Prática 06
Aluna: Airan Rejane
Escola da Nuvem - Aulas técnicas do curso Fundamentos de AWS

"""

"""Exercício 1

Crie um programa que gera uma senha aleatória com o módulo random, 
utilizando caracteres especiais, possibilitando o usuário a informar a quantidade de caracteres 
dessa senha aleatória. ​"""

import random
import string

def gerar_senha():

    print("----- Gerador de Senhas Aleatórias -----\n")

    try:

        tamanho = int(input("Digite a quantidade de caracteres desejada para a senha: "))  

        if tamanho <= 0:
            print("O tamanho da senha deve ser maior que 0.")
            return

        caracteres = string.ascii_letters + string.digits + string.punctuation
        
        
        senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
        
        print(f"\n Sua senha gerada é: {senha}\n")

    except ValueError:
        print("Entrada inválida. Digite um número inteiro para o tamanho da senha.")


gerar_senha()