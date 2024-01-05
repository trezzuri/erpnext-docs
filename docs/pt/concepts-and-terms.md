# Conceitos e Termos



Antes de iniciar a implementação, vamos nos familiarizar com a terminologia que
é usado e alguns conceitos básicos no ERPNext.



### Conceitos Básicos


#### Empresa


Isto representa os registros da Empresa para os quais o ERPNext está configurado. Com este mesmo
configuração, você pode criar vários registros de empresa, cada um representando um diferente
entidade legal. A contabilização de cada Empresa será diferente, mas
compartilhar os registros de Cliente, Fornecedor e Item.



> 
> Configuração > Empresa
> 
> 
> 


#### Cliente


Representa um cliente. Um Cliente pode ser um indivíduo ou uma organização.
Você pode criar vários contatos e endereços para cada cliente.



> 
> Venda > Cliente
> 
> 
> 


#### Fornecedor


Representa um fornecedor de bens ou serviços. Sua companhia telefônica é uma
Fornecedor, seu fornecedor de matérias-primas também. Novamente, um Fornecedor pode ser um
indivíduo ou organização e possui vários contatos e endereços.



> 
> Compra > Fornecedor
> 
> 
> 


#### Item


Um produto, subproduto ou serviço que é comprado, vendido ou fabricado
e é identificado exclusivamente.



> 
> Estoque > Item
> 
> 
> 


#### Conta


Uma conta é um título sob o qual as transações financeiras e comerciais são
continuou. Exemplos de contas são "Devedores", "Credores", "IVA a Pagar", "Despesas de Viagem", "Vendas", "Capital Social", etc.
os saldos dos fornecedores em segundo plano, para que você não precise criar contas dedicadas para eles.



> 
> Contabilidade > Plano de contas
> 
> 
> 


#### Endereço


Um endereço representa detalhes de localização de um Cliente ou Fornecedor. Estes podem ser
de diferentes locais, como sede, fábrica, armazém, loja, etc.



> 
> Venda > Endereço
> 
> 
> 


#### Contato


Um Contato individual pertence a um Cliente ou Fornecedor ou é apenas um
independente. Um contato tem um nome e detalhes de contato, como e-mail e telefone
número.



> 
> Venda > Contato
> 
> 
> 


#### Comunicação


Uma lista de todas as comunicações com um contato ou lead. Todos os e-mails enviados do
sistema são adicionados à tabela Comunicação.



> 
> Suporte > Comunicação
> 
> 
> 


#### Lista de preços


Uma Lista de Preços é um local onde diferentes planos de tarifas podem ser armazenados. É um nome
você dá a um conjunto de preços de itens armazenados em uma lista específica.



> 
> Venda > Lista de Preços
> 
> 
> 



> 
> Compra > Lista de preços
> 
> 
> 



### Contabilidade


#### Ano fiscal


Representa um exercício financeiro ou exercício contábil. Você pode operar vários
Exercícios Fiscais ao mesmo tempo. Cada ano fiscal tem uma data de início e uma data de término
data e as transações só podem ser registradas neste período. Quando você “fecha” um
exercício fiscal, seus saldos são transferidos como saldos de “abertura” para o próximo
ano fiscal.



> 
> Configuração > Empresa > Ano fiscal
> 
> 
> 


#### Centro de Custo


Um Centro de Custo é como uma Conta, mas a única diferença é que seu
A estrutura representa seu negócio mais de perto do que as Contas.
Por exemplo, no seu Plano de Contas, você pode separar suas despesas por tipo
(ou seja, viagens, marketing, etc.). No seu Gráfico de Centros de Custo você pode separar
por linha de produto ou grupo de negócios (por exemplo, vendas on-line, vendas no varejo, etc.).



> 
> Contabilidade > Gráfico de Centros de Custo
> 
> 
> 


#### Lançamento de diário


Um documento que contém entradas do Razão Geral (GL) e a soma de Débitos e
Os créditos dessas entradas são os mesmos. No ERPNext você pode atualizar Pagamentos,
Devoluções, etc., usando lançamentos contábeis manuais.



> 
> Contabilidade > Lançamento contábil manual
> 
> 
> 


#### Fatura de vendas


Uma fatura enviada aos Clientes pela entrega de Itens (bens ou serviços).



> 
> Contabilidade > Fatura de vendas
> 
> 
> 


#### Fatura de compra


Uma fatura enviada por um Fornecedor para entrega de Itens (bens ou serviços).



> 
> Contabilidade > Fatura de compra
> 
> 
> 


#### Moeda


ERPNext permite que você reserve transações em múltiplas moedas. Existe apenas
uma moeda para o seu livro de contas. Ao postar suas faturas com
pagamentos em moedas diferentes, o valor é convertido para o padrão
moeda pela taxa de conversão especificada.



> 
> Configuração > Moeda
> 
> 
> 



### Venda


#### Grupo de clientes


Uma classificação de Clientes, geralmente baseada no segmento de mercado.



> 
> Vendas > Configuração > Grupo de clientes
> 
> 
> 


#### Líder


Uma pessoa que pode ser uma futura fonte de negócios. Um Lead pode gerar
Oportunidades. (de: “pode levar a uma venda”).



> 
> CRM > Lead
> 
> 
> 


#### Oportunidade


Uma venda potencial. (de: “oportunidade de negócio”).



> 
> CRM > Oportunidade
> 
> 
> 


#### Citação


Solicitação do cliente para definir o preço de um item ou serviço.



> 
> Venda > Cotação
> 
> 
> 


#### Pedido de venda


Uma nota confirmando as condições de entrega e o preço de um Item (produto ou
serviço) pelo Cliente. Entregas, Ordens de Serviço e Faturas são feitas
com base em pedidos de vendas.



> 
> Venda > Pedido de venda
> 
> 
> 


#### Território


Uma classificação de área geográfica para gerenciamento de vendas. Você pode definir metas
para Territórios e cada venda está vinculada a um Território.



> 
> Venda > Configuração > Território
> 
> 
> 


#### Parceiro de vendas


Um distribuidor/revendedor/afiliado/agente comissionado terceirizado que vende
os produtos da empresa geralmente mediante o pagamento de uma comissão.



> 
> Vendas > Configuração > Parceiro de vendas
> 
> 
> 


#### Vendedores


Alguém que apresenta o argumento de venda ao cliente e fecha negócios. Você pode definir metas para
Vendedores e marcá-los nas transações.



> 
> Vendas > Configuração > Vendedor
> 
> 
> 



### Comprando


#### Pedido de compra


Um contrato dado a um Fornecedor para entregar os Itens especificados no prazo especificado
custo, quantidade, datas e outros termos.



> 
> Compra > Ordem de compra
> 
> 
> 


#### Solicitação de material


Uma solicitação feita por um usuário do sistema, ou gerada automaticamente pelo ERPNext baseado
no nível de novo pedido ou quantidade projetada no Plano de Produção para comprar um conjunto
de itens.



> 
> Compra > Solicitação de material
> 
> 
> 



### Estoque (Inventário)


#### Armazém


Um armazém lógico no qual são feitas entradas de estoque.



> 
> Estoque > Armazém
> 
> 
> 


#### Entrada de estoque


Transferência de material de um armazém para um armazém ou de um armazém para
outro.



> 
> Estoque > Entrada de estoque
> 
> 
> 


#### Nota de entrega


Uma lista de itens com quantidades para envio. Uma Nota de Entrega reduzirá o
estoque de Itens para o Armazém de onde você envia. Uma nota de entrega é
geralmente feito em relação a um pedido de venda.



> 
> Estoque > Nota de entrega
> 
> 
> 


#### Recibo de compra


Uma nota informando que um determinado conjunto de Itens foi recebido do Fornecedor,
provavelmente contra um pedido de compra.



> 
> Estoque > Recibo de compra
> 
> 
> 


#### Número de série


Um número exclusivo atribuído a uma unidade específica de um item.



> 
> Estoque > Número de série
> 
> 
> 


#### Lote


Um número dado a um grupo de unidades de um item específico que pode ser comprado
ou fabricados em grupo.



> 
> Estoque > Lote
> 
> 
> 


#### Entrada no razão de estoque


Uma tabela unificada para toda a movimentação de materiais de um armazém para outro. Esse
é a tabela que é atualizada quando uma Entrada de Estoque, Nota de Remessa, Compra
É feito o recebimento e a fatura de venda (PDV).


#### Reconciliação de estoque


Atualize o estoque de vários itens a partir de um arquivo de planilha (CSV).



> 
> Estoque > Reconciliação de estoque
> 
> 
> 


#### Inspeção de qualidade


Uma nota preparada para registrar certos parâmetros de um Item no momento do Recebimento
do Fornecedor ou Entrega ao Cliente.



> 
> Estoque > Inspeção de qualidade
> 
> 
> 


#### Grupo de itens


Uma classificação do item.



> 
> Estoque > Configuração > Grupo de itens
> 
> 
> 



### Gestão de Recursos Humanos


#### Funcionário


Registro de uma pessoa que esteve no presente ou no passado no emprego do
empresa.



> 
> Recursos Humanos > Funcionário
> 
> 
> 


#### Sair da inscrição


Um registro de uma solicitação de licença aprovada ou rejeitada.



> 
> Recursos Humanos > Solicitação de licença
> 
> 
> 


#### Tipo de saída


Um tipo de licença (por exemplo, licença médica, licença maternidade, etc.).



> 
> Recursos Humanos > Licença e Presença > Tipo de Licença
> 
> 
> 


#### Lançamento da folha de pagamento


Uma ferramenta que auxilia na criação de vários comprovantes de salário para funcionários.



> 
> Recursos Humanos > Entrada da Folha de Pagamento
> 
> 
> 


#### Recibo de salário


Um registro do salário mensal dado a um Funcionário.



> 
> Recursos Humanos > Comprovante de Salário
> 
> 
> 


#### Estrutura Salarial


Um modelo que identifica todos os componentes do salário (ganhos) de um funcionário,
impostos e outras deduções de segurança social.



> 
> Recursos Humanos > Salário e Folha de Pagamento > Estrutura Salarial
> 
> 
> 


#### Avaliação


Um registro do desempenho de um Funcionário durante um período especificado com base em
determinados parâmetros.



> 
> Recursos Humanos > Avaliação
> 
> 
> 


#### Modelo de avaliação


Um modelo que registra os diferentes parâmetros de desempenho e
seu peso para uma função específica.



> 
> Recursos Humanos > Configuração de Funcionário > Modelo de Avaliação
> 
> 
> 


#### Presença


Um registro que indica a presença ou ausência de um Funcionário em um determinado dia.



> 
> Recursos Humanos > Atendimento
> 
> 
> 



### Fabricação


#### lista de materiais (BOM)


Uma lista de Operações e Itens com suas quantidades, que são necessários para
produzir outro item. Uma lista de materiais (BOM) é usada para planejar compras e
faça o cálculo do custo do produto.



> 
> Fabricação > BOM
> 
> 
> 


#### Estação de trabalho


Um local onde ocorre uma operação de BOM. É útil calcular o
custo direto do produto.



> 
> Fabricação > Estação de trabalho
> 
> 
> 


#### Ordem de serviço


Um documento que sinaliza a produção (fabricação) de um item específico com
quantidades especificadas.



> 
> Fabricação > Ordem de serviço
> 
> 
> 


#### Ferramenta de planejamento de produção


Uma ferramenta para criação automática de Ordens de Serviço e Solicitações de Compra com base
em pedidos de vendas em aberto em um determinado período.



> 
> Fabricação > Ferramenta de planejamento de produção
> 
> 
> 



### Site


#### Postagem no blog


Um pequeno artigo que aparece na seção “Blog” do site gerado
do módulo do site ERPNext. Blog é uma forma abreviada de “Web Log”.



> 
> Site > Postagem do blog
> 
> 
> 


#### Página da Web


Uma página da web com um URL exclusivo (endereço da web) no site gerado a partir de
ERPNext.



> 
> Site > Página da Web
> 
> 
> 



### Configuração/Personalização


#### Campo personalizado


Um campo definido pelo usuário em um formulário/tabela.



> 
> Configuração > Personalizar ERPNext > Campo Personalizado
> 
> 
> 


#### Padrões globais


Esta é a seção onde você define valores padrão para vários parâmetros do
sistema.



> 
> Configuração > Dados > Padrões globais
> 
> 
> 


#### Imprimir cabeçalho


Um título que pode ser definido em uma transação apenas para impressão. Por exemplo, você
deseja imprimir uma cotação com o título “Proposta” ou “Fatura pró-forma”.



> 
> Configuração > Marca e impressão > Imprimir cabeçalhos
> 
> 
> 


#### Termos e Condições


Texto dos termos do seu contrato. Nas transações de Venda/Compra podem existir determinados Termos e Condições com base nos quais o Fornecedor fornece bens ou serviços ao Cliente. Você pode aplicar os Termos e Condições às transações e eles aparecerão na impressão do documento. Para saber mais sobre os Termos e Condições, [clique aqui](/docs/pt/setting-up/print/terms-and-conditions)



> 
> Vendas > Configuração > Termos e Condições
> 
> 
> 


#### Unidade de medida (UM)


Como a quantidade é medida para um item. Por exemplo, Kg, Nº, Par, Pacote, etc.



> 
> Estoque > Configuração > UDM
> 
> 
> 



