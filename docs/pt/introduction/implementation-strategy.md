# Estratégia de implementação


Antes de começar a gerenciar suas operações no SOMA, você deve primeiro se tornar
familiarizado com o sistema e os termos usados. Para isso recomendamos
a implementação deve acontecer em duas fases.


* Uma **fase de teste**, onde você insere registros fictícios que representam suas transações diárias e uma **fase ao vivo**, onde começamos a inserir dados ao vivo.


### Fase de teste


* Leia o Manual
* Crie uma conta gratuita em <https://erpnext.com> (a maneira mais fácil de experimentar).
* Crie seu primeiro cliente, fornecedor e item. Adicione mais alguns para se familiarizar com eles.
* Crie Grupos de Clientes, Grupos de Itens, Armazéns, Grupos de Fornecedores, para que você possa classificar seus Itens.
* Conclua um ciclo de vendas padrão - Lead > Oportunidade > Cotação > Pedido de venda > Nota de entrega > Fatura de venda > Pagamento (registro de diário)
* Conclua um ciclo de compra padrão - Solicitação de material > Pedido de compra > Recibo de compra > Pagamento (registro de diário).
* Conclua um ciclo de fabricação (se aplicável) - BOM > Ferramenta de planejamento de produção > Ordem de serviço > Emissão de material
* Replicar um cenário da vida real no sistema.
* Crie campos personalizados, formatos de impressão, etc, conforme necessário.


### Fase ao vivo


Assim que estiver familiarizado com o SOMA, comece a inserir seus dados ao vivo!


* Limpe a conta dos dados de teste ou melhor, inicie uma nova instalação.
* Se você deseja apenas limpar suas transações e não seus dados mestre, como Item, Cliente, Fornecedor, BOM etc., clique em Excluir as transações de sua empresa e começar do zero. Para fazer isso, abra o Registro da Empresa em Contabilidade > Mestre de Contabilidade > Empresa e exclua as transações da sua Empresa clicando no botão **Excluir Transações da Empresa** na parte inferior do Formulário da Empresa.
* Você também pode configurar uma nova conta em <https://erpnext.com> e usar a avaliação gratuita de 14 dias. [Descubra mais formas de implantar o SOMA](getting-started-with-erpnext)
* Configurar todos os módulos com grupos de clientes, grupos de itens, armazéns, BOMs, etc.
* Importe clientes, fornecedores, itens, contatos e endereços usando a ferramenta de importação de dados.
* Importe o estoque inicial usando a Ferramenta de reconciliação de estoque.
* Crie lançamentos contábeis de abertura por meio do lançamento contábil manual e crie faturas de vendas e faturas de compra pendentes.
* Se precisar de ajuda, [você pode comprar suporte](https://erpnext.com/pricing) ou [perguntar no fórum do usuário](https://discuss.erpnext.com).
