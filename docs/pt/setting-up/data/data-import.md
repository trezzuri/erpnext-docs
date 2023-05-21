# Ferramenta de importação de dados


**A ferramenta de importação de dados permite importar registros de um arquivo CSV/Excel.**


A ferramenta de importação de dados é uma maneira fácil de carregar (ou editar) dados em massa (especialmente dados mestres) no sistema.


Para começar a importar dados, vá para:



>
> Início > Importação de dados e configurações > Importar dados
>
>
>


Ou vá até o documento que deseja importar e clique em Menu > Importar:


![Iniciar importação](/files/task-menu-import.png)


Antes de usar a importação de dados, **certifique-se** de ter todos os seus dados prontos.


## 1. Inserção de Novos Registros


Digamos que você queira importar a lista de Clientes do seu sistema antigo para o ERPNext. O primeiro passo é baixar um modelo no qual podemos inserir nossos dados.


### 1.1 Baixe o Modelo


1. Acesse Lista de Clientes, clique em Menu > Importar. Clique em **Novo**.
2. Selecione Tipo de Importação como Inserir Novos Registros.
3. Clique em **Salvar**.
4. Agora, clique em **Baixar modelo**.
5. Ao inserir novos registros, o modelo deve estar em branco. Se você tiver alguns clientes em seu sistema, poderá selecionar o tipo de exportação como "5 registros" para ver o formato em que deve inserir os dados no modelo.
6. Selecione o tipo de arquivo do modelo de exportação.
7. Selecione os campos que deseja preencher como dados do Cliente.
8. Clique em **Exportar**.


![Baixar modelo](/files/download-template.gif)


### 1.2 Inserindo Dados no Modelo


O modelo baixado ficará mais ou menos assim:


![Modelo em branco](/files/blank-template-file.png)


Abra o modelo baixado em um aplicativo de planilha (como Excel, Numbers ou Libre Office) e insira os dados abaixo dos cabeçalhos das colunas mostrados a seguir:


![Modelo de cliente com dados](/files/customer-template-with-data.png)


Agora, salve seu modelo como um arquivo do Excel ou de valores separados por vírgulas (CSV).



>
> Você pode deixar a coluna ID em branco ao inserir novos registros.
>
>
>


Ao importar este modelo, cada linha fará um cadastro de Cliente no sistema.


### 1.3 Importando o modelo


1. Depois de atualizar seu arquivo de modelo, volte para o formulário de importação de dados e anexe o arquivo clicando no botão **Anexar**.
2. Selecione o arquivo de modelo e clique em **Carregar**.
3. Depois que o upload for bem-sucedido, clique em **Iniciar importação**.


![Carregar arquivo de modelo](/files/upload-template-file.png)


Se houver erros em seu modelo, eles serão mostrados na seção Avisos. Os avisos serão categorizados por Linha ou Coluna com seu número para que você possa rastreá-los facilmente no modelo e resolvê-los. Você deve resolver todos os avisos antes de poder importar os dados.


![Avisos de importação](/files/import-warnings.png)


Depois de resolver os avisos, clique em **Iniciar importação** novamente para importar os dados. Na importação bem-sucedida dos dados, você verá um log de cada registro que foi criado na seção Import Log.


![Importação com sucesso](/files/import-success.png)


## 2. Atualização de registros existentes


Digamos que você queira atualizar os dados do cliente em massa em seu sistema. O primeiro passo é baixar o template com os dados.


### 2.1 Baixe o Modelo


1. Acesse Lista de Clientes, clique em Menu > Importar. Clique em **Novo**.
2. Selecione o tipo de importação como atualizar registros existentes
3. Clique em **Salvar**.
4. Agora, clique em **Baixar modelo**.
5. Ao atualizar os registros existentes, você deve exportar os registros do sistema com o campo ID e os campos que deseja atualizar. Você pode escolher Todos os registros ou Registros filtrados, dependendo do seu caso.
6. Selecione os campos que deseja atualizar para os registros do Cliente.
7. Clique em **Exportar**.


### 2.2 Atualizando Dados no Modelo


O modelo baixado ficará mais ou menos assim:


![Modelo de cliente para atualização](/files/customer-template-for-update.png)


Agora, altere os valores em seu modelo e salve o arquivo como Excel ou CSV.



>
> Ao exportar registros para atualizá-los, certifique-se de que a coluna ID seja exportada e não alterada. Os valores da coluna ID são utilizados para identificar os registros no sistema. Você pode atualizar os valores em outras colunas, mas não na coluna ID. Se você remover alguma linha da tabela filha, o sistema considerará que a linha deve ser excluída.
>
>
>


### 2.3 Importando o modelo


Siga as etapas na seção [Importando o modelo](#23-importando o modelo) acima.


## 3. Importando Registros Filhos


Os dados no ERPNext são armazenados em tabelas como uma planilha com colunas e linhas de dados. Cada formulário, como Pedido de Venda, possui vários campos, como Cliente, Empresa, etc. Também possui tabelas como tabela de itens, tabela de impostos etc. dentro da tabela filho (tabela de itens) são tratados como tabela filho para importação de dados.


Cada formulário no ERPNext pode ter várias tabelas filhas associadas a ele. As tabelas filho são vinculadas às tabelas pai e são implementadas onde há vários valores para qualquer propriedade. Por exemplo, um Item pode ter vários preços, uma Fatura de Vendas pode ter vários Itens, Impostos e assim por diante.


Quando você exporta um documento com tabelas filhas, por exemplo, cada linha filha aparecerá em uma linha separada, mas está associada a uma única linha pai. Os valores subseqüentes nas colunas pai permanecerão em branco. Você deve garantir que essa ordem não seja quebrada ao importá-los por meio da importação de dados.


![Exportação de tabela filha](/files/child-table-export.png)


## 4. Opções de importação


### 4.1 Importar do Planilhas Google


Você também pode importar dados do Planilhas Google. Importe seu modelo no Planilhas Google e insira os dados. Verifique se a planilha do Google é pública. Você pode testar isso abrindo o URL do Planilhas Google em uma janela anônima do navegador.


![Planilhas Google](/files/google-sheets.png)


![Importar via Planilhas Google](/files/import-via-google-sheets.png)


### 4.2 Enviar após a importação


No ERPNext, os tipos de documentos são principalmente de dois tipos - mestres e transações. Os mestres são registros como Cliente e Tarefa, que só podem ser salvos, não enviados. Transações como pedidos de vendas e faturas de compra são documentos que podem ser enviados e podem ser enviados.


Ao selecionar um tipo de documento que pode ser enviado para Importação, você pode marcar **Enviar após a importação** para enviar o documento após a importação.


### 4.3 Não envie e-mails


Digamos que você criou uma [Notificação](/docs/v13/user/manual/en/setting-up/notifications) em seu sistema e sempre que um Lead é criado um e-mail é enviado. Agora, se você estiver importando leads em massa, muitos e-mails serão enviados, o que pode não ser desejado. Você pode desativar esta opção para evitar o envio de e-mails.


## 5. Notas Adicionais


### 5.1 Limite de upload


Não há limite rígido para o número de registros que podem ser importados. Mas você deve tentar carregar apenas alguns milhares de registros por vez. A importação de um grande número de registros (digamos 50.000) pode tornar o sistema consideravelmente lento para os usuários que estão usando o sistema.


### 5.2 Arquivos CSV


Um arquivo CSV (valor separado por vírgula) é um arquivo de dados que você pode carregar no ERPNext para atualizar vários dados. Qualquer arquivo de planilha de aplicativos de planilhas populares, como MS Excel ou Open Office Spreadsheet, pode ser salvo como um arquivo CSV.


Se você estiver usando o Microsoft Excel e usando caracteres não ingleses, certifique-se de salvar seu arquivo codificado como UTF-8.


Para versões mais antigas do Excel, não há uma maneira clara de salvar como UTF-8. Portanto, salve seu arquivo como CSV, abra-o no Bloco de Notas e salve como “UTF-8”. (Ou atualize seu Excel!)


## 6. Vídeo



## 7. Tópicos Relacionados


1. [Importador de planos de contas](/docs/v13/user/manual/en/setting-up/importador de gráficos de contas)
2. [Exportação de dados](/docs/v13/user/manual/en/setting-up/data/data-export)