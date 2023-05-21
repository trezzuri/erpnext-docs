# Contabilidade de parte comum


A Contabilidade de Parte Comum no ERPNext envolve a contabilidade de transações incomuns, como a criação de uma Fatura de Venda contra um Fornecedor principal.


Suponhamos que um usuário do ERPNext que vem efetuando Notas Fiscais de Compra para um Fornecedor, queira emitir uma Nota Fiscal contra o mesmo fornecedor e ajustar esta Nota Fiscal contra uma das compras anteriores.


O acima pode ser alcançado ativando a Contabilidade de Parte Comum.


**Passos:**


1. Vá para Configurações de contas e habilite *Contabilidade de parte comum*.
2. Crie um link entre duas partes


* Se a função principal da parte for Fornecedor, acesse o Cadastro de Fornecedores e clique em Ações -> Vincular com o Cliente
* Se a função principal da parte for Cliente, vá para o Mestre do Cliente e clique em Ações -> Vincular com Fornecedor![Link da Parte](/files/Party_Link.gif)
3. Crie uma Nota Fiscal de Venda contra o Cliente que foi definido como Parte Secundária na 4ª etapa.
4. Ao enviar a Fatura de Venda, um Lançamento Diário será lançado automaticamente, criando um saldo antecipado contra o Fornecedor vinculado.


![Entrada de diário](/files/Entrada de diário.png)
5. Agora, esse adiantamento de lançamento contábil manual pode ser usado para reconciliar com uma fatura de compra.