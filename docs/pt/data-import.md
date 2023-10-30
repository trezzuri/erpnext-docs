# Ferramenta de importação de dados



**A ferramenta de importação de dados permite importar registros de um arquivo CSV/Excel.**


A ferramenta de importação de dados é uma maneira fácil de fazer upload (ou editar) dados em massa (especialmente dados mestre) no sistema.


Para começar a importar dados, acesse:


> Página inicial > Importação de dados e configurações > Importar dados


Ou vá até o documento que deseja importar e clique em Menu > Importar:


![Iniciar importação](/files/task-menu-import.png)


Antes de usar a importação de dados, **certifique-se** de ter todos os seus dados prontos.


## 1. Inserindo Novos Registros


Digamos que você deseja importar a lista de Clientes do seu sistema antigo para o ERPNext. O primeiro passo é baixar um modelo no qual possamos inserir nossos dados.


### 1.1 Baixe o modelo


1. Vá para Lista de Clientes, clique em Menu > Importar. Clique em **Novo**.
2. Selecione o tipo de importação como Inserir novos registros.
3. Clique em **Salvar**.
4. Agora, clique em **Baixar modelo**.
5. Ao inserir novos registros, o modelo deve ficar em branco. Se você tiver alguns clientes em seu sistema, poderá selecionar o tipo de exportação como "5 registros" para ver o formato em que deverá inserir os dados no modelo.
6. Selecione o tipo de arquivo do modelo de exportação.
7. Selecione os campos que deseja preencher como Dados do cliente.
8. Clique em **Exportar**.


![Baixar modelo](/files/download-template.gif)


### 1.2 Inserindo dados no modelo


O modelo baixado será semelhante a este:


![Modelo em branco](/files/blank-template-file.png)


Abra o modelo baixado em um aplicativo de planilha (como Excel, Numbers ou Libre Office) e insira os dados abaixo dos títulos das colunas mostrados a seguir:


![Modelo de cliente com dados](/files/customer-template-with-data.png)


Agora, salve seu modelo como um arquivo Excel ou com valores separados por vírgula (CSV).


> Você pode deixar a coluna ID em branco ao inserir novos registros.


Ao importar este modelo, cada linha criará um registro de Cliente no sistema.


### 1.3 Importando o modelo


1. Depois de atualizar seu arquivo de modelo, volte ao formulário de importação de dados e anexe o arquivo clicando no botão **Anexar**.
2. Selecione o arquivo de modelo e clique em **Fazer upload**.
3. Depois que o upload for bem-sucedido, clique em **Iniciar importação**.


![Carregar arquivo de modelo](/files/upload-template-file.png)


Se houver algum erro no seu modelo, ele será mostrado na seção Avisos. Os avisos serão categorizados por linha ou coluna com seu número para que você possa rastreá-los facilmente no modelo e resolvê-los. Você deve resolver todos os avisos antes de importar os dados.


![Avisos de importação](/files/import-warnings.png)


Depois de resolver os avisos, clique em **Iniciar importação** novamente para importar os dados. Após a importação bem-sucedida dos dados, você verá um registro de cada registro criado na seção Registro de importação.


![Importação bem-sucedida](/files/import-success.png)


## 2. Atualizando Registros Existentes


Digamos que você queira atualizar dados de clientes em massa no seu sistema. O primeiro passo é baixar o modelo com os dados.


### 2.1 Baixe o modelo


1. Vá para Lista de Clientes, clique em Menu > Importar. Clique em **Novo**.
2. Selecione o tipo de importação para atualizar os registros existentes
3. Clique em **Salvar**.
4. Agora, clique em **Baixar modelo**.
5. Ao atualizar os registros existentes, você deve exportar os registros do sistema com o campo ID e os campos que deseja atualizar. Você pode escolher Todos os Registros ou Registros Filtrados dependendo do seu caso.
6. Selecione os campos que deseja atualizar para os registros do cliente.
7. Clique em **Exportar**.


### 2.2 Atualizando dados no modelo


O modelo baixado será semelhante a este:


![Modelo de cliente para atualização](/files/customer-template-for-update.png)


Agora, altere os valores no seu modelo e salve o arquivo como Excel ou CSV.


> Ao exportar registros para atualizá-los, certifique-se de que a coluna ID seja exportada e esteja intacta. Os valores na coluna ID são usados ​​para identificar os registros no sistema. Você pode atualizar os valores em outras colunas, mas não na coluna ID. Se você remover alguma linha da tabela filha, o sistema considerará que a linha deve ser excluída.


### 2.3 Importando o modelo


Siga as etapas na seção [Importando o modelo](#23-importing-the-template) acima.


## 3. Importando registros secundários


Os dados no ERPNext são armazenados em tabelas como uma planilha com colunas e linhas de dados. Cada formulário como o Pedido de Venda possui vários campos como Cliente, Empresa, etc. Ele também possui tabelas como tabela de itens, tabela de impostos, etc. dentro da tabela filha (tabela item) são tratadas como a tabela filha para importação de dados.


Cada formulário no ERPNext pode ter múltiplas tabelas filhas associadas a ele. As tabelas filhas estão vinculadas às tabelas pai e são implementadas onde há vários valores para qualquer propriedade. Por exemplo, um item pode ter vários preços, uma fatura de vendas pode ter vários itens, impostos e assim por diante.


Quando você exporta um documento com tabelas filhas, por exemplo, cada linha filha aparecerá em uma linha separada, mas estará associada a uma única linha pai. Os valores subsequentes nas colunas pai permanecerão em branco. Você deve garantir que esse pedido não seja quebrado ao importá-los por meio da importação de dados.


![Exportação de tabela infantil](/files/child-table-export.png)


## 4. Opções de importação


### 4.1 Importar do Planilhas Google


Você também pode importar dados do Planilhas Google. Importe seu modelo para o Planilhas Google e insira os dados. Certifique-se de que a Planilha Google seja pública. Você pode testar isso abrindo o URL do Planilhas Google em uma janela anônima do navegador.


![Planilhas Google](/files/google-sheets.png)


![Importar via Planilhas Google](/files/import-via-google-sheets.png)


### 4.2 Enviar após importação


No ERPNext os tipos de documentos são principalmente de dois tipos-mestres e transações. Os mestres são registros como Cliente e Tarefa que só podem ser salvos e não enviados. Transações como pedidos de vendas e faturas de compra são documentos submissíveis e podem ser enviados.


Ao selecionar um tipo de documento que pode ser enviado para importação, você pode marcar **Enviar após importação** para enviar o documento depois de importado.


### 4.3 Não envie e-mails


Digamos que você criou uma [Notificação](/docs/pt/setting-up/notifications) em seu sistema e sempre que um Lead é criado, um e-mail é enviado . Agora, se você estiver importando Leads em massa, muitos emails serão enviados, o que pode não ser o desejado. Você pode desativar esta opção para evitar o envio de e-mails.


## 5. Notas Adicionais


### 5.1 Limite de upload


Não há limite rígido para o número de registros que podem ser importados. Mas você deve tentar fazer upload de apenas alguns milhares de registros por vez. Importar um grande número de registros (digamos 50.000) pode tornar o sistema consideravelmente mais lento para os usuários que o utilizam.


### 5.2 Arquivos CSV


Um arquivo CSV (Comma Separated Value) é um arquivo de dados que você pode carregar no ERPNext para atualizar vários dados. Qualquer arquivo de planilha de aplicativos populares como MS Excel ou Open Office Spreadsheet pode ser salvo como um arquivo CSV.


Se você estiver usando o Microsoft Excel e caracteres que não sejam do inglês, salve o arquivo codificado como UTF-8.


Para versões mais antigas do Excel, não há uma maneira clara de salvar como UTF-8. Portanto, salve seu arquivo como CSV, abra-o no Bloco de Notas e salve como “UTF-8”. (Ou atualize seu Excel!)


## 6. Vídeo



## 7. Tópicos Relacionados


1. [Importador de gráficos de contas](/docs/pt/setting-up/chart-of-accounts-importer)
2. [Exportação de dados](/docs/pt/setting-up/data/data-export)



