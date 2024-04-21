
# Leitura do valor de N
N = int(input())

# Leitura dos valores do vetor X
X = list(map(int, input().split()))

# Encontrar o menor valor e sua posição
menor = X[0]
posicao = 0
for i in range(1, N):
    if X[i] < menor:
        menor = X[i]
        posicao = i

# Saída dos resultados
print("Menor valor:", menor)
print("Posicao:", posicao)
