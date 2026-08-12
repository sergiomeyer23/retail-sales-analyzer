import csv

def ler_vendas(caminho_arquivo):
    """Lê arquivo CSV com tratamento de erros."""
    try:
        produtos = []
        with open(caminho_arquivo, 'r') as arquivo:
            leitor = csv.DictReader(arquivo)
            
            for linha in leitor:
                try:
                    produto = {
                        "nome": linha['produto'],
                        "valor": float(linha['valor']),
                        "quantidade": int(linha['quantidade'])
                    }
                    produto['receita'] = produto['valor'] * produto['quantidade']
                    produtos.append(produto)
                except KeyError as e:
                    print(f"Erro: coluna {e} não encontrada")
                    continue
                except ValueError as e:
                    print(f"Erro: valor inválido - {e}")
                    continue
        
        return produtos
        
    except FileNotFoundError:
        print(f"Erro: arquivo '{caminho_arquivo}' não encontrado")
        return []
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return []
    
def gerar_relatorio(produtos):
    if not produtos:
        print("Nenhum produto para gerar o relatório")
        return 
    
    try:
        valores = [p['valor'] for p in produtos]
        quantidades = [p['quantidade'] for p in produtos]
        receitas = [p['receita'] for p in produtos]
        
        total = sum(receitas)
        media = sum(valores) / len(valores)
        total_itens = sum(quantidades)
        
        # Máximos e mínimos
        mais_caro = max(produtos, key=lambda p: p['valor'])
        mais_barato = min(produtos, key=lambda p: p['valor'])
        maior_receita = max(produtos, key=lambda p: p['receita'])
        
        # Produtos acima de R$ 100
        produtos_caro = [p for p in produtos if p['valor'] > 100]
        # Imprimir relatório
        print("=== RELATÓRIO DE VENDAS ===")
        print(f"Total vendido: R$ {total:.2f}")
        print(f"Valor médio dos produtos: R$ {media:.2f}")
        print(f"Quantidade total de itens: {total_itens}")
        print()
        print(f"Produto mais caro: {mais_caro['nome']} (R$ {mais_caro['valor']:.2f})")
        print(f"Produto mais barato: {mais_barato['nome']} (R$ {mais_barato['valor']:.2f})")
        print(f"Produto com maior receita: {maior_receita['nome']} (R$ {maior_receita['receita']:.2f})")
        print()
        print(f"Produtos acima de R$ 100: {len(produtos_caro)}")
        for p in produtos_caro:
            print(f"  - {p['nome']}: R$ {p['valor']:.2f}")
    
        
    except KeyError as e:
        print(f"Erro: produto com estrutura inválida - {e}")
    except Exception as e:
        print(f"Erro ao gerar relatório: {e}")
    
    
if __name__ == "__main__":
    vendas = ler_vendas('vendas_exemplo.csv')
    gerar_relatorio(vendas)