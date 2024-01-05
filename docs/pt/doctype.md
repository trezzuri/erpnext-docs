# TipoDoc



**Um DocType é o elemento central de qualquer aplicativo baseado no Frappe Framework.**


Descreve o modelo e a visualização dos seus dados. Ele contém quais campos são armazenados para seus dados e como eles se comportam entre si. Ele contém informações sobre como seus dados são nomeados. Os formulários como Pedido de Vendas, Faturas de Vendas, Ordem de Serviço são adicionados como DocTypes no backend.


DocType permite que você insira formulários personalizados no ERPNext conforme sua necessidade.


Para criar um novo DocType, vá para:


> Configuração > Personalizar > Tipo de documento > Novo


## 1. Como criar um novo DocType:


1. **Nome**: Insira o nome do novo DocType.
2. **Módulo**: Insira em qual módulo você gostaria que o novo DocType fosse adicionado.
3. Salvar.


![Custom DocType](/files/doctype-employee-transfer.png)


### 1.1. Detalhes Adicionais


1. **Campos**


Você pode optar por adicionar quantos campos desejar. O Rótulo, Tipo de Campo, Campos Obrigatórios e outras opções associadas também podem ser adicionados aqui. Saiba mais sobre os tipos de campo [aqui](/docs/pt/customize-erpnext/articles/field-types.html).


![Campos em DocType personalizado](/files/doctype-employee-transfer-fields.png)
2. **Nomeação**


Aqui você pode escolher se deseja que cada um dos seus formulários neste DocType seja nomeado automaticamente. Conforme indicado na descrição, você pode selecionar o padrão de nomenclatura dos formulários. O mesmo pode ser um campo dentro do DocType, Naming Series, Prompt, Uma série de nomenclatura definida ou um nome baseado em formato. Para Nomenclatura, você também pode adicionar uma Descrição e a caixa do nome (como caixa de título ou caixa alta) para sua conveniência.


![Nomeando DocType personalizado](/files/doctype-employee-transfer-naming.png)
3. **Configurações do formulário**


Configurações adicionais para formulário, campos de imagem, anexos, linha do tempo etc. podem ser definidas aqui. Para saber mais sobre o Formulário, visite [Personalizar Formulário](/docs/pt/customize-erpnext/customize-form).


![Configurações personalizadas do formulário DocType](/files/doctype-employee-transfer-form-settings.png)
4. **Configurações de visualização**


Aqui, você pode definir as configurações de visualização para o DocType, como campos de pesquisa, campo de classificação padrão, ordem de classificação padrão etc.
5. **Regras de permissão**


Você pode definir as regras de permissão para o DocType aqui e configurar quais usuários poderão usar ou fazer alterações neste DocType. Saiba mais sobre [Usuários e permissões](/docs/pt/setting-up/users-and-permissions) aqui.


![Permissões DocType personalizadas](/files/doctype-employee-transfer-permissions.png)
6. **Visualização na Web**


Você pode selecionar se deseja uma visualização da Web deste DocType ou não. Ter uma Web View para um DocType permitirá que os usuários do seu site tenham acesso aos Formulários. Sinta-se à vontade para saber mais sobre [Usuários do site](/docs/pt/setting-up/articles/difference-between-system-user-and-website-user).


### 1.2. Mais propriedades


1. **É submissível**: você pode selecionar se deseja que este DocType seja apenas 'Salvo' ou também 'Enviado' marcando e desmarcando esta caixa.
2. **É Tabela Filho**: Você pode definir se deseja que o Novo DocType seja uma Tabela Filho dentro de outro DocType. Confira [Tabela filho](/docs/pt/customize-erpnext/articles/customizing-data-visibility-in-child-table) para obter mais informações.
3. **É Único**: Se marcado, este Doctype se tornará um formulário único, como Pedido de Venda, cujo usuário irá
não ser capaz de reproduzir. Por exemplo, as configurações de venda no módulo de vendas são um tipo de documento único.
4. **É Árvore**: Alguns DocTypes no ERPNext são estruturados como Árvores, onde existem alguns DocTypes Pai e alguns DocTypes Filhos. Por exemplo, a Doctype Company está estruturada como Árvore, existem Empresas Matrizes e também Empresas Filhos, que chamamos de subsidiárias. Se quiser que seus DocTypes sejam estruturados de forma semelhante, você pode ativar esta opção.


![DocType Tree View](/files/doctype-treeview.png)
5. **Entrada Rápida**: Você pode selecionar se deseja que uma Entrada Rápida seja feita para este DocType. Isso permitirá que você insira apenas alguns dados obrigatórios e salve o DocType, para que seja feita uma Entrada Rápida. Por exemplo, verifique Entrada rápida em [Lançamento de diário](/docs/pt/accounts/journal-entry#11-quick-entry).
6. **Rastrear alterações**: você pode selecionar esta opção se quiser manter um registro das alterações feitas em cada formulário. Confira [Controle de versão de documentos](/docs/pt/using-erpnext/document-versioning) para obter mais compreensão sobre isso.
7. **Rastrear vistos**: você pode selecionar esta opção se quiser manter um registro de todos os usuários que visualizaram este formulário.
8. **Rastrear visualizações**: você pode selecionar esta opção se quiser manter um registro de todas as vezes que cada usuário visualizou este formulário.


![DocType Tree View](/files/doctype-track-views.png)
9. **Personalizado?**: Este campo será verificado por padrão ao adicionar Doctype Personalizado. Da mesma forma, se você estiver personalizando um DocType que já existe no sistema, este campo por padrão estará desmarcado.


## 2. Vídeos






