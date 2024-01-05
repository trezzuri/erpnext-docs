# Transmissão de eventos




> 
> Introduzido na versão 13
> 
> 
> 


O Event Streaming permite comunicações entre sites entre dois ou mais sites. Você pode **assinar** os tipos de documentos e **transmitir** documentos entre diferentes sites.


Por exemplo: Considere que você tem mais de uma Empresa hospedada em sites diferentes, um deles é o site principal onde você deseja fazer lançamentos contábeis e nos outros sites são geradas as Notas Fiscais de Vendas. Você pode usar o streaming de eventos neste caso. Para isso, os sites da sua empresa secundária podem se inscrever no site principal da empresa para os tipos de documento de item, cliente e fornecedor. A empresa principal, por sua vez, pode assinar faturas de vendas nas empresas filhas.


Para acessar o streaming de eventos, acesse:



> 
> Página inicial > Automação > Streaming de eventos
> 
> 
> 


## 1. Pré-requisitos


Antes de criar um Produtor de Eventos, é necessário criar um usuário comum em ambos os sites que será usado para acessar o site e atuará como Assinante do Evento. Certifique-se de que o usuário seja um gerente do sistema e tenha as permissões necessárias para criação, atualização e exclusão dos DocTypes inscritos.


## 2. Como configurar o streaming de eventos


Vamos usar dois sites para explicar o processo. http://test*site:8000 (site do consumidor) e http://test*site\_producer:8000 (site do produtor)


### 2.1 Obtenha as chaves do assinante do evento no site do produtor


1. Em http://test*site*producer:8000 (site do produtor), acesse a lista de usuários.
2. Abra o documento do usuário que você usará como assinante do evento. Role para baixo até a seção chamada "Acesso à API". Nessa seção, gere chaves para o usuário clicando no botão **Gerar Chaves**. Você receberá um prompt com o segredo do usuário, copie o segredo do usuário e salve-o com você. Ele também gerará uma chave de API.


### 2.2 Gerar chaves para o assinante do evento no site do consumidor


1. Em http://test\_site:8000 (site do consumidor), acesse a lista de usuários e siga o mesmo processo especificado na etapa anterior.


### 2.3 Crie um produtor de eventos no site do consumidor


1. O site no qual você deseja se inscrever é chamado de Produtor do Evento. Crie um documento do Event Producer para o site do qual você deseja obter as atualizações.
2. Em http://test\_site:8000 (site do consumidor), vá para **Home > Automation > Event Streaming > Event Producer**.
3. Insira a URL do site que você deseja assinar (neste caso http://test*site*produtor:8000), no campo Producer URL.
4. Adicione todos os tipos de documentos que você deseja assinar na tabela Tipos de documentos do Event Producer.
5. Se você deseja que os documentos criados tenham o mesmo nome que estão no site remoto do Event Producer, marque a caixa de seleção 'Usar o mesmo nome' na tabela em relação ao tipo de documento necessário.
6. Defina o campo Assinante do Evento para o usuário que será usado para criar os documentos buscados no Produtor do Evento. Você precisa criar o mesmo usuário em ambos os sentidos, ou seja, no site do Event Consumer e também no Event Producer antes de criar o Event Producer.
7. Cole a chave de API e o segredo de API que você gerou na primeira etapa (2.1) nos campos chave de API e segredo de API, respectivamente.
8. Salvar.
9. Após salvar, um Event Consumer é criado no site do produtor (http://test*site*producer:8000). As chaves do usuário no site do consumidor são copiadas automaticamente para o documento Event Consumer no site do produtor neste processo.


![Produtor de Eventos](/files/event-producer-doc.png)



> 
> **Observação**: se o segredo da API for alterado para os usuários em qualquer um desses sites, você terá que atualizar manualmente as chaves no Event Producer, bem como no Event Consumer em ambos os sites. sites.
> 
> 
> 


### 2.4 Aprovar o consumidor do evento no site do Event Producer


1. Após a criação do Produtor de Evento, um Consumidor de Evento é criado automaticamente no site do produtor. Por padrão, todos os Tipos de Documentos Assinados possuem o status 'Pendente'. Para permitir que o Consumidor de Eventos consuma os documentos desses Tipos de Documentos, seu Status precisa ser atualizado para 'Aprovado'.
2. Acesse: **Página inicial > Automação > Streaming de eventos > Consumidor de eventos**.
3. Depois de abrir o documento Consumidor de Eventos, você verá todos os Tipos de Documentos que o consumidor assinou. Altere o status de 'Pendente' para 'Aprovado' para todos os tipos de documentos que você deseja aprovar para consumo. Você pode alterar o status para 'Rejeitado' se não quiser que os documentos desse tipo de documento sejam consumidos.
4. Salvar.


![Event Consumer](/files/event-consumer-doc.png)



> 
> **Observação**: as atualizações de documentos para tipos de documentos assinados não serão sincronizadas, a menos que sejam aprovadas.
> 
> 
> 


### 2.5 Acesso off-line com site único


Se você tiver alguns locais onde a conectividade com a Internet é baixa, por exemplo, uma loja em uma área remota onde as faturas de vendas são geradas e quiser sincronizar essas faturas da loja para a conta hospedada, você pode configurar a sincronização off-line usando o comando seguintes etapas:


1. Configure uma instância local do ERPNext. Você pode consultar [este guia](https://github.com/frappe/bench) para configuração local.
2. Você precisa ter uma conta hospedada configurada na sua empresa.
3. Agora crie um Produtor de Eventos na conta hospedada e defina o URL do produtor como o URL da sua conta local.
4. Adicione quaisquer tipos de documentos que você deseja sincronizar na tabela filha Event Producer Document Types.
5. Aprove os doctypes.


## 3. Recursos


### 3.1 Cancelar assinatura das atualizações


Como consumidor de evento, se você deseja cancelar a assinatura das atualizações de qualquer tipo de documento que você assinou anteriormente, marque cancelar a assinatura no tipo de documento. Você não receberá mais atualizações do site do produtor para esse tipo de documento específico depois de cancelar a assinatura.


![Unsubscribe](/files/unsubscribe-event.png)


### 3.2 Registro de atualização de eventos


O "Log de atualização de eventos" registra todas as ações de criação, atualização e exclusão de documentos que possuem consumidores no site do Event Producer.
Para visualizar o log de atualização de eventos:


Acesse: **Página inicial > Automação > Streaming de eventos > Registro de atualização de eventos**.


* Para 'Criar', digite o tipo de atualização, tipo de documento, nome do documento e todo o documento (como JSON) será registrado.
* Para o tipo 'Atualização', o tipo de atualização, tipo de documento, nome do documento e os dados atualizados (diferença entre o estado anterior e o estado atual do documento) são registrados.
* Para o tipo 'Excluir', apenas o tipo de atualização, o tipo de documento e o nome do documento são registrados.


![Log de atualização de eventos](/files/event-update-log-doc.png)


### 3.3 Registro de sincronização de eventos


Assim como o log de atualização, o log de sincronização de eventos registra todos os documentos sincronizados do produtor de eventos no site do consumidor de eventos.
Para visualizar o registro de sincronização de eventos:


Acesse: **Página inicial > Automação > Streaming de eventos > Registro de sincronização de eventos**.


![Log de sincronização de eventos](/files/event-sync-log.png)


Um evento sincronizado com sucesso gera um documento de registro com:


* **Tipo de atualização**: criar, atualizar ou excluir
* **Status**: status de sincronização
* **DocType**
* **Produtor do evento**: o URL do site de onde o documento foi criado
* **Nome do documento**
* **Nome do documento remoto**: se 'Usar o mesmo nome' estiver desmarcado
* **Usar o mesmo nome**
* **Dados**: os dados do documento como JSON


![Log de sincronização de eventos](/files/event-synced.png)


Um evento com falha gera um documento de log com os campos acima junto com:


* **Erro**: o erro pelo qual o documento não foi sincronizado.
![Evento sincronizado](/files/event-failed-error.png)
* **Botão Ressincronizar**: Ele também fornece um botão 'Ressincronizar' para ressincronizar o evento com falha.
![Evento falhou](/files/event-failed.png)


### 3.4 Sincronização de dependências


Certos tipos de documentos têm dependências. Por exemplo, antes de sincronizar uma Fatura de Venda, o Item e o Cliente precisam estar presentes no site atual. Portanto, Item e Cliente são dependências da Nota Fiscal de Venda. O Event Streaming lida com isso por meio da sincronização de dependência sob demanda. Sempre que qualquer documento for sincronizado, ele primeiro verifica se o documento possui alguma dependência (campos de link, campos de link dinâmico, campos de tabela filho, etc.). Se essa dependência não for preenchida, ou seja, o documento dependente (por exemplo: Item) não estiver presente no site do seu consumidor, ele será sincronizado primeiro e depois a fatura de vendas será sincronizada.


Por exemplo: sincronização de fatura de vendas com dependência de item:
 ![Dependência de Evento](/files/event-dependency-sync.gif)


### 3.5 Configuração de nomenclatura


Marque a caixa de seleção 'Usar o mesmo nome' para permitir que os documentos tenham o mesmo nome nos sites Event Producer e Event Consumer. Se esta opção não estiver marcada, o documento será criado usando as convenções de nomenclatura do site atual.


![Usar configuração do mesmo nome](/files/event-use-same-name.png)



> 
> **Nota**: Para tipos de documentos que possuem séries de nomenclatura, é aconselhável manter a caixa de seleção 'Usar o mesmo nome' desmarcada para evitar conflitos de nomenclatura. Se esta opção estiver desmarcada, os documentos serão criados seguindo as convenções de nomenclatura do site atual e os campos personalizados 'Nome do site remoto' e 'Nome do documento remoto' serão definidos no documento sincronizado para armazenar a URL do site do Event Producer e o nome do documento no site remoto, respectivamente.
> 
> 
> 


![Documento inscrito](/files/event-subscribed-doc.png)


### 3.6 Configuração de mapeamento


Se você deseja transmitir documentos entre uma instância do ERPNext e outro aplicativo Frappe para um determinado tipo de documento com estruturas iguais ou diferentes, ou se os nomes dos campos forem diferentes em ambos os sites, você pode usar o Event Streaming com Mapping Configuration.
Para isso, você precisa primeiro configurar um mapeamento de tipo de documento.


Para acessar o mapeamento de tipo de documento, vá para:



> 
> Página inicial > Automação > Streaming de eventos > Mapeamento de tipo de documento.
> 
> 
> 


#### 3.6.1 Mapeamento para DocTypes com estrutura semelhante


* **Nome do mapeamento**: dê um nome exclusivo ao mapeamento
* **Tipo de documento local**: o tipo de documento em seu site atual
* **Tipo de documento remoto**: o tipo de documento no site do Event Producer que você deseja sincronizar


Na tabela filha Mapeamento de campo:


* **Nome do campo local**: o nome do campo no tipo de documento local do seu site atual.
* **Nome do campo remoto**: O nome do campo no tipo de documento remoto do site Produtor de eventos que você deseja mapear para o nome do campo local. Durante a sincronização, o valor do fieldname remoto é copiado para o fieldname local.


![Mapeamento de tipo de documento](/files/event-field-mapping.png)


#### 3.6.2 Valor padrão para algum campo


Se o seu campo não estiver mapeado para nenhum outro nome de campo remoto e você quiser que o campo sempre tenha o mesmo valor, defina o mesmo valor no campo de valor padrão. Evento se você tiver definido o nome do campo remoto, caso durante a sincronização o valor do campo remoto não seja encontrado e se o "Valor Padrão" tiver sido especificado, ele será definido.


![Link de mapeamento de tabela secundária](/files/default.png)


#### 3.6.3 Mapeamento para DocTypes com tabelas filhas


Se o campo que você está tentando mapear for uma tabela filha, será necessário criar outro mapeamento de tipo de documento para os campos da tabela filha.


![Link de mapeamento de tabela secundária](/files/child_table_map_doc.png)


* **Tipo de mapeamento**: selecione o tipo de mapeamento como tabela secundária.
* **Mapeamento**: selecione o documento de mapeamento de tipo de documento que você criou para a tabela secundária.


![Link de mapeamento de tabela filha](/files/event-map-is-child-table.png)


#### 3.6.4 Mapeamento para DocTypes com dependências (campos Link, Dynamic Link)


Se os DocTypes que você está tentando mapear tiverem algum tipo de dependência, como campos de link ou link dinâmico, será necessário configurar outro mapeamento de tipo de documento para sincronizar as dependências.


Por exemplo, vamos supor que o tipo de documento local seja Oportunidade e o tipo de documento remoto seja Oportunidade ERPNext. O campo `party_name` (campo Link para DocType Lead) no Opportunity é mapeado para `full_name` (campo Dados) no ERPNext Opportunity. Durante a sincronização, esse Lead deve ser criado para a Oportunidade principal sincronizar. Portanto, você também precisa configurar um mapeamento para este campo de link.


![Criação de dependência de lead](/files/lead_dependency_creation.png)


* **Tipo de mapeamento**: neste caso, o tipo de mapeamento é Documento.
* **Mapeamento**: selecione o mapeamento que você acabou de criar.
* **Filtros de valor remoto**: você precisa especificar os filtros que irão buscar o documento remoto exato a ser mapeado. Como neste caso, o DocType remoto é o ERPNext Opportunity, que pode ser obtido exclusivamente usando nome, número de telefone e país.


O formato é:


{ "remote fieldname": "campo ou expressão de onde obteremos o valor para esse fieldname"}


Se você quiser buscar o valor de algum lugar, inicie a expressão com eval:


Como neste caso é: `eval:frappe.db.get_value('Global Defaults', None, 'country')`


![Tipo de mapeamento de documento](/files/document_mapping_type.png)


Por último, ative a opção 'Tem mapeamento' na tabela secundária de configuração de evento no Event Producer em relação ao tipo de documento necessário e selecione o mapeamento de tipo de documento que você acabou de criar.


![Configuração de mapeamento](/files/event-mapping-conf.png)


### 3.6 Configuração de eventos condicionais


Se você estiver em uma situação em que não deseja enviar todos os documentos de um doctype ao consumidor, poderá especificar as condições para eles.


Por exemplo, se você quiser emitir apenas os documentos `Nota` que são públicos, você pode especificá-los no documento Produtor/Consumidor.


![Link de mapeamento de tabela secundária](/files/event-streaming-conditions.png)



> 
> Se um documento satisfizer uma condição ao longo de sua vida útil, todos os `registros de atualização de eventos` antigos serão sincronizados com o consumidor
> 
> 
> 


Vamos considerar outro exemplo. Você deseja sincronizar apenas as faturas de vendas enviadas.
Você pode especificar `doc.docstatus == 1` como condição. As faturas não serão sincronizadas até que sejam enviadas.


Para cada log de atualização, você pode ver seus consumidores no documento Log de atualização.


Se precisar de um controle mais preciso sobre as condições, você pode conectar uma função personalizada. Sua função será executada com os parâmetros `consumer`, `doc` e `update_log`. Por exemplo, você deseja sincronizar apenas as notas que são `ímpares`



```
def is_odd_note(consumidor, documento, update_log):
    retornar frappe.db.sql("""
        SELECIONAR
            CONTAR(*)
        DE `tabNote`
        WHERE criação <= %(criação)s
    """, { "criação": doc.creation })[0][0] % 2 != 0

```

Então, você poderia especificar a condição:



```
cmd: my_custom_app.note.is_odd_note

```




