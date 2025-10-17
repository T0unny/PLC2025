# TPC 3 - Máquina de Vending

### Pedro Ribeiro, pg60421 

<img width="175" height="200" alt="1752183184539" src="https://github.com/user-attachments/assets/c0382365-4f1f-48fb-9f94-c1e56fafa0c3" />

## Resumo:
Comecei por criar um analisador léxico para ler a instução dada no imput e ler o ficheiro json.

Depois criei a função mais simples, listar, para conseguir visualizar o stock da máquina.

Em seguida para ser mais facil, dentro da maquina é apenas usado float, por isso criei duas funções, uma que converte moedas em floats e vice-versa.

Para ser mais facil identificar as moedas criei dois tokens, um para euros e outro para centimos.

Quando selecionamos um produto é todo feito um procedimento desde verificar se o produto existe, ver a sua quantidade e comparar o preço, só depois é aceite o pedido, caso contrário o produto não é selecionado.
Para não ter erros na leitura dos códigos dos produtos criei um token para os mesmos.

É tambem possivel verificar o saldo e quando o utilizador sai da máquina esta devolve o dinheiro usando a função de conversão de float para moedas.

Por fim volto a escrever no ficheiro json.

Código de Resolução: [TPC5.py](https://github.com/T0unny/PLC2025/blob/main/TP5/TPC5.py)

Ficheiro JSON exemplo: [Stock.json](https://github.com/T0unny/PLC2025/blob/main/TP5/stock.json)
