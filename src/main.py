import random
import sys
from datetime import datetime

quantidades = [10000, 100000, 500000, 1000000]

#range maior e mais distribuido
for quantidade in quantidades:
    arq = open(f"datasets/aleatorios/{quantidade}Aleatorio.txt", "w")
    # data de criacao do arquivo
    arq.write(f"Data e Hora de criação: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n\n")
    vetA = []
    for i in range(0, quantidade):
        vetA.append(random.randint(1, 1000000))
        arq.write(f'{vetA[i]}{" " if i == quantidade - 1 else ", "}')
    arq.close()

    arqC = open(f"datasets/crescentes/{quantidade}Crescente.txt", "w")
    arqC.write(f"Data e Hora de criação: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n\n")
    arqD = open(f"datasets/decrescentes/{quantidade}Decrescente.txt", "w")
    arqD.write(f"Data e Hora de criação: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n\n")

    vetA.sort()
    
    for i in range(0, quantidade):
        arqC.write(f'{vetA[i]}{" " if i == quantidade - 1 else ", "}')
        arqD.write(f'{vetA[quantidade - i - 1]}{" " if i == quantidade - 1 else ", "}')
    
    arqC.close()
    arqD.close()

# range menor
for quantidade in quantidades:
    arq = open(f"datasets/aleatorios/{quantidade}Aleatorio-RangeMenor.txt", "w")
    arq.write(f"Data e Hora de criação: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n\n")
    vetA = []
    for i in range(0, quantidade):
        vetA.append(random.randint(1, 1000))
        arq.write(f'{vetA[i]}{" " if i == quantidade - 1 else ", "}')
    arq.close()

    arqC = open(f"datasets/crescentes/{quantidade}Crescente-RangeMenor.txt", "w")
    arqC.write(f"Data e Hora de criação: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n\n")
    arqD = open(f"datasets/decrescentes/{quantidade}Decrescente-RangeMenor.txt", "w")
    arqD.write(f"Data e Hora de criação: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n\n")

    vetA.sort()

    for i in range(0, quantidade):
        arqC.write(f'{vetA[i]}{" " if i == quantidade - 1 else ", "}')
        arqD.write(f'{vetA[quantidade - i - 1]}{" " if i == quantidade - 1 else ", "}')
    
    arqC.close()
    arqD.close()

# range maior pouco distribuido
for quantidade in quantidades:
    arq = open(f"datasets/aleatorios/{quantidade}Aleatorio-RangeMaior.txt", "w")
    arq.write(f"Data e Hora de criação: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n\n")
    vetA = []
    for i in range(0, quantidade):
        vetA.append(random.randint(100, 999))
        arq.write(f'{vetA[i]}{" " if i == quantidade - 1 else ", "}')
        if(i == quantidade / 2):
            arq.write(f'{int(sys.maxsize / 10)}, ')

    arq.close()

    arqC = open(f"datasets/crescentes/{quantidade}Crescente-RangeMaior.txt", "w")
    arqC.write(f"Data e Hora de criação: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n\n")
    arqD = open(f"datasets/decrescentes/{quantidade}Decrescente-RangeMaior.txt", "w")
    arqD.write(f"Data e Hora de criação: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n\n")

    vetA.sort()

    arqD.write(f'{int(sys.maxsize / 10)}, ')

    for i in range(0, quantidade):
        arqC.write(f'{vetA[i]}, ')
        arqD.write(f'{vetA[quantidade - i - 1]}{" " if i == quantidade - 1 else ", "}')
    
    arqC.write(f'{int(sys.maxsize / 10)}')
    
    arqC.close()
    arqD.close()


# caso real com ordenação de CEPs
for quantidade in quantidades:
    arq = open(f"datasets/aleatorios/{quantidade}Aleatorio-CEP.txt", "w")
    arq.write(f"Data e Hora de criação: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n\n")
    vetA = []
    for i in range(0, quantidade):
        vetA.append(random.randint(10000000, 99999999))
        arq.write(f'{vetA[i]}{" " if i == quantidade - 1 else ", "}')
    arq.close()

    arqC = open(f"datasets/crescentes/{quantidade}Crescente-CEP.txt", "w")
    arqC.write(f"Data e Hora de criação: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n\n")
    arqD = open(f"datasets/decrescentes/{quantidade}Decrescente-CEP.txt", "w")
    arqD.write(f"Data e Hora de criação: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n\n")

    vetA.sort()

    for i in range(0, quantidade):
        arqC.write(f'{vetA[i]}{" " if i == quantidade - 1 else ", "}')
        arqD.write(f'{vetA[quantidade - i - 1]}{" " if i == quantidade - 1 else ", "}')
    
    arqC.close()
    arqD.close()

# caso extremo apenas com numeros entre int(sys.maxsize / 10) e int(sys.maxsize / 10) - 100000000

for quantidade in quantidades:
    arq = open(f"datasets/aleatorios/{quantidade}Aleatorio-Extremo.txt", "w")
    arq.write(f"Data e Hora de criação: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n\n")
    vetA = []
    for i in range(0, quantidade):
        vetA.append(random.randint((int(sys.maxsize / 10)) - 100000000, int(sys.maxsize / 10)))
        arq.write(f'{vetA[i]}{" " if i == quantidade - 1 else ", "}')
    arq.close()

    arqC = open(f"datasets/crescentes/{quantidade}Crescente-Extremo.txt", "w")
    arqC.write(f"Data e Hora de criação: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n\n")
    arqD = open(f"datasets/decrescentes/{quantidade}Decrescente-Extremo.txt", "w")
    arqD.write(f"Data e Hora de criação: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n\n")

    vetA.sort()

    for i in range(0, quantidade):
        arqC.write(f'{vetA[i]}{" " if i == quantidade - 1 else ", "}')
        arqD.write(f'{vetA[quantidade - i - 1]}{" " if i == quantidade - 1 else ", "}')
    
    arqC.close()
    arqD.close()

# caso com numeros iguais

for quantidade in quantidades:
    arq = open(f"datasets/aleatorios/{quantidade}Aleatorio-Iguais.txt", "w")
    arq.write(f"Data e Hora de criação: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n\n")
    vetA = []
    for i in range(0, quantidade):
        vetA.append(100)
        arq.write(f'{vetA[i]}{" " if i == quantidade - 1 else ", "}')
    arq.close()

    arqC = open(f"datasets/crescentes/{quantidade}Crescente-Iguais.txt", "w")
    arqC.write(f"Data e Hora de criação: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n\n")
    arqD = open(f"datasets/decrescentes/{quantidade}Decrescente-Iguais.txt", "w")
    arqD.write(f"Data e Hora de criação: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n\n")

    vetB = []
    vetC = []

    for i in range(0, quantidade):
        vetB.append(100000)
        vetC.append(1000000000)

    for i in range(0, quantidade):
        arqC.write(f'{vetB[i]}{" " if i == quantidade - 1 else ", "}')
        arqD.write(f'{vetC[i]}{" " if i == quantidade - 1 else ", "}')
    
    arqC.close()
    arqD.close()
