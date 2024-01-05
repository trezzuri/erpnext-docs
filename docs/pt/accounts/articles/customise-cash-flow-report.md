# Personalizar relatório de fluxo de caixa



À medida que seu plano de contas começa a ficar mais complexo e os padrões de relatórios mudam e evoluem, o fluxo de caixa padrão
relatório pode já não ser suficiente. Isto ocorre porque o ERPNext pode não ser capaz de adivinhar com precisão a classificação e
finalidade de todas as contas nos planos de contas. Outra reclamação que você pode ter é a incapacidade de ajustar o relatório
formato que atenda às suas necessidades.


Isso não será mais um problema porque o ERPNext agora permite que os usuários personalizem o relatório de fluxo de caixa.


## Visão geral técnica


A personalização é possível graças à introdução de dois novos doctypes-Cash Flow Mapper e Cash Flow Mapping. Ambos
doctypes contêm as informações necessárias para gerar um relatório de fluxo de caixa.


O mapeamento do fluxo de caixa mostra como as contas em seu plano de contas são mapeadas para um item de linha em seu relatório de fluxo de caixa enquanto
O Cash Flow Mapper obtém todos os mapeamentos de fluxo de caixa relacionados às três seções de uma demonstração de fluxo de caixa.


Com isso, você gera relatórios de fluxo de caixa detalhados de acordo com suas necessidades. Isso pode não fazer muito sentido, mas fará
depois de vermos um exemplo.


## Exemplo


### Informações básicas


Vamos supor que temos uma empresa fictícia para a qual queremos gerar um relatório de fluxo de caixa.
Esta é a aparência do relatório de fluxo de caixa no momento:


![Relatório de fluxo de caixa padrão](/files/default-cash-flow-report.png)


Não gostamos do relatório pelos seguintes motivos:
-O formato do relatório é muito escasso.
-O valor do 'Caixa líquido das operações' está errado


### Processo de personalização


Queremos que o Relatório de Fluxo de Caixa tenha algo semelhante ao formato das imagens abaixo:


![Formato de fluxo de caixa personalizado](/files/format-1.png)


![Formato de fluxo de caixa personalizado](/files/format-2.png)


#### Ativar relatório de fluxo de caixa personalizado


Faça isso nas configurações da conta marcando a caixa de seleção "Usar formato de fluxo de caixa personalizado". Isto fará com que o ERPNext use apenas o seu formato personalizado para relatórios de fluxo de caixa.


![Ativar relatório de fluxo de caixa personalizado](/files/enable-custom-cash-flow.png)


Vá para a próxima seção para criar o relatório.


#### Criar mapeamentos de fluxo de caixa


Para cada linha, precisamos criar um documento de Mapeamento de Fluxo de Caixa para representá-la.


![Novo mapeamento de fluxo de caixa](/files/new-cash-flow-mapping.png)


Você pode pensar no Mapeamento de Fluxo de Caixa como uma representação de cada linha do relatório de fluxo de caixa. Um mapeamento de fluxo de caixa
é filho de um Mapeador de Fluxo de Caixa que será explicado mais tarde.


Vamos começar criando Mapeamentos de Fluxo de Caixa que representarão o acréscimo de despesas não monetárias já reconhecidas em
a demonstração de lucros ou perdas. Queremos que eles apareçam no extrato de caixa como:
-Imposto de renda reconhecido no resultado
-Despesas financeiras reconhecidas no resultado
-Depreciação de ativos não circulantes


Comece abrindo um novo formulário de mapeamento de fluxo de caixa.


Os campos no tipo de documento Mapeamento de Fluxo de Caixa são:
-**Nome**: É algo para identificar este documento. Dê um nome relacionado ao rótulo
-**Rótulo**: é o que aparecerá na demonstração do fluxo de caixa
-**Contas**: Esta tabela contém todas as contas às quais esta linha se refere.


Com essas informações, vamos em frente e criar o Documento de Mapeamento do Fluxo de Caixa para a linha 'Imposto de renda reconhecido no resultado'


![Mapeamento de fluxo de caixa para despesas de imposto de renda](/files/cash-flow-mapping-for-income-tax.png)


Eu o chamei de 'Encargo de Imposto de Renda' e dei a ele o rótulo de 'Imposto de Renda reconhecido no lucro ou prejuízo'. Nós queremos isso
linha para refletir as despesas de imposto de renda de nossa demonstração de lucros ou perdas. A conta onde isso acontece em nosso gráfico
da conta é chamada de 'Imposto de Renda' (uma despesa), então adicionei 'Imposto de Renda' à tabela de contas. Se você tem
mais contas representando despesas de imposto de renda, você deve adicionar todas elas aqui.


Como a despesa com Imposto de Renda precisa ser ajustada ainda mais na demonstração do fluxo de caixa, marque a opção 'É Despesa com Imposto de Renda'
caixa de seleção. Isto é o que ajudará o ERPNext a calcular corretamente os ajustes a serem feitos.


*Para obter melhores resultados, permita que as contas principais tenham contas secundárias que tenham o mesmo tratamento para relatórios de fluxo de caixa
porque o ERPNext calculará a variação líquida de todas as contas infantis em uma situação onde a conta selecionada
é uma conta pai.*


Da mesma forma, criei para os dois mapeamentos restantes.


![Mapeamento de fluxo de caixa para custos financeiros](/files/cash-flow-mapping-for-finance-cost.png)


Os custos financeiros também precisam ser ajustados, portanto marque a caixa de seleção "É custo financeiro".


![Mapeamento de fluxo de caixa para depreciação](/files/cash-flow-mapping-for-depreciation.png)


A seguir, vamos adicionar o Mapeamento de Fluxo de Caixa para itens que mostram alterações no capital de giro:


* Aumento/(diminuição) de outros passivos
* (Aumento)/diminuição em contas comerciais e outras contas a receber
* Aumento/(diminuição) em contas comerciais e outras contas a pagar
* IVA a pagar
* (Aumento)/diminuição no estoque


![Mapeamento de fluxo de caixa para outras responsabilidades](/files/cash-flow-mapping-for-other-liabilities.png)


![Mapeamento de fluxo de caixa para contas a receber](/files/cash-flow-mapping-for-receivables.png)


![Mapeamento de fluxo de caixa para contas a pagar](/files/cash-flow-mapping-for-payables.png)


![Mapeamento de fluxo de caixa para taxas e impostos](/files/cash-flow-mapping-for-taxes-payables.png)


![Mapeamento de fluxo de caixa para estoque](/files/cash-flow-mapping-inventory.png)


Não se esqueça de informar ao ERPNext que esses mapeamentos representam mudanças no capital de giro, marcando a opção 'Está Funcionando
Caixa de seleção maiúscula.


Neste ponto criamos todos os mapeamentos necessários para a seção Atividades Operacionais do nosso fluxo de caixa
declaração. No entanto, o ERPNext ainda não sabe disso até criarmos os documentos do Cash Flow Mapper. Criaremos Fluxo de Caixa
Documentos do mapeador a seguir.


#### Criar mapeadores de fluxo de caixa


Mapeadores de fluxo de caixa representam as seções da demonstração do fluxo de caixa. Uma demonstração de fluxo de caixa padrão tem apenas três
Portanto, ao visualizar a lista do Mapeador de Fluxo de Caixa, você verá que três foram criadas para você, nomeadas:
-Atividades operacionais
-Atividades Financeiras
-Atividades de investimento


Você não poderá adicionar ou remover nenhum deles, mas eles são editáveis ​​e podem ser renomeados.


![Mapeadores de fluxo de caixa](/files/cash-flow-mappers-standard.png)


Abra o Mapeador de Fluxo de Caixa de Atividades Operacionais para que possamos adicionar os Mapeamentos de Fluxo de Caixa que criamos.


* **Nome da seção**: este é o título da seção.
* **Líder da seção**: Este é o primeiro subcabeçalho imediatamente após o valor do lucro. Refere-se apenas à operação
Mapeador de fluxo de caixa de atividades
* **Subtotal da Seção**: Este é o rótulo do subtotal na seção da demonstração do fluxo de caixa. Refere-se apenas à operação
Mapeador de fluxo de caixa de atividades
* **Rodapé da seção**: este é o rótulo do total na seção da demonstração do fluxo de caixa.
* **Mapeamento**: Esta tabela contém todos os Mapeamentos de Fluxo de Caixa relacionados ao Mapeador de Fluxo de Caixa.


Agora adicione todos os mapeamentos de fluxo de caixa que você criou e salve. Você deverá ter algo assim:


![Mapeador de fluxo de caixa da atividade operacional](/files/cash-flow-mapper-operating-activity.png)


Atualize a demonstração do fluxo de caixa e visualize as alterações.
![Relatório de fluxo de caixa atualizado](/files/cash-flow-report-customized.png)


Parece próximo aos nossos requisitos, mas ainda não terminamos. Crie novos mapeamentos para 'Atividades de Investimento' e 'Financiamento
Seções de atividades da demonstração do fluxo de caixa.


![Mapeamento de fluxo de caixa para propriedades](/files/cash-flow-mapping-for-property.png)


![Mapeamento de fluxo de caixa para patrimônio](/files/cash-flow-mapping-for-equity.png)


![Mapeamento de fluxo de caixa para investimentos](/files/cash-flow-mapping-for-investing.png)


![Mapeamento de fluxo de caixa para atividades de financiamento](/files/cash-flow-mapping-for-financing-activities.png)


Esta é a aparência do nosso demonstrativo de fluxo de caixa:


![Relatório de fluxo de caixa personalizado](/files/final-cash-flow.png)



