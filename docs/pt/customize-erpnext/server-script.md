# script do servidor


**Um Server Script permite definir dinamicamente um Python Script que é executado no servidor em um evento de documento ou API**



>
> Introduzido na versão 12
>
>
>


## 1. Como criar um script de servidor


Para criar um script de servidor


1. Se o seu site estiver hospedado em [erpnext.com](https://erpnext.com/), entre em contato com o suporte para ativar o Server Script.
No caso de contas auto-hospedadas, defina `server_script_enabled` como true em site\_config.json do seu site.
2. Para adicionar/editar script de servidor, certifique-se de que sua função seja Gerente do sistema.
3. Crie um novo script de servidor por meio de "Novo script de servidor" na barra de ferramentas.
4. Selecione o tipo de script do servidor: Document Event, API, Permission Query.
5. Defina o tipo de documento e o nome do evento, ou nome do método, script e salve.


## 2. Características


### 2.1 Ativando o Script do Servidor


O script do servidor deve ser ativado via site\_config.json



```
banco --site site1.local set-config server_script_enabled true

```

### 2.2 Documentar Eventos


Para scripts que devem ser chamados por meio de eventos de documento, você deve definir o tipo de documento de referência e o nome do evento para definir o acionador


* Antes de inserir
* Antes de Salvar
* Depois de Salvar
* Antes de enviar
* Depois de enviar
* Antes de Cancelar
* Após Cancelar
* Antes de Excluir
* Após Excluir
* Antes de Salvar (Documento Enviado)
* Após Salvar (Documento Enviado)


### 2.3 Scripts de API


Você pode criar uma nova API que pode ser acessada via `api/method/[methodname]` pelo tipo de script "API"


Se você deseja que o usuário convidado acesse a API, você deve marcar "Permitir convidado"


A resposta pode ser definida por meio do objeto `frappe.response["message"]`


### 2.4 Consulta de Permissão


Esse tipo de script permite adicionar condições personalizadas na cláusula where para uma consulta de lista DocType.


Por exemplo, digamos que você queira mostrar a lista de registros ToDo apenas para um usuário
se eles atribuíram o registro ou se foi atribuído a eles. Isso pode ser implementado por
o seguinte roteiro:



```
condições = 'dono = {usuário} ou atribuído_by = {usuário}'.format(usuário=frappe.db.escape(usuário))

```

A consulta `select` resultante será mais ou menos assim:



```
selecione * de `tabToDo` onde owner = 'faris@erpnext.com' ou assign_by = 'faris@erpnext.com'

```

Agora, a exibição de lista do ToDo mostrará os registros restritos. Isso também irá restringir
os resultados mostrados nos campos Link.


### 2.5 Segurança


Frappe Framework usa a biblioteca RestrictedPython para restringir o acesso aos métodos disponíveis para scripts de servidor. Apenas os métodos seguros listados abaixo estão disponíveis em scripts de servidor



```
json # módulo json
dict # dict interno
_ # método tradutor
_dict # frappe._dict método interno
frappe.flags # sinalizadores globais

# FORMATAÇÃO
frappe.format # frappe.format_value(valor, dict(fieldtype='Moeda'))
frappe.format_value # frappe.format_value(value, dict(fieldtype='Moeda'))
frappe.date_format # formato de data padrão
frappe.format_date # retorna a data como "1º de setembro de 2019"

# SESSÃO
frappe.form_dict # parâmetros de formulário / solicitação
frappe.request # objeto de solicitação
frappe.response # objeto de resposta
frappe.session.user # usuário atual
frappe.session.csrf_token # token CSRF da sessão atual
frappe.user # usuário atual
frappe.get_fullname # nome completo do usuário atual
frappe.get_gravatar # frappe.utils.get_gravatar_url
frappe.full_name = # nome completo do usuário atual

# ORM
frappe.get_meta # obtém objeto de metadados
frappe.get_doc
frappe.get_cached_doc
frappe.get_list
frappe.get_all
frappe.get_system_settings

# banco de dados
frappe.db.get_list
frappe.db.get_all
frappe.db.get_value
frappe.db.get_single_value
frappe.db.get_default
frappe.db.escape
frappe.db.exists
frappe.db.commit

# SERVIÇOS DE UTILIDADE PÚBLICA
frappe.msgprint # msgprint
frappe.get_hooks # ganchos de aplicativo
frappe.utils # métodos em frappe.utils
frappe.render_template # frappe.render_template,
frappe.get_url # frappe.utils.get_url
frappe.sendmail # envia e-mail via script de servidor
frappe.get_print # obtém pdf para um documento
frappe.attach_print # anexar PDF a um e-mail
socketio_port # porta para socketio
style.border_color # '#d1d8dd'
get_next_link
esfregar
palpite_mimetype = mimetypes.guess_type,
html2texto = html2texto,
dev_server # True se estiver no modo de desenvolvedor
run_script # Executa outro script de servidor

#CACHE
frappe.cache.set_value
frappe.cache.get_value
frappe.cache.hset
frappe.cache.hget

```

## 3. Exemplos


### 3.1 Alterar o valor de uma propriedade antes da alteração


Tipo de script: Antes de salvar



```
se "teste" em doc.description:
    doc.status = 'Fechado'

```

### 3.2 Validação personalizada


Tipo de script: "Antes de salvar"



```
se "validar" em doc.description:
    raise frappe.ValidationError

```

### 3.3. Criação Automática de Tarefas


Tipo de script: "Depois de salvar"



```
se doc.allocated_to:
    frappe.get_doc(dict(
        doctype = 'ToDo'
        proprietário = doc.allocated_to,
        descrição = doc.assunto
    )).inserir()

```

### API 3.4


* Tipo de script: API
* Nome do método: `test_method`



```
frappe.response['mensagem'] = "olá"

```

Solicitação: `/api/method/test_method`