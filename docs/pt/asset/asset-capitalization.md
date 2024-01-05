# Capitalização de ativos



O recurso Capitalização de ativos permite fazer o seguinte:

* Converter um ou mais itens de estoque em um novo ativo composto
* Converter um ou mais itens de estoque em um novo ativo composto e capitalizar o custo das despesas de serviço
* Converter um ou mais ativos em um novo ativo composto
* Converter um ou mais ativos em um novo item de estoque

Para acessar o recurso Capitalização de ativos, acesse:


> Home > Ativos > Manutenção > Capitalização de ativos
> 
> 

![](/files/jdmoSl4.png)  
  
Vamos examinar os casos de uso mencionados acima, um por um.

## 1. Converter um ou mais itens de estoque em um novo ativo composto

**Etapas**:

* Criar uma nova capitalização de ativos
* Se você deseja que um novo ativo composto seja criado, escolha o Método de capitalização como "Criar um novo ativo composto" e defina o Código do item de destino para o item do ativo fixo a ser vinculado ao novo ativo e o Local do ativo de destino para o Local do novo ativo. Se desejar que um ativo composto WIP seja usado, escolha o Método de capitalização como "Escolha um ativo composto WIP" e defina o Ativo alvo como o ativo composto.
* Altere a nomenclatura Série, Empresa, Livro Financeiro e Data de Lançamento se necessário
* Insira os itens de estoque a serem convertidos em Itens de Estoque Consumidos. Se você escolher o método de capitalização como "Escolha um ativo composto WIP", todos os itens marcados no ativo por meio de recibos/faturas de compra serão buscados automaticamente.
* Salvar e enviar
* Defina os detalhes de depreciação (se houver) do ativo recém-criado e envie-o.

**Efeito contábil** :

Os Itens de Estoque Consumidos serão reduzidos pela quantidade selecionada nos armazéns selecionados e as Contas de Estoque em Armazém serão creditadas com o valor do estoque emitido. A conta do Ativo Fixo do Ativo criado será debitada pelo Valor Total.

## 2. Converter um ou mais itens de estoque em um novo ativo composto e capitalizar o custo das despesas de serviço

Os pré-requisitos, etapas e efeito contábil para isso são quase os mesmos do anterior, a única adição é que você pode adicione as Despesas do Serviço e as Contas de Despesas dos serviços serão creditadas com o valor do serviço.

## 3. Converter um ou mais ativos em um novo ativo composto

**Pré-requisitos**:

Um novo item de ativo fixo (com `É ativo fixo` caixa de seleção marcada), pois seria o item vinculado ao novo ativo.

**Etapas**:

* Criar uma nova Capitalização de ativos
* Defina o código do item de destino para o item a ser vinculado ao novo ativo
* Defina o local do ativo de destino para o local do novo ativo
* Altere a série de nomenclatura, empresa, livro financeiro e data de lançamento, se necessário
* Insira os ativos para ser convertido em Ativos Consumidos
* Salvar e Enviar
* Defina os detalhes de depreciação (se houver) do ativo recém-criado e envie-o.

**Efeito contábil**:

Os Ativos Consumidos serão depreciados (se configurados para depreciação) até o lançamento os lançamentos contábeis manuais de data e depreciação serão criados em segundo plano. Então eles seriam descartados e seu status seria definido como “Capitalizado”. As contas do Ativo Fixo dos Ativos Consumidos serão creditadas pelo seu valor bruto de compra e as contas da Depreciação Acumulada serão debitadas pela sua depreciação total acumulada. A conta do Ativo Fixo do Ativo criado será debitada pelo Valor Total.

## 4. Converter um ou mais ativos em um novo item de estoque

**Pré-requisitos**:

Um novo item de estoque (com a caixa de seleção `Manter estoque` marcada) para as quais

**Etapas**:

* Criar uma nova capitalização de ativos
* Definir o tipo de entrada para descapitalização
* Definir o código do item de destino para o novo item
* Definir o armazém de destino e o destino Quantidade
* Altere a série de nomenclatura, empresa, livro financeiro e data de lançamento, se necessário
* Insira os ativos a serem convertidos Ativos Consumidos
* Salvar e Enviar
* Defina os detalhes de depreciação (se houver) do ativo recém-criado e envie-o.

**Efeito contábil**:

Os Ativos Consumidos serão depreciados (se configurados para depreciação) até a data de lançamento e Depreciação As entradas de diário serão criadas em segundo plano. Então eles seriam eliminados e seu status seria definido como “Descapitalizados”. As contas do Ativo Fixo dos Ativos Consumidos serão creditadas pelo seu valor bruto de compra e as contas da Depreciação Acumulada serão debitadas pela sua depreciação total acumulada. O novo Item de estoque será adicionado pela Quantidade Alvo no Armazém Alvo e a Conta do Armazém Alvo será debitada pelo Valor Total.



