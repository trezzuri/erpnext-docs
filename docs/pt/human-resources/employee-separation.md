# Separação de funcionários



**Separação de Funcionário é uma situação em que o contrato de serviço de um Funcionário com sua organização termina e o Funcionário sai da organização.**


A Separação de Funcionário é criada para um Funcionário que pediu demissão ou demitiu-se da organização.


**Caso de uso:** vamos supor que a seguir estão as atividades que precisam ser executadas assim que um funcionário precisa ser separado da organização.


* Coletar laptop
* Eliminar taxas
* Excluir conta de e-mail do funcionário
* Coletar carteira de identidade


No Frappe HR, essas atividades padrão podem ser acompanhadas no Modelo de Separação de Funcionários. Para acessar a Separação de Funcionários, acesse:


> Recursos Humanos > Ciclo de Vida do Funcionário > Separação de Funcionário


## 1. Pré-requisitos


Antes de criar uma Separação de Funcionário, é aconselhável que você crie os seguintes documentos:


* [Funcionário](/docs/pt/human-resources/employee)
* [Departamento](/docs/pt/human-resources/department)
* [Designação](/docs/pt/human-resources/designation)
* [Classificação de funcionário](/docs/pt/human-resources/employee-grade)


## 2. Como criar uma separação de funcionários


1. Acesse: Separação de funcionários > Novo.
2. Selecione o Funcionário. Assim que o Funcionário for selecionado, as informações correspondentes do Funcionário, como Departamento, Designação e Grau do Funcionário, serão obtidas automaticamente.
3. Selecione o [Modelo de separação de funcionários](#31-employee-separation-template). Com base no modelo selecionado, serão buscadas automaticamente informações como Departamento, Designação e Grau do Funcionário (caso já mencionadas no Modelo de Separação).
4. Insira a data da carta de demissão.
5. Além disso, você também pode inserir o Resumo da Entrevista de Saída.
6. Salvar e enviar.


![Modelo de separação](/files/employee-separation.png)


> Observação 1: se um modelo de separação de funcionários não for criado, você poderá preencher diretamente as informações de separação no próprio tipo de documento de separação de funcionários.


> Nota 2: O 'Status' da Separação de Funcionário mudará para Concluído assim que todas as Atividades associadas forem concluídas.


## 3. Recursos


### 3.1 Modelo de separação de funcionários


O modelo de separação de funcionários é um modelo que contém uma lista predefinida de atividades para separação de funcionários. Um modelo de separação de funcionários pode ser criado para um departamento, designação e categoria de funcionário específicos.


Para criar um novo modelo de separação de funcionários:


1. Acesse: Recursos Humanos > Ciclo de Vida do Funcionário > Modelo de Separação de Funcionário > Novo.
2. Insira o departamento, a designação e a categoria do funcionário (opcional).
3. Mencione as atividades para separação. Para cada Atividade, você também pode mencionar o Usuário ou Função, ou um deles, a quem esta Atividade será atribuída.
4. Você também pode agendar as Atividades de Separação especificando o **Início em (Dias)**, ou seja, quando a atividade deve começar e a **Duração (Dias)** para a atividade. mesmo.


![Modelo de separação](/files/separation-template.png)


### 3.2 Tarefas e atribuições


Ao enviar a Separação de Funcionário, um [Projeto](https://docs.erpnext.com/docs/v143/user/videos/learn/project-and-task) será criada. Dentro do Projeto, [Tarefas](https://docs.erpnext.com/docs/v143/user/videos/learn/project-and-task) também serão criadas para cada Atividade.
Se você definiu a data e a duração das atividades, as tarefas serão criadas com as datas de início e término apropriadas, exceto feriados.


Você pode visualizar os projetos e tarefas criados em Exibir > Projeto/Tarefas.


Além disso, cada atividade pode receber pesos com base em sua importância.


![Tarefas e atribuições](/files/employee-sep1.png)


Com base no progresso das Tarefas, o progresso pode ser atualizado no processo de Separação de Funcionários.


### 3.3 Status do funcionário


Você pode visualizar diretamente o Funcionário separado por meio do tipo de documento Separação de Funcionário em Exibir > Funcionário assim que o formulário for enviado.


## 4. Tópicos Relacionados


1. [Integração de funcionários](/docs/pt/human-resources/employee-onboarding)
2. [Promoção de funcionários](/docs/pt/human-resources/employee_promotion)
3. [Separação de funcionários](/docs/pt/human-resources/employee-separation)



