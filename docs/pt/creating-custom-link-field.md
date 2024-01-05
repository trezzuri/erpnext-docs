# Criando campo de link personalizado



Campos de link são aqueles vinculados a outro tipo de documento. Por exemplo, o campo Cliente é um campo de link no pedido de vendas. Este campo está vinculado ao cadastro do Cliente.

Você pode inserir o Campo de Link Personalizado seguindo as etapas abaixo.

#### Etapa 1: Vá para Personalizar Formulário

> Home > Personalização > Personalização do Formulário > Personalizar Formulário

#### Etapa 2: Selecione o Formulário

Em Personalizar Formulário, selecione o Tipo de Documento (Cotação, Pedido de Venda, Item da Fatura de Compra etc.). Assim que os campos forem atualizados na tabela abaixo, abra um campo acima daquele onde deseja inserir seu campo personalizado. Em seguida, clique em "Inserir acima" para inserir o novo campo personalizado.

![Select Docytpe](/files/personalize-custom-link-field.gif)![]()

#### Etapa 4 : Valores de campos personalizados

Para definir o campo como Link, insira os valores conforme abaixo.

1. Rótulo: rótulo desejado que o usuário deseja exibir no formulário.
2. Tipo: Definir como 'Link'
3. Nome: Nome desejado para o campo
4. Opções: Insira o nome do DocType ao qual o campo está vinculado

![Enter Values](/files/customize-creating-custom-link-fields.png)![]()  


## Adicionando filtros ao campo de link

O Frappe fornece uma abordagem amigável para aplicar filtros em campos de link usando o Form Builder.

Você notará um ícone de ação em todos os campos de link em um Doctype, que oferece a opção de selecionar os filtros que deseja aplicar.![1](/files/1.png "1.png")Por exemplo, no caso de "Empresa", clicar no ícone abrirá uma caixa de diálogo onde você poderá escolher os filtros desejados.

![2](/files/2.png "2.png")![]()  


Depois de fazer sua seleção e clicar em aplicar, os resultados filtrados serão exibidos de acordo.

![3](/files/3.png "3.png")![]()  


Se você estiver personalizando um formulário e decidir alterar os filtros, um botão "Redefinir para padrão" aparecerá. Clicar aqui reverterá os filtros ao seu estado original. **No entanto, é importante observar que quaisquer filtros em "Personalizar formulário" substituirão os filtros padrão**

![4](/files/4.png "4.png")![]()  


**Observação:** os filtros aplicados por meio de **frm.set\_query** terão precedência sobre os filtros aplicados por meio da interface do usuário (IU).

  




