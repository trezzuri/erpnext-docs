# Copiar e colar vários registros do Excel



**Se você possui uma sequência de registros salvos em uma planilha Excel, que precisam ser mapeados em uma Tabela Filho no ERPNext, o mesmo pode ser feito usando este recurso.**


Digamos que você tenha uma lista de itens salva em uma planilha do Excel e precise copiá-la para a tabela secundária 'Itens' no pedido de vendas.


**Etapas para copiar e colar registros do Excel**


* Prepare os dados de origem no Excel ou em um editor de texto com cada coluna separada por uma tabulação.


![Copiar e colar](/files/using-copy-paste-1.png)
* Arraste para selecionar os registros e clique no botão do menu copiar ou por Ctrl + C (Cmd + C) para


Caso 1. A primeira coluna da planilha Excel deve ser o cabeçalho da coluna e o conteúdo dele.


Caso 2. Quando não há cabeçalho de coluna definido, os dados serão mapeados para as colunas visíveis.


![Copiar e colar](/files/using-copy-paste-4.png)
* Coloque o cursor no campo de entrada de destino da tabela filha e cole-o. Ao contrário do recurso de importação via upload de arquivo, esse recurso de copiar e colar acionará eventos de alteração de campo automaticamente.


![Copiar e colar](/files/using-copy-paste-3.gif)


Para considerar o desempenho, você deve colar apenas um número menor ou igual a 100 registros por vez.



