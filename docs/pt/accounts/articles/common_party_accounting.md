# Contabilidade comum das partes



A Contabilidade de Partes Comuns no ERPNext envolve a contabilização de transações incomuns, como a criação de uma Fatura de Vendas contra um Fornecedor primário. 


Vamos supor que um usuário do ERPNext que tem feito Faturas de Compra contra um Fornecedor, queira fazer uma Fatura de Venda contra o mesmo fornecedor e ajustar esta Fatura de Venda contra uma das compras anteriores.


O acima exposto pode ser alcançado ativando a Contabilidade de Partes Comuns.


**Etapas:**


1. Vá para Configurações de contas e ative a *Contabilidade de partes comuns*.
2. Crie um vínculo entre duas partes


	* Se a função principal da parte for Fornecedor, vá para o Cadastro de Fornecedores e clique em Ações-> Vincular ao Cliente
	* Se a função principal da parte for Cliente, vá para o Cadastro de Clientes e clique em Ações-> Vincular ao Fornecedor![Party Link](/files/Party_Link.gif)
3. Crie uma fatura de venda para o cliente que foi definido como parte secundária na quarta etapa.
4. Ao enviar a fatura de vendas, um lançamento contábil manual será lançado automaticamente, criando um saldo adiantado em relação ao fornecedor vinculado.


![Lançamento de diário](/files/Journal-Entry.png)
5. Agora, esse adiantamento de lançamento contábil manual pode ser usado para reconciliar com uma fatura de compra.



