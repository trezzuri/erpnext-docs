# Ferramenta de criação de fatura de abertura



A Ferramenta de Criação de Nota Fiscal de Abertura permite importar dados de Notas Fiscais de Compra ou Venda pendentes para o ERPNext. Esta ferramenta específica é usada no lugar da Ferramenta de Importação de Dados para casos onde os dados do Item são irrelevantes e os saldos pendentes contra Clientes/Fornecedores devem ser importados para o ERPNext.


Para acessar a Ferramenta de Criação de Nota Fiscal de Abertura, acesse:


> Home > Contabilidade > Abertura e Fechamento > Ferramenta de Criação de Fatura de Abertura


## 1: Como importar faturas de abertura


1. Selecione a empresa para a qual deseja importar os saldos iniciais.
2. Selecione o tipo de fatura. Selecionar Vendas ou Compra gerará faturas de vendas ou faturas de compra, respectivamente.
3. Marcar a caixa de seleção "Criar parte ausente" criará automaticamente clientes ou fornecedores, caso estejam ausentes, de acordo com o nome fornecido na coluna Parte.


![Ferramenta de criação de fatura de abertura](/files/opening-invoice-creation-tool.png)
4. Preencha a tabela Faturas. Consiste nos seguintes campos:


	* **Parte**: Você pode selecionar um Cliente/Fornecedor existente ou inserir o nome de um novo que será criado automaticamente.
	* **Data de lançamento**: a data em que a fatura será lançada.
	* **Data de Vencimento**: a data após a qual a fatura estará vencida.
	* **Nome do item**: (opcional) o nome do item inserido aqui será mostrado na tabela de itens da fatura.
	* **Valor pendente**: o valor pendente da fatura.
	* **Número da fatura**: O número da fatura correspondente conforme presente no sistema anterior. Se este campo estiver vazio, será usada a série de nomenclatura do ERPNext.


> **Dica**: você pode clicar no botão de download para baixar uma planilha Excel que pode ser facilmente preenchida com dados apropriados. Se você baixou a planilha Excel, use o botão Upload para carregá-la. Depois de fazer upload da planilha, a tabela será preenchida com as linhas de dados apropriadas.



