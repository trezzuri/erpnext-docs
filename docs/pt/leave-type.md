# Deixar digitar



**Tipo de licença refere-se aos tipos de licenças alocadas a um funcionário que ele pode usar ao fazer solicitações de licença.**

Você pode criar qualquer número de tipos de licença com base de acordo com os requisitos da sua empresa.

Para acessar o tipo de licença, vá para:


> Home > Recursos Humanos > Licenças > Tipo de licença
> 
> 

##  1. Como criar um tipo de licença

1. Vá para a lista Tipo de licença, clique em Novo.
2. Insira o nome do tipo de licença.
3. Insira a alocação máxima de férias permitida, aplicável após (dias úteis), máximo de licenças consecutivas permitidas (opcional).
4. Salvar.

![](/files/22ZtSxQ.png)![]()

Abaixo está uma explicação detalhada de todos os campos e caixas de seleção em Tipo de licença.

* **Alocação máxima de licenças permitida:** Este campo permite definir o número máximo de alocação anual deste tipo de licença ao criar a Política de licenças.
* **Aplicável após (dias úteis):** Insira aqui o número mínimo de dias úteis. Somente os funcionários que trabalharam este número de dias ou mais poderão solicitar este tipo específico de licença. Quaisquer outras licenças (como licença casual, licença médica, etc.) aproveitadas pelos funcionários após a data de adesão também serão consideradas no cálculo dos dias úteis do funcionário.
* **Máximo de licenças consecutivas permitidas:** Refere-se ao número máximo de dias que este tipo de licença específico pode ser aproveitado de uma só vez. Se um funcionário exceder o número máximo de dias, sua licença estendida será considerada como 'Licença sem remuneração'.
* **É transportado:** Se marcado , o saldo de licenças deste tipo de licença será transportado para o próximo período de alocação.
* **É licença sem remuneração:** Isso garante que o tipo de licença serão tratadas como licenças sem remuneração e o salário será deduzido para este tipo de licença.
* **É licença opcional:** licenças opcionais são feriados que os funcionários podem escolher aproveitar uma lista de feriados publicada pela empresa. A lista de feriados para licenças opcionais pode ter qualquer número de feriados, mas você pode restringir o número dessas licenças definindo o campo Máximo de dias de licença permitidos.
* **Permitir negativo Saldo:** Se marcado, o sistema sempre permitirá aplicar e aprovar [Solicitações de licença](/docs/pt/human-resources/leave-application) para o tipo de licença, mesmo que não haja saldo de licença.
* **Permitir superalocação:** se marcada, o sistema permitirá a alocação de mais licenças do que o número de dias no período de alocação.
* **Incluir feriados nas licenças como licenças:** Marque esta opção se você deseja contar os feriados dentro das licenças como uma 'licença'. Por exemplo, se um funcionário solicitou licença na sexta e segunda-feira, e sábado e domingo são folgas semanais, se a caixa de seleção 'Incluir feriados nas férias como licenças' para o tipo de licença estiver marcada, o sistema considerará sábado como domingo como férias também. Tais férias serão deduzidas do número total de licenças.
* **É Compensatória:** As licenças compensatórias são licenças concedidas por horas extras ou feriados, normalmente compensadas como uma licença recuperável. Você pode marcar esta opção para marcar o Tipo de Licença como compensatório. Um funcionário pode solicitar licenças compensatórias usando [Solicitação de licença compensatória](/docs/pt/human-resources/compensatory-leave-request) .


> Introduzido na versão 13
> 
> 

* **É parcialmente pago Licenças:** Esta caixa de seleção garante que o Tipo de Licença será tratado como parcialmente pago e parte dos rendimentos diários será paga através do comprovante de salário. Se esta caixa de seleção estiver habilitada, aparecerá um campo "Fração do Salário Diário por Licença" onde você poderá definir a fração do salário diário pago no dia da licença parcial.

![](/files/8IeXPo5.png)![]()


> **Nota:** O tipo de licença pode ser licença sem remuneração ou parcialmente remunerada.
> 
> 

## 2. Recursos

### 2.1 Pagamento de licenças

É possível que os funcionários possam receber dinheiro de seu empregador por licenças não utilizadas concedidas a eles em um período de licença. Nem todos os tipos de licença precisam ser recuperáveis, portanto, você deve definir "Permitir cobrança" apenas para os tipos de licença que podem ser recuperáveis.


> **Observação:** o cobrança de licença é permitido somente no último mês do período de licença.
> 
> 

![](/files/N7AiiYE.png)![]()  


**Folhas Não-Encaixáveis:** Este campo indica o número de dias de folga que os Funcionários não poderão cobrar. Acima dos dias mencionados, o Funcionário é elegível para receber licenças.

Por exemplo, se houver 10 licenças de um determinado tipo de licença que podem ser cobradas e o Funcionário tiver 8 licenças restantes. Se Folhas Não Reembolsáveis ​​= 5, o Funcionário recebe apenas 8-5 = 3 licenças.

**Componente de Ganhos:** Este campo permite que você especifique o Componente Salarial que será será cobrado aos funcionários como parte de seu salário no comprovante de salário.


> **Observação:** ao enviar um [Leave Encashment](/docs/pt/human-resources/leave-encashment) para um funcionário, o Frappe HR cria automaticamente um [Salário Adicional](/docs/pt/human-resources/additional-salary) que será adicionado ao Comprovante de Salário do Funcionário ao processar a próxima folha de pagamento.
> 
> 

### 2.2 Licenças Ganhas

Licenças Ganhas são licenças obtidas por um Funcionário após trabalhar na empresa por um determinado período de tempo. Marcar "É licença ganha" atribuirá folhas proporcionalmente, atualizando automaticamente a alocação de licenças para licenças deste tipo em intervalos definidos por 'Frequência de licenças ganhas'.

Por exemplo, um funcionário recebe 24 licenças privilegiadas. em um ano, em que a Licença Privilégio é definida como Licença Ganha com Dotação Mensal. Neste caso, o Colaborador ganhará 2 (24 licenças/12 meses) Licenças Privilegiadas ao final de cada mês. O processo de atribuição de licenças (trabalho em segundo plano) apenas alocará folhas considerando o número máximo de licenças para o tipo de licença e arredondará para 'Arredondamento' para frações.

![](/files/1SrI5mm.png)![]()  



> **Observação:** A alocação inicial deste tipo de licença será 0. As licenças serão atualizadas no final do mês (ou de acordo com o conjunto de 'Frequência de licenças ganhas').
> 
> 

### 2.3 Tipos de licença padrão

Existem alguns tipos de licença pré-carregados no sistema, como abaixo:

* **Licença sem remuneração :** Você pode aproveitar essas licenças para diversos fins, como problemas médicos prolongados, fins educacionais ou motivos pessoais inevitáveis. A caixa de seleção 'Licença sem remuneração' para este tipo de licença está marcada por padrão. O funcionário não é pago por essas licenças.
* **Licenças privilegiadas:** são como licenças merecidas que podem ser aproveitadas para viagens, férias familiares e e assim por diante.
* **Licença médica:** você pode aproveitar essas licenças se não estiver bem.
* **Folgas compensatórias:** são licenças compensatórias atribuídas aos funcionários por horas extras. A caixa de seleção 'É Compensatória' para este tipo de licença está marcada por padrão.
* **Licença casual:** você pode aproveitar esta licença para cuidar de assuntos urgentes. e assuntos invisíveis.

## 3. Tópicos relacionados

1. [Período de licença](/docs/pt/human-resources/leave-period)
2. [Política de licença](/docs/pt/human-resources/leave-policy)
3. [Deixar alocação](/docs/pt/human-resources/leave-allocation)
4. [Sair do aplicativo](/docs/pt/human-resources/leave-application)
5. [Solicitação de licença compensatória](/docs/pt/human-resources/compensatory-leave-request)
6. [Sair do reembolso](/docs/pt/human-resources/leave-encashment)


