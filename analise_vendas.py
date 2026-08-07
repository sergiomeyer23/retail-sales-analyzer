def media(lista):
    i = 0
    soma = 0
    while len(lista) > i:
        soma += lista[i]
        i += 1
    return soma / len(lista)


def maior_menor(lista):
    i = 0
    maior = lista[0]
    menor = lista[0]
    while i < len(lista):
        if lista[i] > maior:
            maior = lista[i]
        if lista[i] < menor:
            menor = lista[i]
        i += 1
    return maior, menor


vendas = [
    {"produto": "Camiseta", "valor": 49.90},
    {"produto": "Calça", "valor": 129.90},
    {"produto": "Boné", "valor": 39.90},
    {"produto": "Tênis", "valor": 249.90},
]

valores = []
i = 0
while i < len(vendas):
    valores.append(vendas[i]["valor"])
    i += 1

total = sum(valores)
media_venda = media(valores)
maior, menor = maior_menor(valores)

print("=== RELATÓRIO DE VENDAS ===")
print(f"Total vendido: R$ {total:.2f}")
print(f"Média por venda: R$ {media_venda:.2f}")
print(f"Maior venda: R$ {maior:.2f}")
print(f"Menor venda: R$ {menor:.2f}")