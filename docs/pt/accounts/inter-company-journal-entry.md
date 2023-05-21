# Lançamento Diário Intercompanhia


**Uma entrada de diário entre empresas é feita entre organizações que pertencem ao mesmo grupo.**


Você pode criar um lançamento contábil entre empresas se estiver fazendo transações com várias empresas.
Você pode selecionar as contas que deseja usar nas transações entre empresas. Um possível caso de uso seria uma empresa comprando mercadorias em nome de outra empresa.


Os lançamentos contábeis manuais entre empresas são criados usando o formulário de lançamento contábil manual no ERPNext. Para acessar a lista de entrada de diário, vá para:



>
> Home > Contabilidade > Empresa e Contas > Lançamento do Diário
>
>
>


## 1. Pré-requisitos


Antes de criar um lançamento contábil entre empresas, você precisa do seguinte:


* Pelo menos duas [Empresas](/docs/v13/user/manual/en/setting-up/company-setup)


## 2. Como criar um Lançamento Diário Interempresarial


1. Vá para a lista Lançamento do diário e clique em Novo.
2. Selecione o tipo de entrada como 'Entrada de diário entre empresas'.
3. Defina a empresa que está comprando itens em nome de outra empresa.
4. Adicione linhas para os lançamentos contábeis individuais. Somente contas entre empresas podem ser buscadas aqui.
5. Em cada linha, você deve especificar:
* A conta interna que será afetada.
* O valor para Débito ou Crédito.
* O Centro de Custo (Se for uma Receita ou Despesa).
6. Ao enviar o Lançamento Diário, você encontrará um botão no canto superior direito, **Fazer Lançamento Diário Interempresarial**.


![Entrada no diário da empresa](/files/inter-company-journal-entry.png)
7. Clique no botão. Agora, você será solicitado a selecionar a empresa contra a qual deseja criar o lançamento contábil vinculado.


![Mestre da empresa](/files/select-company-in-inter-company-journal-entry.png)
8. Ao selecionar a Empresa, você será direcionado para outro Lançamento no Diário, onde os campos relevantes serão mapeados, ou seja, Empresa, Tipo de Voucher, Referência do Lançamento no Diário Interempresarial, etc.


![Entrada de diário entre empresas gerada automaticamente](/files/auto-generated-intercompany-journal-entry.png)
9. Selecione as contas internas para a segunda empresa na tabela.
10. Envie a entrada de diário.
11. Certifique-se de que os valores totais de débito e crédito sejam iguais aos valores totais de crédito e débito do lançamento contábil criado anteriormente, respectivamente, mas os débitos e créditos serão opostos.


**Observação:** As contas no segundo lançamento no diário devem ser o oposto do que você fez no primeiro lançamento no diário.
Por exemplo, a Empresa A está comprando algo da Empresa B. É assim que o ciclo de pagamento entre as duas empresas se parecerá usando o Lançamento Diário Interempresarial.


1. Debitar a Conta Bancária em 500 e creditar a conta Devedores da Empresa B em 500.
2. Agora, no Lançamento Diário Interempresarial, debite a conta dos Credores da Empresa A em 500 e credite a Conta Bancária em 500.
3. Você também precisa selecionar as partes para a conta Credores e Devedores antes de prosseguir com o Lançamento Diário.


Você também pode encontrar o link de referência na parte inferior, que será adicionado em ambos os lançamentos contábeis vinculados e será removido se algum dos lançamentos contábeis for cancelado.


### 3. Tópicos Relacionados


1. [Entrada de diário](/docs/v13/user/manual/en/accounts/journal-entry)
2. [Faturas entre empresas](/docs/v13/user/manual/en/accounts/inter-company-invoices)