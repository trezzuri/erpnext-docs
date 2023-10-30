# Gratificação



> Este recurso foi introduzido na versão 13, que fará parte de um módulo de folha de pagamento separado.


**A gratificação é dada pelo empregador ao seu empregado pelos serviços por ele prestados durante o período de emprego. Geralmente é pago no momento da aposentadoria, mas pode ser pago mais cedo, desde que certas condições sejam atendidas.**


No Frappe HR você pode gerenciar pagamentos de gratificações de funcionários, com base em diferentes [Regras de gratificações](/docs/pt/human-resources/gratuity-rule) que variam de região para região.


Para acessar a Gratificação acesse:


> Página inicial > Folha de pagamento > Gratificação


## 1. Pré-requisitos


Antes de criar uma Gratificação, é aconselhável criar o seguinte:


1. [Funcionário](/docs/pt/human-resources/employee)
2. [Regra de gratuidade](/docs/pt/human-resources/gratuity-rule)
3. [Componente salarial](/docs/pt/human-resources/salary-component)


## 2. Como criar gratificação


1. Cheguei em Gratuidade > Novo
2. Selecione Regra de Funcionário e Gratificação. Ao selecioná-lo, será calculada a experiência de trabalho atual e o valor total da gratificação com base na regra da gratificação e na data de isenção.
3. Marque a caixa de seleção Pagar via comprovante de salário. se desejar pagamento de gratificação por meio do comprovante de salário.
4. Salvar e enviar


![Gratuity](/files/gratuity.png)


## 3. Métodos de pagamento de gorjetas


No Frappe RH, permitimos o pagamento do valor via Boleto Salarial ou Entrada de Pagamento.


### 3.1 Pagamento via recibo de salário


Para pagar o valor da Gratificação via Comprovante de Salário é necessário marcar a caixa de seleção **Pagar via Comprovante de Salário**. Selecione **Data da folha de pagamento** e **Componente salarial**, que aparecerão em Cheque.


![pagamento conf via comprovante de salário](/files/payment-conf-via-salary-slip.png)


Ao enviar, será criado automaticamente um Salário Adicional com a respectiva Data da Folha de Pagamento e Componente Salarial.


![pagamento de gratificação via comprovante de salário](/files/gratuity-payment-via-salary-slip.png)


### Pagamento via entrada de pagamento


Para pagar o valor da gratificação por meio de entrada de pagamento, você precisa certificar-se de que a caixa de seleção **Pagar via comprovante de salário** esteja desmarcada. Depois disso, você poderá selecionar **Conta a Pagar**, **Conta de Despesas** e **Modo de Pagamento**.


![pagamento conf via entrada de pagamento](/files/payment-conf-via-payment-entry.png)


Após enviar o registro clique no botão “Criar entrada de pagamento” que o redirecionará para o Formulário de entrada de pagamento, preencha os dados, salve e envie.


![pagamento de gratificação via entrada de pagamento](/files/gratuity-payment-via-payment-entry.png)



