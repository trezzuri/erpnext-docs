# Busque todo o texto do endereço em um campo personalizado



Este artigo ajudará você a adicionar um campo personalizado para buscar endereços completos em qualquer DocType, usando uma abordagem de 3 etapas.

  
**Etapa 1. Personalizações cosméticas no DocType necessário**

  


Precisamos primeiro adicionar dois novos campos no DocType para buscar endereços:-

  


a) Um campo do tipo 'Link' que aponta para nosso endereço master

b) Um campo do tipo 'Somente leitura' que exibiria o endereço completo

  


Anote os nomes das variáveis ​​dos novos campos que você criar. Essas informações serão exigidas posteriormente no processo.

  


![](/files/q90efZM.png)

  


Para obter informações sobre como criar campos personalizados em um DocType, você pode consultar o seguinte link-[Campos personalizados no ERPNext](https://docs.erpnext.com/docs/pt/customize-erpnext/custom-field)

  


Uma vez concluída esta etapa, você deverá ter dois novos campos no DocType selecionado, conforme ilustrado abaixo:-

  


![](/files/SabQi7A .png)

  


  


**Etapa 2. Adicionando um script de cliente para obter o endereço completo de nosso mestre de endereços**

  


Pesquise 'Client Script' na barra de pesquisa e crie um novo Client Script. Selecione o DocType necessário no qual precisamos buscar o endereço.

  


Na seção do script, cole o seguinte script do cliente:-

  



```
frappe. ui.form.on("Nome do tipo de documento", "address\_link\_field", function(frm, cdt, cdn) {    if(frm .doc.address\_link\_field){     return frm.call({      método: "frappe.contacts.doctype.address.address.get\_address\_display",      args: {        "address\_dict": frm.doc.address\_link\_field      },      retorno de chamada: function(r) {       if(r.message)           frm.set\_value("full\_address\_field", r.message);              }     });    }    else{        frm.set\_value ("full\_address\_field", "");    }});
```
  


Aqui precisaremos substituir as seguintes alterações com base no seu caso de uso:-a) Substitua 'DocType Name' pelo nome do DocType no qual precisamos buscar o endereço. Por exemplo. Fatura de venda, pedido de compra etc.

b) Substitua 'address\_link\_field' pelo nome da variável do campo de link personalizado que criamos na Etapa 1

c) Substitua 'full\_address\_field' pelo nome da variável do campo somente leitura personalizado que criamos na Etapa 1

  


Depois disso estiver pronto, você terá um script de cliente parecido com o seguinte:-

  


![](/files/VukPzs4.png)

  


**Etapa 3. Salve, ative e teste o script do cliente**

  


Depois que o script do cliente for alterado de acordo com seu caso de uso, podemos salvá-lo e ativá-lo clicando na caixa de seleção "Ativado".

Vá para o DocType necessário e atualize a página para que as alterações entrem em vigor .

  


Agora, quando um endereço for selecionado em nosso campo de link personalizado, o endereço inteiro será buscado em nosso campo personalizado somente leitura, conforme ilustrado abaixo:-

  


![](/files/W3kxhT2.gif)







