# Personalizar relatório de fluxo de caixa


À medida que seu plano de contas começa a ficar mais complexo e os padrões de relatórios mudam e evoluem, o fluxo de caixa padrão
relatório pode não ser mais suficiente. Isso ocorre porque o ERPNext pode não ser capaz de adivinhar com precisão a classificação e
finalidade de todas as contas nos planos de contas. Outra reclamação que você pode ter é a incapacidade de ajustar o relatório
formato para atender às suas necessidades.


Isso não será mais um problema porque o ERPNext agora permite que os usuários personalizem o relatório de fluxo de caixa.


## Visão geral técnica


A personalização é possível graças à introdução de dois novos tipos de documento - Cash Flow Mapper e Cash Flow Mapping. Ambos
doctypes contêm as informações necessárias para gerar um relatório de fluxo de caixa.


O mapeamento de fluxo de caixa mostra como as contas em seus planos de contas são mapeadas para um item de linha em seu relatório de fluxo de caixa enquanto
O Mapeador de fluxo de caixa obtém todos os mapeamentos de fluxo de caixa relacionados às três seções de uma demonstração de fluxo de caixa.


Com isso, você gera relatórios detalhados de fluxo de caixa de acordo com suas necessidades. Isso pode não fazer muito sentido, mas fará
depois de passarmos por um exemplo.


## Exemplo


### Informações básicas


Vamos supor que temos uma empresa fictícia para a qual queremos gerar um relatório de fluxo de caixa.
É assim que o relatório de fluxo de caixa se parece no momento:


![Relatório de fluxo de caixa padrão](/files/default-cash-flow-report.png)


Não gostamos do relatório pelos seguintes motivos:
- O formato do relatório é muito escasso.
- O número 'Net Cash From Operations' está errado


### Processo de personalização


Queremos que o Relatório de fluxo de caixa seja semelhante ao formato das imagens abaixo:


![Formato de fluxo de caixa personalizado](/files/format-1.png)


![Formato de fluxo de caixa personalizado](/files/format-2.png)


#### Ativar relatório de fluxo de caixa personalizado


Faça isso em Configurações de contas marcando a caixa de seleção 'Usar formato de fluxo de caixa personalizado'. Isso fará com que o ERPNext use apenas seu formato personalizado para relatórios de fluxo de caixa.


![Ativar relatório de fluxo de caixa personalizado](/files/enable-custom-cash-flow.png)


Vá para a próxima seção para criar o relatório.


#### Criar mapeamentos de fluxo de caixa


Para cada linha, precisamos criar um documento de Mapeamento de Fluxo de Caixa para representá-la.


![Novo mapeamento de fluxo de caixa](/files/new-cash-flow-mapping.png)


Você pode pensar no Mapeamento do Fluxo de Caixa como uma representação de cada linha no relatório de fluxo de caixa. Um mapeamento de fluxo de caixa
é um filho de um mapeador de fluxo de caixa que será explicado mais tarde.


Vamos começar criando Mapeamentos de Fluxo de Caixa que representarão a adição de despesas não monetárias já reconhecidas em
a demonstração de Lucros ou Perdas. Queremos que eles apareçam no extrato de caixa como:
- Impostos de renda reconhecidos no resultado
- Despesas financeiras reconhecidas no resultado
- Depreciação de ativos não circulantes


Comece abrindo um novo formulário de Mapeamento de Fluxo de Caixa.


Os campos do tipo de documento Mapeamento de Fluxo de Caixa são:
- **Nome**: Este algo para identificar este documento. Nomeie algo relacionado ao rótulo
- **Rótulo**: é o que aparecerá no demonstrativo de fluxo de caixa
- **Contas**: Esta tabela contém todas as contas às quais esta linha se refere.


De posse dessas informações, vamos criar o Documento de Mapeamento do Fluxo de Caixa para a linha 'Impostos de renda reconhecidos no resultado'


![Mapeamento do fluxo de caixa para despesas com imposto de renda](/files/cash-flow-mapping-for-income-tax.png)


Chamei-o de 'Cobrança de imposto de renda' e dei a ele o rótulo 'Impostos de renda reconhecidos no lucro ou prejuízo'. nós queremos isso
linha para refletir os encargos de imposto de renda de nossa demonstração de lucros ou perdas. A conta onde isso acontece em nosso gráfico
da conta é chamada 'Impostos de Renda' (uma despesa), então adicionei 'Impostos de Renda' na tabela de contas. Se você tem
mais contas representando despesas de imposto de renda, você deve adicionar todas aqui.


Como a despesa com imposto de renda precisa ser ajustada ainda mais na demonstração do fluxo de caixa, marque a opção 'É despesa com imposto de renda'
checkbox. É isso que ajudará o ERPNext a calcular corretamente os ajustes a serem feitos.


*Para obter melhores resultados, permita que as contas principais tenham contas secundárias com o mesmo tratamento para relatórios de fluxo de caixa
porque o ERPNext calculará a variação líquida de todas as contas filhas em uma situação em que a conta selecionada
é uma conta principal.*


Da mesma forma, criei para os dois mapeamentos restantes.


![Mapeamento de fluxo de caixa para custo financeiro](/files/cash-flow-mapping-for-finance-cost.png)


Os custos financeiros também precisam ser ajustados, portanto, marque a caixa de seleção "É custo financeiro".


![Mapeamento de fluxo de caixa para depreciação](/files/cash-flow-mapping-for-depreciation.png)


Em seguida, vamos adicionar o Mapeamento de Fluxo de Caixa para itens que mostram mudanças no capital de giro:


* Aumento/(diminuição) em outros passivos
* (Aumento)/diminuição de contas a receber e outras contas a receber
* Aumento/(diminuição) em fornecedores e outras contas a pagar
* IVA a pagar
* (Aumento)/redução no estoque


![Mapeamento de fluxo de caixa para outras obrigações](/files/cash-flow-mapping-for-other-liabilities.png)


![Mapeamento de fluxo de caixa para contas a receber](/files/cash-flow-mapping-for-receivables.png)


![Mapeamento de fluxo de caixa para contas a pagar](/files/cash-flow-mapping-for-payables.png)


![Mapeamento de fluxo de caixa para taxas e impostos](/files/cash-flow-mapping-for-taxes-payables.png)


![Mapeamento de fluxo de caixa para inventário](/files/cash-flow-mapping-inventory.png)


Não se esqueça de informar ao ERPNext que esses mapeamentos representam mudanças no capital de giro marcando a caixa 'Está funcionando
Caixa de seleção maiúscula.


Neste ponto, criamos todos os mapeamentos necessários para a seção de atividades operacionais do nosso fluxo de caixa
declaração. No entanto, o ERPNext ainda não sabe disso até que criemos os documentos do Cash Flow Mapper. Faremos o Fluxo de Caixa
Documentos do mapeador a seguir.


#### Criar mapeadores de fluxo de caixa


Os mapeadores de fluxo de caixa representam as seções do demonstrativo de fluxo de caixa. Uma demonstração de fluxo de caixa padrão tem apenas três
seções, portanto, quando você visualizar a lista do Mapeador de Fluxo de Caixa, verá que três foram criadas para você com os nomes:
- Atividades operacionais
- Atividades Financeiras
- Atividades de investimento


Você não poderá adicionar ou remover nenhum deles, mas eles são editáveis ​​e podem ser renomeados.


![Cash Flow Mappers](/files/cash-flow-mappers-standard.png)


Abra o Mapeador de Fluxo de Caixa de Atividades Operacionais para que possamos adicionar os Mapeamentos de Fluxo de Caixa que criamos.


* **Nome da seção**: este é o título da seção.
* **Líder de seção**: Este é o primeiro subtítulo imediatamente após o valor do lucro. Refere-se apenas ao Operacional
Mapeador de Fluxo de Caixa de Atividades
* **Subtotal da seção**: este é o rótulo do subtotal na seção de demonstração do fluxo de caixa. Refere-se apenas ao Operacional
Mapeador de Fluxo de Caixa de Atividades
* **Rodapé da seção**: este é o rótulo para o total na seção de demonstração do fluxo de caixa.
* **Mapeamento**: Esta tabela contém todos os Mapeamentos de Fluxo de Caixa relacionados ao Mapeador de Fluxo de Caixa.


Agora adicione todos os mapeamentos de fluxo de caixa que você criou e salve. Você deve ter algo assim:


![Mapeador de fluxo de caixa da atividade operacional](/files/cash-flow-mapper-operating-activity.png)


Atualize o demonstrativo de fluxo de caixa e visualize as alterações.
![Relatório de fluxo de caixa atualizado](/files/cash-flow-report-customized.png)


Parece próximo de nossos requisitos, mas ainda não terminamos. Crie novos mapeamentos para 'Investing Activities' e 'Financing Activities'
Seções de atividades da demonstração do fluxo de caixa.


![Mapeamento de fluxo de caixa para propriedade](/files/cash-flow-mapping-for-property.png)


![Mapeamento de fluxo de caixa para ações](/files/cash-flow-mapping-for-equity.png)


![Mapeamento de fluxo de caixa para investimento](/files/cash-flow-mapping-for-investing.png)


![Mapeamento de fluxo de caixa para atividades de financiamento](/files/cash-flow-mapping-for-financing-activities.png)


Aqui está a aparência do nosso demonstrativo de fluxo de caixa:


![Relatório de fluxo de caixa personalizado](/files/final-cash-flow.png)

