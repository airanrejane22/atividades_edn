
"""
Atividade Prática 05
Aluna: Airan Rejane
Escola da Nuvem - Aulas técnicas do curso Fundamentos de AWS

Atividade 1

Enunciado: Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada 
no valor total da conta e na porcentagem de gorjeta desejada.​

Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.​

Parâmetros:​
valor_conta (float): O valor total da conta​
porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%)​

Retorna:​
float: O valor da gorjeta calculada​"""

def gorjeta(valor_conta: float,porcen_gorjeta:float):

    print("--------Cálculo de gorjeta-------- \n")
    
    valor_gorjeta = valor_conta * (porcen_gorjeta/100)

    print("-----Resumo das informações-----")
    print("Valor total da conta: R$",valor_conta,".")
    print(f"Porcentagem da gorjeta:{porcen_gorjeta:.0f}%.")
    print(f"Valor da gorjeta: R${valor_gorjeta:.2f}.")
    print("----------FIM---------- \n")

    return valor_gorjeta


gorjeta(100,15)
gorjeta(950,20)