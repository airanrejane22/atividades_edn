"""
Atividade Prática 04
Aluna: Airan Rejane
Escola da Nuvem - Aulas técnicas do curso Fundamentos de AWS

"""

# ATIVIDADE 01

def calculadora():
    
    while True:
        try:
            print("-------Calculadora-------") 

            #MENU
            print("---Menu de operações---")
            print("Soma: +")
            print("Subtração: - ")
            print("Multiplicação: *")
            print("Divisão: /")
            print("\nPara sair do aplicativo, digite 0 como operação.")


            #Solicitando números
            num1 = float(input("Digite um número:")) 
            num2 = float(input("Digite outro número:"))

            #Escolhendo a operação
            operacao = input("Digite o número da operação:")
            
            #Caso opte por sair do programa!
            if operacao == 0:
                print("----Encerrando o programa----")
                break

            if operacao not in ["+","-","*","/"]: #CAPTURA DE ERRO
                raise ValueError("Operação inválida. Use apenas uma das operações do menu: +, -, * ou /.")

            #operações matemáticas
            if operacao == "+": # SOMA
                resultado = num1 + num2
        
            elif operacao == "-": # SUBTRAÇÃO
                resultado = num1 - num2
            
            elif operacao == "*": # MULTIPLICAÇÃO
                resultado = num1 * num2
                
            elif operacao == "/": # DIVISÃO
                if num2 == 0:
                    raise ZeroDivisionError("Operação Inválida!Não é possível realizar divisão com zero.") #CAPTURA ERRO DIVISÃO POR ZERO
                resultado = num1 / num2
            else:
                raise ValueError("Operação Inválida!")
            
            #Resultado
            print(f"Resultado: {resultado}.")
            break
          
        #Exceções

        except ZeroDivisionError as ve:
            print("Você não pode dividir por zero!Erro: {ve}.")
        except ValueError:
            print("Por favor, digite um número válido.")
        except TypeError:
            print("Erro: Tipo de dado inválido. Certifique-se de usar números.")




