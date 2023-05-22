# Incluir imposto ou cobrança na avaliação ou total?


O campo Considerar Imposto ou Encargo na tabela de Impostos e Encargos das transações de compra ou venda tem três valores.


* Total
* Valorização
* Total e avaliação


![Valuation And Total](/files/valuation-and-total.png)


Vamos considerar um exemplo para entender um efeito de cada tipo de cobrança. Compramos dez unidades do item, à taxa de $ 800. O valor total da compra é $ 800. O item comprado tem 4% de IVA aplicado e INR 100 foi incorrido no transporte.


#### Total:


Taxa ou cobrança categorizada como **Total** será incluída no total das transações de compra. Mas não terá impacto na avaliação do item comprado.


Se o IVA de 4% for aplicado no item, será INR 32 (a taxa baseada no item é de 800). Sendo o IVA o imposto sobre o consumo, deverá ser adicionado ao valor da Ordem de Compra/Factura, uma vez que será incluído na conta a pagar ao fornecedor. Mas não deve ser adicionado ao valor do item comprado.


Quando a fatura de compra for enviada, o lançamento do razão geral será feito para impostos/cobrança categorizados como Total.


#### Valorização:


O imposto ou cobrança categorizada como **Valorização** será adicionado ao valor do item comprado, mas não ao total dessa transação de compra.


A taxa de transporte de INR 100 deve ser categorizada como avaliação. Com isso, o valor do item comprado passará de 800 para 900. Além disso, essa cobrança não será somada ao total da transação de compra, pois é uma despesa sua, e não deve ser repassada ao fornecedor.


Verifique [aqui](/docs/pt/stock/perpetual-inventory) para saber sobre lançamentos gerais feitos para despesas categorizadas como avaliação.


#### Total e avaliação:


Taxa ou Taxa categorizada como **Total e Avaliação** será adicionada na avaliação do item, bem como nos totais das transações de compra.


Vamos supor que o transporte seja providenciado pelo nosso fornecedor, mas precisamos pagar as taxas de transporte a eles. Nesse caso, para despesas de transporte, a categoria selecionada deve ser Total e Avaliação. Com isso, a taxa de transporte de INR 100 será adicionada ao valor real da compra de 800. Além disso, INR 100 será refletido no total, pois será pago por nós ao fornecedor.

