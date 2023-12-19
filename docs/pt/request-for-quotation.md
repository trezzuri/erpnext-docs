# Solicitação de cotação



**Uma solicitação de cotação é um documento que uma organização envia a um ou mais fornecedores solicitando uma cotação de itens.**

![Fluxo de compra](/files/buying_flow_rfq.png)![]()

Para acessar a **Solicitação de Cotação**, abra a área de trabalho "Compra" e, em "Relatórios & Mestres" > "Compra", clique em "Solicitação de Citação".

## 1. Pré-requisitos

Antes de criar e usar uma **Solicitação de Cotação**, é aconselhável que você crie primeiro o seguinte:

* [Fornecedor](/docs/pt/buying/supplier)
* [Item](/docs/pt/stock/item)

## 2. Como criar uma solicitação de cotação

1. Vá para a lista **Solicitação de cotação** e clique em "+ Adicionar solicitação de cotação".
2. Insira a *Data obrigatória* até a qual você precisará dos materiais solicitados.
3. Preencha os "Fornecedores" lista com possíveis fornecedores.  
Se você definir um *Contato* e um *Id de e-mail*, eles poderão ser usados ​​posteriormente para enviar a **Solicitação de Cotação** via e-mail e conceda acesso ao portal do fornecedor.
4. Na próxima tabela, insira os itens necessários junto com a UOM e a quantidade, bem como o armazém de destino.
5. O *Armazém* pode ser deixado em branco se *Manter Estoque* não estiver habilitado para o item.
6. Se desejar enviar a **Solicitação de Cotação** aos seus fornecedores por e-mail, você pode criar um **Modelo de E-mail** e selecioná-lo aqui. No modelo, você pode usar variáveis ​​especiais para dados específicos do fornecedor:  
  



	1. `&lcub;&lcub; update_password_link }}` : um link onde seu fornecedor pode definir uma nova senha para fazer login em seu portal.
	2. `&lcub;&lcub; portal_link }}`: um link a esta RFQ no portal do fornecedor.
	3. `&lcub;&lcub; fornecedor_name }}`: o nome da empresa do seu fornecedor.
	4. `&lcub;&lcub; contact.salutation }} &lcub;&lcub; contact.last_name }}`: a pessoa de contato do seu fornecedor.
	5. `&lcub;&lcub; user_fullname }}`: seu nome completo.  
	  
	Além desses, você pode acessar todos os valores nesta RFQ, como `&lcub;&lcub; message_for_supplier }}` ou `&lcub;&lcub; termos }}`.
7. Você pode verificar como o e-mail procurará um fornecedor específico usando o botão "Visualizar e-mail".

![Visualizar e-mail](/files/email-preview.png)![]()
8. Se você deseja enviar mais anexos para seu fornecedores, você pode ativar a caixa de seleção   
*Enviar arquivos anexados*. Isso adicionará cada arquivo anexado à **Solicitação de cotação** como um anexo ao e-mail de cada fornecedor.
9. Quando terminar, salve o **Solicitação de cotação** como um rascunho.
10. Quando estiver pronto, você poderá enviar a **Solicitação de cotação**. Isso acionará um e-mail para cada fornecedor que tiver *Enviar e-mail* ativado.

![Criar RFQ](/files/rfq-create.png)![]()  


Uma Solicitação de Cotação (RFQ) também pode ser criada a partir de uma Solicitação de Material enviada. Depois que uma RFQ for criada, você poderá imprimir e enviar aos fornecedores o PDF que conterá todos os detalhes inseridos relevantes para a RFQ. Você também pode obter a resposta (cotação do fornecedor) no próprio ERPNext, consulte a seção [4.1 Cotação do fornecedor por usuário](#41-supplier-quotation-by-user) . Contudo, para um grande número de itens, seu fornecedor pode se sentir mais confortável com uma planilha Excel, etc.

## 3. Recursos

### 3.1 Obter itens de

Os itens na tabela de itens podem ser obtidos de outros documentos. As opções são: Solicitação de Material, Oportunidade e Possível Fornecedor.

* **Solicitação de Material**: Os itens serão obtidos de uma Solicitação de Material enviada que você selecionar. Uma Solicitação de Material pode ser pesquisada com algumas palavras correspondentes e um intervalo de datas também pode ser selecionado para filtrar as Solicitações de Material.
* **Oportunidade**: os itens serão obtido de uma oportunidade salva. Um intervalo de datas também pode ser selecionado aqui.
* **Possível Fornecedor**: Selecione um possível fornecedor. Então, se você tiver alguma solicitação de material enviada para esse fornecedor, os itens poderão ser obtidos dele.

![RFQ get items](/files/rfq-get-items.png)![]()  
 

### 3.2 Obter Fornecedores

Em vez de inserir os fornecedores manualmente na tabela, você também pode buscá-los usando o botão 'Obter Fornecedores'. Ao clicar em **Ferramentas > Obter Fornecedores**, você verá o campo 'Obter Fornecedores por'. Existem duas opções para buscar fornecedores: Por Tag ou Por Grupo.

* **Por tag**: Vá para 'Categoria de Tag' pesquisando na barra de pesquisa. Você deve primeiro ter criado tags aqui e atribuído a um Fornecedor no módulo Compras. Então você pode selecionar 'Por Tag'. Ao clicar em Adicionar 'Todos os Fornecedores', os fornecedores com tags correspondentes serão buscados.
* **Por Grupo**: Selecione 'Grupo de Fornecedores' e escolha o grupo de fornecedores dos quais os fornecedores precisam ser adicionados. Por exemplo, se você selecionar Hardware, todos os seus fornecedores de hardware serão adicionados para que você possa obter uma cotação de todos eles.

![RFQ obter fornecedores ](/files/rfq-get-suppliers.png)![]()  


Na tabela Fornecedor, ao expandir uma linha com o triângulo invertido, você verá a opção 'Baixar PDF' que abrirá um PDF da RFQ.### 3.3 Link para Solicitações de Materiais:

Ao clicar em **Ferramentas > Link para Solicitações de Materiais**, vincula a Solicitação de Cotação às Solicitações de Materiais disponíveis. Os itens devem ser os mesmos na Solicitação de Cotação e na Solicitação de Material.

![Link to Material Request](/files/link-to-material-request.png)![]()  


Agora , ao salvar a Solicitação de Cotação, você pode ver no Dashboard que ela está vinculada à Solicitação de Material. Se houver várias Solicitações de Material com os mesmos itens, o link será criado com a Solicitação de Material mais recente.

### 3.5 Termos e Condições

Em transações de Venda/Compra, pode haver certos Termos e Condições com base nos quais o Fornecedor fornece bens ou serviços ao Cliente. Você pode aplicar os Termos e Condições às transações e eles aparecerão na impressão do documento. Para saber mais sobre os Termos e Condições, [clique aqui](/docs/pt/setting-up/print/terms-and-conditions) 

### 3.6 Configurações de impressão

#### Papel timbrado

Você pode imprimir sua solicitação de cotação/pedido de compra em papel timbrado da sua empresa. Saiba mais [aqui](/docs/pt/setting-up/print/letter-head).

'Agrupar os mesmos itens' agrupará os mesmos itens adicionados várias vezes na tabela de itens. Isso pode ser visto quando você o imprime.

#### Imprimir cabeçalhos

Os títulos dos seus documentos podem ser alterados. Saiba mais [aqui](/docs/pt/setting-up/print/print-headings).

#### Propriedades especiais

Ao imprimir uma RFQ através do botão "Ferramentas > Baixar PDF", você será solicitado a selecionar o fornecedor específico que deseja abordar. No **Formato de impressão** para RFQ, essas informações podem ser acessadas por meio de propriedades especiais:

* `&lcub;&lcub; doc.vendor }}` contém o ID do fornecedor selecionado.
* `&lcub;&lcub; doc.items[i].supplier_part_no }}` contém o *número da peça do fornecedor* de um item de linha solicitado.

Os dados do primeiro fornecedor serão usados ​​durante a renderização da visualização de impressão padrão. Se desejar imprimir para um fornecedor diferente, use o botão "Ferramentas > Baixar PDF".

## 4. Criando uma cotação de fornecedor após RFQ

Após a criação da solicitação de cotação, há duas maneiras de gerar a cotação de fornecedor a partir da solicitação de cotação.

### 4.1 Cotação de fornecedor por usuário

1. Abra a solicitação de cotação e clique em **Cotação do fornecedor > Criar**.

![Cotação do fornecedor da RFQ](/files/make-supplier-quotation-from-rfq.png)![]()
2. Selecione o Fornecedor, clique no fornecedor novamente. Nesta página, clique no + ao lado de 'Cotação do fornecedor'. Uma nova página de cotação do fornecedor será aberta, o usuário deverá inserir a quantidade, taxa e enviá-la.

![Cotação do fornecedor do fornecedor](/files/supplier-quotation-from-sup.png)![]()

### 4.2 Cotação do Fornecedor

1. Se um [Contato](/docs/pt/CRM/contact ) é criado para o Fornecedor e um endereço de e-mail é associado ao Contato, os detalhes do Contato e o endereço de e-mail serão obtidos ao selecionar o Fornecedor. Crie um contato e um endereço de e-mail, se ainda não estiver presente.
2. Clique em **Ferramentas > Enviar e-mails para fornecedores**.

**Se a conta do Fornecedor não estiver presente**: O sistema criará a conta do Fornecedor e enviará os detalhes ao Fornecedor. O Fornecedor deverá clicar no link (Atualização de Senha) presente no email. Após a atualização da senha, o Fornecedor poderá acessar seu portal através do formulário ‘Solicitação de Cotação’. O Fornecedor será criado como um Usuário do Site.

![E-mail do fornecedor se a conta não estiver presente](/files/fornecedor-email-with-update-password.png)![]()  


 **Se a conta do Fornecedor estiver presente**: O sistema enviará um link de Solicitação de Cotação ao Fornecedor. O Fornecedor deverá fazer login com suas credenciais para visualizar o formulário de Solicitação de Cotação no portal.

![E-mail do fornecedor se conta presente](/files/supplier-email-normal.png)![]()
3. De qualquer forma, quando o Fornecedor fizer login, a tela a seguir será mostrada a ele. A partir daqui, eles podem lhe enviar uma cotação:

![Supplier Quotation Screen](/files/rfq-supplier-quote.png)![]()  


O Fornecedor deve inserir o valor e as notas (pagamento termos) no formulário e clique em Enviar. Na seção Cotações, as cotações anteriores estarão visíveis.
4. Ao enviar, o ERPNext criará uma Cotação do Fornecedor (modo rascunho) contra o Fornecedor. O usuário deve revisar a Cotação do Fornecedor e enviá-la. Quando todos os itens da Solicitação de Cotação tiverem sido cotados por um Fornecedor, o status da cotação será atualizado para 'Recebido' na tabela 'Fornecedores' da Solicitação de Cotação.

![RFQ status após cotação do fornecedor](/files/rfq-supplier-quoted.png)![]()

Leia [Cotação do fornecedor](/docs/pt/buying/supplier-quotation) para saber mais.

## 5. Vídeo

### 6. Tópicos relacionados

1. [Ordem de compra](/docs/pt/buying/purchase-order)
2. [Fornecedor](/docs/pt/buying/supplier)
3. [Cotação do fornecedor](/docs/pt/buying/supplier-quotation)
4. [Cotação](/docs/pt/selling/quotation)
5. [Solicitação de material](/docs/pt/stock/material-request )




