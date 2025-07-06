"""
Atividade Prática 04
Aluna: Airan Rejane
Escola da Nuvem - Aulas técnicas do curso Fundamentos de AWS

Atividade 3

Crie um programa que verifique se uma senha é forte. Uma senha forte deve ter pelo menos 8 caracteres
e conter pelo menos um número. O programa deve continuar pedindo senhas até que uma válida 
seja inserida ou o usuário digite 'sair'.​

​"""

def verificar_senha():
    print("--- Programa de verificação de senha forte --- \n")
    print("Crie uma senha forte. A senha deve ter pelo menos 8 caracteres e conter pelo menos um número. \n")
    print("Quando terminar, digite 'sair'.\n")


    while True:
    
        entrada = input("Digite uma senha forte ou 'sair' para encerrar o programa:")

        if entrada.lower() == 'sair':
            print("Programa encerrado. Nenhuma senha foi registrada.")
            break

        # Verifica se tem pelo menos 8 caracteres
        if len(entrada) < 8:
            print("Senha muito curta. Use no mínimo 8 caracteres.")

        if not any(char.isdigit() for char in entrada):
            print("Senha inválida. A senha precisa conter pelo menos um número.")
            continue
        
        print(f"Senha válida registrada: {entrada}")
        break
            
            

verificar_senha()



    
