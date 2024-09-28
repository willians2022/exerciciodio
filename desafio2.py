"""Você está trabalhando em um projeto de Power BI onde precisa analisar dados de vendas mensais de uma empresa. Em Power BI, os dados são frequentemente representados em tabelas, e você precisa calcular alguns indicadores básicos. Sua tarefa é calcular o total de vendas e a média mensal de vendas que serão usados para gerar relatórios e gráficos no Power BI, além de criar uma lista em Python para calcular o total de vendas e a sua média mensal."""


"""Na função obter_entrada_vendas() você deverá:

Utilizar o método split(',') para dividir a string de entrada em elementos separados por vírgula, criando assim uma lista de strings.

Aplique a função map(int, ...) para converter cada elemento dessa lista de strings em um inteiro.

Usar a função list() para converter o objeto map resultante em uma lista de inteiros.

Essa lista de inteiros representará os valores de vendas que serão utilizados para calcular o total e a média mensal de vendas em outra função."""


def analise_vendas(vendas):
    # Calcula o total de vendas
    total_vendas = sum(vendas)
    
    # Calcula a média mensal de vendas
    media_vendas = total_vendas / len(vendas)
    
    # Retorna a saída formatada com o total e a média (com duas casas decimais)
    return f"{total_vendas}, {media_vendas:.2f}"

def obter_entrada_vendas():
    # Solicita a entrada do usuário em uma única linha
    entrada = input().strip()
    
    # Divide a string de entrada por vírgulas, mapeia os valores para inteiros e converte para uma lista
    vendas = list(map(int, entrada.split(',')))
    
    return vendas
vendas = obter_entrada_vendas()
print(analise_vendas(vendas))
