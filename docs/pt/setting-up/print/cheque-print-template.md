# Modelo de impressão de cheque



**Modelo de impressão de cheque permite definir modelos para cheques bancários.**


Os negócios envolvem efetuar pagamentos a diversas partes, como fornecedores e funcionários. O pagamento pode ser feito em várias modalidades, como dinheiro, NEFT ou cheque. Se você estiver fazendo um pagamento através de cheque, você também pode criar um Formato de Impressão para imprimir Cheques do ERPNext com base na Entrada de Pagamento.


Para acessar o modelo de impressão de cheque, acesse:
> Home > Contabilidade > Modelo de impressão de cheque


Usando o modelo de impressão de cheques você pode gerar um novo formato de impressão para cheques. Ele será criado com base no formato de cheque fornecido pelo seu banco.


Um exemplo de cheque:


![Cheque de amostra](/files/sample-cheque.jpg)


## 1. Como criar um modelo de impressão de cheque


1. Vá para a lista Verificar modelo de impressão e clique em Novo.
2. Você pode definir a posição de vários itens no cheque.
3. Salvar.


No modelo de impressão de cheque, para cada valor (por exemplo, Beneficiário, Data), as coordenadas exatas são fornecidas com base em onde esse valor deve ser impresso em um cheque. As coordenadas são fornecidas em centímetros. Aqui está uma representação da estrutura:


![Amostra de cheque](/files/cheque-1.png)


### 1.1 Novo formato por digitalização


Para acelerar a criação de um novo formato de impressão de cheque, você pode fazer upload de uma imagem digitalizada do cheque. Considerando a imagem digitalizada do cheque, o sistema atualiza automaticamente as coordenadas para cada valor, como nome da parte, valor, data, valor por extenso, etc.


### 1.2 Novo formato de impressão manualmente


Se a visualização parecer boa, clique no botão **Criar formato de impressão** para criar um novo formato de impressão para imprimir o cheque. Com base nos valores fornecidos no Modelo de Impressão de Cheque, o sistema gerará automaticamente um script HTML para o Formato de Impressão do cheque.


Você pode fornecer manualmente a coordenada para cada valor com base em onde deseja que ele seja impresso no cheque e personalizar com HTML/CSS.


#### Visualização


Com base nas coordenadas fornecidas para todos os valores, será mostrada uma prévia de como os valores serão impressos no cheque.


![Amostra de cheque](/files/cheque-2.png)


### 1.3 Impressão de cheques


O novo formato de impressão gerado para o cheque ficará visível no formulário de Entrada de Pagamento. Depois de criar o lançamento de pagamento, você poderá imprimir os detalhes da transação no cheque.


![Amostra de cheque](/files/cheque-3.gif)


### 2. Tópicos Relacionados


1. [Modelo de endereço](/docs/pt/setting-up/print/address-template)
2. [Modelo de Termos e Condições](/docs/pt/setting-up/print/terms-and-conditions)



