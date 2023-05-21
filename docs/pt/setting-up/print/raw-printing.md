# Impressão Bruta



>
> Introduzido na versão 12
>
>
>


**O envio de uma sequência de comandos para uma impressora diretamente em seu idioma nativo é chamado de impressão bruta.**


Muitas impressoras térmicas precisam que esses comandos brutos sejam enviados a elas para executar funções como impressão de código de barras, impressão de recibos, impressão de etiquetas, etc. A impressão bruta ignora os drivers da impressora na maioria dos casos, tornando-os muito rápidos e confiáveis. A impressão bruta também é capaz de executar alguns recursos avançados, como cortar papel de recibo, abrir gavetas de dinheiro, etc.


## 1. Configurando a impressão bruta no ERPNext


### 1.1 Instalação do aplicativo QZ Tray no computador cliente


Baixe e instale o aplicativo QZ Tray no computador ao qual sua impressora térmica está conectada. Este aplicativo pode ser encontrado em seu [site oficial](https://qz.io/download/). Atualmente, Windows, macOS e Linux são suportados pelo QZ Tray. Durante a instalação, você será solicitado a instalar o Java, se ainda não estiver instalado, instale o Java para concluir a instalação.


Mais instruções sobre como instalar o aplicativo QZ Tray podem ser [aqui](https://qz.io/wiki/using-qz-tray).


### 1.2 Criar formato de impressão de comandos brutos


Para poder enviar comandos brutos para uma impressora, você precisa primeiro criar um formato de impressão em comandos brutos. A linguagem de modelagem Jinja é usada em comandos brutos, assim como no [formato de impressão personalizado HTML](/docs/v13/user/manual/en/customize-erpnext/print-format).


Para criar um novo formato de impressão para Raw Printing:


1. Vá para a lista de formatos de impressão: **Página inicial > Configurações > Impressão > Formato de impressão**
2. Clique em Novo.
3. Selecione o DocType relevante.
4. Marque as opções **Formato personalizado** e **Impressão bruta**.
5. Preencha o campo **Raw Commands** com os comandos brutos necessários para serem enviados à impressora.
6. Clique em Salvar.


![Formato de impressão de comandos brutos](/files/raw-command-print-format.png)


Atualmente, qualquer linguagem de impressora baseada em string pode ser usada no campo `Raw Commands` no formato de impressão. Escrever comandos brutos requer conhecimento da linguagem nativa da impressora fornecida pelo fabricante da impressora. Consulte o manual do desenvolvedor fornecido pelo fabricante da impressora sobre como escrever seus comandos nativos.


### 1.3 Ativar impressão bruta na configuração de impressão


Para habilitar a impressão bruta:


1. Vá para: **Página inicial > Configurações > Impressão > Configurações de impressão > Impressão bruta**.
2. Marque a opção **Ativar impressão bruta**.
3. Salve.


## 2. Métodos para utilizar a impressão raw no ERPNext


Há duas maneiras de enviar comandos de impressão bruta para sua impressora.


### 2.1 Clicar em imprimir na página de exibição de impressão


Para imprimir um formato de impressão de comando bruto na exibição de impressão de documento:


1. Selecione o formato de impressão apropriado. Para o formato de impressão em comandos brutos, a mensagem "Nenhuma visualização disponível" é exibida no lugar da visualização de impressão.
2. Clique no botão imprimir.
3. Permita o prompt de conexão da bandeja QZ para as ações que você iniciou (atalho de teclado: Alt + A).
* ![Prompt da bandeja QZ](/files/qz-tray-prompt.png)
4. Você pode ser solicitado a selecionar o "formato de impressão - mapeamento da impressora".


* Este mapeamento é usado para enviar os comandos de impressão para a impressora apropriada.
* A impressora precisa estar instalada em seu computador para poder mapeá-la para um formato de impressão.
![formato de impressão - mapeamento da impressora](/files/printer-settings.png)
* Este mapeamento é armazenado localmente no mesmo computador e deverá ser configurado em cada máquina cliente.
* Você também pode editar isso clicando no botão **Configurações da impressora**.


![Impressão bruta da visualização de impressão](/files/raw-printing-from-print-view.gif)


### 2.2 Chamando funções Raw Print de um script de cliente


Muitas vezes, é um requisito que um comando de impressão seja emitido em um determinado evento (como enviar, salvar, corrigir, etc.). É possível escrever um [script de cliente](/docs/v13/user/manual/en/customize-erpnext/client-scripts) para fazer isso para você.


A seguir estão as funções de impressão bruta relevantes:


1. função: `frappe.ui.form.qz_connect`
* Um wrapper de conexão para estabelecer uma conexão com o aplicativo QZ Tray.
* Retorna uma promessa que resolve o estabelecimento bem-sucedido de uma conexão.
* Permite que conexões ativas e inativas sejam resolvidas independentemente. Portanto, pode ser chamado sempre antes de enviar um comando.
* Exemplo de uso:



```
    frappe.ui.form.qz_connect()
    .então(função () {
        return qz.print(config, data);
    })
    .then(frappe.ui.form.qz_success)
    .catch(err => {
        frappe.ui.form.qz_fail(err);
    });

```

Aqui, `qz` é um objeto global fornecido pela biblioteca `qz-tray.js`.


2. função: `frappe.ui.form.qz_get_printer_list`


* Fornece a lista de impressoras disponíveis para o aplicativo QZ Tray
* Retorna uma promessa que resulta em uma lista de impressoras. Exemplo de uso:



```
     frappe.ui.form.qz_get_printer_list().then(
           // Ação necessária para obter a lista de impressoras.
           // Nota: A lista de impressoras é um array de strings.
      );

```

3. função: `frappe.ui.form.qz_success`


* Exibe um "Impressão enviada para a impressora!" alerta ao usuário. Pode ser chamado após o comando de impressão ser bem-sucedido.
4. função: `frappe.ui.form.qz_fail`


* Exibe a mensagem de erro para o usuário. Deve ser chamado em caso de falha na conexão da Bandeja QZ.


Você também pode acessar diretamente as funções fornecidas pela biblioteca `qz-tray.js` através do objeto `qz`. [Clique aqui para obter a documentação da biblioteca qz-tray.js](https://qz.io/api/). Nota: O objeto `qz` é inicializado somente após chamar o `frappe.ui.form.qz_connect` pela primeira vez. Caso você precise do objeto `qz` antes disso, você pode usar o `frappe.ui.form.qz_init`.


### 3. Tópicos Relacionados


1. [Configurações de impressão](/docs/v13/user/manual/en/setting-up/print/print-settings)
2. [Formato de impressão](/docs/v13/user/manual/en/setting-up/print/print-format)
3. [Estilo de impressão](/docs/v13/user/manual/en/setting-up/print/print-style)