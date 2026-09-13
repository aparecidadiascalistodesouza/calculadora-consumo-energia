# Programa para calcular desconto

# Solicita o valor total da compra
valor_compra = float(input("Digite o valor total da compra: R$ "))

# Define o percentual de desconto
if valor_compra >= 500:
    percentual_desconto = 10
elif valor_compra >= 200:
    percentual_desconto = 5
else:
    percentual_desconto = 0

# Calcula o valor do desconto
valor_desconto = valor_compra * percentual_desconto / 100

# Calcula o valor final da compra
valor_final = valor_compra - valor_desconto

# Exibe os resultados
print(f"Valor da compra: R$ {valor_compra:.2f}")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Total a pagar: R$ {valor_final:.2f}")