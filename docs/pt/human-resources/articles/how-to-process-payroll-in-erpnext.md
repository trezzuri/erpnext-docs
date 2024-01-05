# Como processar a folha de pagamento no ERPNext



A maioria dos usuários acha difícil processar a folha de pagamento no ERPNext, mas em vez de ser difícil, é um pouco tedioso na configuração inicial. Depois de feita a configuração, o processo dos meses seguintes fica mais fácil. Siga as etapas abaixo para obter um guia rápido:


**1) Criar período de folha de pagamento**


Aqui você define um período para o qual deseja processar a folha de pagamento. Pode ser de janeiro a dezembro ou de abril a março, conforme o ano seguido pela sua empresa.


**2) Criar placas de imposto de renda**


Aqui, você pode criar várias placas de Imposto de Renda se estiver seguindo o sistema de Imposto de Renda Indiano. Definir as lajes conforme norma governamental. Você também pode adicionar impostos adicionais na seção abaixo e condições na tabela, se necessário, e também marcar 'Permitir isenção de impostos' caso haja uma dedução padrão aplicável.


![](/files/J2NBGym.png)


**3) Enviar declaração de isenção fiscal do funcionário**


Um funcionário que possui alguns investimentos pode apresentar declarações fiscais para usufruir de benefícios fiscais e assim reduzir o valor do Imposto de Renda. Eles podem investir em várias subcategorias abaixo de 80C, 80D, etc. (aplicável à tributação indiana).


**4) Definir componentes salariais**


Você pode criar componentes salariais e definir se o componente é um componente de Remuneração ou Dedução. Existem certas caixas de seleção que você pode marcar dependendo do tipo de componente. Selecione a empresa e uma conta contábil padrão. Agora, esses componentes salariais podem ser baseados em uma fórmula específica ou podem ter um valor fixo. Somente para a componente Imposto de Renda é necessário marcar uma caixa específica chamada “Variável com base no Salário Tributável”. Isso garantirá que o Imposto de Renda seja calculado automaticamente no backend.


**5)Crie uma estrutura salarial**


Depois de criar todos os componentes salariais, você pode definir uma estrutura salarial. Você também pode definir se o salário será baseado em planilhas de horas. Você pode adicionar os ganhos e deduções conforme sua escolha e a forma de pagamento.


![](/files/AnuaBH8.png)


**6) Atribuir a estrutura salarial**


Uma vez criadas as estruturas salariais, é necessário atribuí-las aos funcionários. Se você perder esta etapa, não poderá prosseguir. Durante a atribuição, deve-se selecionar a Laje do Imposto de Renda (caso possua múltiplas lajes), pois o percentual de dedução do Imposto de Renda será calculado com base na mesma. Você também pode definir um valor base se suas estruturas salariais forem baseadas em fórmulas.


![](/files/Zg8nsfS.png)


**7) Crie um lançamento de folha de pagamento e recibos de salário**


Depois que todas as etapas acima forem concluídas, você precisará criar um lançamento na folha de pagamento. Depois de selecionar a data e frequência da folha de pagamento e adicionar a conta de pagamento, você pode filtrar os funcionários com base no departamento, designação e filial. Se não desejar fazê-lo, você pode clicar diretamente em 'Obter funcionários'. Ao fazer isso, uma lista de todos os funcionários será preenchida na seção Detalhes do Funcionário. Você pode então prosseguir clicando em "Criar recibos de salário" e todos os recibos de salário serão gerados em rascunho.


![](/files/HQAMnYm.png)


Você pode verificar os rascunhos dos comprovantes de salário e enviá-los por meio do lançamento da folha de pagamento. Ao enviar os comprovantes de vencimento, será criado um lançamento contábil manual. Isso significa que estamos contabilizando as despesas salariais no sistema e não as pagando.![](/files/z7DIBpo.png)


**8) Lançamento bancário**


Depois de registrar os comprovantes de vencimento acumulados, como último passo é necessário fazer um Lançamento Bancário. Com esta última etapa, seu processo de folha de pagamento é concluído, mas isso não significa que os salários sejam transferidos no banco. Essa pequena etapa deve ser feita manualmente.


![](/files/iOrcSFs.png)



