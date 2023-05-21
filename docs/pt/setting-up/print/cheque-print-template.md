# Verifique o modelo de impressão


**Cheque Print Template permite definir modelos para cheques bancários.**


O negócio envolve fazer o pagamento a várias partes, como fornecedores e funcionários. O pagamento pode ser feito em vários modos como dinheiro, NEFT ou cheque. Caso esteja efetuando um pagamento através de cheque, também é possível criar um Formato de Impressão para impressão de Cheques do ERPNext com base no Lançamento de Pagamento.


Para acessar o modelo de impressão de cheque, acesse:



>
> Início > Contabilidade > Modelo de impressão de cheque
>
>
>


Usando o Modelo de Impressão de Cheque, você pode gerar um novo Formato de Impressão para cheques. Ele será criado com base no formato de cheque fornecido pelo seu banco.


Exemplo de cheque:


![Sample Cheque](/files/sample-cheque.jpg)


## 1. Como criar um modelo de impressão de cheque


1. Vá para a lista Verificar modelo de impressão e clique em Novo.
2. Você pode definir a posição de vários itens no cheque.
3. Salve.


No Modelo de Impressão de Cheque, para cada valor (por exemplo, Beneficiário, Data), são fornecidas coordenadas exatas com base em onde esse valor deve ser impresso em um cheque. As coordenadas são fornecidas em centímetros. Aqui está uma representação da estrutura:


![Cheque de amostra](/files/cheque-1.png)


### 1.1 Novo formato por digitalização


Para acelerar a criação de um novo formato de impressão de cheque, você pode fazer o upload de uma imagem digitalizada do cheque. Considerando a imagem digitalizada do cheque, o sistema atualiza automaticamente as coordenadas para cada valor como nome da parte, valor, data, valor por extenso, etc.


### 1.2 Novo formato de impressão manualmente


Se a visualização parecer boa, clique no botão **Criar formato de impressão** para criar um novo formato de impressão para imprimir o cheque. Com base nos valores fornecidos no Modelo de Impressão de Cheque, o sistema irá gerar automaticamente um script HTML para o Formato de Impressão do cheque.


Você pode fornecer manualmente a coordenada para cada valor com base em onde deseja que seja impresso no cheque e personalizar com HTML/CSS.


#### Visualização


Com base nas coordenadas fornecidas para todos os valores, será mostrada uma prévia de como os valores serão impressos no cheque.


![Cheque de amostra](/files/cheque-2.png)


### 1.3 Cheques de impressão


O novo formato de impressão gerado para o cheque ficará visível no formulário de Entrada de Pagamento. Depois de criar a entrada de pagamento, você poderá imprimir os detalhes da transação no cheque.


![Cheque de amostra](/files/cheque-3.gif)


### 2. Tópicos Relacionados


1. [Modelo de endereço](/docs/v13/user/manual/en/setting-up/print/address-template)
2. [Modelo de termos e condições](/docs/v13/user/manual/en/setting-up/print/terms-and-conditions)