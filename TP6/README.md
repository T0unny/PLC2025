# TPC 6 - Prasser/Analizador sintático

### Pedro Ribeiro, pg60421 

<img width="175" height="200" alt="1752183184539" src="https://github.com/user-attachments/assets/c0382365-4f1f-48fb-9f94-c1e56fafa0c3" />

## Resumo:

Para este tpc modifiquei o código fornecido para a gamática pretendida.

Neste caso precisamos fazer um analisador sintático recursivo descendente para expressões aritméticas.

A gramática que usei foi a seguinte:

#P1: Exp      --> Termo SomaMenos
#P2: SomaMenos  --> '+' Termo SomaMenos
#P3:           | '-' Termo SomaMenos
#P4:           | ε
#P5: Termo    --> NumPar MultDiv
#P6: MultDiv  --> '*' NumPar MultDiv
#P7:           | '/' NumPar MultDiv
#P8:           | ε
#P9: NumPar       --> NUM
#P10:          | '(' Exp ')'

Depois modifiquei o parsser, para reconhecer numeros, parenteses e operações.

Foi criado tambem um analisador lexico correspondete para a gramática.

Código de Resolução: [TPC6.py]()

