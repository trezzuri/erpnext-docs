# Receita Diferida


**Receita diferida refere-se a pagamentos antecipados que uma empresa recebe por produtos ou serviços que serão entregues ou executados no futuro.**


Também é conhecido como receita não auferida.


A empresa que recebe o pagamento antecipado registra o valor como Receita Diferida em seu balanço como um passivo. A receita diferida é um passivo porque se refere à receita que não foi obtida e representa produtos ou serviços devidos a um Cliente. À medida que o produto ou serviço é entregue ao longo do tempo, ele é reconhecido como receita na demonstração do resultado.


## 1. Configurando Contabilidade Diferida



> 
> Introduzido na versão 13
> 
> 
> 


Antes de começar a usar a contabilidade diferida, você deve estar ciente das configurações abaixo, que lhe darão mais controle sobre como você gerencia sua contabilidade diferida


![Deferred Accounting Settings](/files/deferred-accounting-settings.png)


1. **Processar entrada contábil diferida automaticamente:** essa configuração é ativada por padrão. Caso você não queira que os lançamentos contábeis diferidos sejam lançados automaticamente, você pode desabilitar esta configuração. Se esta configuração estiver desativada, a contabilidade diferida terá que ser processada manualmente usando [Processar contabilidade diferida](/docs/pt/accounts/process-deferred-accounting)
2. **Reservar entradas diferidas com base em:** O valor da receita diferida pode ser contabilizado com base em dois critérios. A opção padrão aqui é "Dias". Se "Dias" for selecionado, o valor da receita diferida será contabilizado com base no número de dias de cada mês e, se "Meses" for selecionado, será contabilizado com base no número de meses. **Por exemplo:** Se "Dias" for selecionado e a receita de US$ 12.000 tiver que ser adiada por um período de 12 meses, então US$ 986,30 serão para o mês com 30 dias e US$ 1.019,17 serão reservados para o mês com 31 dias. Se "Meses" for selecionado, a receita diferida de US$ 1.000 será registrada a cada mês, independentemente do número de dias em um mês.
3. **Liberar lançamentos diferidos por meio de lançamento contábil manual:** por padrão, os lançamentos contábeis são lançados diretamente para registrar receita diferida em relação a uma fatura. Para contabilizar esse lançamento de valor diferido por meio do lançamento contábil manual, essa opção pode ser habilitada.
4. **Enviar lançamentos contábeis manuais:** esta opção é aplicável somente se lançamentos contábeis diferidos forem lançados por meio de lançamento contábil manual. Por padrão, os lançamentos contábeis adiados são mantidos no estado Rascunho e o usuário precisa verificar esses lançamentos e enviá-los manualmente. Se esta opção estiver habilitada, os lançamentos contábeis serão enviados automaticamente sem qualquer intervenção do usuário.


## 2. Como usar receita diferida


Os provedores de serviços de transmissão e Internet oferecem planos de assinatura trimestrais ou anuais. Eles recebem o pagamento adiantado do cliente por alguns meses, mas registram a receita mensalmente em seu livro de contas. Esta é a Receita Diferida para o Fornecedor e [Despesa Diferida](/docs/pt/accounts/deferred-expense) para o Cliente. Veja a seguir como eles devem configurar a contabilidade de receita diferida no ERPNext para automatizar o processo.


### 2.1 Item


No mestre de itens criado para o plano de assinatura, na seção Receita diferida, marque o campo **Ativar receita diferida**. Você também pode selecionar uma conta de receita diferida para este item específico e número de meses.


![Item com receita diferida](/files/deferred-item.png)


### 2.2 Fatura de vendas


Ao criar a Nota Fiscal de Venda do Item de Receita Diferida, ao invés de lançar na Conta de Receita, a conta de Receita Diferida é creditada pelo valor da venda. Se você definiu a conta e o período no Item, as datas de início e término da conta e do serviço serão buscadas automaticamente.


![Fatura com receita diferida](/files/deferred-invoice.gif)


### 2.3 Entrada no diário


Com base nas datas inicial e final definidas na tabela Item da fatura de vendas, os lançamentos contábeis manuais são criados automaticamente no final de cada mês. Debita o valor da conta de Receitas Diferidas e credita a Conta de Receitas selecionada para um Item na Nota Fiscal de Venda.


A seguir está um exemplo de receita para o item de receita diferida registrado por meio de vários lançamentos contábeis.


![Deferred Revenue GL](/files/deferred-revenue-gl.png)


## 3. Vídeo






### 4. Tópicos Relacionados


1. [Fatura de vendas](/docs/pt/accounts/sales-invoice)
2. [Entrada de diário](/docs/pt/accounts/journal-entry)
3. [Plano de contas](/docs/pt/accounts/chart-of-accounts)
