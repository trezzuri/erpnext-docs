# Contabilidade da parte comum


A contabilidade de parte comum no SOMA envolve a contabilidade de transações incomuns, como a criação de uma fatura de venda contra um fornecedor principal. 


Vamos supor que um usuário do SOMA que vem fazendo Notas Fiscais de Compra para um Fornecedor, queira fazer uma Nota Fiscal de Venda contra o mesmo fornecedor e ajustar essa Nota Fiscal contra uma das compras anteriores.


O que foi dito acima pode ser alcançado ativando a Contabilidade de Parte Comum.


**Etapas:**


1. Vá para Configurações de contas e ative *Contabilidade de parte comum*.
2. Criar um link entre duas partes


	* Se a função principal da parte for Fornecedor, vá para o Cadastro de fornecedores e clique em Ações -> Vincular com o cliente
	* Se a função principal da parte for Cliente, vá para o Cadastro de Clientes e clique em Ações -> Vincular com o Fornecedor![Party Link](/files/Party_Link.gif)
3. Crie uma Fatura de Venda contra o Cliente que foi definido como Parte Secundária na 4ª etapa.
4. Ao enviar a fatura de venda, um lançamento contábil manual será lançado automaticamente, criando um saldo antecipado em relação ao fornecedor vinculado.


![Journal Entry](/files/Journal-Entry.png)
5. Agora, esse adiantamento de entrada no diário pode ser usado para reconciliar com uma fatura de compra.
