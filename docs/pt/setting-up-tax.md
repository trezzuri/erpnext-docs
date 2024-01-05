# Configurando a dedução do imposto de renda



Calcular as deduções fiscais para funcionários todos os meses é uma atividade demorada para a maioria das empresas, especialmente para grandes empresas. Se configurado corretamente, o Frappe HR simplifica a maioria dos cálculos fiscais, calculando automaticamente as deduções fiscais ao gerar recibos de salário. Veja como você pode configurar o Frappe HR para facilitar o processamento da folha de pagamento-


# Isenção de imposto de renda


Em muitos países, especialmente na Índia, os regulamentos permitem isentar uma parte (ou a totalidade) de algum tipo de despesas dos indivíduos de serem adicionadas ao seu rendimento tributável anual. Exemplos de tais despesas poderiam ser as contribuições para instituições de caridade, o montante gasto na educação das crianças, investimentos específicos, etc.
aproveitar a isenção de seus rendimentos tributáveis, os indivíduos são obrigados a apresentar comprovante de tais gastos.


O Frappe HR permite configurar Lajes de Imposto de Renda e o imposto é calculado com base na projeção de rendimento anual do funcionário. Para isso, os funcionários são obrigados a declarar o valor da isenção que pretendem reivindicar no início do exercício, para que as deduções fiscais na folha de pagamento sejam calculadas com base no rendimento anual projetado menos a isenção. Os funcionários podem declarar isso por meio da [Declaração de isenção fiscal do funcionário](/docs/pt/human-resources/employee-tax-exemption-declaration).


Se não for apresentada nenhuma declaração pelo trabalhador, as deduções mensais serão calculadas sem qualquer isenção da remuneração anual do trabalhador. Porém, caso o empregado apresente a declaração entre o período da folha de pagamento, a isenção do imposto será aplicada a partir da próxima folha de pagamento. Qualquer imposto adicional cobrado em folhas de pagamento anteriores será ajustado na última folha de pagamento ou ao usar *Dedução de imposto para comprovante de isenção fiscal não enviado* no lançamento da folha de pagamento ou no comprovante de salário.


Além disso, no final do ano, os funcionários enviam o comprovante real dos gastos para arquivamento via [Envio de comprovante de isenção fiscal de funcionário](/docs/pt/human-resources/employee-tax-exemption-proof-submit). Na última folha de pagamento do Período Consignado, o Frappe RH verifica o envio de comprovantes dos funcionários e, caso não seja encontrado, o imposto referente à renda isenta será adicionado ao componente de dedução padrão.


### Categoria de isenção de impostos para funcionários


As isenções de salário tributável são geralmente restritas a gastos em categorias específicas decididas pelo governo ou agências reguladoras. O Frappe HR permite configurar diversas categorias que podem ser isentas. Exemplos disso poderiam ser, para a Índia, 80G, 80C, B0CC, etc.


Você pode configurar a categoria de isenção de impostos para funcionários acessando,
> Recursos humanos > Configuração da folha de pagamento > Categoria de isenção fiscal para funcionários > Nova categoria de isenção fiscal para funcionários


![Categoria de isenção de impostos para funcionários](/files/employee-tax-exemption-category.png)


### Subcategoria de isenção de impostos para funcionários


Em cada categoria, pode haver muitas cabeças para as quais as isenções são permitidas. Por exemplo, na Índia, as subcategorias abaixo de 80C poderiam ser Prêmio de Seguro de Vida


Você pode configurar a subcategoria de isenção de impostos para funcionários acessando,
> Recursos humanos > Configuração da folha de pagamento > Subcategoria de isenção de impostos para funcionários > Nova subcategoria de subisenção de impostos para funcionários


![Subcategoria de isenção de impostos para funcionários](/files/employee-tax-exemption-subcategory.png)


### Isenção HRA-Regional, Índia


Para o ano fiscal de 2018-19, na Índia, a isenção do subsídio de aluguel de casa (HRA) dos rendimentos tributáveis ​​é o mínimo de:
 \* O valor real alocado pelo empregador como HRA.
 \*Aluguel real pago menos 10% do salário base.
 \* 50% do salário base, se o funcionário estiver hospedado em cidade metropolitana (40% para cidade não metropolitana).


Como parte da Declaração de Isenção Fiscal do Funcionário, os funcionários também deverão preencher a Isenção HRA. A Frappe HR calculará a isenção elegível para HRA e a isentará no cálculo do lucro tributável.


> Observação: Os componentes do salário básico e do HRA devem ser configurados na Empresa para que a isenção do HRA funcione


### Opções de lançamento de folha de pagamento e recibo de salário


O Frappe HR simplifica o processamento da folha de pagamento processando automaticamente a folha de pagamento em massa por meio de [Entrada da folha de pagamento](/docs/pt/human-resources/payroll-entry).

 >
* Dedução de imposto para benefícios de funcionários não reclamados: Benefícios flexíveis (componentes salariais que são *É benefício flexível*) não estão incluídos na renda tributável do funcionário. No entanto, o valor recebido por esses componentes será incluído nos rendimentos tributáveis ​​do funcionário se ele não apresentar  [Solicitação de benefício de funcionário](/docs/pt/human-resources/employee-benefit-claim) durante o cálculo do imposto na última folha de pagamento do período processado na folha de pagamento.


Se você deseja recolher impostos sobre benefícios antes da última folha de pagamento, marque esta opção e o Frappe HR recalculará o imposto e adicionará o imposto para todos os benefícios não tributados ao gerar o Comprovante de Salário.


* Deduzir imposto para comprovante de isenção fiscal não enviado: esta opção permite deduzir impostos sobre os rendimentos que foram isentos em folhas de pagamento anteriores, conforme declarado em [Declaração de isenção fiscal do funcionário](/docs/pt/human-resources/Employee-tax-exemption-declaration), mas o funcionário não enviou provas suficientes via [Envio de prova de isenção fiscal de funcionário](/docs/pt/human-resources/employee-tax-isenção-prova-submissão). Deve-se observar que se esta opção for marcada, o Frappe HR não considera a Declaração de Isenção de Imposto de Funcionário dos funcionários e levará apenas em consideração o *Envio de Comprovante de Isenção de Imposto de Funcionário* ao calcular a isenção dos rendimentos anuais dos funcionários. .


> Nota: Se necessário, você ainda pode processar a folha de pagamento dos funcionários individualmente, criando manualmente um novo Comprovante de Salário e ambas as opções são disponibilizadas no Comprovante de Salário


# Laje de Imposto de Renda


A [Laje de Imposto de Renda](/docs/pt/human-resources/income-tax-slab) ajuda a definir as lajes de Imposto aplicáveis ​​ao período, facilitando para gerenciar as mudanças nas leis. Você pode adicionar vários blocos fiscais para o período processado na folha de pagamento, dependendo das regulamentações fiscais. Observe que você pode usar campos no documento Funcionário no campo *Condição* para aplicar lajes fiscais com base nos atributos dos funcionários.


# Componente Salarial


Para habilitar a dedução fiscal automática com base nas lajes fiscais configuradas na Laje do Imposto de Renda, é necessário configurar um Componente Salarial do tipo *Dedução* com a opção *Variável Baseada no Salário Tributável* habilitada . Este checkbox permite o cálculo automático do Imposto de Renda considerando as lajes fiscais e a declaração apresentada pelo funcionário. O imposto será calculado anualmente sobre o salário tributável restante e dividido igualmente em 12 meses.


>**Observação Importante:** Se você configurar condição e fórmula para este componente de Dedução, a condição e fórmula serão consideradas para cálculo do Componente Salarial e as Lajes Fiscais configuradas na Laje Imposto de Renda serão ignoradas. No entanto, você ainda pode usar a opção *Deduzir Imposto por Comprovante de Isenção de Imposto Não Submetido* em Lançamento de Folha de Pagamento/Recibo de Salário para deduzir impostos com base nas Lajes Fiscais configuradas na Laje de Imposto de Renda, isentando [Envio de prova de isenção fiscal de funcionário](/docs/pt/human-resources/employee-tax-exemption-proof-submission) que dará precedência à dedução fiscal baseada na Laje Fiscal.
Isso é particularmente útil se você precisar deduzir um valor fixo como dedução em cada folha de pagamento, em vez de o Frappe HR calcular automaticamente as deduções com base no salário anual projetado do funcionário após a isenção declarada pelo funcionário via [Declaração de isenção fiscal do funcionário](/docs/pt/human-resources/employee-tax-exemption-declaration). No final do ano fiscal, você ainda pode usar *Deduzir imposto para comprovante de isenção fiscal não enviado* para deduzir o passivo fiscal restante do funcionário durante todo o período.



