# Transmissão de eventos



>
> Introduzido na versão 13
>
>
>


O Event Streaming permite comunicações entre dois ou mais sites. Você pode **assinar** os Tipos de Documentos e **transmitir** Documentos entre sites diferentes.


Por Exemplo: Considere que você tem mais de uma Empresa hospedada em sites diferentes, um deles é o site principal onde você deseja fazer o lançamento contábil e em outros sites são geradas as Notas Fiscais de Vendas. Você pode usar o Streaming de eventos neste caso. Para isso, os sites de sua empresa filha podem se inscrever no site principal da empresa para tipos de documento de item, cliente e fornecedor. A Empresa principal, por sua vez, pode se inscrever nas empresas filhas para Notas Fiscais.


Para acessar o Event Streaming, acesse:



>
> Início > Automação > Transmissão de eventos
>
>
>


## 1. Pré-requisitos


Antes de criar um Produtor de Eventos, é necessário criar um usuário comum em ambos os sites que será usado para acessar o site e atuará como um Assinante do Evento. Certifique-se de que o usuário seja um System Manager e tenha as permissões necessárias para criação, atualização e exclusão dos DocTypes inscritos.


## 2. Como configurar o streaming de eventos


Vamos pegar dois sites para explicar o processo. http://test*site:8000 (site do consumidor) e http://test*site\_producter:8000 (site do produtor)


### 2.1 Obtenha as chaves do Assinante do Evento no Site do Produtor


1. Em http://test*site*producer:8000 (site do produtor), vá para a lista de usuários.
2. Abra o documento do usuário que você usará como assinante do evento. Role para baixo até a seção denominada "Acesso à API". Nessa seção, gere chaves para o usuário clicando no botão **Gerar Chaves**. Você receberá um prompt com o segredo do usuário, copie o segredo do usuário e salve-o com você. Ele também irá gerar uma chave de API.


### 2.2 Gerar Chaves para o Assinante do Evento no Site do Consumidor


1. Em http://test\_site:8000 (site do consumidor), acesse a lista Usuário e siga o mesmo processo especificado na etapa anterior.


### 2.3 Criar um Produtor de Eventos no Site do Consumidor


1. O site que você deseja assinar é chamado de Produtor de Eventos. Crie um documento do Event Producer para o site do qual você deseja obter as atualizações.
2. Em http://test\_site:8000 (site do consumidor), vá para **Home > Automation > Event Streaming > Event Producer**.
3. Insira a URL do site que deseja assinar (neste caso http://test*site*producter:8000), no campo Producer URL.
4. Adicione todos os Tipos de Documentos que deseja assinar na tabela Tipos de Documentos do Produtor de Eventos.
5. Se você deseja que os documentos criados tenham o mesmo nome que estão no site do Event Producer remoto, marque a caixa de seleção 'Use Same Name' na tabela em relação ao tipo de documento necessário.
6. Defina o campo Assinante do Evento para o usuário que será usado para criar os documentos buscados no Produtor do Evento. Você precisa criar o mesmo usuário nos dois sentidos, ou seja, no site Event Consumer e no Event Producer antes de criar o Event Producer.
7. Cole a API key e API Secret que você gerou na primeira etapa (2.1) nos campos API key e API secret, respectivamente.
8. Salve.
9. Depois de salvar, um consumidor de evento é criado no site do produtor (http://test*site*producer:8000). As chaves do usuário no site do consumidor são copiadas automaticamente para o documento Event Consumer no site do produtor neste processo.


![Produtor de evento](/files/event-producer-doc.png)



>
> **Observação**: Se o Segredo da API for alterado para os usuários em qualquer um desses sites, você terá que atualizar manualmente as chaves no Produtor de evento, bem como no Consumidor de evento em ambos os sites.
>
>
>


### 2.4 Aprovar consumidor de evento no site do produtor de evento


1. Após a criação do Produtor de Evento, um Consumidor de Evento é criado automaticamente no site do produtor. Por defeito, todos os Tipos de Documentos Subscritos têm o estado 'Pendente'. Para permitir que o Consumidor de Evento consuma os documentos desses Tipos de Documentos, seu Status precisa ser atualizado para 'Aprovado'.
2. Acesse: **Página inicial > Automação > Streaming de eventos > Consumidor de eventos**.
3. Depois de abrir o documento Event Consumer, você verá todos os Tipos de Documentos aos quais o consumidor se inscreveu. Altere o status de 'Pendente' para 'Aprovado' para todos os Tipos de Documentos que você deseja aprovar para serem consumidos. Você pode alterar o status para 'Rejeitado' se não quiser que os documentos desse Tipo de Documento sejam consumidos.
4. Salve.


![Consumidor de evento](/files/event-consumer-doc.png)



>
> **Observação**: as atualizações de documentos para tipos de documentos assinados não serão sincronizadas, a menos que sejam aprovadas.
>
>
>


### 2.5 Acesso offline com site único


Se você tiver alguns lugares onde a conectividade com a Internet é baixa, por exemplo, uma loja em uma área remota onde as faturas de vendas são geradas e deseja sincronizar essas faturas da loja para a conta hospedada, você pode configurar a sincronização offline usando as seguintes etapas:


1. Configure uma instância local do ERPNext. Você pode consultar [este guia](https://github.com/frappe/bench) para configuração local.
2. Você precisa ter uma conta hospedada com sua empresa configurada.
3. Agora crie um Produtor de Evento na conta hospedada e defina a URL do produtor para a URL de sua conta local.
4. Adicione os tipos de documento que deseja sincronizar na tabela filho Tipos de documento do produtor de evento.
5. Aprove os doctypes.


## 3. Características


### 3.1 Cancelar a assinatura das atualizações


Como Consumidor de Eventos, se você deseja cancelar a assinatura das atualizações de quaisquer doctypes nos quais você se inscreveu anteriormente, verifique cancelar a assinatura no doctype. Você não receberá mais atualizações do site do produtor para esse tipo de documento específico depois de cancelar a inscrição.


![Cancelar inscrição](/files/unsubscribe-event.png)


### 3.2 Registro de atualização de eventos


O "Log de atualização de eventos" registra todas as ações de criação, atualização e exclusão de documentos que possuem consumidores no site do Event Producer.
Para visualizar o log de atualização de eventos:


Acesse: **Página inicial > Automação > Transmissão de eventos > Log de atualização de eventos**.


* Para 'Criar', digite o tipo de atualização, tipo de documento, nome do documento e todo o documento (como JSON) é registrado.
* Para 'Atualizar' digite o tipo de atualização, tipo de documento, nome do documento e os dados atualizados (diferença entre o estado anterior e o estado atual do documento) são registrados.
* Para o tipo 'Excluir', apenas o Tipo de atualização, o Tipo de documento e o Nome do documento são registrados.


![Registro de atualização de eventos](/files/event-update-log-doc.png)


### 3.3 Log de Sincronização de Eventos


Assim como o log de atualização, o log de sincronização de eventos registra todos os documentos sincronizados do produtor de eventos no site do consumidor de eventos.
Para visualizar o log de sincronização de eventos:


Acesse: **Página inicial > Automação > Transmissão de eventos > Log de sincronização de eventos**.


![Log de sincronização de eventos](/files/event-sync-log.png)


Um evento sincronizado com sucesso gera um documento de log com:


* **Tipo de atualização**: criar, atualizar ou excluir
* **Status**: Status da sincronização
* **DocType**
* **Produtor do evento**: URL do site de onde o documento foi criado
* **Nome do Documento**
* **Remote Document Name**: Se 'Use Same Name' estiver desmarcado
* **Use o mesmo nome**
* **Data**: Os dados do documento como JSON


![Log de sincronização de eventos](/files/event-synced.png)


Um evento com falha gera um documento de log com os campos acima junto com:


* **Erro**: O erro devido ao qual o documento não foi sincronizado.
![Evento sincronizado](/files/event-failed-error.png)
* **Botão Ressincronizar**: Ele também fornece um botão 'Resincronizar' para ressincronizar o evento com falha.
![Falha no evento](/files/event-failed.png)


### 3.4 Sincronização de Dependência


Certos tipos de documento têm dependências. Por exemplo, antes de sincronizar uma Nota Fiscal de Venda, o Item e o Cliente precisam estar presentes no site atual. Assim, Item e Cliente são dependências da Nota Fiscal de Venda. O Event Streaming lida com isso por sincronização de dependência sob demanda. Sempre que algum documento for sincronizado, ele primeiro verifica se o documento possui dependências (campos de link, campos de link dinâmico, campos de tabela filho, etc.). Se essa dependência não for preenchida, ou seja, o documento dependente (por exemplo: Item) não estiver presente no site do consumidor, ele será sincronizado primeiro e, em seguida, a Fatura de Vendas será sincronizada.


Por exemplo: Sincronização da Fatura de Vendas com a dependência do Item:
 ![Dependência de evento](/files/event-dependency-sync.gif)


### 3.5 Configuração de Nomenclatura


Marque a caixa de seleção 'Usar o mesmo nome' para permitir que os documentos tenham o mesmo nome nos sites Produtor de evento e Consumidor de evento. Se isso não estiver marcado, o documento será criado usando as convenções de nomenclatura do site atual.


![Configuração de uso do mesmo nome](/files/event-use-same-name.png)



>
> **Observação**: Para Tipos de Documentos que possuem séries de nomenclatura, é recomendável manter a caixa de seleção 'Usar Mesmo Nome' desmarcada para evitar conflitos de nomenclatura. Se esta opção estiver desmarcada, os documentos serão criados seguindo as convenções de nomenclatura no site atual e os campos personalizados 'Nome do site remoto' e 'Nome do documento remoto' serão definidos no documento sincronizado para armazenar a URL do site do produtor de evento e o nome do documento no site remoto, respectivamente.
>
>
>


![Documento Assinado](/files/event-subscribe-doc.png)


### 3.6 Configuração do Mapeamento


Se você deseja transmitir documentos entre uma instância do ERPNext e outro aplicativo Frappe para um tipo de documento específico com estruturas iguais ou diferentes, ou se os nomes dos campos forem diferentes em ambos os sites, você pode usar o Streaming de Eventos com Configuração de Mapeamento.


Para isso, você precisa primeiro configurar um mapeamento de tipo de documento.


Para acessar o Mapeamento de Tipo de Documento, acesse:



>
> Home > Automação > Streaming de eventos > Mapeamento de tipo de documento.
>
>
>


#### 3.6.1 Mapeamento para DocTypes com estrutura semelhante


* **Nome do mapeamento**: Dê um nome exclusivo ao mapeamento
* **Tipo de documento local**: o tipo de documento em seu site atual
* **Tipo de Documento Remoto**: O Tipo de Documento no site do Produtor de Eventos que você deseja sincronizar


Na tabela filho Mapeamento de Campo:


* **Nome do campo local**: O nome do campo no tipo de documento local do seu site atual.
* **Remote Fieldname**: O fieldname no tipo de Documento Remoto do site do Produtor de Eventos que você deseja mapear para o Local Fieldname. Durante a sincronização, o valor do fieldname remoto é copiado para o fieldname local.


![Mapeamento de tipo de documento](/files/event-field-mapping.png)


#### 3.6.2 Valor padrão para algum campo


Se o seu campo não estiver mapeado para nenhum outro nome de campo remoto e você sempre quiser que o campo tenha o mesmo valor, defina o mesmo conjunto no campo de valor padrão. Evento se você tiver definido o nome do campo remoto, caso durante a sincronização, o valor do campo remoto não seja encontrado e se o "Valor padrão" tiver sido especificado, ele será definido.


![Link de mapeamento da tabela filha](/files/default.png)


#### 3.6.3 Mapeamento para DocTypes com tabelas filhas


Se o campo que você está tentando mapear for uma tabela filho, será necessário criar outro mapeamento de tipo de documento para os campos da tabela filho.


![Link de mapeamento da tabela filha](/files/child_table_map_doc.png)


* **Tipo de mapeamento**: Selecione o tipo de mapeamento como tabela filha.
* **Mapeamento**: Selecione o documento de mapeamento de tipo de documento que você criou para a tabela filha.


![Link de mapeamento da tabela filha](/files/event-map-is-child-table.png)


#### 3.6.4 Mapeamento para DocTypes com dependências (campos Link, Dynamic Link)


Se os DocTypes que você está tentando mapear tiverem algum tipo de dependência, como os campos Link ou Dynamic Link, será necessário configurar outro Mapeamento de tipo de documento para sincronizar as dependências.


Por exemplo, vamos supor que o doctype local seja Opportunity e o doctype remoto seja ERPNext Opportunity. O campo `party_name` (campo Link para DocType Lead) na Oportunidade é mapeado para `full_name` (campo Dados) no ERPNext Opportunity. Durante a sincronização, este Lead deve ser criado para que a Oportunidade principal seja sincronizada. Portanto, você também precisa configurar um mapeamento para este campo de link.


![Criação de dependência de lead](/files/lead_dependency_creation.png)


* **Tipo de Mapeamento**: Neste caso, o Tipo de Mapeamento é Documento.
* **Mapeamento**: Selecione o mapeamento que você acabou de criar.
* **Filtros de valor remoto**: Você precisa especificar os filtros que buscarão o documento remoto exato a ser mapeado. Como neste caso, o DocType remoto é ERPNext Opportunity, que pode ser obtido exclusivamente usando nome, número de telefone e país.


O formato é:


{ "remote fieldname": "campo ou expressão de onde obteremos o valor para esse fieldname"}


Se você quiser buscar o valor de algum lugar, comece a expressão com eval:


Como neste caso é: `eval:frappe.db.get_value('Global Defaults', None, 'country')`


![Tipo de mapeamento de documento](/files/document_mapping_type.png)


Por fim, habilite a opção 'Has Mapping' na tabela filho Event Configuration no Event Producer em relação ao tipo de documento necessário e selecione o mapeamento de tipo de documento que você acabou de criar.


![Configuração de mapeamento](/files/event-mapping-conf.png)


### 3.6 Configuração de Eventos Condicionais


Se você estiver em um cenário em que não deseja enviar todos os documentos em um doctype ao consumidor, poderá especificar as condições para eles.


Por exemplo, se você quiser emitir apenas os documentos 'Nota' que são públicos, você pode especificá-los no documento Produtor/Consumidor.


![Link de mapeamento da tabela filha](/files/event-streaming-conditions.png)



>
> Se um documento satisfizer uma condição ao longo de sua vida útil, todos os 'Registros de atualização de eventos' antigos serão sincronizados com o consumidor
>
>
>


Vamos considerar outro exemplo. Você deseja sincronizar apenas as faturas de vendas enviadas.
Você pode especificar `doc.docstatus == 1` como a condição. As faturas não serão sincronizadas até que sejam enviadas.


Para cada log de atualização, você pode ver seus consumidores no documento Log de atualização.


Se precisar de um controle mais preciso sobre as condições, você pode conectar uma função personalizada. Sua função será executada com os parâmetros `consumer`, `doc` e `update_log`. Por exemplo, você deseja sincronizar apenas as notas que são `ímpares`



```
def is_odd_note(consumidor, doc, update_log):
    return frappe.db.sql("""
        SELECIONE
            CONTAR(*)
        DE `tabNote`
        WHERE criação <= %(criação)s
    """, { "criação": doc.criação })[0][0] % 2 != 0

```

Então, você poderia especificar a condição:



```
cmd: my_custom_app.note.is_odd_note

```