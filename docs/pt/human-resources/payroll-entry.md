# Lançamento da folha de pagamento



**A folha de pagamento é a soma total de todas as remunerações que uma empresa deve pagar aos seus funcionários por um determinado período de tempo ou em uma determinada data.**

No Frappe HR , a entrada da folha de pagamento permite o processamento em massa da folha de pagamento dos funcionários. Em outras palavras, processar os comprovantes de salário de todos os funcionários de uma só vez. O processamento em massa pode ser para toda a empresa ou baseado nestas categorias: Filial, Departamento ou Designação.

Para acessar o lançamento da folha de pagamento, vá para:


> Home > Recursos Humanos > Folha de pagamento > Entrada da folha de pagamento
> 
> 

## 1. Como criar um lançamento de folha de pagamento

1. Vá para a lista de lançamento de folha de pagamento e clique em Novo.
2. Selecione a frequência da folha de pagamento.
3. Selecione Filial, Designação e Departamento para filtrar funcionários (opcional).
4. Selecione Projeto (opcional) se desejar executar a folha de pagamento em relação a um projeto.
5. Selecione as caixas de seleção 'Validar frequência' e 'Comprovante de salário com base no quadro de horários' caso queira deduzir o salário com base na frequência e se desejar considerar também as planilhas de horas dos funcionários respectivamente.
6. Selecione a Conta de Pagamento para fazer o Lançamento Bancário.
7. Salvar.

Depois que as informações forem salvas, clique no botão **Obter Funcionários** para obter uma lista de funcionários para os quais os comprovantes de salário serão criados com base em critérios selecionados.

Uma vez obtida a lista de funcionários, clique no botão **Criar recibos de salário** para gerar recibos de salário.

![ Entrada da folha de pagamento](/files/payroll-entry-get-employees.png)


> **Observação:** Se os comprovantes de salário já tiverem sido criados, o sistema não criará mais recibos de salário. Você também pode simplesmente salvar o formulário como Rascunho e criar os recibos de salário posteriormente.
> 
> 

## 2. Recursos

### 2.1 Acúmulo de Salário

Depois de verificar os comprovantes de salário, você pode enviá-los todos juntos clicando no botão **Enviar comprovante de salário**.

 ![Payroll Entry](/files/payroll-entry.png)

Isso também reservará a conta padrão da folha de pagamento a pagar em relação aos respectivos cabeçalhos de despesas (conforme configurado em Salário Componentes) para registrar o acúmulo de salário aos funcionários.

**Centro de Custo:**

Você pode selecionar Centro de Custo na Entrada da Folha de Pagamento contra a qual as despesas serão lançada.

Se desejar registrar despesas em vários centros de custo com base no Funcionário/Departamento, você poderá fazer isso definindo Centro de Custo da Folha de Pagamento no cadastro de Funcionário/Departamento.

![](/files/ViFAtRT.png)

Até mesmo vários centros de custo podem ser atribuídos a um único funcionário. Você pode fazer isso por meio do documento Atribuição de estrutura salarial.

![](/files/hUnTWPJ.png)

Centro de custo atribuído na Atribuição de estrutura salarial obtém a prioridade mais alta e, em seguida, o mestre do Funcionário e do Departamento, respectivamente. A menor prioridade é dada ao Centro de Custo selecionado em Entrada da Folha de Pagamento.

![Entrada da Folha de Pagamento](/files/payroll-make-accrual-entry.png)


> **Observação:** O envio manual de recibos de salário um por um não criará o lançamento contábil manual para registrar o acúmulo de salário.
> 
> 

### 2.2 Pagamento de salário

A etapa final é agendar o pagamento do salário.

Os salários nas empresas geralmente são tratados com extrema privacidade. Na maioria dos casos, as empresas emitem um único pagamento ao banco combinando todos os salários e o banco distribui os salários para a conta salarial de cada funcionário.

Desta forma, há apenas um lançamento de pagamento nos livros de contas da empresa e de qualquer pessoa. com acesso às contas da empresa não terá acesso aos salários individuais.

O lançamento de pagamento de salário é um lançamento contábil manual que debita o total do componente salarial do tipo Lucro e credita o total do componente salarial do tipo Deduções de todos os Funcionários para a conta padrão definida no nível do Componente Salarial para cada componente.

Para gerar seu comprovante de pagamento de salário a partir do Lançamento da Folha de Pagamento, clique no botão **Fazer Lançamento Bancário**.

O lançamento da folha de pagamento encaminhará você para o lançamento contábil manual com filtros relevantes para visualizar os rascunhos de comprovantes contábeis criados. Você terá que definir o número de referência e a data das transações e enviar o lançamento contábil manual.

![Payroll Entry](/files/payroll-make-bank-entry.png)


> **Observação:** para componentes salariais que são benefícios flexíveis e têm a opção *Criar entrada de pagamento separada contra reivindicação de benefício* marcada, o Frappe HR reservará rascunhos de lançamentos contábeis separados.
> 
> 

## 3. Tópicos relacionados

1. [Componente Salarial](/docs/pt/human-resources/salary-component)
2. [Estrutura Salarial](/docs/pt/human-resources/salary-structure)
3. [Período da folha de pagamento](/docs/pt/human-resources/payroll-period)
4. [Lançamento de diário](/docs/pt/accounts/journal-entry)


