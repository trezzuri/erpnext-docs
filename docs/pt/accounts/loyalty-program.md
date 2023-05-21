# Programa de lealdade


**Um Programa de Fidelidade permite que os Clientes ganhem pontos ao gastar um determinado valor e os resgatem em compras futuras.**


Um Programa de Fidelidade do Cliente é um esforço de marketing estruturado e de longo prazo que fornece incentivos para clientes recorrentes. Programas bem-sucedidos são projetados para motivar os clientes no mercado-alvo de uma empresa a retornar com frequência, fazer compras frequentes e evitar concorrentes.


Para acessar a lista do Programa de Fidelidade, acesse:



>
> Home > Varejo > Operações de Varejo > Programa de Fidelidade
>
>
>


## 1. Pré-requisitos


Antes de criar e usar um Programa de Fidelidade, é aconselhável criar primeiro o seguinte:


1. [Cliente](/docs/v13/user/manual/en/CRM/cliente)
2. [Fatura de vendas](/docs/v13/user/manual/en/accounts/fatura de vendas)


## 2. Como criar um programa de fidelidade


1. Acesse a lista Programa de Fidelidade e clique em Novo.
2. Digite um Nome para o Programa de Fidelidade.
3. Selecione se o programa é de Camada Única ou Camada Múltipla (ouro, prata, etc.).
4. Defina uma data inicial e final para o programa.
5. Selecione o Grupo de Clientes e Território para os quais este programa é aplicável, o padrão é todos.
6. Para optar por todos os clientes por padrão, marque 'Auto Opt In (para todos os clientes)'. Caso contrário, o programa precisa ser atribuído a partir do [Mestre do cliente](/docs/v13/user/manual/en/accounts/loyalty-program#22-loyalty-points-in-customer).
7. Na tabela, digite:
2. **Nome do nível**: A ser atribuído a um cliente com base em sua elegibilidade.
3. **Fator de Arrecadação**: Quanto precisa ser gasto para ganhar 1 Ponto Fidelidade no ERPNext.
4. **Montante Mínimo**: Valor mínimo a ser gasto para se qualificar para uma categoria.
8. Defina o fator de conversão, por exemplo: 10 USD = 1 ponto.
9. Salve.


![Programa de fidelidade](/files/loyalty-program.png)


### 2.1 Seção de Resgate


* **Fator de Conversão**: Ao resgatar pontos de fidelidade, este fator decide quanto dinheiro vale 1 Ponto de Fidelidade. Por exemplo, se um cliente tiver 100 pontos de fidelidade e 1 ponto de fidelidade = 1 USD, o cliente usará itens de até 100 USD com seus pontos de fidelidade para compras futuras.
* **Conta de Despesas**: Defina uma Conta de Despesas de onde você oferecerá os benefícios. Isso é útil para rastrear os benefícios oferecidos separadamente.
* **Duração da expiração (em dias)**: Os pontos de fidelidade acumulados expirarão após o número de dias definido neste campo.


### 2.2 Pontos de Fidelização no Cliente


Defina uma seção do Programa de Fidelidade no mestre de Clientes para atribuir um Programa de Fidelidade a um Cliente.


![Programa de fidelidade no cliente](/files/loyalty-program-in-customer.png)


Os **pontos de fidelidade** ganhos podem ser visualizados no painel do cliente.


![Pontos de fidelidade](/files/loyalty-points-in-customer.png)


### 2.3 Entrada de ponto de fidelidade


Acesse: **Contas > Operações de varejo > Entrada de ponto de fidelidade**.
Isso funciona como um registro para fornecer uma visão geral de qual cliente ganhou quantos pontos em relação a qual fatura de venda. Contém os dados Nota Fiscal e Cliente.


![Entrada no Programa de Fidelidade](/files/loyalty-program-entry.png)


## 3. Como funciona um Programa de Fidelidade?


### 3.1 Ganhando Pontos


* Primeiramente, um **Programa de Fidelidade** precisa ser criado conforme explicado na primeira seção.
* Atribua este **Programa de Fidelidade** a um **Cliente**.
* Crie uma nova Nota Fiscal de Venda para o **Cliente** ao qual você atribuiu o **Programa de Fidelidade**.
* Para este exemplo, uma fatura é criada com um total geral de 3.000 INR e de acordo com o **Programa de Fidelidade** para um gasto mínimo de 2.000 INR, o fator de cobrança Silver Tier será elegível e para cada 300 INR gastos, o **Cliente** receberá 1 ponto (portanto, o total de pontos ganhos nesta transação é 15).
* Após o envio da fatura, uma **Entrada de Ponto de Fidelidade** será criada para esta fatura (conforme mostrado acima na seção Entrada no Programa de Fidelidade).
* Em nosso **Programa de Fidelidade**, com um gasto mínimo de 6.000, o nível Gold seria elegível. Assim, ao enviar outra fatura com o mesmo valor, o total de vendas deste Cliente passa a 6.000. Agora, o **Cliente** será atualizado automaticamente para o nível Gold.



>
> Observação: O mínimo gasto no Programa de Fidelidade não significa um valor mínimo para uma única fatura. Em vez disso, significa a soma do valor das faturas do Cliente em um determinado esquema de Programa de Fidelidade.
>
>
>


### 3.2 Resgate de Pontos


* Vamos continuar com o exemplo acima, onde criamos 1 fatura e ganhamos 15 pontos com ela. Ao criar outra fatura para o mesmo Cliente, aceda à secção Pontos Fidelidade e ative a caixa de seleção 'Trocar Pontos Fidelidade'.
![Resgatar pontos de fidelidade](/files/redeem-loyalty-points.png)
* Os campos 'Ponto Fidelidade', 'Conta de Resgate' e 'Centro de Custo de Resgate' ficarão visíveis nesta seção. A conta e o Centro de Custo serão buscados no **Programa de Fidelidade** atribuído ao **Cliente**.
* Como o cliente ganhou 15 pontos, podemos usar todos até o vencimento. Se tentarmos usar mais do que temos, um erro será lançado.
* No exemplo acima, usamos 6375 pontos a serem resgatados. Fazê-lo vai habilitar outro campo que exibirá o valor calculado usando (ponto de fidelidade \* fator de conversão). Portanto, USD 6375 serão deduzidos de nosso valor, pois nosso 'Fator de conversão' era '1'.
* Quando enviado, 2 **Entradas de pontos de fidelidade** serão criadas. Uma para resgatados, que será um valor negativo e outra para a fatura atual.
![Ponto de fidelidade](/files/loyalty-point-entry-redeem.png)



>
> Nota: Para uma fatura na qual os pontos foram ganhos, se uma fatura de devolução for criada, ela excluirá a Entrada de Ponto de Fidelidade original e criará uma nova depois de subtrair o valor devolvido do valor original. Além disso, ao cancelar uma fatura, sua entrada de ponto de fidelidade subsequente será excluída.
>
>
>


### 4. Tópicos Relacionados


1. [Centro de custo](/docs/v13/user/manual/en/accounts/cost-center)
2. [Fatura de vendas](/docs/v13/user/manual/en/accounts/fatura de vendas)
3. [Cliente](/docs/v13/user/manual/en/CRM/cliente)
4. [Grupo de clientes](/docs/v13/user/manual/en/CRM/customer-group)