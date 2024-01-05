# Integração Unicommerce



Unicommerce é um agregador para muitas plataformas de comércio eletrônico que permite vender itens em vários mercados suportados e processar pedidos por meio de uma interface unificada chamada Uniware. Saiba mais sobre o Unicommerce em <https://unicommerce.com/>


## Integração ERPNext com Unicommerce


ERPNext oferece integração bidirecional completa com Unicommerce usando APIs REST da Uniware. Esta integração é fornecida usando o Frappe App oficialmente suportado pela equipe Frappe. Em termos gerais, esta integração abrange:


1. Sincronização do catálogo de itens com Unicommerce (bidirecional)
2. Sincronização de inventário (unidirecional do ERPNext para Unicommerce)
3. Sincronização de novos pedidos de vendas
4. Sincronização de faturas de vendas OU geração de faturas de vendas (qualquer opção deve ser usada)


## Instalação de aplicativo


* Se você estiver hospedando seu site ERPNext no Frappe Cloud, você pode instalar o aplicativo rapidamente acessando o Painel do seu site. O aplicativo está disponível no [Frappe Cloud Marketplace](https://frappecloud.com/marketplace/apps/ecommerce_integrations)
* Se o seu site for hospedado pela Frappe, abra um ticket de suporte para instalar o aplicativo no seu site.
* Se você hospeda o ERPNext você mesmo pode instalar o aplicativo usando o banco Frappe. Consulte a [documentação do Bench](https://frappeframework.com/docs/user/en/bench/frappe-commands#app-installation) para instalar o Frappe Apps. `bench get-app ecommerce_integrations--branch main`


## Autenticação e configuração básica


![unicommerce auth setup](/files/unicommerce-auth-setup.png)


1. Depois que o aplicativo estiver instalado, vá para a página "Configurações do Unicommerce".
2. Clique na caixa de seleção "Ativar Unicommerce".
3. Insira seu site Unicommerce, nome de usuário e senha.
4. O ID do cliente é adicionado por padrão, mas se você configurou um ID do cliente separado, será necessário atualizá-lo aqui. Se não tiver certeza sobre seu ID de cliente, entre em contato com a equipe de suporte do Unicommerce.
5. Clique em "Salvar" para iniciar o processo de autenticação com Unicommerce e configuração de campos personalizados para integração.
6. Assim que a configuração for concluída, você verá tokens de acesso/atualização na seção "Detalhes de autenticação". Isso significa que a autenticação foi bem-sucedida e agora você pode começar a trabalhar em outras configurações.


Se a autenticação falhar:


1. Verifique novamente os detalhes inseridos.
2. Seu servidor pode estar na lista de bloqueio do firewall. Entre em contato com a equipe de suporte do Unicommerce para colocar o IP do seu servidor na lista de permissões.


## Sincronização de itens


Essa integração verifica itens recém-criados e os carrega no Unicommerce de hora em hora. Para ativar esse recurso, você precisa configurar o seguinte:


1. Vá para "Configurações do Unicommerce" e ative "Fazer upload de novos itens para o Unicommerce".
2. Defina um grupo de itens padrão. Isso só é usado como substituto caso o grupo de itens esteja faltando.
3. Ao criar um novo item, marque a caixa de seleção "Sincronizar com Unicommerce" para fazer upload desse item para o Unicommerce.
4. Essa caixa de seleção também pode ser ativada em itens existentes.


O código SKU do Unicommerce é imutável, portanto você não deve alterar o código do item após a criação.


Para sincronizar corretamente o grupo de itens com as categorias de produtos, você precisa mapear todos os grupos de itens para suas respectivas categorias de produtos no Unicommerce.


Para mapear um grupo de itens para uma categoria de produto:


1. Primeiro encontre o código da categoria do produto no Unicommerce.
2. Abra o Grupo de Itens relacionados no ERPNext e atualize o código da categoria do produto Unicommerce lá.


![Categoria de produto Unicommerce](/files/unicommerce-product-category.png)
![Grupo de itens ERPNext](/files/erpnext-item-group.png)


O mapeamento do campo de sincronização de itens é o seguinte:




| ERPNext field | Campo Unicommerce | Comentários |
| --- | --- | --- |

| Código do item | SKU | Aplicam-se restrições de SKU do Unicommerce |

| Nome do item | Nome do item |  |

| Descrição | Descrição |  |

| Peso por unidade | Peso | Somente se definido em gramas. |

| Prazo de validade em dias | Prazo de validade |  |

| Código HSN | Código HSN |  |

| Imagem | Imagem |  |

| Comprimento do item Unicommerce | Comprimento |  |

| Largura do item Unicommerce | Largura |  |

| Altura do item Unicommerce | Altura |  |

| Desativado | Ativado | (o oposto está mapeado) |

| Código de barras EAN | EAN |  |

| Código de barras UPC | UPC-A |  |

| Grupo de itens | Categoria do produto |  |



## Sincronização de inventário


Depois que a sincronização de itens estiver configurada, a sincronização de inventário poderá ser ativada. A integração verifica alterações no inventário do ERPNext e as envia para o Unicommerce no intervalo configurado. Os níveis de inventário do ERPNext são considerados fonte de verdade pela integração e os níveis de inventário do Unicommerce são substituídos pelos valores de inventário do ERPNext.


1. Vá para "Configurações do Unicommerce" e role para baixo até a seção "Sincronização de inventário".
2. Marque "Ativar sincronização de inventário"
3. Configure a frequência de sincronização. A frequência recomendada é de 15 a 60 minutos.
4. Na tabela de mapeamento do Warehouse adicione todos os códigos de instalação que você possui no Unicommerce e mapeie-os com o armazém ERPNext.
5. Marque a caixa de seleção "Ativado" para todos os recursos que deseja ativar.
6. Salve as configurações.



> 
> Observação: todo o inventário é enviado para a estante "DEFAULT". As prateleiras do Unicommerce não são suportadas por esta integração. Certifique-se de ter apenas uma prateleira no Unicommerce chamada "DEFAULT" para garantir a sincronização correta do inventário.
> 
> 
> 



> 
> Observação: o Unicommerce, assim como outras integrações de comércio eletrônico, não oferece suporte a inventário fracionário.
> 
> 
> 


## Processamento de pedidos de vendas-Fluxo de trabalho


A seguir está o fluxo de trabalho para processamento de pedidos no ERPNext. Como alternativa, você também pode processar pedidos no Unicommerce e sincronizar apenas os pedidos finalizados. 


![fluxo de trabalho do Unicommerce](/files/unicommerce_workflow.png)


## Sincronização de pedidos de vendas-configuração de canais


A integração Unicommerce oferece suporte ao recebimento e processamento de vários canais. Para permitir isso, a configuração da sincronização de pedidos de vendas também deve ser feita em vários estágios.


### Padrões para sincronização de pedidos de vendas


![sincronização padrão do pedido de vendas](/files/sales-order-sync.png)


1. Vá para "Configurações do Unicommerce".
2. Role até a seção de configuração "Sincronização de pedidos de vendas".
3. Configure a frequência de sincronização do pedido. A frequência recomendada é de 30 a 60 minutos.
4. Configure o grupo de clientes padrão e a série de nomenclatura para documentos.


### Configurações de sincronização de pedidos de vendas específicas do canal


![sincronização de pedidos de vendas específicos do canal](/files/unicommerce-channel-setup.png)


Para permitir uma configuração flexível para cada canal, você precisa criar o documento "Canal Unicommerce" para cada canal que deseja ativar para sincronização de pedidos de vendas.


1. Vá para "Canal Unicommerce" na barra de pesquisa ou na página de configurações do Unicommerce.
2. Clique em "Adicionar canal Unicommerce"
3. Preencha os detalhes necessários, como ID do canal, armazém padrão, empresa, contas e série de nomes.
4. Se o envio para este canal for feito pelo marketplace, clique em "Frete feito pelo marketplace" ou desmarque-a.
5. Após configurar totalmente o canal, clique na caixa de seleção "Ativado".


Novos pedidos de vendas criados no Unicommerce agora começarão a ser sincronizados com o ERPNext. Durante este processo, se um novo item for encontrado, ele será criado no ERPNext usando informações do Unicommerce. Informações relevantes sobre o pedido Unicommerce são mapeadas para os campos ERPNext. Informações adicionais podem ser encontradas na seção "Detalhes do Unicommerce" no Pedido de Vendas.


## Sincronização de faturas de vendas


A sincronização da fatura de vendas pode ser feita de duas maneiras. Selecione a opção apropriada de acordo com suas necessidades.


#### 1. Processamento de fatura no Unicommerce (recomendado)


Se você deseja processar pedidos e faturas no Unicommerce e sincronizar apenas pedidos totalmente processados ​​no ERPNext, ative "Sincronizar somente pedidos concluídos" nas configurações do Unicommerce.


#### 2. Processando fatura no ERPNext


Se você deseja processar pedidos apenas do ERPNext, então você precisa gerar a fatura do Pedido de Vendas do ERPNext.


Para gerar fatura, acesse Pedido de Venda Unicommerce sincronizado, clique em "Unicommerce > gerar fatura". Isso criará uma fatura de vendas e deduzirá o estoque também.


![botão gerar fatura](/files/generate-invoice.png)


## Manifesto de Remessa


Se você estiver processando pedidos no ERPNext usando o método nº 2 descrito acima, você precisará criar e enviar um manifesto de envio para informar ao Unicommerce que você enviou os pedidos.


Os pré-requisitos são configurar os seguintes tipos de documentos. Você pode encontrar o código na página de criação de manifesto do Unicommerce:
1. Crie um provedor de remessa Unicommerce
2. Crie um método de envio Unicommerce


![Manifesto de remessa Unicommerce](/files/shipment-manifest.png)


Processo de criação do manifesto:


1. Quando estiver pronto para despachar os pacotes para o fornecedor de remessa, você deve criar o documento "Manifesto de Remessa Unicommerce". Vá para a barra de pesquisa > "Manifesto de envio Unicommerce" > + Adicionar
2. Selecione o ID do canal, o método de envio e o código do fornecedor de envio.
3. Agora você pode usar o botão "Obter pacote" para buscar pedidos abertos com base nos filtros selecionados ou usar o campo "Verificar código AWB" para verificar o AWB de pacotes. Ambos preencherão automaticamente os detalhes restantes após salvar.
4. Quando tiver certeza de que todos os detalhes estão corretos, salve e envie o documento.
5. Ao enviar o manifesto, o mesmo manifesto é criado e fechado no Unicommerce e as remessas são marcadas como “Enviadas”. O PDF do Manifesto Unicommerce também é obtido e anexado ao documento manifesto do ERPNext.


## Atualizações de status


![Seção de detalhes do Unicommerce](/files/unicommerce-details-section.png)


O status do Unicommerce é atualizado periodicamente no ERPNext, você pode ver o status atual na seção "Detalhes do Unicommerce".


## Cancelamentos de pedidos


Quando o pedido é cancelado no Unicommerce, a integração sincroniza esta ação e cancela o pedido também no ERPNext. Pedidos parcialmente cancelados também são sincronizados e itens cancelados são removidos do Pedido de Vendas do ERPNext. Os cancelamentos totais e parciais são sincronizados de hora em hora e logo antes da geração das faturas. 


## Devoluções de pedidos


Quando a devolução é criada no Unicommerce, a integração sincroniza esta ação e cria uma Nota de Crédito *Rascunho* no ERPNext. 


Ambos os casos de devolução são tratados pela integração:


* RTO (retorno à origem)
Quando a remessa é devolvida à origem, o status da remessa muda e uma Nota de Crédito (com Atualização de Estoque) é criada no ERPNext. A nota de crédito será de retorno total.
* CIR (devolução iniciada pelo cliente)
Quando um cliente devolve uma remessa, isso é refletido na seção Pedido de Venda do Unicommerce. A nota de crédito total ou parcial é criada dependendo da natureza da devolução iniciada pelo cliente.


Você pode visualizar todas as devoluções acessando "Fatura de venda" e filtrando por "É devolução" definido como Sim. O código de rastreamento de devolução também é capturado na nota de crédito.


Ao criar devoluções, o armazém de devoluções é selecionado com base no armazém de devoluções configurado nas configurações do Unicommerce. Se não estiver definido, o armazém original será usado. 


![Armazém de devolução Unicommerce](/files/return-warehouse-map.png)



