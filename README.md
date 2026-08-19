Retail Sales Analyzer

Análise de vendas a partir de arquivo CSV: estatísticas gerais, produto mais caro/barato, maior receita e filtro por valor mínimo — com tratamento robusto de erros.

Funcionalidades

    Lê vendas de um CSV (produto, valor, quantidade)
    Calcula total vendido, valor médio e quantidade total de itens
    Identifica produto mais caro, mais barato e de maior receita
    Lista produtos acima de um limite configurável (padrão: R$ 100)
    Tratamento de erros por arquivo, por coluna e por valor

Como rodar
python analise_vendas.py

Para usar outro limite de valor (ex.: R$ 50):

from analise_vendas import ler_vendas, gerar_relatorio
vendas = ler_vendas("vendas_exemplo.csv")
gerar_relatorio(vendas, limite=50)

Exemplo de saída

=== RELATÓRIO DE VENDAS ===
Total vendido: R$ 3391.50
Valor médio dos produtos: R$ 113.23
Quantidade total de itens: 85

Produto mais caro: Tênis (R$ 249.90)
Produto mais barato: Meia (R$ 9.90)
Produto com maior receita: Tênis (R$ 749.70)

Produtos acima de R$ 100: 3
  - Calça: R$ 129.90
  - Tênis: R$ 249.90
  - Jaqueta: R$ 199.90

Stack

Python 3 — módulo padrão csv, sem dependências externas.
