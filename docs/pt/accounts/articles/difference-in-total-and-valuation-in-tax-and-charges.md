# Incluir impostos ou taxas na avaliação ou no total?



Considere que o campo Imposto ou Encargo na tabela Impostos e Encargos das transações de compra ou venda tem três valores.


* Total
* Avaliação
* Total e avaliação


![Avaliação e total](/files/avaliação-and-total.png)


Vamos considerar um exemplo para entender o efeito de cada tipo de cobrança. Compramos dez unidades do item, à taxa de 800. O valor total da compra é 800. O item adquirido tem 4% de IVA aplicado e INR 100 foi incorrido no transporte.


#### Total:


Imposto ou Taxa categorizado como **Total** será incluído no total das transações de compra. Mas não terá impacto na avaliação do item adquirido.


Se o IVA de 4% for aplicado ao item, ele totalizará INR 32 (a alíquota baseada no item é 800). Sendo o IVA o imposto sobre o consumo, deverá ser adicionado ao valor da Nota de Encomenda/Fatura, uma vez que será incluído na conta a pagar ao fornecedor. Mas não deve ser adicionado ao valor do item adquirido.


Quando a fatura de compra for enviada, o lançamento no razão geral será feito para impostos/cobranças categorizados como Total.


#### Avaliação:


Imposto ou cobrança categorizada como **Avaliação** será adicionada ao valor do item comprado, mas não ao total da transação de compra.


A taxa de transporte de INR 100 deve ser categorizada como avaliação. Com isso, o valor do item adquirido será aumentado de 800 para 900. Além disso, esse encargo não será adicionado ao total da transação de compra, pois é uma despesa sua e não deve ser refletida ao fornecedor.


Confira [aqui](/docs/pt/stock/perpetual-inventory) para saber o lançamento geral feito para despesas categorizadas como Avaliação.


#### Total e avaliação:


Imposto ou Encargo categorizado como **Total e Avaliação** serão adicionados na avaliação do item, bem como nos totais das transações de compra.


Vamos supor que o transporte seja providenciado pelo nosso fornecedor, mas precisamos pagar as despesas de transporte a ele. Nesse caso, para despesas de transporte, a categoria selecionada deverá ser Total e Avaliação. Com isso, a taxa de transporte de INR 100 será adicionada ao valor real da compra de 800. Além disso, INR 100 será refletido no total, pois será pago por nós ao fornecedor.



