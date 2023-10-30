# Despesa diferida



**Despesa diferida é um custo que já foi incorrido, mas que ainda não foi consumido.**


O custo é registado como um ativo até ao momento em que os bens ou serviços subjacentes sejam consumidos; nesse ponto, o custo é debitado como despesa. Uma Despesa Diferida é inicialmente registrada como um ativo, para que apareça no balanço patrimonial (geralmente como um Ativo Circulante, uma vez que não é utilizada no momento e provavelmente será consumida dentro de um ano).


## 1. Configurando a contabilidade diferida



> 
> Introduzido na versão 13
> 
> 
> 


Antes de começar a usar a contabilidade diferida, você deve estar ciente das configurações abaixo, que lhe darão mais controle sobre como você gerencia sua contabilidade diferida.


![Configurações de contabilidade diferida](/files/deferred-accounting-settings.png)


1. **Processar lançamento contábil diferido automaticamente:** esta configuração está habilitada por padrão. Caso não queira que os lançamentos contábeis diferidos sejam lançados automaticamente, você pode desabilitar esta configuração. Se esta configuração estiver desativada, a contabilidade diferida terá que ser processada manualmente usando [Processar contabilidade diferida](/docs/pt/accounts/process-deferred-accounting)

- **Contar lançamentos diferidos com base em:** O valor da despesa diferida pode ser contabilizado com base em dois critérios. A opção padrão aqui é “Dias”. Se for selecionado “Dias”, o valor da despesa diferida será contabilizado com base no número de dias de cada mês e se for selecionado “Meses”, então será contabilizado com base no número de meses. **Por exemplo:** se "Dias" for selecionado e a despesa de US$ 12.000 tiver que ser adiada durante um período de 12 meses, então US$ 986,30 serão para o mês com 30 dias e US$ 1.019,17 serão reservados para o mês com 31 dias. dias. Se "Meses" for selecionado, despesas diferidas de US$ 1.000 serão contabilizadas a cada mês, independentemente do número de dias do mês.
- **Livrar lançamentos diferidos por meio de lançamento contábil manual:** Por padrão, os lançamentos contábeis são lançados diretamente no registro de despesas diferidas em relação a uma fatura. Para contabilizar esse lançamento de valor diferido via lançamento contábil manual, esta opção pode ser habilitada.
- **Enviar lançamentos contábeis manuais:** esta opção será aplicável somente se lançamentos contábeis diferidos forem lançados por meio de lançamento contábil manual. Por padrão, os lançamentos contábeis manuais para lançamento diferido são mantidos no estado Rascunho e o usuário deve verificar esses lançamentos e enviá-los manualmente. Se esta opção estiver ativada, os lançamentos contábeis manuais serão enviados automaticamente sem qualquer intervenção do usuário.


## 2. Como usar a Despesa Diferida


Como exemplo de despesa diferida, a Unico Plastics paga US$ 10.000 em abril pelo aluguel de maio. Difere esse custo no momento do pagamento (em abril) na conta do ativo de aluguel pré-pago. Em maio, a Unico Plastics já consumiu o ativo pré-pago, então credita a conta do ativo de aluguel pré-pago e debita a conta de despesas de aluguel.


Outros exemplos de despesas diferidas são:


* Custos de juros capitalizados como parte de um ativo fixo para o qual os custos foram incorridos
* Seguro pago antecipadamente para cobertura em meses futuros
* O custo de um ativo fixo que é contabilizado como despesa ao longo de sua vida útil na forma de depreciação
* O custo incorrido para registrar a emissão de um instrumento de dívida
* O custo de um ativo intangível que é contabilizado como despesa ao longo de sua vida útil como amortização
* Para uma assinatura de Internet, o valor é pago antecipadamente e o serviço é entregue mensalmente. Portanto, é uma Despesa Diferida para o Cliente.


A seguir está como você pode configurar a contabilidade de despesas diferidas no ERPNext para automatizar o processo.


### 2.1 Item


No cadastro de itens, na seção Despesa Diferida, marque o campo **Ativar Despesa Diferida**. Nesta seção, você também pode selecionar uma conta de Despesa Diferida (Conta de Ativo, de preferência Ativo Circulante) para este item específico e não. de meses.


![Item com despesa diferida](/files/deferred-item-expense.png)


### 2.2 Fatura de compra


Na criação da fatura de compra para o item de despesa diferida, em vez de lançar na conta de despesas, a conta de despesas diferidas (conta de ativo) é creditada pelo valor da compra. Vamos considerar um exemplo simples de assinatura de Internet aqui:


![Fatura com despesa diferida](/files/deferred-purchase-invoice.gif)


### 2.3 Lançamento de diário


Com base nas datas inicial e final definidas na tabela item da fatura de compra, os lançamentos contábeis manuais são criados automaticamente no final de cada mês. Ele debita o valor da conta de despesas diferidas e credita a conta de despesas selecionada para um item na fatura de compra.



