
valor1, valor2 = map(int, input().split())
    
inicio = min(valor1, valor2)
fim = max(valor1, valor2)

soma = 0

for i in range(inicio, fim + 1):
    if i % 13 != 0:
        soma += i

        print(soma)