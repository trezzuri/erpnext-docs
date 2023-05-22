# Programa de fidelidade


**Um Programa de Fidelidade permite que os Clientes ganhem pontos ao gastar um determinado valor e permite resgatar os pontos em compras futuras.**


Um Programa de Fidelidade de Clientes é um esforço de marketing estruturado e de longo prazo que fornece incentivos para clientes recorrentes. Os programas bem-sucedidos são projetados para motivar os clientes no mercado-alvo de uma empresa a retornar com frequência, fazer compras frequentes e evitar concorrentes.


Para acessar a lista do Programa de Fidelidade, acesse:



> 
> Página inicial > Varejo > Operações de varejo > Programa de fidelidade
> 
> 
> 


## 1. Pré-requisitos


Antes de criar e usar um Programa de Fidelidade, é recomendável criar primeiro o seguinte:


1. [Cliente](/docs/pt/CRM/customer)
2. [Fatura de vendas](/docs/pt/accounts/sales-invoice)


## 2. Como criar um programa de fidelidade


1. Vá para a lista do Programa de Fidelidade e clique em Novo.
2. Digite um nome para o programa de fidelidade.
3. Selecione se o programa é de camada única ou de várias camadas (ouro, prata etc.).
4. Defina uma data de início e término para o programa.
5. Selecione o Grupo de Clientes e Território para os quais este programa é aplicável, o padrão é todos.
6. Para ativar todos os clientes por padrão, marque 'Aceitação automática (para todos os clientes)'. Caso contrário, o programa precisa ser atribuído a partir do [Mestre do cliente](/docs/pt/accounts/loyalty-program#22-loyalty-points-in-customer).
7. Na tabela, digite:
	2. **Nome do nível**: a ser atribuído a um cliente com base em sua elegibilidade.
	3. **Fator de Arrecadação**: Quanto precisa ser gasto para ganhar 1 Ponto de Fidelidade no SOMA.
	4. **Valor mínimo**: valor mínimo a ser gasto para se qualificar para uma modalidade.
8. Defina o fator de conversão, por exemplo: 10 USD = 1 ponto.
9. Salvar.


![Programa de fidelidade](/files/loyalty-program.png)


### 2.1 Seção de resgate


* **Fator de conversão**: ao resgatar pontos de fidelidade, esse fator decide quanto dinheiro vale 1 ponto de fidelidade. Por exemplo, se um cliente tiver 100 pontos de fidelidade e 1 ponto de fidelidade = 1 USD, o cliente usará itens de até 100 USD com seus pontos de fidelidade para compras futuras.
* **Conta de Despesas**: Defina uma Conta de Despesas a partir da qual você oferecerá os benefícios. Isso é útil para rastrear os benefícios oferecidos separadamente.
* **Duração da expiração (em dias)**: Os pontos de fidelidade coletados expirarão após o número de dias definido neste campo.


### 2.2 Pontos de fidelidade no cliente


Defina uma seção do Programa de fidelidade no cadastro de clientes para atribuir um Programa de fidelidade a um cliente.


![Programa de fidelidade no cliente](/files/loyalty-program-in-customer.png)


Os **pontos de fidelidade** ganhos podem ser visualizados no painel do cliente.


![Pontos de fidelidade](/files/loyalty-points-in-customer.png)


### 2.3 Entrada de ponto de fidelidade


Vá para: **Contas > Operações de varejo > Entrada de ponto de fidelidade**.
Isso funciona como um registro para fornecer uma visão geral de qual cliente ganhou quantos pontos em relação a qual fatura de venda. Ele contém os dados da Fatura e do Cliente.


![Entrada no Programa de Fidelidade](/files/loyalty-program-entry.png)


## 3. Como funciona um Programa de Fidelidade?


### 3.1 Ganhando pontos


* Em primeiro lugar, um **Programa de Fidelidade** precisa ser criado conforme explicado na primeira seção.
* Atribua este **Programa de Fidelidade** a um **Cliente**.
* Crie uma nova Fatura de Venda para o **Cliente** ao qual você atribuiu o **Programa de Fidelidade**.
* Para este exemplo, uma fatura é criada com um total geral de 3.000 INR e, de acordo com o **Programa de fidelidade**, para um gasto mínimo de 2.000 INR, o fator de cobrança Silver Tier será elegível e para cada 300 INR gastos, o **Cliente** receberá 1 ponto (portanto, o total de pontos ganhos nesta transação é 15).
* Após o envio da fatura, uma **Entrada de ponto de fidelidade** será criada para esta fatura (conforme mostrado acima na seção Entrada no programa de fidelidade).
* Em nosso **Programa de Fidelidade**, com um gasto mínimo de 6.000, o nível Gold seria qualificado. Assim, ao enviar outra fatura com o mesmo valor, o total de vendas deste Cliente passa a 6.000. Agora, o **Cliente** será atualizado automaticamente para o nível Gold.



> 
> Observação: O mínimo gasto no Programa de Fidelidade não significa um valor mínimo para uma única fatura. Em vez disso, significa a soma do valor das faturas para o Cliente em um esquema específico do Programa de Fidelidade.
> 
> 
> 


### 3.2 Resgate de pontos


* Vamos continuar a partir do exemplo acima, onde criamos 1 fatura e ganhamos 15 pontos com ela. Ao criar outra fatura para o mesmo Cliente, aceda à secção Pontos Fidelidade e ative a caixa de seleção 'Trocar Pontos Fidelidade'.
![Resgatar pontos de fidelidade](/files/redeem-loyalty-points.png)
* Os campos 'Ponto de Fidelidade', 'Conta de Resgate' e 'Centro de Custo de Resgate' ficarão visíveis nesta seção. A conta e o Centro de Custos serão buscados no **Programa de Fidelidade** atribuído ao **Cliente**.
* Como o cliente ganhou 15 pontos, podemos usar todos até o vencimento. Se tentarmos usar mais do que temos, um erro será lançado.
* No exemplo acima, usamos 6375 pontos a serem resgatados. Ao fazer isso, outro campo será ativado, exibindo o valor calculado usando (ponto de fidelidade \* Fator de conversão). Portanto, USD 6.375 serão deduzidos de nosso valor, pois nosso 'Fator de conversão' era '1'.
* Ao enviar, 2 **Entradas de pontos de fidelidade** serão criadas. Uma para resgatados, que será um valor negativo e outra para a fatura atual.
![Loyalty Point](/files/loyalty-point-entry-redeem.png)



> 
> Observação: Para uma fatura na qual os pontos foram ganhos, se uma fatura de devolução for criada, ela excluirá a Entrada de Ponto de Fidelidade original e criará uma nova depois de subtrair o valor devolvido do valor original. Além disso, ao cancelar uma fatura, sua entrada de ponto de fidelidade subsequente será excluída.
> 
> 
> 


### 4. Tópicos Relacionados


1. [Centro de custo](/docs/pt/accounts/cost-center)
2. [Fatura de vendas](/docs/pt/accounts/sales-invoice)
3. [Cliente](/docs/pt/CRM/customer)
4. [Grupo de clientes](/docs/pt/CRM/customer-group)
