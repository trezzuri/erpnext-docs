# Comprovante de custo final



**Custo final é o custo total final associado a um produto para que ele chegue à porta do comprador.**


Os custos de entrega incluem o custo original do item, custos completos de envio, taxas alfandegárias, impostos, seguros, taxas de conversão de moeda, etc. Todos esses componentes podem não ser aplicáveis ​​em todas as remessas, mas os componentes relevantes devem ser considerados como um parte do custo final.


> **O que é custo final?**


> Para entender melhor o custo final, vamos dar um exemplo baseado em nosso dia a dia. Você precisa comprar uma nova máquina de lavar para sua casa. Antes de fazer uma compra real, você provavelmente faz algumas pesquisas para saber o melhor preço. Nesse processo, muitas vezes você encontra um negócio melhor em uma loja que fica muito longe de sua casa. Mas você também deve considerar o custo de envio ao comprar nessa loja. O custo total, incluindo frete, pode ser maior do que o preço obtido na loja mais próxima. Nesse caso, você optará por comprar na loja mais próxima, pois o custo final do item é mais barato na loja mais próxima.


Da mesma forma nos negócios, identificar o custo final de um item/produto é muito importante, pois ajuda a decidir o custo de venda desse item e impacta a lucratividade da empresa. Portanto, todos os encargos de custo no destino aplicáveis ​​devem ser incluídos na taxa de avaliação do item.


De acordo com o [estudo de logística de terceiros](http://www.3plstudy.com/), apenas 45% dos entrevistados afirmaram usar extensivamente o custo final. Os principais motivos para não usar o Landing Cost foram a indisponibilidade dos dados necessários (49%), a falta de ferramentas adequadas (48%), o tempo insuficiente (31%) e a falta de certeza de como aplicar o Landing Cost (27%).


Para acessar a lista de vouchers de custo final, acesse:
> Home > Estoque > Ferramentas > Voucher de custo final


## 1. Pré-requisitos


Antes de criar e usar o Voucher de Custos Adicionais, é aconselhável que você crie primeiro o seguinte:


* [Recibo de compra](/docs/pt/stock/purchase-receipt)


Ou
* [Fatura de compra](/docs/pt/accounts/purchase-invoice)


## 2. Como criar um voucher de custo final


1. Vá para a lista de vouchers de custo final e clique em Novo.
2. Selecione o tipo de documento de recebimento, seja fatura de compra ou recibo. Você pode selecionar vários documentos.
3. Selecione a fatura ou recibo específico. O nome do fornecedor e o total geral serão obtidos automaticamente.
4. Clique no botão Obter itens dos recibos de compra para obter os detalhes do item na fatura/recibo de compra.
5. Selecione se Distribuir encargos com base em deve ser na quantidade ou no valor.
6. Insira a Conta de Despesas e o Valor dos Custos Adicionais na tabela Impostos e Encargos. O valor será distribuído igualmente com base na quantidade ou valor conforme sua seleção.
7. Salvar e enviar.


![Voucher de custo no destino](/files/landed-cost-voucher.png)


No documento, você pode selecionar vários recibos/faturas de compra e buscar todos os itens desses recibos de compra. Depois deverá adicionar os encargos aplicáveis ​​na tabela “Impostos e Encargos”. Você pode excluir facilmente um item se as cobranças adicionais não se aplicarem a ele.


Os encargos adicionais são distribuídos proporcionalmente entre todos os itens com base em seu valor ou quantidade. Se você selecionou com base no valor, o item com o valor mais alto receberá a maior proporção dos encargos. Em caso de quantidade, o Item com maior quantidade receberá a maior parte dos encargos e os demais Itens receberão valores menores. Isso é mostrado na captura de tela a seguir:


![Voucher de custo de destino](/files/landed-cost-distribution.png)


## 3. Ações relacionadas


### 3.1 Adicionando custo no destino no próprio recibo de compra


No ERPNext, você pode adicionar encargos relacionados ao custo de entrega na tabela “Impostos e Encargos” ao criar o Recibo de Compra (PR). Você deve adicionar esses encargos para “Total e Avaliação” ou “Avaliação” no campo ‘Considerar Imposto ou Encargo para’. Os encargos devidos ao mesmo Fornecedor de quem você está comprando os itens devem ser marcados como “Total e Avaliação”. Caso contrário, se os encargos aplicáveis ​​forem pagos a terceiros, deverão ser marcados como “Avaliação”. Ao enviar o Recibo de Compra, o sistema calculará o custo de entrega de todos os itens, considerando esses encargos. Este custo final será considerado para calcular a Taxa de Avaliação do item (com base no método FIFO/Média Móvel).


Mas, na realidade, ao fazer o Recibo de Compra, podemos não saber todos os encargos aplicáveis ​​ao custo final. Sua transportadora pode enviar a fatura após 1 mês, mas não adianta esperar pela reserva do Recibo de Compra até então. As empresas que importam seus produtos/peças pagam uma quantia enorme de Imposto Aduaneiro. E geralmente eles recebem faturas da Alfândega depois de um tempo. Nesses casos, o “Voucher de custo final” torna-se útil, pois permite adicionar essas cobranças adicionais em uma data posterior e atualizar o custo final dos itens comprados.


### 3.2 O que acontece no envio?


1. A taxa de avaliação dos itens é recalculada com base no novo custo final.
2. Se você estiver usando “Estoque Perpétuo”, o sistema lançará lançamentos no razão geral para corrigir o saldo de estoque em mãos. Irá debitar (aumentar) a correspondente “conta de armazém” e creditar (diminuir) a **Conta de Despesas** mencionada na tabela de Impostos e Taxas. Se os itens já foram entregues, o valor do Custo dos Produtos Vendidos (CPV) foi contabilizado de acordo com a taxa de avaliação antiga. Conseqüentemente, as entradas do razão geral são relançadas para todas as entradas de saída futuras de itens associados, para corrigir o valor do CPV.


### 4. Tópicos Relacionados


1. [Viagem de entrega](/docs/pt/stock/delivery-trip)
2. [Recibo de compra](/docs/pt/stock/purchase-receipt)



