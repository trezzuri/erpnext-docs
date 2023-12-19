# Configurações de nomenclatura de documentos



**Mestres e transações podem receber prefixos na forma de séries de nomenclatura.**


ERPNext permite que você crie prefixos em seus documentos, com cada prefixo
formando sua própria série. Por exemplo, uma série com prefixo INV12#### terá
números INV120001, INV120002 e assim por diante.


Você pode ter múltiplas séries para todas as suas transações. Por exemplo, IDs de faturas de vendas como estes podem ser gerados:


* ACC-SINV-.AAAA.-
* SINV12####
* SALESINV-00####


Você pode definir ou selecionar o padrão de série de nomenclatura em:


> Página inicial > Configurações > Configurações de nomenclatura de documentos


## 1. Configurando séries de nomenclatura para documentos


1. Selecione a transação para a qual deseja fazer a série. O sistema atualizará a série atual na caixa de texto.
2. Edite a série conforme necessário com prefixos exclusivos para cada série.
O primeiro prefixo será o prefixo padrão. Cada nova série de nomenclatura de prefixo deve ser adicionada em uma nova linha. A série de nomes recém-adicionada estará disponível no documento.


![configurações de nomenclatura de documentos](/files/document_naming_settings.gif)


3. Se você deseja que o usuário selecione explicitamente uma série em vez da série padrão, marque a caixa de seleção “O usuário deve sempre selecionar”.
Não haverá série de nomenclatura padrão se esta opção estiver marcada.
4. Você também pode atualizar o ponto inicial de uma série inserindo o nome da série e o ponto inicial na seção “Atualizar série”.
5. Clique no botão Atualizar para atualizar o conjunto de séries de nomenclatura do documento selecionado.


> Observação: para ver a série de nomes recém-adicionada, clique em Configurações > Recarregar.


## 2. Ano Financeiro na Série de Nomenclatura


Você também pode mostrar o ano financeiro na Série de Nomenclatura. Por padrão, se você inserir 'AAAA' na série de nomenclatura, o ano atual será selecionado. Para definir séries de nomenclatura com base no ano fiscal, insira algo como 'ACC-SINV-.19-20.-' onde 19-20 é o ano fiscal atual. É comum ter uma série separada para cada exercício financeiro.


Como você pode ver, na captura de tela a seguir de uma fatura de vendas, o ano de 2019 está listado:


![Ano fiscal na série de nomenclatura](/files/year-naming-series.png)


## 3. Atualizando o valor atual da série de nomenclatura existente


Você pode alterar o número de sequência inicial/atual de uma série existente.


1. Na seção Atualizar série, selecione o prefixo cuja sequência será alterada.
2. O valor atual será obtido e exibido.
3. Altere o número de sequência inicial/existente, se necessário.
4. Clique em Atualizar número de série.


Por exemplo, se o número de série do Pedido de Venda atual for 16 e você quiser reiniciá-lo ou defini-lo como 50, insira 0 ou 50 dependendo do seu caso. Qualquer novo pedido de vendas criado começará a partir do novo número de sequência.


Para saber mais sobre isso, [acesse este artigo](/docs/pt/setting-up/articles/naming-series-current-value).


> Dica: você pode ter uma série separada para cada tipo de Cliente ou para
cada um dos seus pontos de venda.


## 4. Usando valores de campo em séries de nomenclatura


Algumas empresas preferem usar "códigos de acesso" para fornecedores, ou seja, WN para "Web Notes" da empresa que posteriormente podem ser usados ​​na nomenclatura de séries para identificação rápida.


Por exemplo:



```
Um campo personalizado "ID do fornecedor" é criado em Documento: Fornecedor.
Então, em Naming Series, permitimos algo como
    PO-.AA.MM.-.vendor_id.-.####
    Resultando em "PO-1503-WN-00001"

```

## 5. Vídeo








## 7. Tópicos Relacionados


1. [Renomear em massa](/docs/pt/setting-up/settings/bulk-rename)



