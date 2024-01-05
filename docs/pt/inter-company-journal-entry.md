# Lançamento contábil entre empresas



**Um lançamento contábil entre empresas é feito entre organizações que pertencem ao mesmo grupo.**


Você pode criar um lançamento contábil entre empresas se estiver fazendo transações com várias empresas.
Você pode selecionar as contas que deseja usar nas transações entre empresas. Um possível caso de uso seria uma empresa comprando produtos em nome de outra empresa.


Os lançamentos contábeis manuais entre empresas são criados usando o formulário de lançamento contábil manual no ERPNext. Para acessar a lista de lançamentos contábeis manuais, vá para:



> 
> Página inicial > Contabilidade > Empresa e contas > Lançamento contábil manual
> 
> 
> 


## 1. Pré-requisitos


Antes de criar um lançamento contábil entre empresas, você precisa do seguinte:


* Pelo menos duas [Empresas](/docs/pt/setting-up/company-setup)


## 2. Como criar um lançamento contábil entre empresas


1. Vá para a lista de lançamentos contábeis manuais e clique em Novo.
2. Selecione o tipo de lançamento como 'Lançamento contábil entre empresas'.
3. Defina a Empresa que está comprando Itens em nome de outra empresa.
4. Adicione linhas para os lançamentos contábeis individuais. Somente contas entre empresas podem ser obtidas aqui.
5. Em cada linha, você deve especificar:
	* A conta interna que será afetada.
	* O valor a débito ou crédito.
	* O centro de custo (se for uma receita ou despesa).
6. Ao enviar o lançamento contábil manual, você encontrará um botão no canto superior direito, **Fazer lançamento contábil manual entre empresas**.


![Lançamento contábil entre empresas](/files/inter-company-journal-entry.png)
7. Clique no botão. Agora, você será solicitado a selecionar a empresa contra a qual deseja criar o lançamento contábil vinculado.


![Company Master](/files/select-company-in-inter-company-journal-entry.png)
8. Ao selecionar a Empresa, você será direcionado para outro Lançamento Contábil onde os campos relevantes serão mapeados, ou seja, Empresa, Tipo de Voucher, Referência de Lançamento Contábil Inter Empresa, etc.


![Lançamento contábil entre empresas gerado automaticamente](/files/auto-generated-intercompany-journal-entry.png)
9. Selecione as contas internas da segunda empresa na tabela.
10. Envie o lançamento contábil manual.
11. Certifique-se de que os valores totais de débito e crédito sejam iguais aos valores totais de crédito e débito do lançamento contábil criado anteriormente, respectivamente, mas os débitos e créditos serão opostos.


**Observação:** as contas no segundo lançamento contábil manual devem ser o oposto do que você fez no primeiro lançamento contábil manual.
Por exemplo, a Empresa A está comprando algo da Empresa B. É assim que será o ciclo de pagamento entre as duas empresas usando o lançamento contábil manual entre empresas.


1. Débitar a conta bancária em 500 e creditar a conta dos devedores da Empresa B em 500.
2. Agora, no lançamento contábil manual entre empresas, debite a conta dos credores da empresa A em 500 e credite a conta bancária em 500.
3. Você também precisa selecionar as partes da conta de Credores e Devedores antes de prosseguir com o lançamento contábil manual.


Você também pode encontrar o link de referência na parte inferior, que será adicionado em ambos os lançamentos contábeis manuais vinculados e será removido se algum dos lançamentos contábeis manuais for cancelado.


### 3. Tópicos Relacionados


1. [Lançamento de diário](/docs/pt/accounts/journal-entry)
2. [Faturas entre empresas](/docs/pt/accounts/inter-company-invoices)



