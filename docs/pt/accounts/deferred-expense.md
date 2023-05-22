# Despesa Diferida


**Despesa diferida é um custo que já foi incorrido, mas que ainda não foi consumido.**


O custo é registrado como um ativo até o momento em que os bens ou serviços subjacentes são consumidos; nesse ponto, o custo é cobrado como despesa. Uma Despesa Diferida é inicialmente registrada como um ativo, para que apareça no balanço (geralmente como um Ativo Circulante, uma vez que não é usado até agora e provavelmente será consumido dentro de um ano).


## 1. Configurando Contabilidade Diferida



> 
> Introduzido na versão 13
> 
> 
> 


Antes de começar a usar a contabilidade diferida, você deve estar ciente das configurações abaixo, que lhe darão mais controle sobre como você gerencia sua contabilidade diferida


![Deferred Accounting Settings](/files/deferred-accounting-settings.png)


1. **Processar entrada contábil diferida automaticamente:** essa configuração é ativada por padrão. Caso você não queira que os lançamentos contábeis diferidos sejam lançados automaticamente, você pode desabilitar esta configuração. Se esta configuração estiver desativada, a contabilidade diferida terá que ser processada manualmente usando [Processar contabilidade diferida](/docs/pt/accounts/process-deferred-accounting)
2. **Reservar entradas diferidas com base em:** O valor da despesa diferida pode ser contabilizado com base em dois critérios. A opção padrão aqui é "Dias". Se "Dias" for selecionado, o valor da despesa diferida será contabilizado com base no número de dias de cada mês e, se for selecionado "Meses", será contabilizado com base no número de meses. **Por exemplo:** Se "Dias" for selecionado e a despesa de $ 12.000 tiver que ser adiada por um período de 12 meses, então $ 986,30 serão para o mês com 30 dias e $ 1.019,17 serão reservados para o mês com 31 dias. Se "Meses" for selecionado, despesas diferidas de US$ 1.000 serão registradas a cada mês, independentemente do número de dias em um mês.
3. **Liberar lançamentos diferidos por meio de lançamento contábil manual:** por padrão, os lançamentos contábeis são lançados diretamente para registrar despesas diferidas em relação a uma fatura. Para contabilizar esse lançamento de valor diferido por meio do lançamento contábil manual, essa opção pode ser habilitada.
4. **Enviar lançamentos contábeis manuais:** esta opção é aplicável somente se lançamentos contábeis diferidos forem lançados por meio de lançamento contábil manual. Por padrão, os lançamentos contábeis adiados são mantidos no estado Rascunho e o usuário precisa verificar esses lançamentos e enviá-los manualmente. Se esta opção estiver habilitada, os lançamentos contábeis serão enviados automaticamente sem qualquer intervenção do usuário.


## 2. Como usar Despesas Diferidas


Como exemplo de Despesa Diferida, a Unico Plastics paga US$ 10.000 em abril pelo aluguel de maio. Ele adia esse custo no momento do pagamento (em abril) na conta do ativo de aluguel pré-pago. Em maio, a Unico Plastics já consumiu o ativo pré-pago, então ela credita a conta do ativo de aluguel pré-pago e debita a conta de despesas de aluguel.


Outros exemplos de despesas diferidas são:


* Custos de juros que são capitalizados como parte de um ativo fixo para o qual os custos foram incorridos
* Seguro pago antecipadamente para cobertura nos próximos meses
* O custo de um ativo fixo que é cobrado como despesa ao longo de sua vida útil na forma de depreciação
* O custo incorrido para registrar a emissão de um instrumento de dívida
* O custo de um ativo intangível que é cobrado como despesa ao longo de sua vida útil como amortização
* Para uma Assinatura de Internet, o valor é pago antecipadamente e o serviço é prestado mensalmente. Portanto, é Despesa Diferida para o Cliente.


A seguir, você pode configurar a contabilidade de despesas diferidas no ERPNext para automatizar o processo.


### 2.1 Item


No cadastro de itens, na seção Despesas diferidas, marque o campo **Ativar despesas diferidas**. Nesta seção, você também pode selecionar uma conta de Despesas Diferidas (Conta de Ativo, de preferência Ativo Circulante) para este item específico e não. de meses.


![Item com despesa diferida](/files/deferred-item-expense.png)


### 2.2 Fatura de compra


Ao criar a Fatura de Compra para o Item de Despesa Diferida, em vez de lançar na Conta de Despesas, a conta de Despesas Diferidas (conta de Ativo) é creditada pelo valor da compra. Vamos considerar um exemplo simples de assinatura de Internet aqui:


![Fatura com despesas diferidas](/files/deferred-purchase-invoice.gif)


### 2.3 Entrada no diário


Com base nas datas inicial e final definidas na tabela Item da fatura de compra, os lançamentos contábeis manuais são criados automaticamente no final de cada mês. Debita o valor da conta de Despesas Diferidas e credita a Conta de Despesas selecionada para um Item na Nota Fiscal de Compra.

