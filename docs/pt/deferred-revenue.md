# Receita diferida



**A receita diferida refere-se a pagamentos antecipados que uma empresa recebe por produtos ou serviços que serão entregues ou executados no futuro.**


Também é conhecida como receita não obtida.


A empresa que recebe o pré-pagamento registra o valor como Receita Diferida em seu balanço como passivo. A receita diferida é um passivo porque se refere a receitas que não foram auferidas e representa produtos ou serviços devidos a um Cliente. À medida que o produto ou serviço é entregue ao longo do tempo, ele é reconhecido como receita na demonstração do resultado.


## 1. Configurando a contabilidade diferida


> Introduzido na versão 13


Antes de começar a usar a contabilidade diferida, você deve estar ciente das configurações abaixo, que lhe darão mais controle sobre como você gerencia sua contabilidade diferida.


![Configurações de contabilidade diferida](/files/deferred-accounting-settings.png)


1. **Processar lançamento contábil diferido automaticamente:** esta configuração está habilitada por padrão. Caso você não queira que os lançamentos contábeis diferidos sejam lançados automaticamente, você pode desabilitar esta configuração. Se esta configuração estiver desativada, a contabilidade diferida deverá ser processada manualmente usando [Processar contabilidade diferida](/docs/pt/accounts/process-deferred-accounting)
2. **Contratar lançamentos diferidos com base em:** O valor da receita diferida pode ser contabilizado com base em dois critérios. A opção padrão aqui é “Dias”. Se "Dias" for selecionado, o valor da receita diferida será contabilizado com base no número de dias de cada mês e se "Meses" for selecionado, então será contabilizado com base no número de meses. **Por exemplo:** se "Dias" for selecionado e a receita de US$ 12.000 tiver que ser diferida durante um período de 12 meses, então US$ 986,30 serão para o mês com 30 dias e US$ 1.019,17 serão reservados para o mês com 31 dias. dias. Se "Meses" for selecionado, a receita diferida de US$ 1.000 será reservada a cada mês, independentemente do número de dias do mês.
3. **Registrar lançamentos diferidos por meio de lançamento contábil manual:** Por padrão, os lançamentos contábeis são lançados diretamente para registrar receitas diferidas em relação a uma fatura. Para contabilizar esse lançamento de valor diferido via lançamento contábil manual, esta opção pode ser habilitada.
4. **Enviar lançamentos contábeis manuais:** esta opção será aplicável somente se lançamentos contábeis diferidos forem lançados por meio de lançamento contábil manual. Por padrão, os lançamentos contábeis manuais para lançamento diferido são mantidos no estado Rascunho e o usuário deve verificar esses lançamentos e enviá-los manualmente. Se esta opção estiver ativada, os lançamentos contábeis manuais serão enviados automaticamente sem qualquer intervenção do usuário.


## 2. Como usar a receita diferida


Os provedores de serviços de transmissão e Internet oferecem planos de assinatura trimestrais ou anuais. Eles recebem o pagamento antecipado do Cliente por alguns meses, mas registram a receita mensalmente em seu livro de contas. Esta é a Receita Diferida para o Fornecedor e [Despesa Diferida](/docs/pt/accounts/deferred-expense) para o Cliente. A seguir está como eles devem configurar a contabilidade de Receita Diferida no ERPNext para automatizar o processo.


### 2.1 Item


No cadastro de itens criado para o plano de assinatura, na seção Receita Diferida, marque o campo **Ativar Receita Diferida**. Você também pode selecionar uma conta de receita diferida para esse item específico e número de meses.


![Item com receita diferida](/files/deferred-item.png)


### 2.2 Fatura de vendas


Na criação da fatura de vendas para o item de receita diferida, em vez de lançar na conta de receita, a conta de receita diferida é creditada pelo valor da venda. Se você definiu a conta e o período no Item, as datas de início e término da conta e do serviço serão obtidas automaticamente.


![Fatura com receita diferida](/files/deferred-invoice.gif)


### 2.3 Lançamento de diário


Com base nas datas inicial e final definidas na tabela de itens da fatura de vendas, os lançamentos contábeis manuais são criados automaticamente no final de cada mês. Debita o valor da conta de Receita Diferida e credita a Conta de Receita selecionada para um Item na Fatura de Venda.


A seguir está um exemplo de receita para o item de receita diferida registrado por meio de vários lançamentos contábeis manuais.


![Receita diferida GL](/files/deferred-revenue-gl.png)


## 3. Vídeo






### 4. Tópicos Relacionados


1. [Fatura de vendas](/docs/pt/accounts/sales-invoice)
2. [Lançamento de diário](/docs/pt/accounts/journal-entry)
3. [Plano de contas](/docs/pt/accounts/chart-of-accounts)



