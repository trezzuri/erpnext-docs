# Copiar e colar vários registros do Excel


**Caso você tenha uma sequência de registros salva em uma planilha de Excel, que precisa ser mapeada em uma Tabela Filho no ERPNext, o mesmo pode ser feito utilizando este recurso.**


Digamos que você tenha uma lista de itens salva em uma planilha do Excel e precise copiá-la para a tabela filho 'Itens' no pedido de venda.


**Etapas para copiar e colar registros do Excel**


* Prepare os dados de origem no Excel ou editor de texto com cada coluna separada por uma tabulação.


![Copy Pasting](/files/using-copy-paste-1.png)
* Arraste para selecionar os registros, e clique no botão copiar do menu ou pelo Ctrl + C (Cmd + C) para


Caso 1. A primeira coluna da folha de Excel deve ser o cabeçalho da coluna e o seu conteúdo.


Caso 2. Quando não houver cabeçalho de coluna definido, os dados serão mapeados para as colunas visíveis.


![Copy Pasting](/files/using-copy-paste-4.png)
* Coloque o cursor no campo de entrada de destino da tabela filho e cole-o. Ao contrário da importação por meio do recurso de upload de arquivo, este recurso de copiar e colar acionará eventos de alteração de campo automaticamente.


![Copy Pasting](/files/using-copy-paste-3.gif)


Para consideração de desempenho, você deve colar apenas menos ou igual a 100 registros por vez.