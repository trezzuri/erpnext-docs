# Armazém



**Um armazém é um edifício comercial para armazenamento de mercadorias. Armazéns são usados
por fabricantes, importadores, exportadores, atacadistas, empresas de transporte,
costumes, etc.**


Geralmente são grandes edifícios simples em áreas industriais de
cidades, vilas e aldeias. Eles geralmente têm docas de carga para carregar e descarregar
mercadorias de caminhões.


A terminologia de 'Armazém' no ERPNext é um pouco mais ampla e talvez possa ser considerada como "locais de armazenamento". Você pode criar um subarmazém que pode ser uma prateleira dentro de sua localização real.


Isso pode se tornar uma árvore bastante detalhada como esta:


*Armazém > Sala > Linha > Prateleira > Caixa*


Para acessar a lista do Armazém, acesse:
> Home > Estoque > Configurações > Armazém


## 1. Como criar um Armazém


1. Vá para a lista Armazém e clique em Novo.
2. Insira um nome para o Armazém.
3. Definir/verificar o Armazém Pai. Se você marcar 'É grupo', poderá criar subarmazéns neste grupo Armazém.
4. Salvar.


Os Armazéns são salvos com as respectivas abreviações da Empresa. Isso facilita
identificando rapidamente qual armazém pertence a qual empresa.


### 1.1 Opções adicionais ao criar um armazém


**Conta**: Defina aqui uma conta padrão para todas as transações com este Armazém. A configuração desta conta mostrará as transações deste Armazém no Razão Contábil.
**Tipo de Armazém**: Você pode criar um Tipo de Armazém para classificar os Armazéns. Por exemplo, Armazéns de Fornecedores, Armazéns de Estoque, Armazéns WIP, Salas, etc. podem ser marcados. Esta classificação é útil na geração de relatórios ou em determinadas transações de ações.


#### Endereço e contato


Você pode adicionar endereços de cobrança, entrega e outros tipos de endereço para o armazém. Você também pode adicionar um contato, que pode ser o Gerente do Armazém, por exemplo.


![Warehouse](/files/warehouse.png)


### 1.2 Depois de salvar


Depois de salvar um Armazém, você verá as seguintes opções:


* **Saldo de estoque**: Isso abrirá o relatório Saldo de estoque para exibir a quantidade, avaliação, saldo, etc.
* **Contabilidade**: Isso abrirá a Contabilidade para exibir as transações contábeis.
* **Não-Grupo para Grupo**: Se o Armazém for um Armazém Não-Grupo, ou seja, não puder conter outros Armazéns sob ele, este botão o tornará um Armazém de Grupo.


## 2. Recursos


### 2.1 Visualização em árvore


Você também pode mudar para a visualização em 'Árvore', que mostrará todos os armazéns do grupo e dos filhos.


![Warehouse](/files/warehouse-tree.png)


### 2.2 Conta de armazém


No ERPNext, se você ativar [Inventário Perpétuo](/docs/pt/stock/perpetual-inventory), cada Armazém deve pertencer a uma empresa específica para manter
balanço de estoque da empresa. Para isso, cada Armazém deverá estar vinculado a um
Conta no Plano de Contas (mesmo nome do próprio Armazém). Esta conta captura o equivalente monetário dos bens ou materiais armazenados nesse armazém específico.


Se você tiver uma Árvore de Armazém mais detalhada, provavelmente será uma boa ideia vincular os sublocais (sala, linha, prateleira, etc.) à conta do Armazém real (o Armazém raiz dessa Árvore) como maioria
os cenários não exigem contabilizar o valor dos itens em estoque por prateleira ou compartimento. Por exemplo, se você tem o Armazém A e o quarto, as linhas são B, C, etc., vincule B e C à conta de A.


> Dica: ERPNext mantém o equilíbrio do estoque para cada combinação distinta
de Item e Armazém. Assim, você pode obter o saldo de estoque de qualquer item específico em um determinado armazém em qualquer data específica.


### 3. Tópicos Relacionados


1. [Finalidade de entrada de estoque](/docs/pt/stock/articles/stock-entry-purpose)
2. [Relatório de nível de estoque](/docs/pt/stock/stock-level-report)



