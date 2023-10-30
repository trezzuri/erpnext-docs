# Período contábil



**Um Período Contábil define um período de tempo no qual as demonstrações financeiras são registradas.**

No ERPNext, o Período Contábil é um período fora do qual as transações submissíveis selecionadas (como Vendas/Fatura de compra, lançamento de estoque, lançamento de folha de pagamento, lançamento contábil manual, etc.) não podem ser criados. Em outras palavras, as transações selecionadas só podem ser criadas dentro do Período Contábil definido.

**Por que o Período Contábil é necessário?**

Quando as transações são enviadas , eles afetam os ledgers e os relatórios que processam os dados do ledger. Isso pode causar problemas quando relatórios financeiros precisam ser gerados para auditoria pelas autoridades ou para fechamento dos livros contábeis do exercício financeiro.

Aqui o Período Contábil pode ser usado para limitar o período de tempo dentro do qual as transações podem ser enviadas. preservar a integridade dos relatórios correspondentes.

## 1. Como criar um período contábil

### 1.1 Para que serve a opção "Fechado" para as transações selecionadas?

![Tabela filho do período contábil](/files/accounting-period-closed.png)![]()

A opção "Fechado" na tabela filho para tipos de documentos de transação é usada para selecionar quais deles serão restritos após o final do Período Contábil.

 Observe que se o Período Contábil terminar e se alguma das transações selecionadas na tabela secundária não tiver a opção "Fechada" marcada, elas não serão restritas após o término do Período Contábil.

1. Insira um nome para o período contábil.
2. Defina um período definindo datas de início e término.
3. Adicione ou remova transações da tabela. Observe que todas as transações listadas na tabela com a opção "Fechada" marcada serão restritas após o término do período contábil.
4. Salvar e enviar. ![Período contábil](/files/accounting-period.png)![]()

Se você tentar salvar uma transação fechada após o término do período contábil, você verá um erro de validação impedindo de fazer isso. ![Período contábil](/files/accounting-period-closed-for-transaction.png)![]()  



> Nota: Nenhuma função pode salvar ou enviar transações definidas no Período Contábil, mesmo a Função definida em ' Função com permissão para definir contas congeladas e editar entradas congeladas em [Configurações da conta](/docs/pt/accounts/accounts-settings).
> 
> 

## 2. Tópicos Relacionados

* [Como o período contábil é usado para fechar livros contábeis](https://frappe.io/blog/erpnext-features/closing-accounting-books-in-erpnext)
* [Voucher de encerramento do período](/docs/pt/contas/voucher de encerramento do período)


