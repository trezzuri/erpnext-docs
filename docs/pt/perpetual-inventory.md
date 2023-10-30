# Inventário Perpétuo



De acordo com o sistema de inventário permanente, o lançamento contábil é feito para cada transação de estoque. Caso contrário, é feito em intervalos maiores, por exemplo, mensalmente ou trimestralmente. Cada armazém está vinculado a um responsável de conta correspondente.


Ao receber itens em um determinado depósito, o saldo da Conta do Armazém aumentará. Da mesma forma, quando os itens são entregues do Armazém, uma despesa será contabilizada e o saldo na Conta do Armazém será reduzido.


### 1. Como ativar o inventário permanente


1. Ativar inventário permanente:


**Página inicial > Contabilidade > Empresa > Ativar inventário permanente**


![Inventário permanente](/files/perpetual-1.png)
Observe que se você desativar o inventário permanente, os usuários terão que gerenciar as entradas da conta manualmente.
2. Configure as seguintes contas padrão para cada empresa, se não estiver definido. Estas contas são criadas automaticamente nas novas contas ERPNext.


	* Conta de inventário padrão (ativo)
	* Estoque recebido, mas não faturado (passivo)
	* Conta de ajuste de estoque (despesa)
	* Despesas incluídas na avaliação (despesa)
	* Centro de Custo
3. Se o usuário quiser definir uma conta individual para cada armazém, crie um cabeçalho de conta para cada conta. Acesse:


**Contas > Plano de Contas > Empresa > Aplicação de Fundos (Ativos) > Ativo Circulante > Ativos Estoque > *Crie uma nova conta com o mesmo nome do Armazém***


Agora, vá até um armazém e vincule esta conta ao armazém. Isso ajuda na filtragem e visualização de extratos em termos de armazenamento.
4. Para transações de estoque, entradas de razão geral feitas no Cabeçalho da conta definido no armazém. Se o usuário não tiver definido a conta para o armazém, o sistema obterá o cabeçalho da conta do armazém pai. Se a conta não tiver sido definida para o armazém pai, o sistema obterá a conta (conta de estoque padrão) do mestre da empresa.



### 2. Exemplo


Considere o seguinte plano de contas e configuração de armazém para sua empresa:


Plano de contas:


* Ativos (Dr.)
	+ Ativo Circulante
		- Contas a receber
			* Devedores
		- Ativos de estoque
			* Lojas
			* Produtos Acabados
			* Trabalho em andamento
		- Ativos fiscais
			* IVA
* Passivos (Cr)
	+ Passivo Circulante
		- Contas a Pagar
			* Credores
		- Passivos de ações
			* Estoque recebido, mas não faturado
		- Responsabilidades fiscais
			* Imposto sobre serviços
* Renda (Cr)
	+ Renda Direta
		- Conta de vendas
* Despesas (Dr.)
	+ Despesas Diretas
		- Despesas com estoque
			* Custo dos produtos vendidos
			* Despesas incluídas na avaliação
			* Ajuste de estoque
	+ Despesas indiretas
		- Custos de envio
		- Direitos Aduaneiros


#### 2.1 Armazém-Configuração da conta


* Lojas
* Trabalho em andamento
* Produtos Acabados


#### 2.2 Recibo de compra


Suponha que você comprou *10 nos* do item "RM0001" por *$200* do fornecedor "Arcu Vel Quam Fabricators". A seguir estão os detalhes do recibo de compra:


**Fornecedor:** Fabricantes Arcu Vel Quam


**Itens:**




| Item | Armazém | Quantidade | Taxa | Valor | Valor da avaliação |
| --- | --- | --- | --- | --- | --- |

| RM0001 | Lojas | 10 | 200 | 2000 | 2250 |



**Impostos:**





| Conta | Valor | Categoria |
| --- | --- | --- |

| Taxas de envio | 100 | Total e avaliação |

| IVA (10%) | 200 | Total |

| Direitos Aduaneiros | 150 | Avaliação |



**Registro de estoque**


![Inventário permanente](/files/perpetual-receipt-sl-1.png)


**Conta fiscal**


![Inventário permanente](/files/perpetual-receipt-gl-2.png)


À medida que o saldo do estoque aumenta através do Recibo de Compra, as contas "Loja" são debitadas e uma conta temporária "Recebimento de estoque mas não faturado" é creditada, para manter o sistema de contabilidade de partidas dobradas. Ao mesmo tempo, a despesa negativa é contabilizada no cabeçalho da conta tendo a categoria “Avaliação” ou “Total e Avaliação” na tabela de impostos e encargos pelo valor adicionado para fins de avaliação, para evitar dupla contabilização de despesas.


#### 2.3 Fatura de compra


Ao receber a fatura do fornecedor, para o recibo de compra acima, você emitirá a fatura de compra do mesmo. As entradas do razão geral são as seguintes:


**Conta fiscal**


![Inventário permanente](/files/perpetual-pinv-gl-3.png)


Aqui a conta "Estoque Recebido mas Não Faturado" é debitada e anulada a
efeito do recibo de compra.


#### 2.4 Nota de entrega


Digamos que você tenha um pedido da "Utah Automation Services" para entregar 5 números do item "RM0001"
por $ 300. A seguir estão os detalhes da Nota de Entrega:


**Cliente:** Utah Automation Services


**Itens:**




| Item | Armazém | Quantidade | Taxa | Valor |
| --- | --- | --- | --- | --- |

| RM0001 | Lojas | 5 | 300 | 1500 |



**Impostos:**





| Conta | Valor |
| --- | --- |

| Imposto sobre serviços | 150 |

| IVA | 100 |



**Registro de estoque**


![Inventário permanente](/files/perpetual-dn-sl-4.png)


**Conta fiscal**


![Inventário permanente](/files/perpetual-dn-gl-5.png)


À medida que um item é entregue do armazém "Lojas", a conta "Lojas" é creditada e
igual valor é debitado na conta de despesas “Custo dos Produtos Vendidos”. O
o valor de débito/crédito é igual ao valor total de avaliação (custo de compra) de
os itens vendidos. E o valor da avaliação é calculado com base na sua preferência
método de avaliação (FIFO/Média Móvel) ou custo real dos itens serializados.



```
Neste exemplo, consideramos o método de avaliação como FIFO.
Taxa de avaliação = taxa de compra + encargos incluídos na avaliação
                = 200 + (250/10)
                = 225
Valor total da avaliação = 220 * 5
                        = 1125

```


### 2.5 Fatura de vendas com atualização de estoque


Digamos que você não fez a Nota de Entrega do pedido acima e, em vez disso,
você efetuou a Nota Fiscal de Venda diretamente, com as opções "Atualizar Estoque". Os detalhes
da fatura de venda são iguais à nota de entrega acima.


**Registro de estoque**


![Inventário permanente](/files/perpetual-inv-sl-6.png)


**Conta fiscal**


![Inventário permanente](/files/perpetual-inv-gl-7.png)


Aqui, além dos lançamentos normais de conta para uma fatura, "Lojas" e "Custo de
As contas "Mercadorias Vendidas" também são afetadas com base no valor da avaliação.


#### 2.6 Entrada de estoque (recebimento de material)


**Itens:**




| Item | Armazém de destino | Quantidade | Taxa | Valor |
| --- | --- | --- | --- | --- |

| RM0001 | Lojas | 50 | 220 | 11.000 |



**Registro de estoque**


![Inventário permanente](/files/perpetual-st-receipt-sl.png)


**Conta fiscal**


![Inventário permanente](/files/perpetual-st-receipt-gl.png)


#### 2.7 Entrada em estoque (emissão de material)


**Itens:**




| Item | Armazém de Origem | Quantidade | Taxa | Valor |
| --- | --- | --- | --- | --- |

| RM0001 | Lojas | 10 | 220 | 2200 |



**Registro de estoque**


![Inventário permanente](/files/perpetual-st-issue-sl.png)


**Conta fiscal**


![Inventário permanente](/files/perpetual-st-issue-gl.png)


#### 2.8 Entrada de estoque (transferência de material)


**Itens:**




| Item | Armazém de Origem | Armazém de destino | Quantidade | Taxa | Valor |
| --- | --- | --- | --- | --- | --- |

| RM0001 | Lojas | Trabalho em andamento | 10 | 220 | 2200 |



**Registro de estoque**


![Inventário permanente](/files/perpetual-st-transfer-sl.png)


**Conta fiscal**


![Inventário permanente](/files/perpetual-st-transfer-gl.png)


#### 3. Tópicos Relacionados


1. [Contabilidade do estoque](/docs/pt/stock/accounting-of-inventory-stock)
2. [Migrar para o inventário permanente](/docs/pt/stock/articles/migrate-to-perpetual-inventory)










