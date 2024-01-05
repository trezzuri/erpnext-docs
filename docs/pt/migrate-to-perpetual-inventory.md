# Migrar para o inventário permanente



A avaliação de estoque permanente está ativada por padrão no sistema.


Para os usuários que atualmente seguem o sistema de avaliação de estoque periódico e desejam migrar para o sistema de avaliação de estoque permanente, siga as etapas explicadas abaixo.


### 1. Como migrar para o inventário permanente


1. Para ativar o estoque permanente, certifique-se de que a conta de estoque em mãos esteja sincronizada com o valor real do estoque em seu(s) armazém(s). Para sincronizá-lo, você terá que criar um lançamento contábil manual para o valor da diferença em relação à conta de despesas (geralmente usado na fatura de compra).


Por exemplo, quando o estoque permanente foi desativado, você deve ter despesas (custo dos produtos vendidos) registradas por meio de faturas de compra. Agora, você terá que criar um lançamento contábil manual para mover o valor do estoque existente da conta de despesas para a conta de estoque em estoque.


Cr. Conta de despesas ......... XXX


Dr. Conta de estoque em mãos... XXX


Também pode funcionar de forma inversa se você estiver selecionando uma conta de estoque em estoque na fatura de compra.
2. Antes de ativar o estoque permanente, certifique-se de que as contas de estoque (razão) estejam vinculadas ao armazém existente. A conta de estoque de um Armazém pode ser definida em três níveis.


	* No próprio mestre do armazém
	* No mestre do armazém pai
	* Conta de estoque em estoque padrão no mestre da empresa, se você mantiver apenas uma conta de estoque em estoque para todos os armazéns.
3. Lançamento diário para atualizar o estoque recebido, mas não a conta faturada


Uma conta "Estoque recebido mas não faturado" é uma conta de ajuste que reflete o valor do estoque para o qual o recibo de compra foi enviado, mas a fatura de compra ainda não foi criada. Um lançamento contábil manual deve ser criado para atualizar o valor do recibo de compra aberto pendente para faturamento na conta "Estoque recebido, mas não faturado".


Para saber o valor do stock recebido mas não faturado, poderá consultar o relatório “Itens Recebidos Pendentes para Faturação” no módulo Contas.


Crie um lançamento contábil manual da seguinte maneira para atualizar o valor na conta Estoque recebido, mas não faturado.


Cr. Estoque recebido mas não faturado ........... XXX


Dr. Conta de despesas (CPV) ................... XXX
4. Configure as seguintes contas padrão para cada empresa


	* Estoque recebido, mas não faturado
	* Conta de ajuste de estoque
	* Despesas incluídas na avaliação
	* Centro de Custo
	* Ativar inventário permanente
5. Acesse: **Home > Contabilidade > Empresa**


![Inventário permanente](/files/perpetual-1.png)


#### 2. Tópicos Relacionados


1. [Contabilidade do estoque](/docs/pt/stock/accounting-of-inventory-stock)
2. [Inventário permanente](/docs/pt/stock/perpetual-inventory)



