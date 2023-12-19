# Configurações de RH



**As configurações de RH permitem configurações globais para documentos relacionados a RH.**

Para acessar as configurações de RH, vá para: > Página inicial > Recursos humanos > Configurações > Configurações de RH

Existem várias configurações disponíveis nas Configurações de RH.

## 1. Configurações do funcionário

![Experiência profissional anterior](/files/hr-settings1.png)![]()

### 1.1. Idade de aposentadoria:

Você pode inserir a idade de aposentadoria (em anos) para seus funcionários.

### 1.2 Registros de funcionários a serem criados

A nomenclatura dos documentos de funcionários é baseado no valor selecionado neste campo.

* **Série de Nomenclatura**: Os documentos de funcionários criados serão nomeados usando a série de nomenclatura selecionada em 'Série' campo.
* **Número do Funcionário**: O campo Número do Funcionário fica visível ao selecionar este campo, e a nomeação do documento do funcionário acontece com base neste campo.
* **Nome completo**: O documento do funcionário é nomeado usando o nome completo do funcionário.

### 1.3 Parar lembretes de aniversário

Um e-mail é enviado a todos os funcionários da empresa quando um funcionário faz aniversário. Para impedir que este e-mail seja enviado, você pode marcar esta opção.

### 1.4 Aprovador de despesas obrigatório no relatório de despesas

No documento de relatório de despesas, o campo 'Aprovador de despesas' é definido como obrigatório na verificação esta opção.

> As configurações da folha de pagamento farão parte das configurações de RH até a versão 12. Na versão 13, as configurações da folha de pagamento farão parte do novo módulo, Folha de pagamento.

## 2. Configurações de folha de pagamento

![Experiência profissional anterior](/files/hr-settings2.png)![]()  


### 2.1 Calcular dias úteis da folha de pagamento com base em

dias úteis no comprovante de salário podem ser calculado com base no pedido de licença ou nos registros de presença. Você pode selecionar a opção com base no que deseja calcular os dias úteis.

### 2.2 Máximo de horas de trabalho em relação ao quadro de horários

Para comprovantes de salário baseados no quadro de horários, você pode definir o máximo de horas permitidas contra um único quadro de horários. Defina este valor como zero para desabilitar esta validação.

### 2.3 Incluir feriados no Total no. de Dias Úteis

Se marcado, o número total de dias úteis incluirá feriados, e isso reduzirá o valor do salário por dia.

### 2.4 Desativar Total Arredondado

Você pode ativar esta opção para desativar o arredondamento do valor total nos comprovantes de salário.

### 2,5 Fração de Salário Diário para Meio Dia

Com base nesta fração, o salário para Meio Dia será calculado. Por exemplo, se o valor for definido como 0,75, os três quartos do salário serão dados para a frequência de meio dia.

### 2.6 Enviar recibo de salário por e-mail ao funcionário

Um e-mail com o salário o comprovante de salário é enviado para o endereço de e-mail preferido do respectivo funcionário no momento do envio do comprovante de salário.

### 2.7 Criptografar comprovantes de salário em e-mails

O PDF do comprovante de salário enviado ao funcionário é criptografado usando o mencionado Política de Senha.

### 2.8 Política de Senha

Este campo se torna visível e obrigatório ao marcar a opção acima para criptografar o comprovante de salário no e-mail.

Aqui está um exemplo sobre como definir uma Política de Senha para o PDF do comprovante de salário.

**Exemplo:**


```
SAL-{first_name}-{date_of_birth.year}
  

```
Isso gerará uma senha como SAL-Jane-1972

## **3. Configurações de mudança**

**![](https://lh7-us.googleusercontent.com/A9IyXp8Eyjcnl4aVb164XrJ-bE-senEbgybURCe9zXcvMAKbzj-wXdCNPNgBc8xyWvpCBDQrXnHfMv5827Q6nFb2tEj-zwLnYtsuSpuaTbyKdqFOhenGoOsqQRydhWMbIalDoshnR1Lh)![]()**  


###  **3.1 Permitir múltiplas atribuições de turno para a mesma data**

Ativar esta opção permite que o usuário crie atribuições de turno para um funcionário com atribuições pré-existentes em qualquer uma das datas dentro do intervalo selecionado e vice-versa. 

## 4. Sair das configurações

![Experiência de trabalho anterior](/files/hr-settings3.png)![]()  


### 4.1 Modelo de notificação de aprovação de licença

Ao criar ou atualizar um pedido de licença com um aprovador de licença, um e-mail será enviado a esse aprovador de licença notificando sobre o novo pedido de licença. O modelo de e-mail utilizado para este fim pode ser selecionado aqui.

### 4.2 Modelo de notificação de status de licença

No envio/cancelamento de um pedido de licença, o funcionário recebe um e-mail com o status atualizado de seu pedido de licença. O modelo de e-mail usado para essa finalidade pode ser selecionado aqui.

### 4.3 Aprovador de licença obrigatório no pedido de licença

No documento de solicitação de licença, o campo 'Aprovador de licença' é definido como obrigatório ao verificar isso. opção.

### 4.4 Mostrar licenças de todos os membros do departamento no calendário

As licenças aprovadas de todos os funcionários do mesmo departamento são mostradas na visualização do calendário ao marcar esta opção.

 ### 4.5 Reembolso automático de licenças

Se marcado, o sistema gera um registro preliminar de Resgate de licenças no vencimento da alocação de licenças para todos os tipos de licenças recuperáveis.

### 4.6 Restringir solicitação de licença retroativa

Se marcada, o sistema não permitirá fazer um pedido de licença retroativo.

> Introduzido na versão 13

### 4.7 Alocação automática de licenças com base na política de licenças

Se marcado, as licenças serão concedidas aos funcionários automaticamente com base na data de vigência a partir de acordo com a presente Atribuição de Política de Licenças.

## 5. Configurações de contratação

![image](https://user-images.githubusercontent.com/24353136/135511758-4300b29e-78c2-4492-a6a7-d75d0632fd5a.png)![]()  


### 5.1 Verificar vagas Na criação de ofertas de emprego

Na criação de uma oferta de emprego para um determinado cargo, as vagas presentes no plano de pessoal desse cargo são verificadas para alertar o usuário sobre contratações excessivas para um determinado cargo.

 ### 5.2 Enviar lembrete de entrevista

Ativar esta opção enviará um e-mail de lembrete a todos os entrevistadores associados à rodada de entrevista de uma entrevista futura. Este e-mail será agendado de acordo com o campo Lembrar antes definido pelo usuário.

### 5.2 Enviar lembrete de feedback da entrevista

Ativar esta opção acionará e-mails de lembrete a serem enviados aos entrevistadores associados. com uma rodada de entrevistas conduzida, mas ainda não enviou seu feedback.



