# TPC 2 - Conversor MarkDown Para HTML

### Pedro Ribeiro, pg60421, 

<img width="175" height="200" alt="1752183184539" src="https://github.com/user-attachments/assets/c0382365-4f1f-48fb-9f94-c1e56fafa0c3" />

## Resumo:

Os parâmetros de Cabeçalho, Bold, Itálico, Imagens e Links são tratados com substituições simples usando re.compile e o re.sub, o que torna o código mais limpo e fácil de ler.

Nos cabeçalhos, a ordem de substituição é importante, temos que começa-se por ###, depois ## e só no fim #. Desta forma, evitamos que uma linha marcada como ### seja interpretada incorretamente como # ou ##. O mesmo é aplicado a Imagens e Links, primeiro processamos as Imagens e só depois os Links.

Para as listas, foi necessário separar o texto em partes quando existe mais que uma lista, usando a função list2. Cada bloco é depois tratado pela list1, que a partir do tamanho da lista numerada, faz as substituições necessárias de Markdown para HTML.

No Notebook há comentários para uma melhor explicação.

Código da resolução do TPC : [TP2/TPC2.py](https://github.com/T0unny/PLC2025/blob/main/TP2/TPC2.py)

Notebook do código com exemplo : [TP2/TPC2.ipynb](https://github.com/T0unny/PLC2025/blob/main/TP2/TPC2.ipynb) 
