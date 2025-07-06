"""
Atividade Prática 07
Aluna: Airan Rejane
Escola da Nuvem - Aulas técnicas do curso Fundamentos de AWS


Atividade 1

Leia um arquivo que contém dados de log de treinamento de modelos de Machine Learning. Calcule a média e o desvio padrão do tempo de execução constantes. ​
​"""

import statistics

def analisar_tempos_log(arquivo):
    tempos = []

    with open(arquivo, 'r') as f:
        for linha in f:
            if "Tempo:" in linha:
                tempo = float(linha.strip().split(":")[1])
                tempos.append(tempo)

    if tempos:
        media = statistics.mean(tempos)
        desvio = statistics.stdev(tempos)

        print(f"Média do tempo: {media:.2f}")
        print(f"Desvio padrão: {desvio:.2f}")
    else:
        print("Nenhum tempo encontrado no arquivo.")

analisar_tempos_log("log.txt")