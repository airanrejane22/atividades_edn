"""
Atividade Prática 04
Aluna: Airan Rejane
Escola da Nuvem - Aulas técnicas do curso Fundamentos de AWS

"""

"""Crie um programa que permita a um professor registrar as notas de uma turma. O programa deve continuar 
solicitando notas até que o professor digite 'fim'. Notas válidas são de 0 a 10. O programa deve ignorar notas 
inválidas e continuar solicitando. No final, deve exibir a média da turma. Notas = [] -> len(Notas)"""

def registro_notas():
    notas = []

    
    print("--- Registro de Notas da Turma ---")
    print("Digite as notas dos alunos (entre 0 e 10).")
    print("Quando terminar, digite 'fim'.\n")

    
    while True:
        entrada = input("Digite uma nota ou 'fim' para encerrar o programa:")

        if entrada.lower() == 'fim':
            break
  
        try:
            nota = float(entrada)

            if  0 <= nota <= 10:
                notas.append(nota)

            else:
                print("Nota inválida. Digite um valor entre 0 e 10.")
        
        except ValueError:
            print("Entrada inválida. Digite um número ou 'fim'.")

    if len(notas) > 0:
        media = sum(notas) / len(notas)
        print(f"Média da turma é {media:.2f}")
        print("Quantidade de alunos:{}.".format(len(notas)))
    else:
        print("Nenhuma nota válida foi registrada no sistema.")


registro_notas()

