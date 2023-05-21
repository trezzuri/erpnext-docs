# Período contábil


**Um período contábil define um período de tempo no qual as demonstrações financeiras são registradas.**


No ERPNext, o Período Contábil é um período de tempo fora do qual transações submissíveis selecionadas (como Fatura de Venda/Compra, Lançamento em Estoque, Lançamento em Folha de Pagamento, Lançamento no Diário, etc.) não podem ser criadas. Em outras palavras, as transações selecionadas só podem ser criadas dentro do Período Contábil definido.


**Por que o Período Contábil é necessário?**


Quando as transações são enviadas, elas afetam os livros contábeis e os relatórios que processam os dados contábeis.
Isso pode causar problemas quando os relatórios financeiros precisam ser gerados para auditoria pelas autoridades ou para fechar os livros contábeis do exercício.


Aqui, o período contábil pode ser usado para limitar o período de tempo dentro do qual as transações podem ser enviadas para preservar
a integridade dos relatórios correspondentes.


## 1. Como criar um Período Contábil


### 1.1 Para que serve a opção "Fechado" para as transações selecionadas?


![Tabela filho do período contábil](/files/accounting-period-closed.png)


A opção "Fechado" na tabela filho para tipos de transação é usada para selecionar quais deles serão restringidos após o término do Período Contábil.


Observe que, se o Período Contábil terminar e se alguma das transações selecionadas na tabela filho não tiver "Fechado" marcada, elas não serão restritas após o término do Período Contábil.


1. Insira um nome para o Período Contábil.
2. Defina um período de tempo definindo as datas de início e término.
3. Adicione ou remova transações da tabela. Observe que todas as transações listadas na tabela com a opção "Fechado" marcada serão restritas após o término do período contábil.
4. Salve e envie.
![Período contábil](/files/accounting-period.png)


Se você tentar enviar uma transação fechada após o término do Período Contábil, verá um erro de validação impedindo-o de fazê-lo.
![Período Contábil](/files/período-accounting-closed-for-transaction.png)



>
> Observação: Nenhuma função pode enviar transações definidas no Período contábil, mesmo a Função definida em 'Função permitida para definir contas congeladas e editar entradas congeladas' em [Configurações da conta](/docs/v13/user/manual/en/accounts/ configurações de contas).
>
>
>


## 2. Tópicos Relacionados


* [Como o período contábil é usado para fechar livros contábeis](https://frappe.io/blog/erpnext-features/closing-accounting-books-in-erpnext)
* [Voucher de Encerramento de Período](/docs/v13/user/manual/en/accounts/voucher de encerramento de período)