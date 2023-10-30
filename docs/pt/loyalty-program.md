# Programa de fidelidade



**Um Programa de Fidelidade permite que os Clientes ganhem pontos gastando uma determinada quantia e permite que eles resgatem os pontos em compras futuras.**


Um Programa de Fidelização de Clientes é um esforço de marketing estruturado e de longo prazo que fornece incentivos para clientes recorrentes. Programas bem-sucedidos são projetados para motivar os clientes no mercado-alvo de uma empresa a retornar com frequência, fazer compras frequentes e evitar concorrentes.


Para acessar a lista do Programa de Fidelidade, acesse:



> 
> Página inicial > Varejo > Operações de varejo > Programa de fidelidade
> 
> 
> 


## 1. Pré-requisitos


Antes de criar e usar um Programa de Fidelidade, é aconselhável criar primeiro o seguinte:


1. [Cliente](/docs/pt/CRM/customer)
2. [Fatura de vendas](/docs/pt/accounts/sales-invoice)


## 2. Como criar um programa de fidelidade


1. Vá para a lista do Programa de Fidelidade e clique em Novo.
2. Insira um nome para o programa de fidelidade.
3. Selecione se o programa é de camada única ou multicamadas (ouro, prata, etc.).
4. Defina uma data de início e término para o programa.
5. Selecione o grupo de clientes e o território ao qual este programa é aplicável. O padrão é todos.
6. Para ativar todos os clientes por padrão, marque "Ativação automática (para todos os clientes)". Caso contrário, o programa precisa ser atribuído a partir do [Mestre do cliente](/docs/pt/accounts/loyalty-program#22-loyalty-points-in-customer).
7. Na tabela, insira:
	2. **Nome do nível**: a ser atribuído a um Cliente com base em sua elegibilidade.
	3. **Fator de Coleta**: Quanto valor precisa ser gasto para ganhar 1 Ponto de Fidelidade no ERPNext.
	4. **Valor mínimo**: valor mínimo a ser gasto para se qualificar para um nível.
8. Defina o Fator de Conversão, por exemplo: 10 USD = 1 ponto.
9. Salvar.


![Programa de fidelidade](/files/loyalty-program.png)


### 2.1 Seção de resgate


* **Fator de conversão**: ao resgatar pontos de fidelidade, esse fator decide quanto vale 1 ponto de fidelidade. Por exemplo, se um Cliente tiver 100 Pontos de Fidelidade e 1 Ponto de Fidelidade = 1 USD, então o Cliente usará Itens de até 100 USD com seus pontos de fidelidade para compras futuras.
* **Conta de despesas**: defina uma conta de despesas onde você oferecerá os benefícios. Isso é útil para monitorar os benefícios oferecidos separadamente.
* **Duração de Validade (em dias)**: Os pontos de fidelidade coletados expirarão após o número de dias definido neste campo.


### 2.2 pontos de fidelidade no cliente


Defina uma seção do Programa de Fidelidade no cadastro do Cliente para atribuir um Programa de Fidelidade a um Cliente.


![Programa de fidelidade no cliente](/files/loyalty-program-in-customer.png)


Os **pontos de fidelidade** ganhos podem ser visualizados no painel do Cliente.


![Pontos de fidelidade](/files/loyalty-points-in-customer.png)


### 2.3 Entrada de pontos de fidelidade


Acesse: **Contas > Operações de varejo > Entrada de pontos de fidelidade**.
Isto funciona como um registro para fornecer uma visão geral de qual Cliente ganhou quantos pontos em relação a cada Fatura de Venda. Contém os dados da Fatura e do Cliente.


![Entrada no programa de fidelidade](/files/loyalty-program-entry.png)


## 3. Como funciona um Programa de Fidelidade?


### 3.1 Ganhar pontos


* Em primeiro lugar, um **Programa de Fidelidade** precisa ser criado conforme explicado na primeira seção.
* Atribuir este **Programa de Fidelidade** a um **Cliente**.
* Crie uma nova fatura de vendas para o **Cliente** ao qual você atribuiu o **Programa de Fidelidade**.
* Para este exemplo, uma fatura é criada com um total geral de 3.000 INR e de acordo com o **Programa de Fidelidade** para um gasto mínimo de 2.000 INR, o fator de cobrança Silver Tier será elegível e para cada 300 INR gastos, o **Cliente** receberá 1 ponto (portanto, o total de pontos ganhos nesta transação é 15).
* Após o envio da fatura, uma **entrada de pontos de fidelidade** será criada para esta fatura (conforme mostrado acima na seção Entrada no programa de fidelidade).
* Em nosso **Programa de Fidelidade**, após um gasto mínimo de 6.000, o nível Gold seria elegível. Assim, quando for apresentada outra fatura com o mesmo valor, o total de vendas deste Cliente passa a ser 6.000. Portanto, agora, o **Cliente** será automaticamente atualizado para o nível Gold.



> 
> Observação: O mínimo gasto no Programa Fidelidade não significa valor mínimo para uma única fatura. Em vez disso, significa a soma do valor das faturas do Cliente sob um esquema específico do Programa de Fidelidade.
> 
> 
> 


### 3.2 Resgate de pontos


* Vamos continuar com o exemplo acima, onde criamos 1 fatura e ganhamos 15 pontos com ela. Ao criar outra fatura para o mesmo Cliente, vá até a seção Pontos de Fidelidade e ative a caixa de seleção ‘Resgatar Pontos de Fidelidade’.
![Resgatar pontos de fidelidade](/files/redeem-loyalty-points.png)
* Os campos para 'Ponto de Fidelidade', 'Conta de Resgate' e 'Centro de Custo de Resgate' ficarão visíveis nesta seção. A conta e o Centro de Custo serão obtidos no **Programa de Fidelidade** atribuído ao **Cliente**.
* Como o Cliente ganhou 15 pontos, podemos utilizá-los todos até o vencimento. Se tentarmos usar mais do que temos, um erro será gerado.
* No exemplo acima, usamos 6.375 pontos para serem resgatados. Isso ativará outro campo que exibirá o valor calculado usando (ponto de fidelidade \* Fator de conversão). Portanto, US$ 6.375 serão deduzidos do valor, já que nosso 'Fator de conversão' era '1'.
* Quando enviadas, serão criadas 2 **inscrições de pontos de fidelidade**. Um para resgatado, que será um valor negativo e outro para a fatura atual.
![Loyalty Point](/files/loyalty-point-entry-redeem.png)



> 
> Observação: para uma fatura na qual foram ganhos pontos, se uma fatura de devolução for criada, ela excluirá a entrada de pontos de fidelidade original e criará uma nova após subtrair o valor devolvido do valor original. Além disso, ao cancelar uma fatura, a entrada subsequente de Pontos de Fidelidade será excluída.
> 
> 
> 


### 4. Tópicos Relacionados


1. [Centro de custos](/docs/pt/accounts/cost-center)
2. [Fatura de vendas](/docs/pt/accounts/sales-invoice)
3. [Cliente](/docs/pt/CRM/customer)
4. [Grupo de clientes](/docs/pt/CRM/customer-group)



