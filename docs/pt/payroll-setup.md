# Configuração da folha de pagamento



Salário é uma quantia fixa de dinheiro ou remuneração paga a um funcionário por um empregador em troca do trabalho realizado.


A folha de pagamento é a administração dos registros financeiros de salários, vencimentos, bônus, remuneração líquida e deduções dos funcionários.


Para processar folha de pagamento no Frappe HR,


1. Definir [Período da folha de pagamento](/docs/pt/human-resources/payroll-period.html) (opcional)
2. Definir [placa de imposto de renda](/docs/pt/human-resources/income-tax-slab.html) (opcional)
3. Criar estrutura salarial com componentes salariais (ganhos e deduções)
4. Atribuir estruturas salariais a cada funcionário por meio da atribuição de estrutura salarial
5. Gere recibos de salário por meio de [Lançamento da folha de pagamento](/docs/pt/human-resources/payroll-entry.html).
6. Reserve o Salário em suas Contas.


## Período da folha de pagamento


[Período da folha de pagamento](/docs/pt/human-resources/payroll-period.html), no Frappe HR, é um período pelo qual os funcionários são pagos sua ocupação na Empresa. O período da folha de pagamento ajuda a definir as taxas fiscais aplicáveis ​​ao período, facilitando o gerenciamento das mudanças nas leis.


> Observação: configurar o período da folha de pagamento é opcional se você não pretende usar benefícios flexíveis ou faixas fiscais


## Componente Salarial


Este documento permite definir cada componente de Rendimentos e Deduções que pode ser utilizado para criar uma Estrutura Salarial e posteriormente criar Recibo de Salário ou Salário Adicional. Você também pode configurar o tipo, condição e fórmula, bem como outras configurações discutidas abaixo. Você deve ser capaz de ativar várias combinações das opções a seguir para configurar cada componente de acordo com as políticas da sua empresa/regional.


* Depende de licença sem remuneração: a licença sem remuneração (LWP) ocorre quando um funcionário fica sem licenças alocadas
ou tira licença sem aprovação (por meio do Pedido de Licença). Se habilitado, o Frappe HR deduzirá automaticamente o
pague na proporção dos dias LWP divididos pelo total de dias úteis do mês (com base na Lista de Feriados).


> Observação: se você não deseja que o RH do Frappe gerencie o LWP, não ative esta sinalização em nenhum dos componentes salariais
* Não incluir no total: Se esta opção estiver habilitada, o componente não será adicionado ao total dos Rendimentos ou Descontos do Comprovante de Salário


#### Ganhos


![Ganhos do componente salarial](/files/salary-component.png)


* É Componente Adicional: Esta opção especifica que o componente só poderá ser pago como Salário Adicional. Exemplos desta componente podem ser o Bónus de Desempenho ou o pagamento recebido por representação no local, etc. Tais componentes não são considerados parte da estrutura salarial normal. Em vez disso, o Salário Adicional com esses componentes pode ser enviado conforme necessário, e será adicionado automaticamente ao Comprovante de Salário.
* O imposto é aplicável: Se um componente precisar ser considerado para cálculos de impostos especificados de acordo com o período da folha de pagamento, você pode querer ativar esta opção. Será necessário que você tenha um Período de Folha de Pagamento e uma Placa de Imposto de Renda configurados com Placas de Imposto válidas para processamento da folha de pagamento.
* É a Pagar: Tais componentes podem ser contabilizados em contas a pagar separadas e as Contas devem ser configuradas na tabela Contas
* Benefícios Flexíveis: Benefícios Flexíveis são componentes de ganho que os Funcionários podem optar por receber proporcionalmente ou anualmente quando solicitarem. Estes são, em sua maioria, isentos de impostos, a menos que o Funcionário não apresente a reclamação com faturas/documentos adequados. Se ativado, você poderá especificar o benefício máximo permitido para um funcionário em um ano. Os funcionários podem criar [Aplicativo de benefícios para funcionários](/docs/pt/human-resources/employee-benefit-application) com aqueles que escolherem.


>Observação: a Aplicação de Benefícios a Empregados permitirá apenas que os Funcionários escolham apenas entre os componentes flexíveis que estão presentes na Estrutura Salarial atribuída ao Funcionário


	+ Reivindicação de Pagamento Contra Benefícios: Os funcionários podem optar por receber benefícios flexíveis anualmente por meio de Solicitação de Benefícios a Empregados ou junto com seu salário todos os meses. Se você ativar esta opção, o valor alocado para o componente será pago quando o funcionário enviar um [Benefício de funcionário Reivindicar](/docs/pt/human-resources/employee-benefit-claim.html). Caso contrário, o valor será distribuído como parte do salário do Funcionário de forma proporcional.
	
	
		- Apenas Impacto Fiscal (Não pode ser reivindicado, mas parte do Lucro Tributável): Tais componentes são aqueles que a empresa já pagou ao Funcionário em dinheiro ou por algum outro meio, por exemplo, um carro adquirido para uso do Funcionário. O Funcionário não pode reclamar, mas é responsável pelo pagamento do imposto. O valor atribuído a esta componente será considerado no cálculo do rendimento tributável do Colaborador.
		- Criar entrada de pagamento separada para reivindicação de benefício: alguns dos benefícios flexíveis podem ser legalmente exigidos para serem pagos por meio de vouchers separados. Se você ativar esta opção, ao lançar o lançamento bancário, o valor pago por tais componentes será lançado como um lançamento separado para cada Funcionário.![Componente salarial flexível](/files/salary-component-1.png)
	
	
	> Nota: O cálculo do Imposto Normal não inclui Benefícios Flexíveis, pois na maioria dos casos estes estão isentos de Imposto. Para tributar esses componentes a qualquer momento antes da última folha de pagamento, use "Deduzir imposto para benefícios de funcionários não reclamados" em Entrada da folha de pagamento/Recibo de salário ao processar o salário.


#### Dedução


![Dedução do componente salarial](/files/salary-component-2.png)


* Variável com Base no Salário Tributável: Se você ativar esta opção, o componente será considerado como o componente padrão de dedução fiscal. O imposto será calculado com base na Tabela de Imposto de Renda vinculada ao funcionário.


## Estrutura Salarial


Estrutura Salarial representa como os Salários são estruturados e calculados com base em Rendimentos e Deduções. As estruturas salariais são usadas para ajudar as organizações:


1. Manter níveis salariais competitivos com o mercado de trabalho externo,
2. Manter relações salariais internas entre cargos,
3. Reconheça e recompense as diferenças no nível de responsabilidade, habilidade e desempenho, e gerencie as despesas salariais.


Os componentes usuais de uma estrutura salarial (na Índia) incluem:


* Salário Básico: É o rendimento base tributável e geralmente não superior a 40% do CTC.
* Subsídio para aluguel de casa: O HRA constitui 40 a 50% do salário base.
* Subsídios Especiais: Compensa a parte restante do salário, em sua maioria menor que o salário base, que é totalmente tributável.
* Subsídio de viagem por licença: o valor não tributável pago pelo empregador ao funcionário para férias/viagens com a família na Índia.
* Gorjeta: é basicamente um valor fixo pago pelo empregador quando o funcionário se demite da organização ou se aposenta.
* PF: Fundo arrecadado em situações de emergência ou velhice. 12% do salário base é descontado automaticamente e vai para a caixa de previdência dos funcionários.
* Subsídio Médico: O empregador paga ao empregado pelas despesas médicas incorridas. É isento de impostos até Rs.15.000.
* Bônus: parte tributável do CTC, geralmente um valor único anual, concedido ao funcionário com base no desempenho individual e organizacional no ano.
* Opções de ações para funcionários: ESOPS são ações gratuitas/com desconto dadas pela empresa aos funcionários. Isso é feito principalmente para aumentar a retenção de funcionários.


![Estrutura salarial enviada](/files/salary-structure.png)
Uma estrutura salarial enviada


### Criando uma nova estrutura salarial


Para criar uma nova Estrutura Salarial acesse:


> Recursos Humanos > Configuração da Folha de Pagamento > Estrutura Salarial > Nova Estrutura Salarial


Na nova estrutura salarial,


1. Nomeie a estrutura salarial e defina a empresa, papel timbrado para impressão do comprovante de salário e frequência da folha de pagamento etc.
2. Defina a data de início da validade (Nota: Só pode haver uma Estrutura Salarial que pode estar “Ativa” para um Funcionário durante qualquer período).
3. Configure o valor do reembolso de licenças por dia, que será o valor a pagar aos funcionários nas solicitações de reembolso de licenças.
4. O valor máximo de benefícios é o valor máximo elegível como Componentes Flexíveis para funcionários.


#### Recibo de salário com base no quadro de horários


O comprovante de salário baseado em quadro de horários é aplicável se você tiver um sistema de folha de pagamento baseado em quadro de horários


1. Verifique "Recibo de salário com base no quadro de horários"
2. Selecione o componente salarial e insira a Taxa Horária (Observação: Este componente salarial é adicionado aos ganhos no Comprovante de Salário)


![Comprovante de salário baseado no quadro de horários](/files/salary-timesheet.png)


#### Ganhos e deduções na estrutura salarial


Nas tabelas “Rendimentos” e “Descontos”, você pode selecionar os componentes de rendimentos e descontos. A condição e a fórmula configuradas no Componente Salarial serão copiadas por padrão, mas você poderá alterar isso se necessário. Você também pode selecionar o componente Base na tabela Ganhos. Observe que o valor elegível para cada funcionário deverá ser configurado em Atribuição de Estrutura Salarial.


Se a condição e a fórmula para qualquer um dos rendimentos ou deduções não estiverem configuradas no Componente Salarial, você poderá calcular os valores dos Componentes Salariais com base em,


#### Condição e Fórmula


![Condição e Fórmula](/files/condition-formula.png)


#### Condição e valor


![Condição e valor](/files/condition-amount.png)


Em condições e fórmulas,


* Use o campo "base" para utilizar o salário base do Funcionário
* Use abreviações dos componentes salariais. Por exemplo: BS para Salário Básico
* Use o nome do campo para detalhes do funcionário. Por exemplo: Tipo de emprego para Employment\_type


#### Detalhes da conta


![Conta de estrutura salarial](/files/salary-structure-account.png)


* Selecione a forma de pagamento e a conta de pagamento para os comprovantes de salário que serão gerados usando esta estrutura salarial


Finalmente, *salve* a estrutura salarial.


### Sair sem remuneração (LWP)


A Licença Sem Remuneração (LWP) acontece quando um Funcionário fica sem licenças alocadas ou tira uma licença sem aprovação (por meio do Pedido de Licença). Se você deseja que o Frappe HR desconte automaticamente o salário em caso de LWP, então você deve verificar
a coluna “Aplicar LWP” nos mestres Tipo de ganho e Tipo de dedução. O valor do corte salarial é a proporção de dias LWP dividida pelo total de dias úteis do mês (com base na Lista de Feriados).


Se você não deseja que o Frappe HR gerencie o LWP, deixe o LWP desmarcado em todos os Tipos de Ganhos e Tipos de Dedução.


## Atribuição de estrutura salarial


Atribuição de estrutura salarial permite atribuir uma estrutura salarial e especificar o pagamento base elegível para cada funcionário. É importante que você defina o salário base para cada atribuição, pois este será o salário base utilizado para os cálculos conforme a Estrutura Salarial.


Para criar uma nova Atribuição de Estrutura Salarial, acesse:


> Recursos Humanos > Folha de Pagamento > Atribuição de Estrutura Salarial > Nova Atribuição de Estrutura Salarial


![Atribuição de estrutura salarial](/files/salary-structure-assignment.png)



# Processamento de folha de pagamento


Você pode processar a folha de pagamento em massa para funcionários de um departamento, filial ou designação ou processar a folha de pagamento individualmente criando recibos de salário para cada funcionário.


## Processamento de folha de pagamento usando entrada de folha de pagamento


Você também pode criar comprovantes de salário para vários funcionários usando o lançamento da folha de pagamento:


> Recursos Humanos > Folha de Pagamento > Lançamento da Folha de Pagamento > Novo Lançamento da Folha de Pagamento


#### Lançamento da folha de pagamento


![Entrada da folha de pagamento](/files/payroll-entry.png)


No lançamento da folha de pagamento,


1. Selecione a Empresa para a qual deseja criar os Recibos de Salário. Você também pode selecionar outros campos como Filial, Departamento, Designação ou Projeto para ser mais específico.
2. Verifique o *Recibo de salário com base no quadro de horários* se desejar processar recibos de salário com base no quadro de horários.
3. Selecione a Data de Postagem e a periodicidade da folha de pagamento com a qual deseja gerar os Recibos de Salário.
4. Clique em "Obter detalhes do funcionário" para obter uma lista de funcionários para os quais os comprovantes de salário serão criados com base nos critérios selecionados.
5. Insira as datas de início e término do período processado na folha de pagamento.
6. Você pode marcar *Deduzir imposto para benefícios de funcionários não reclamados* se quiser deduzir impostos para todos os benefícios (componentes salariais que são *É benefício flexível*) pagos aos funcionários até o atual folha de pagamento
7. Da mesma forma, *Deduzir imposto para comprovante de isenção fiscal não enviado* permite que você deduza impostos sobre os rendimentos que foram isentos nas folhas de pagamento anteriores, conforme declarado em [Declaração de isenção fiscal do funcionário](/docs/pt/human-resources/employee-tax-exemption-declaration) mas o funcionário não enviou provas suficientes [Envio de prova de isenção fiscal de funcionário](/docs/pt/human-recursos/employee-tax-isemption-proof-submission)
8. Selecione o centro de custo e a conta de pagamento.
9. Salve o formulário e envie-o para criar registros de recibo de salário para cada funcionário ativo no período selecionado. Caso os Boletos de Salário já tenham sido criados, o sistema não criará mais Boletos de Salário. Você também pode simplesmente salvar o formulário como Rascunho e criar os comprovantes de salário posteriormente.


![Entrada da folha de pagamento enviada](/files/created-payroll.png)


Depois que todos os comprovantes de salário forem criados, você poderá usar *Ver comprovantes de salário* para verificar se eles foram criados corretamente ou editá-los se desejar deduzir licença sem remuneração (LWP).


Após a verificação, você pode "Enviar" todos juntos clicando em "Enviar comprovante de salário".


>Observação: o envio de comprovantes de salário também reservará a conta padrão da Folha de Pagamento a Pagar para registrar o acúmulo de salário.


#### Reserva de salários em contas


A etapa final é registrar os Salários em suas Contas.


Os salários nas empresas geralmente são tratados com extrema privacidade. Na maioria dos casos, as empresas emitem um único pagamento ao banco combinando todos os salários e o banco distribui os salários para a conta salário de cada funcionário. Dessa forma, haverá apenas um lançamento de pagamento nos livros contábeis da empresa e qualquer pessoa com acesso às contas da empresa não terá acesso aos salários individuais.


O lançamento de pagamento de salário é um lançamento contábil manual que debita o total do componente salarial do tipo de ganho e credita o total do componente salarial do tipo dedução de todos os funcionários na conta padrão definida no nível do componente salarial para cada componente.


Para gerar seu comprovante de pagamento de salário a partir do Lançamento da Folha de Pagamento, clique em-
> Fazer > Lançamento Bancário


![Payroll Make Entry](/files/payroll-make-bank-entry.png)


O lançamento da folha de pagamento encaminhará você para o lançamento contábil manual com filtros relevantes para visualizar os rascunhos de comprovantes contábeis criados. Você deve definir o número de referência e a data das transações e enviar os lançamentos contábeis manuais.


>Observação: para componentes salariais que são benefícios flexíveis e têm a opção *Criar entrada de pagamento separada contra reivindicação de benefício* marcada, o Frappe HR reservará lançamentos contábeis manuais separados.


![Entrada da folha de pagamento](/files/payroll-journal-entry.png)


## Criando recibos de salário manualmente


Depois que a Estrutura Salarial for criada e atribuída aos funcionários via Atribuição de Estrutura Salarial, você poderá fazer um Comprovante de Salário individualmente. Acesse:


> Recursos Humanos > Folha de Pagamento > Comprovante de Salário > Novo Comprovante de Salário


#### Recibo de salário


![Recibo de salário](/files/salary-slip.png)



