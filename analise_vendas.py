vendas = [
    {"produto": "Camiseta", "valor": 49.90},
    {"produto": "Calça", "valor": 129.90},
    {"produto": "Boné", "valor": 39.90},
    {"produto": "Tênis", "valor": 249.90},
]

valores = [i["valor"] for i in vendas]

valores_altos = [i["valor"] for i in vendas if i["valor"]>100]

nomes = [i["produto"] for i in vendas]


total = sum(valores)
media_venda = sum(valores)/len(vendas)
maior = max(valores)
menor = min(valores)

print("=== RELATÓRIO DE VENDAS ===")
print(f"Total vendido: R$ {total:.2f}")
print(f"Média por venda: R$ {media_venda:.2f}")
print(f"Maior venda: R$ {maior:.2f}")
print(f"Menor venda: R$ {menor:.2f}")
print(f"\nProdutos acima de R$ 100: {valores_altos}")
print(f"Nomes dos produtos: {nomes}")