# Período Contábil


**Um período contábil define um período de tempo no qual as demonstrações financeiras são registradas.**


No ERPNext, o Período Contábil é um período de tempo fora do qual as transações submissíveis selecionadas (como Fatura de Vendas/Compras, Lançamento em Estoque, Lançamento em Folha de Pagamento, Lançamento no Diário, etc.) não podem ser criadas. Em outras palavras, as transações selecionadas só podem ser criadas dentro do Período Contábil definido.


**Por que o período contábil é necessário?**


Quando as transações são enviadas, elas afetam os livros contábeis e os relatórios que processam os dados contábeis.
Isso pode causar problemas quando os relatórios financeiros precisam ser gerados para auditoria pelas autoridades ou para fechar os livros contábeis do exercício financeiro.


Aqui, o período contábil pode ser usado para limitar o período de tempo dentro do qual as transações podem ser enviadas para preservar
a integridade dos relatórios correspondentes.


## 1. Como criar um período contábil


### 1.1 Para que é usada a opção "Fechado" para as transações selecionadas?


![Tabela filho do período contábil](/files/accounting-period-closed.png)


A opção "Fechado" na tabela filho para tipos de documento de transação é usada para selecionar quais deles devem ser restritos após o final do Período Contábil.


Observe que, se o Período Contábil terminar e se alguma das transações selecionadas na tabela filho não tiver "Fechado" marcada, elas não serão restritas após o término do Período Contábil.


1. Digite um nome para o período contábil.
2. Defina um período de tempo definindo as datas de início e término.
3. Adicione ou remova transações da tabela. Observe que todas as transações listadas na tabela com a opção "Fechada" marcada serão restritas após o término do período contábil.
4. Salvar e enviar.
![Período contábil](/files/accounting-period.png)


Se você tentar enviar uma transação fechada após o término do Período Contábil, verá um erro de validação impedindo-o de fazê-lo.
![Período de contabilidade](/files/accounting-period-closed-for-transaction.png)



> 
> Observação: nenhuma função pode enviar transações definidas no período contábil, mesmo a função definida em 'Função permitida para definir contas congeladas e editar entradas congeladas' em [Configurações da conta](/docs/pt/ accounts/accounts-settings).
> 
> 
> 


## 2. Tópicos Relacionados


* [Como o período contábil é usado para fechar livros contábeis](https://frappe.io/blog/erpnext-features/closing-accounting-books-in-erpnext)
* [Comprovante de fechamento de período](/docs/pt/accounts/period-closing-voucher)
