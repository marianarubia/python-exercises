# cálculo da SOMA
INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K += 1
    SOMA += K

print(SOMA)

# verificação na sequência de Fibonacci
def pertence_fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

numero = int(input("Informe um número: "))
if pertence_fibonacci(numero):
    print(f"{numero} pertence à sequência de Fibonacci.")
else:
    print(f"{numero} não pertence à sequência de Fibonacci.")

# análise de faturamento diário
import json

dados = '''
{
    "faturamento": [1000, 2000, 3000, null, 5000, 0, 7000, 8000, null, 9000, 10000, 0, 11000]
}
'''

faturamento = json.loads(dados)['faturamento']

# filtrando valores válidos
valores_validos = [valor for valor in faturamento if valor is not None]

menor = min(valores_validos)
maior = max(valores_validos)
media = sum(valores_validos) / len(valores_validos)

dias_acima_media = len([valor for valor in valores_validos if valor > media])

print(f"Menor faturamento: {menor}")
print(f"Maior faturamento: {maior}")
print(f"Número de dias acima da média: {dias_acima_media}")

# percentual de representação por estado
faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total = sum(faturamento_estados.values())

percentuais = {estado: (valor / total) * 100 for estado, valor in faturamento_estados.items()}

for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")

# inversão de uma string
def inverter_string(s):
    resultado = ""
    for char in s:
        resultado = char + resultado
    return resultado

string = input("informe uma string: ")
string_invertida = inverter_string(string)
print(f"string invertida: {string_invertida}")