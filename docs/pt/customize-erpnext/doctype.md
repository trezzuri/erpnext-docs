# DocType


**Um DocType é o bloco de construção principal de qualquer aplicativo baseado no Frappe Framework.**


Descreve o Modelo e a Visualização dos seus dados. Ele contém quais campos são armazenados para seus dados e como eles se comportam uns com os outros. Ele contém informações sobre como seus dados são nomeados. Os formulários como Pedido de Vendas, Faturas de Vendas e Pedidos de Serviço são adicionados como DocTypes no back-end.


DocType permite que você insira formulários personalizados no SOMA conforme sua necessidade.


Para criar um novo DocType, acesse:



> 
> Configuração > Personalizar > Tipo de documento > Novo
> 
> 
> 


## 1. Como criar um novo DocType:


1. **Nome**: digite o nome do novo DocType.
2. **Módulo**: digite em qual módulo você gostaria que o novo DocType fosse adicionado.
3. Salvar.


![Custom DocType](/files/doctype-employee-transfer.png)


### 1.1. Detalhes Adicionais


1. **Campos**


Você pode optar por adicionar quantos campos quiser. O rótulo, tipo de campo, campos obrigatórios e outras opções associadas também podem ser adicionados aqui. Saiba mais sobre os tipos de campo [aqui](/docs/pt/customize-erpnext/articles/field-types.html).


![Campos em Custom DocType](/files/doctype-employee-transfer-fields.png)
2. **Nomenclatura**


Aqui você pode escolher se deseja que cada um dos seus formulários dentro deste DocType seja nomeado automaticamente. Conforme informado na descrição, você pode selecionar o padrão de nomenclatura dos formulários. O mesmo pode ser um campo dentro do DocType, série de nomenclatura, prompt, uma série de nomenclatura definida ou um nome baseado em formato. Para Nomenclatura, você também pode adicionar uma Descrição e a Maiúscula do Nome (como Título ou MAIÚSCULAS) para sua conveniência.


![Naming Custom DocType](/files/doctype-employee-transfer-naming.png)
3. **Configurações de formulário**


Configurações adicionais para o formulário, campos de imagem, anexos, linha do tempo etc. podem ser configuradas aqui. Para saber mais sobre o formulário, visite [Personalizar formulário](/docs/pt/customize-erpnext/customize-form).


![Custom DocType Form Settings](/files/doctype-employee-transfer-form-settings.png)
4. **Ver configurações**


Aqui, você pode definir as configurações de exibição para o DocType, como campos de pesquisa, campo de classificação padrão, ordem de classificação padrão, etc.
5. **Regras de permissão**


Você pode definir as regras de permissão para o DocType aqui e configurar quais usuários poderão usar ou fazer alterações neste DocType. Saiba mais sobre [Usuários e permissões](/docs/pt/setting-up/users-and-permissions) aqui.


![Custom DocType Permissions](/files/doctype-employee-transfer-permissions.png)
6. **Visualização da Web**


Você pode selecionar se deseja uma Visualização da Web deste DocType ou não. Ter uma Web View para um DocType permitirá que os usuários do seu site tenham acesso aos formulários. Fique à vontade para saber mais sobre [Usuários do site](/docs/pt/setting-up/articles/difference-between-system-user-and-website-user).


### 1.2. Mais propriedades


1. **Pode ser enviado**: você pode selecionar se deseja que este DocType seja apenas 'Salvo' ou também 'Enviado' marcando e desmarcando esta caixa.
2. **É tabela filha**: Você pode definir se deseja que o Novo DocType seja uma tabela filha dentro de outro DocType. Confira [Tabela filha](/docs/pt/customize-erpnext/articles/customizing-data-visibility-in-child-table) para obter mais informações.
3. **É Único**: Se marcada, este Doctype se tornará um formulário único, como Pedido de Venda, cujo usuário
não conseguir reproduzir. Por exemplo, as configurações de venda no módulo de vendas são um único tipo de documento.
4. **É Árvore**: Alguns DocTypes no SOMA são estruturados como Árvores, onde existem alguns DocTypes Pais e alguns DocTypes Filhos. Por exemplo, a Doctype Company é estruturada como Tree, existem empresas-mãe e também empresas-filho, que chamamos de subsidiárias. Se você deseja que seus DocTypes sejam estruturados de forma semelhante, você pode habilitar esta opção.


![DocType Tree View](/files/doctype-treeview.png)
5. **Entrada Rápida**: Você pode selecionar se deseja que uma Entrada Rápida seja feita para este DocType. Isso permitirá que você insira apenas alguns detalhes obrigatórios e salve o DocType, para que uma entrada rápida seja feita. Por exemplo, verifique Entrada rápida em [Entrada de diário](/docs/pt/accounts/journal-entry#11-quick-entry).
6. **Rastrear alterações**: você pode selecionar esta opção se quiser manter um registro das alterações feitas em cada formulário. Confira [Controle de versão de documento](/docs/pt/using-erpnext/document-versioning) para entender mais sobre isso.
7. **Rastrear visto**: você pode selecionar esta opção se quiser manter um registro de todos os usuários que viram este formulário.
8. **Rastrear visualizações**: você pode selecionar esta opção se quiser manter um registro de todas as vezes que cada usuário visualizou este formulário.


![DocType Tree View](/files/doctype-track-views.png)
9. **Personalizado?**: Este campo será verificado por padrão ao adicionar o tipo de documento personalizado. Da mesma forma, se você estiver personalizando um DocType que já existe no sistema, este campo por padrão estaria desmarcado.


## 2. Vídeos




