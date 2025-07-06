"""
Atividade Prática 05
Aluna: Airan Rejane
Escola da Nuvem - Aulas técnicas do curso Fundamentos de AWS

Atividade 2

Crie uma função que verifique se uma palavra ou frase é um palíndromo 
(lê-se igual de trás para frente, ignorando espaços e pontuação). 
Se o resultado é True, responda “Sim”, se o resultado for False, responda "Não"
"""
def palindromo(texto: str):

    texto_limpo =  "".join(char.lower() for char in texto if char.isalnum())

    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
       return "Não"

print(palindromo("aca"))
