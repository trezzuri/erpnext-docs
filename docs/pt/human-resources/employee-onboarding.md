# Integração de funcionários



**No processo de contratação de um Colaborador, existe um conjunto de atividades padrão que precisam ser executadas. Este recurso ajuda você a manter o controle dessas atividades, além de criar um conjunto de tarefas no momento da contratação de cada Colaborador.**


O Employee Onboarding é criado para um formulário de emprego, que é aprovado para a contratação.


**Caso de uso:** vamos supor que a seguir estão as atividades que precisam ser executadas assim que um candidato a emprego for aprovado para ser contratado.


* Realize uma verificação de antecedentes jurídicos e profissionais
* Criar um cadastro de funcionários
* Crie uma conta de e-mail
* Crie uma carteira de identidade
* Alocar folhas


No Frappe HR, essas atividades padrão podem ser acompanhadas no modelo de integração de funcionários. Para acessar a integração de funcionários, acesse:


> Recursos Humanos > Ciclo de Vida do Funcionário > Integração do Funcionário


## 1. Pré-requisitos


Antes de criar um Employee Onboarding, é aconselhável que você crie os seguintes documentos:


* [Candidato a emprego](/docs/pt/human-resources/job-applicant)
* [Funcionário](/docs/pt/human-resources/employee)
* [Departamento](/docs/pt/human-resources/department)
* [Designação](/docs/pt/human-resources/designation)
* [Classificação de funcionário](/docs/pt/human-resources/employee-grade)


## 2. Como criar um Onboarding de Funcionários


1. Acesse: Integração de funcionários > Novo.
2. Selecione o candidato ao emprego. assim que o Candidato for selecionado, o Funcionário correspondente será obtido automaticamente.
3. Selecione o [Modelo de integração de funcionários](#31-employee-onboarding-template). Com base no modelo selecionado, informações como Departamento, Designação e Grau do Funcionário serão buscadas automaticamente (caso já mencionadas no Modelo de Onboarding).
4. Insira a data de adesão.
5. Salvar e enviar.


![Modelo de integração](/files/employee-onboarding1.png)


> Observação 1: se um modelo de integração de funcionários não for criado, você poderá preencher diretamente as informações de integração no próprio tipo de documento de integração de funcionários.


> Nota 2: O 'Status' da integração do funcionário mudará para Concluído assim que todas as atividades associadas forem concluídas.


## 3. Recursos


### 3.1 Modelo de integração de funcionários


O modelo de integração de funcionários é um modelo que contém uma lista predefinida de atividades para integração de funcionários. Um modelo de integração de funcionários pode ser criado para um departamento, designação e categoria de funcionário específicos.


Para criar um novo modelo de integração de funcionários:


1. Acesse: Recursos Humanos > Ciclo de Vida do Funcionário > Modelo de integração de funcionários > Novo.
2. Insira o departamento, a designação e a categoria do funcionário (opcional).
3. Mencione as atividades de integração. Para cada Atividade, você também pode mencionar o Usuário ou Função, ou uma delas, a quem esta Atividade será atribuída.
4. Você também pode agendar as atividades de integração especificando o **Início em (dias)**, ou seja, quando a atividade deve começar e a **Duração (em dias)** para o mesmo.


![Modelo de integração](/files/onboarding-template972e99.png)


### 3.2 Tarefas e atribuições


Após o envio da integração do funcionário, um [Projeto](https://docs.erpnext.com/docs/v143/user/manual/en/projects/project) será criado. Dentro do Projeto, [Tarefas](https://docs.erpnext.com/docs/v143/user/manual/en/projects/tasks) também serão criadas para cada Atividade.
Se você definiu a data e a duração das atividades, as tarefas serão criadas com as datas de início e término apropriadas, exceto feriados.


Você pode visualizar os Projetos e Tarefas criados conforme mostrado abaixo:


![Modelo de integração](/files/project-task.png)


Além disso, cada atividade pode receber pesos com base em sua importância.


![Tarefas e atribuições](/files/employee-onboarding3.png)


Com base no progresso das Tarefas, o progresso pode ser atualizado no processo de integração de funcionários.


### 3.3 Criação de funcionários


Você pode criar um funcionário diretamente por meio do tipo de documento de integração de funcionários (se ainda não tiver sido criado) assim que todas as tarefas obrigatórias de integração forem concluídas.


![Modelo de integração](/files/onboarding-employee.png)


## 4. Tópicos Relacionados


1. [Promoção de funcionários](/docs/pt/human-resources/employee_promotion)
2. [Separação de funcionários](/docs/pt/human-resources/employee-separation)
3. [Transferência de funcionários](/docs/pt/human-resources/employee_transfer)



