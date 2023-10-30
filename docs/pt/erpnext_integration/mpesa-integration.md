# Integração M-Pesa



**A integração M-Pesa permite o processamento de transações com o provedor de gateway de pagamento M-Pesa.**


A integração M-Pesa facilita o processamento de pagamentos entre a aplicação M-Pesa e o ERPNext. A Integração M-Pesa só funciona com o POS para facilitar os pagamentos do mesmo. Este recurso não funciona com o carrinho de compras.


Para configurar o M-Pesa, acesse:
> Integrações > Pagamentos > Configurações M-Pesa


## 1.Como obter suas credenciais M-Pesa?


1. Para ativar suas credenciais API, você precisa fazer login na sua conta M-Pesa.
2. Em seguida, abra a seção Go Live do aplicativo e siga as etapas para obter a aprovação do aplicativo.
3. Quando todos os casos de teste forem satisfeitos e os resultados esperados corresponderem aos resultados finais, você precisará enviar o documento e seguir as etapas para obter as credenciais finais para sua aplicação.
4. Os detalhes mencionados na seção URL de produção e credenciais são as credenciais que você deve usar nas configurações do M-Pesa.


![Credenciais Mpesa](/files/mpesa_credentials.png)


## 2.Configurando o M-Pesa


Para ativar o M-Pesa Express, você precisa configurar todos os parâmetros obrigatórios que recebeu do M-Pesa. Se quiser usar o ambiente de teste da integração, você pode selecionar a opção de teste e usar as credenciais de teste fornecidas pela M-Pesa criando um aplicativo separado para o mesmo.
![Configurações Mpesa](/files/mpesa_settings.png)


Ao habilitar a integração M-Pesa no ERPNext, o sistema criará um registro de Gateway de Pagamento e um cabeçalho de Conta no Plano de Contas com o tipo de Conta como Banco, conforme visto na imagem a seguir.


![Mpesa COA](/files/mpesa_coa.png)
![Configurações de PDV Mpesa](/files/mpesa_pos_settings.png)


Ele também criará um modo de pagamento com o mesmo nome e conta do gateway de pagamento, junto com determinados campos personalizados nas configurações do PDV para lidar com os pagamentos do PDV.


![Conta de gateway de pagamento](/files/payment_gateway_account_mpesa.png)


Depois de configurar a conta do gateway de pagamento, você poderá aceitar pagamentos online via M-Pesa.


## 3. Pagamentos POS M-Pesa


Ao configurar o perfil POS com modo de pagamento M-Pesa, o checkout do POS mostraria uma seção de informações adicionais. Esta seção contém dois campos que foram configurados automaticamente ao adicionar configurações do M-Pesa.


![Informações adicionais de PDV](/files/additional-information.png)


Assim que um usuário do PDV preencher o número do celular do cliente, ele poderá iniciar uma solicitação de pagamento do cliente. Uma solicitação é enviada ao aplicativo móvel M-Pesa do cliente vinculado ao número de celular especificado. Assim que o pagamento for processado pelo usuário, ele receberá uma caixa de diálogo de confirmação para enviar o pagamento.


## 4. Saldo da conta M-Pesa


O saldo da conta vinculado a um M-Pesa individual pode ser obtido através do botão Obter Saldo da Conta. Isso carregará os detalhes do saldo da conta M-Pesa no painel.


![Saldo da conta PDV](/files/mpesa_account_balance.png)


## 5. Suporte a moedas de transação


M-Pesa só funcionará para a Empresa que tenha KSH (Xelim Queniano) como moeda da Empresa.



