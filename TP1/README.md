TPC 1 - Expressões Regulares

Pedro Ribeiro, pg60421,

O exercícios consiste em uma expressão regular para um numero binário que não pode conter o subconjunto 011.
Para não obtermos este subconjunto, após um 0 apenas um 1 pode existir.
1* faz com que seja possível iniciar com o valor 1 e também permite a sua repetição ou até nenhuma iteração, ex. 111111
0+ serve para termos repetições de 0 ou apenas uma se for esse o caso, ex. 000000
1? faz com que apenas possa existir um 1 ou nenhum
(0+1?)* juntando os dois temos que após um zero ou uma sequência deles apenas um 1 pode existir, este padrão pode se repetir várias vezes ou não existir de um todo, ex. 00101

Resposta: ^1*(0+1?)*$

Resolução do TPC 1: https://github.com/T0unny/PLC2025/blob/main/TP1/Resolu%C3%A7%C3%A3o.txt

<img width="200" height="200" alt="1752183184539" src="https://github.com/user-attachments/assets/c0382365-4f1f-48fb-9f94-c1e56fafa0c3" />
