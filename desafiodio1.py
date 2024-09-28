def analise_vendas(vendas):
    # Calcula o total de vendas
    total_vendas = sum(vendas)
    
    # Calcula a média mensal de vendas
    media_vendas = total_vendas / len(vendas)
    
    # Retorna o total de vendas e a média formatados com duas casas decimais
    return f"{total_vendas}, {media_vendas:.2f}"

def obter_entrada_vendas():
    # Solicita a entrada do usuário em uma única linha
    entrada = input()
    
    # Divide a string de entrada e converte cada elemento para inteiro
    vendas = list(map(int, entrada.split(',')))
    
    return vendas

# Executa o programa
vendas = obter_entrada_vendas()
print(analise_vendas(vendas))
