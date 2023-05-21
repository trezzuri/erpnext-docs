# Ferramenta de criação de fatura de abertura


A Ferramenta de Criação de Nota Fiscal de Abertura permite importar dados de Notas Fiscais de Compra ou Venda pendentes para o ERPNext. Esta ferramenta específica é utilizada no lugar da Ferramenta de Importação de Dados para os casos em que os dados do Item são irrelevantes e os saldos pendentes de Clientes/Fornecedores devem ser importados para o ERPNext.


Para acessar a Ferramenta de Criação de Nota Fiscal de Abertura, acesse:



>
> Home > Contabilidade > Abertura e Fechamento > Ferramenta de Criação de Fatura de Abertura
>
>
>


## 1: Como importar Notas Fiscais


1. Selecione a Empresa para a qual deseja importar os saldos iniciais.
2. Selecione o Tipo de Fatura. Selecionar Vendas ou Compras gerará Faturas de Vendas ou Faturas de Compras, respectivamente.
3. Marcar a caixa de seleção "Criar parte ausente" criará automaticamente clientes ou fornecedores, se ausentes, de acordo com o nome fornecido na coluna Parte.


![Ferramenta de criação de fatura de abertura](/files/opening-invoice-creation-tool.png)
4. Preencha a tabela Faturas. É composto pelos seguintes campos:


* **Parte**: Você pode selecionar um Cliente/Fornecedor existente ou inserir o nome de um novo que será criado automaticamente.
* **Data de Lançamento**: A data em que a fatura será lançada.
* **Due Date**: A data após a qual a fatura estará vencida.
* **Nome do item**: (Opcional) O nome do item inserido aqui será mostrado na tabela de itens da fatura.
* **Valor pendente**: O valor pendente da fatura.
* **Número da Nota Fiscal**: O número da nota fiscal correspondente conforme presente no sistema anterior. Se este campo estiver vazio, será utilizada a série de nomenclatura ERPNext.



>
> **Dica**: você pode clicar no botão de download para baixar uma planilha do Excel que pode ser preenchida facilmente com os dados apropriados. Se você baixou a planilha do Excel, use o botão Carregar para carregá-la. Depois de carregar a planilha, a tabela será preenchida com as linhas de dados apropriadas.
>
>
>