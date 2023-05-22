# Configurações de nomeação de documentos


**Os mestres e as transações podem receber prefixos na forma de séries de nomenclatura.**


SOMA permite que você crie prefixos para seus documentos, com cada prefixo
formando sua própria série. Por exemplo, uma série com prefixo INV12#### terá
números INV120001, INV120002 e assim por diante.


Você pode ter várias séries para todas as suas transações. Por exemplo, IDs de fatura de vendas como estes podem ser gerados:


* ACC-SINV-.AAAA.-
* SINV12####
* VENDASINV-00####


Você pode definir ou selecionar o padrão de série de nomes em:



> 
> Página inicial > Configurações > Configurações de nomenclatura do documento
> 
> 
> 


## 1. Configurando séries de nomenclatura para documentos


1. Selecione a transação para a qual deseja fazer a série. O sistema atualizará a série atual na caixa de texto.
2. Edite a série conforme necessário com prefixos exclusivos para cada série.
O primeiro prefixo será o prefixo padrão. Cada novo prefixo Naming Series deve ser adicionado em uma nova linha. A série de nomenclatura recém-adicionada estará disponível no documento.


![configurações de nomenclatura de documentos](/files/document_naming_settings.gif)


3. Se você deseja que o usuário selecione explicitamente uma série em vez da padrão, marque a caixa de seleção "O usuário sempre deve selecionar".
Não haverá série de nomenclatura padrão se esta opção estiver marcada.
4. Você também pode atualizar o ponto inicial de uma série inserindo o nome da série e o ponto inicial na seção "Atualizar série".
5. Clique no botão Atualizar para atualizar o conjunto de séries de nomes para o documento selecionado.



> 
> Observação: para ver a série de nomes recém-adicionada, clique em Configurações > Recarregar.
> 
> 
> 


## 2. Ano financeiro na série de nomes


Você também pode mostrar o ano financeiro na série de nomes. Por padrão, se você inserir 'AAAA' na série de nomenclatura, ele selecionará o ano atual. Para definir séries de nomenclatura com base no ano fiscal, digite algo como 'ACC-SINV-.19-20.-' onde 19-20 é o ano fiscal atual. É comum ter uma série separada para cada exercício financeiro.


Como você pode ver, na captura de tela a seguir de uma fatura de venda, o ano de 2019 está listado:


![Ano fiscal na série de nomes](/files/year-naming-series.png)


## 3. Atualizando o valor atual para a série de nomenclatura existente


Você pode alterar o número de sequência inicial/atual de uma série existente.


1. Na seção Update Series, selecione o prefixo cuja sequência deve ser alterada.
2. O valor atual será obtido e exibido.
3. Altere o número de sequência inicial/existente, se necessário.
4. Clique em Atualizar número de série.


Por exemplo, se o número de série atual do Pedido de Vendas for 16 e você quiser reiniciá-lo ou defini-lo como 50, digite 0 ou 50, dependendo do seu caso. Qualquer novo pedido de venda criado começará a partir do novo número de sequência.


Para saber mais sobre isso, [visite este artigo](/docs/pt/setting-up/articles/naming-series-current-value).



> 
> Dica: Você pode ter uma série separada para cada tipo de Cliente ou para
>  cada um de seus pontos de venda.
> 
> 
> 


## 4. Usando valores de campo na série de nomenclatura


Algumas empresas preferem usar "short-codes" para fornecedores, ou seja, WN para empresas "Web Notes" que posteriormente podem ser usadas em séries de nomenclatura para identificação rápida.


Por exemplo:



```
Um campo personalizado "ID do fornecedor" é criado em Documento: Fornecedor.
Em seguida, em Naming Series, permitimos algo como
    PO-.YY.MM.-.vendor_id.-.####
    Resultando em "PO-1503-WN-00001"

```

## 5. Vídeo








## 7. Tópicos Relacionados


1. [Renomear em massa](/docs/pt/setting-up/settings/bulk-rename)
