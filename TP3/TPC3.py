
import sys
import re

def tokenize(input_string,linha):
    reconhecidos = []
    mo = re.finditer(r'(?P<SELECT>SELECT)|(?P<WHERE>WHERE)|(?P<Variavel>\?\w+)|(?P<PA>\{)|(?P<PONTO>\.)|(?P<String>\w*:\w+)|(?P<PF>\})|(?P<SKIP>[ \t])|(?P<NEWLINE>\n)|(?P<ERRO>.)', input_string)
    for m in mo:
        dic = m.groupdict()
        if dic['SELECT']:
            t = ("SELECT", dic['SELECT'], linha, m.span())

        elif dic['WHERE']:
            t = ("WHERE", dic['WHERE'], linha, m.span())
    
        elif dic['Variavel']:
            t = ("Variavel", dic['Variavel'], linha, m.span())
    
        elif dic['PA']:
            t = ("PA", dic['PA'], linha, m.span())
    
        elif dic['PONTO']:
            t = ("PONTO", dic['PONTO'], linha, m.span())
    
        elif dic['String']:
            t = ("String", dic['String'], linha, m.span())
    
        elif dic['PF']:
            t = ("PF", dic['PF'], linha, m.span())
    
        elif dic['SKIP']:
            t = ("SKIP", dic['SKIP'], linha, m.span())
    
        elif dic['NEWLINE']:
            t = ("NEWLINE", dic['NEWLINE'], linha, m.span())
    
        elif dic['ERRO']:
            t = ("ERRO", dic['ERRO'], linha, m.span())
    
        else:
            t = ("UNKNOWN", m.group(), linha, m.span())
        if not dic['SKIP'] and t[0] != 'UNKNOWN': reconhecidos.append(t)
    return reconhecidos


cont = 0
for linha in sys.stdin:
    cont += 1
    for tok in tokenize(linha,cont):
        print(tok)    

