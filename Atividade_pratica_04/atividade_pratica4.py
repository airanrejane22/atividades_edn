"""
Atividade Prática 04
Aluna: Airan Rejane
Escola da Nuvem - Aulas técnicas do curso Fundamentos de AWS

"""

""""Atividade 4

Crie um programa que solicite ao usuário que insira números inteiros. O programa deve continuar solicitando 
números até que o usuário digite 'fim'. Para cada número inserido, o programa deve informar se é par ou ímpar. 
Se o usuário inserir algo que não seja um número inteiro, o programa deve informar o erro e continuar. 
No final, o programa deve exibir a quantidade de números pares e ímpares inseridos.​"""

def gerador_numeros():

    print("***** Bem-vindo(s) ao Gerador de Números inteiros ***** \n")
    
    par = []
    impar = []
    
    while True:
        
        entrada = input("Digite um número inteiro ou 'fim' para sair do programa:")

        if entrada.lower() == 'fim':
            print("Encerrando o programa...")
            break

        
        try:

            numero = int(entrada)

            if numero % 2 == 0:
                par.append(numero)
                print(f"{numero} é PAR.")   
            else:
                impar.append(numero)
                print(f"{numero} é ÍMPAR.")
        
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
        
    print("===== Resumo Final =====")
    print(f"Quantidade de números pares: {len(par)}")
    print(f"Quantidade de números ímpares: {len(impar)}")
    print(f"Números pares: {par}")
    print(f"Números ímpares: {impar}")


gerador_numeros()




