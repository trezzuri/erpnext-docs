# ERPNext Migrador de QuickBooks


## Como configurar o QuickBooks Migrator?


### Criar um aplicativo QuickBooks Online


1. Na Awesome-bar, vá para DocType "QuickBooks Migrator".
2. Acesse [Inuit Developer Portal](https://developer.intuit.com)
3. Faça login com sua conta existente ou cadastre-se.
4. Vá para a página "Meus aplicativos".
5. Clique em "Selecionar APIs".
6. Em "API do QuickBooks", marque "Contabilidade".
7. Clique em "Criar aplicativo".


	* Você será direcionado para o Painel do seu aplicativo.
8. Vá para a guia "Chaves".
9. Vá para a seção "Chaves de produção".


	* Requisitos completos.
10. No "QuickBooks Migrator" DocType, um "URL de redirecionamento" será gerado para você e adicionado à lista de "URIs de redirecionamento" do seu aplicativo Inuit (na seção "Chaves de produção"). Clique em Salvar.


	* Certifique-se de que o URL de redirecionamento comece com `https`.
11. Na seção "Chaves de produção", copie "ID do cliente" e "Segredo do cliente" para o DocType "QuickBooks Migrator".
12. Salve "QuickBooks Migrator".


### Conectar-se à API QuickBooks Online


1. Clique em "Conectar ao QuickBooks".
2. Uma nova guia será aberta em seu navegador e você será solicitado a fazer login.
3. Se você tiver mais de uma empresa, selecione a empresa que deseja migrar.
4. Clique em "Conectar".
5. Após a autorização bem-sucedida, a guia será fechada.
6. O indicador será definido como "Conectado ao QuickBooks".
7. Em "QuickBooks Migrator", selecione "Empresa" para onde deseja migrar seus dados.
8. Salve "QuickBooks Migrator".


### Migrar dados


1. Clique no botão "Buscar dados".
2. O indicador mudará de "Conectado ao QuickBooks" para "Em andamento".
3. As barras de progresso mostrarão o status da migração.
4. Isso levará alguns minutos, dependendo do tamanho dos dados.
5. Após a conclusão da migração, o indicador mudará para "Concluída" ou "Falha".


## O que acontecerá quando eu clicar em Buscar dados?


## Conta


### Plano de contas existente



```
Ao criar uma Empresa o ERPNext cria um plano de contas para aquela empresa, essas contas serão mantidas.

```

### Nomenclatura de contas



```
Para evitar colisão de nomes com contas existentes, todas as contas do QuickBooks receberão o sufixo "- QB".

por exemplo. `Job Expense` se tornará `Job Expense - QB`.

**Observação**: ERPNext também codifica nomes de contas com a abreviação da empresa. Levando isso em consideração, `Job Expense` se tornará `Job Expense - QB - AZ` (assumindo que `AZ` é a abreviação da empresa).

```

### Contas raiz



```
Cinco contas root, ou seja, `Asset`, `Equity`, `Expense`, `Liability`, `Income` serão criadas e todas as contas (dependendo do tipo de conta) se tornarão filhas dessas contas.

```

### Contas de grupo



```
QuickBooks permite transações em contas de grupo, o que não é permitido no ERPNext, para lidar com isso, cada conta de grupo terá um filho com um nome hifenizado.

por exemplo.

```


```
 Despesas de trabalho
        Materiais de Trabalho

```

 se tornará
 
```
 Despesas de Trabalho
        Despesas de Trabalho - 1
        Materiais de Trabalho

```



### Colisões de nomes



```
O QuickBooks permite que várias contas tenham o mesmo nome, o que não é permitido no ERPNext, para lidar com isso, toda conta duplicada terá um nome hifenizado.

por exemplo.

```


```
 Seguro
        Materiais de Trabalho
    Despesas de trabalho
        Materiais de Trabalho

```

 se tornará
  Seguro
 Materiais de Trabalho
 Despesas de trabalho
 Materiais de Trabalho - 1



## Item


### Nomenclatura



```
Todos os itens terão nomes codificados da empresa.

por exemplo. `Pen` se tornará `Pen - AZ` (assumindo que `AZ` é a abreviação da empresa).

```

### UOM



```
Todos os itens serão atribuídos `Unit` como o UDM padrão.

```

### UM fracionário



```
`Unit` poderá ter valor fracionário.

```

### Inventário



```
Independentemente de o item ser um item de estoque ou não em QuickBooks, nenhuma informação relacionada ao estoque será mantida.

```

## Cliente e Fornecedor


### Nomenclatura



```
Todos os clientes e fornecedores terão nomes codificados da empresa.

por exemplo. `Pen` se tornará `Pen - AZ` (assumindo que `AZ` é a abreviação da empresa).

```

## Fatura


### Variantes



```
QuickBooks tem quatro variantes transacionais de Fatura, todas elas serão salvas como Fatura de Vendas.

- **Fatura** é equivalente a uma Nota Fiscal de Venda.
- **Recibo de Venda** é equivalente a uma Nota Fiscal de Venda PDV.
- **Nota de Crédito** é equivalente a uma Nota Fiscal de Venda de devolução (Nota de Crédito).
- **Recibo de Reembolso** é equivalente a uma Fatura de Venda PDV de devolução.

```

### Desconto e acréscimo



```
QuickBooks usa contas especiais para Markup e Discount, ERPNext não lida com a despesa de desconto e markup desta forma, em vez disso, todos os itens verão a mudança em suas contas de receita.

```

### Envio



```
Para Notas Fiscais com Frete, será adicionado na tabela Item um Item com o nome Frete.

```

### Arredondamento


ERPNext usa método de arredondamento diferente do QuickBooks, por isso, em Notas Fiscais com Imposto e com moeda diferente da moeda da empresa, a Nota Fiscal de Venda terá total geral diferente da Nota Fiscal QuickBooks.

### Caso especial



```
Se uma fatura do QuickBooks estiver vinculada a uma `Cobrança atrasada` ou `Cobrança de extrato`, uma `Entrada de diário` equivalente será criada para esta fatura.

```

## Conta


### Variantes



```
QuickBooks tem duas variantes transacionais de Bill, todas elas serão salvas como Fatura de Compra.

- **Bill** é equivalente a uma Fatura de Compra.
- **Crédito do Fornecedor** é equivalente a uma Fatura de Compra de devolução.

```

## Outro


As transações a seguir serão salvas como entrada no diário


* Pagamento antecipado
* Pagamento de contas
* Cheque
* Crédito de cartão de crédito
* Despesa
* Ajuste de quantidade de estoque
* Entrada de diário
* Pagamento
* Pagamento de Impostos


## Imposto


Para cada taxa de imposto do QuickBooks, uma conta ERPNext será criada.


## Campos personalizados


O QuickBooks Migrator adicionará os seguintes campos personalizados


* Campo Empresa


	+ Cliente
	+ Item
	+ Fornecedor
* Campo de ID do QuickBooks


	+ Cliente
	+ Item
	+ Entrada de diário
	+ Fatura de compra
	+ Fatura de venda
	+ Fornecedor
