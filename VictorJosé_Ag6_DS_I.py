# Sistema de Cálculo de Descontos por Faixa de Valor

# Entrada de dados: solicita o valor total da compra ao usuário
valor = float(input("Digite o valor total da compra: "))

# Verificação das faixas de desconto
# Faixa 1: compras abaixo de 200 recebem 5% de desconto
if valor < 200:
    desconto = valor * 0.05
    print("Você ganhou 5% de desconto!")

# Faixa 2: compras entre 200 e 299.99 recebem 10% de desconto
elif 200 <= valor < 300:
    desconto = valor * 0.10
    print("Você ganhou 10% de desconto!")

# Faixa 3: compras a partir de 300 recebem 15% de desconto
elif valor >= 300:
    desconto = valor * 0.15
    print("Você ganhou 15% de desconto!")

# Cálculo do valor a pagar subtraindo o desconto aplicado
valor_final = valor - desconto

# Exibição do total a pagar com o desconto aplicado
print("Valor final com desconto: R$", valor_final)