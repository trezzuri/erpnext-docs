# Migrador ERPNext QuickBooks



## Como configurar o QuickBooks Migrator?


### Crie um aplicativo QuickBooks Online


1. Na barra Awesome, vá para DocType "QuickBooks Migrator".
2. Acesse o [Portal do desenvolvedor Inuit](https://developer.intuit.com)
3. Faça login com sua conta existente ou inscreva-se.
4. Vá para a página "Meus aplicativos".
5. Clique em "Selecionar APIs".
6. Em "API QuickBooks", marque "Contabilidade".
7. Clique em "Criar aplicativo".


	* Você será direcionado ao painel do seu aplicativo.
8. Vá para a guia "Chaves".
9. Vá para a seção "Chaves de produção".


	* Requisitos completos.
10. Em "QuickBooks Migrator" DocType um "URL de redirecionamento" será gerado para você e adicioná-lo na lista de "URIs de redirecionamento" do seu aplicativo Inuit (na seção "Chaves de produção"). Clique em Salvar.


	* Certifique-se de que o URL de redirecionamento comece com `https`.
11. Na seção "Chaves de produção", copie "ID do cliente" e "Segredo do cliente" para o DocType "QuickBooks Migrator".
12. Salvar "QuickBooks Migrator".


### Conectar-se à API QuickBooks Online


1. Clique em "Conectar ao QuickBooks".
2. Uma nova guia será aberta no seu navegador e você será solicitado a fazer login.
3. Se você tiver mais de uma empresa, selecione a empresa que deseja migrar.
4. Clique em "Conectar".
5. Após a autorização bem-sucedida, a guia será fechada.
6. O indicador será definido como "Conectado ao QuickBooks".
7. Em "QuickBooks Migrator" selecione "Empresa" para onde deseja migrar seus dados.
8. Salvar "QuickBooks Migrator".


### Migrar dados


1. Clique no botão "Obter dados".
2. O indicador mudará de "Conectado ao QuickBooks" para "Em andamento".
3. As barras de progresso mostrarão o status da migração.
4. Isso levará alguns minutos dependendo do tamanho dos dados.
5. Depois que a migração for concluída, o indicador mudará para "Concluído" ou "Falha".


## O que acontecerá quando eu clicar em Buscar dados?


## Conta


### Plano de contas existente



```
Ao criar uma Empresa o ERPNext cria um plano de contas para aquela empresa, essas contas serão mantidas.

```

### Nomeação de conta



```
Para evitar colisão de nomes com contas existentes, todas as contas do QuickBooks receberão o sufixo "-QB".

por exemplo. `Despesa de Trabalho` se tornará `Despesa de Trabalho-QB`.

**Nota**: ERPNext também codifica nomes de contas com a abreviatura da Empresa. Levando isso em consideração, `Job Expense` se tornará `Job Expense-QB-AZ` (assumindo que `AZ` seja a abreviatura da empresa).

```

### Contas raiz



```
Cinco contas raiz, nomeadamente `Asset`, `Equity`, `Expense`, `Liability`, `Income` serão criadas e todas as contas (dependendo do tipo de conta) se tornarão filhas dessas contas.

```

### Contas de grupo



```
QuickBooks permite transações em contas de grupo, o que não é permitido no ERPNext, para lidar com isso, cada conta de grupo terá um filho com um nome hifenizado.

por exemplo.

```


```
 Despesas de Trabalho
        Materiais de trabalho

```

 se tornará
 
```
 Despesas de Trabalho
        Despesas de Trabalho-1
        Materiais de trabalho

```



### Nomear colisões



```
QuickBooks permite que várias contas tenham o mesmo nome, o que não é permitido no ERPNext, para lidar com isso, cada conta duplicada terá um nome hifenizado.

por exemplo.

```


```
 Seguro
        Materiais de trabalho
    Despesas de Trabalho
        Materiais de trabalho

```

 se tornará
  `Seguro
 Materiais de trabalho
 Despesas de Trabalho
 Materiais de Trabalho-1`


## Item


### Nomeação



```
Todos os itens terão nomes codificados pela empresa.

por exemplo. `Pen` se tornará `Pen-AZ` (assumindo que `AZ` seja a abreviatura da empresa).

```

### UOM



```
Todos os itens receberão `Unit` como UOM padrão.

```

### UM fracionária



```
`Unit` poderá ter valor fracionário.

```

### Inventário



```
Independentemente de o item ser um item de estoque ou não de estoque em QuickBooks, nenhuma informação relacionada ao estoque será mantida.

```

## Cliente e Fornecedor


### Nomeação



```
Todos os Clientes e Fornecedores terão nomes codificados da empresa.

por exemplo. `Pen` se tornará `Pen-AZ` (assumindo que `AZ` seja a abreviatura da empresa).

```

## Fatura


### Variantes



```
QuickBooks tem quatro variantes transacionais de fatura, todas elas serão salvas como fatura de vendas.

-**Fatura** equivale a uma Fatura de Venda.
-**Recibo de Venda** equivale a uma Fatura de Venda de PDV.
-**Nota de Crédito** equivale a uma Fatura de Venda de devolução (Nota de Crédito).
-**Recibo de reembolso** equivale a uma fatura de venda de PDV de devolução.

```

### Desconto e acréscimo



```
QuickBooks usa contas especiais para marcação e desconto, o ERPNext não lida com despesas de desconto e marcação dessa forma; em vez disso, todos os itens verão a mudança em suas contas de receita.

```

### Envio



```
Para Notas Fiscais com Frete, será adicionado um Item com nome Frete na tabela de Itens.

```

### Arredondamento



```
ERPNext utiliza método de arredondamento diferente do QuickBooks, por isso, nas Notas Fiscais com Imposto e com moeda diferente da moeda da empresa, a Nota Fiscal de Venda terá um total geral diferente do da Nota Fiscal do QuickBooks.

```

### Caso especial



```
Se uma fatura do QuickBooks estiver vinculada a uma `Cobrança atrasada` ou `Cobrança de extrato`, um `Lançamento contábil manual` equivalente será criado para esta fatura.

```

## Conta


### Variantes



```
QuickBooks tem duas variantes transacionais de Bill, todas elas serão salvas como fatura de compra.

-**Conta** equivale a uma fatura de compra.
-**Crédito do fornecedor** equivale a uma fatura de compra de devolução.

```

## Outro


As seguintes transações serão salvas como lançamento contábil manual


* Pagamento Antecipado
* Pagamento de contas
* Cheque
* Crédito no cartão de crédito
* Despesa
* Ajuste da quantidade de estoque
* Lançamento do diário
* Pagamento
* Pagamento de impostos


## Imposto


Para cada taxa de imposto do QuickBooks, uma conta ERPNext será criada.


## Campos personalizados


QuickBooks Migrator adicionará os seguintes campos personalizados


* Campo empresa


	+ Cliente
	+ Item
	+ Fornecedor
* Campo de ID do QuickBooks


	+ Cliente
	+ Item
	+ Lançamento do diário
	+ Fatura de compra
	+ Fatura de vendas
	+ Fornecedor



