
import sys
import re

def tokenize(input_string,linha):
    reconhecidos = []
    mo = re.finditer(r'(?P<SELECT>SELECT|select)|(?P<WHERE>WHERE|where)|(?P<LIMIT>LIMIT)|(?P<Variavel>\?\w+)|(?P<abreviacaoRdf>a)|(?P<PA>\{)|(?P<PONTO>\.)|(?P<PrefixedName>\w*:\w+)|(?P<String>"(\w+ ?)+")|(?P<idoma>@\w+)|(?P<int>\d+)|(?P<PF>\})|(?P<SKIP>( )|(\t)|(#.*\n))|(?P<NEWLINE>\n)|(?P<ERRO>.)', input_string)
    for m in mo:
        dic = m.groupdict()
        if dic['SELECT']:
            t = ("SELECT", dic['SELECT'], linha, m.span())

        elif dic['WHERE']:
            t = ("WHERE", dic['WHERE'], linha, m.span())
    
        elif dic['LIMIT']:
            t = ("LIMIT", dic['LIMIT'], linha, m.span())
    
        elif dic['Variavel']:
            t = ("Variavel", dic['Variavel'], linha, m.span())
    
        elif dic['abreviacaoRdf']:
            t = ("abreviacaoRdf", dic['abreviacaoRdf'], linha, m.span())
    
        elif dic['PA']:
            t = ("PA", dic['PA'], linha, m.span())
    
        elif dic['PONTO']:
            t = ("PONTO", dic['PONTO'], linha, m.span())
    
        elif dic['PrefixedName']:
            t = ("PrefixedName", dic['PrefixedName'], linha, m.span())
    
        elif dic['String']:
            t = ("String", dic['String'], linha, m.span())
    
        elif dic['idoma']:
            t = ("idoma", dic['idoma'], linha, m.span())
    
        elif dic['int']:
            t = ("int", dic['int'], linha, m.span())
    
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

counter= 0
for linha in sys.stdin:
    counter+=1
    for tok in tokenize(linha,counter):
        print(tok)    

