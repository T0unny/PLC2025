import json
import ply.lex as lex
from datetime import datetime

# Carregar o stock de produtos a partir do ficheiro JSON
with open('TP5/stock.json', 'r', encoding='utf-8') as f:
    stock = json.load(f)

tokens=('LISTAR','MOEDA','SELECIONAR','SAIR','SALDO','MOEDA_EURO','MOEDA_CENT','COD') #Tokens para ler o imput

# Definição das expressões regulares para cada token
t_LISTAR = r'LISTAR'
t_MOEDA = r'MOEDA'
t_SELECIONAR = r'SELECIONAR'
t_SAIR = r'SAIR'
t_SALDO = r'SALDO'
t_MOEDA_EURO = r'1E|2E'
t_MOEDA_CENT = r'50C|20C|10C|5C|2C|1C'
t_COD = r'\w\d\d'
t_ignore = '( ,\t)'

def t_error(t):
    print(f"Erro de sintaxe na linha {t.value}")
    t.lexer.skip(1)

lexer = lex.lex()

# Função para listar os produtos disponíveis
def listar_produtos(produtos):
    print(f"{'Codigo':<10} {'Nome':<20} {'Quantidade':<15} {'Preço':<10}")
    print("-" * 55)
    for produto in produtos:
        print(f"{produto['cod']:<10} {produto['nome']:<20} {produto['quant']:<15} {produto['preco']:<10}")

# Função para converter moedas inseridas em float
def moedas_para_float(moeda_sting,saldo):
    lexer.input(moeda_sting)
    for tok in lexer:
        if tok.type == 'MOEDA_EURO':
            saldo += int(tok.value[:-1])
        elif tok.type == 'MOEDA_CENT':
            saldo += int(tok.value[:-1]) / 100
    return saldo

# Função para converter float em lista de moedas
def float_para_moedas(valor):
    valor = round(valor*100)
    moedas = [200, 100, 50, 20, 10, 5, 2, 1]
    resultado =[]
    for m in moedas:
        q = valor // m
        if q > 0:
            valor -= q*m
            if m >= 100:
                resultado.append(f"{q:.0f}x {int(m/100)}e")
            else:
                resultado.append(f"{q:.0f}x {int(m)}c")
    return resultado

def maquina():
    saldo=0.0
    rounded_saldo = round(saldo, 2)
    
    print(f"{datetime.now().strftime("%Y-%m-%d %H:%M")}, Stock carregado, Estado Atualizado")
    print("Bom dia. Estou disponível para ateder o seu pedido.")
    
    while True:
        comando = input(">> ").upper() # Para ler o imput com letras maiusculas ou minusculas
        lexer.input(comando)
        
        for tok in lexer:
            if tok.type == 'LISTAR':
                listar_produtos(stock)
                
            elif tok.type == 'MOEDA':
                saldo = moedas_para_float(comando,saldo)
                print(f"Saldo atual: {saldo//1:.0f}e {((saldo)%1)*100:.0f}c")
            
            elif tok.type == 'SELECIONAR':
                partes = comando.split()
                if len(partes) > 1: # Verifica se o código do produto foi fornecido
                    for produto in stock: # Percorre a lista de produtos para encontrar o produto selecionado
                        if produto['cod'] ==partes[1]: # Verifica se o código do produto corresponde ao código fornecido
                            if produto['quant'] > 0: # Verifica se o produto está disponível
                                if saldo >= produto['preco']: # Verifica se o saldo é suficiente para comprar o produto
                                    produto['quant'] -= 1
                                    saldo -= produto['preco']
                                    print(f"Pode retirar o produto dispensado: {produto["nome"]}")
                                    print(f"Saldo = {saldo//1:.0f}e {((saldo)%1)*100:.0f}c")
                                else:
                                    print("Saldo insuficiente para satisfazer o seu pedido")
                                    print(f"Saldo = {saldo//1:.0f}e {((saldo)%1)*100:.0f}c ; Pedido={produto['preco']//1:.0f}e {((produto['preco'])%1)*100:.0f}c")
                            else:
                                print("Produto esgotado")
                else:
                    print("Instrução inválida")
                
            elif tok.type == 'SALDO':
                print(f"Saldo = {saldo//1:.0f}e {((saldo)%1)*100:.0f}c")
            
            elif tok.type == 'SAIR':
                if saldo > 0:
                    print(f"Pode retirar o seu troco: {float_para_moedas(saldo)}.")
                print("Até à próxima")
                return

maquina()

# Guardar o stock atualizado no ficheiro JSON
with open('TP5/stock.json', 'w', encoding='utf-8') as f:
    produtos = json.dump(stock, f, indent=4)
