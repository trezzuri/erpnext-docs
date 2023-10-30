# Importando fatura eletrônica do fornecedor



> Introduzido na versão 13


A partir de 1º de janeiro de 2019, a fatura eletrônica é obrigatória para empresas nacionais que operam com transações domésticas B2B e B2C na Itália. O ERPNext possui um recurso para importar faturas de fornecedores a partir de arquivos XML fornecidos pelos fornecedores ao governo.


O ERPNext possui um recurso para importar faturas de fornecedores a partir de arquivos XML fornecidos pelos fornecedores ao governo. Usando isso você pode importar faturas eletrônicas de fornecedores para o ERPNext. Os detalhes do fornecedor, como nomes de fornecedores, endereços e faturas de compra, serão criados automaticamente no sistema a partir dos arquivos XML.


## 1. Pré-requisitos


* A UOM de estoque padrão deve ser especificada no tipo de documento de configurações de estoque.
* Ative a verificação da exclusividade da fatura do fornecedor no tipo de documento de configurações de contas.
* Crie um arquivo Zip com todos os seus arquivos XML de fatura de fornecedor.


### 2. Como usar a fatura do fornecedor de importação


1. Navegue até o tipo de documento Importar fatura do fornecedor na barra de pesquisa global e insira a série da fatura, empresa, grupo de fornecedores, conta fiscal, código do item e lista de preços de compra padrão.
 ![](/files/import_einvoice.png)


	* Série de faturas-A série com a qual as novas faturas de compra serão criadas.
	* Empresa: a empresa para a qual as novas faturas de compra serão criadas.
	* Grupo de Fornecedores-O grupo de fornecedores sob o qual os novos fornecedores serão criados.
	* Conta Fiscal-A conta sob a qual os impostos seriam inseridos para as faturas de compra criadas.
	* Código do item-O código do item que seria usado para a criação da fatura de compra.
	* Lista de preços de compra padrão: a lista de preços de compra padrão a ser usada para a fatura de compra.
2. Após inserir os detalhes acima, clique em Salvar.
3. Anexe o arquivo zip com as faturas XML.
4. Clique em Importar faturas e as faturas de compra serão criadas. Os fornecedores seriam criados se ainda não existissem no sistema.
![](/files/purchase_invoices_created.png)
5. Se a importação do arquivo for concluída com êxito, você verá o status Importação de arquivo concluída. Se houver algum erro, você poderá visualizá-lo no Log de Erros.
![](/files/file_import_completed.png)



