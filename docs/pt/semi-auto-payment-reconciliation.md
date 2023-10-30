# Reconciliação de pagamento semiautomática



Se houver um grande número de faturas que precisam ser reconciliadas rapidamente sem alocação manual, o tipo de documento `Processar reconciliação de pagamento` pode ser usado.


## Etapas:


1. Primeiro, esse recurso deve ser ativado nas configurações de contas. Ative `Reconciliação automática de pagamentos` nas configurações da conta. ![Screenshot 2023 04 21 às 19h45min58](/files/Screenshot 2023/04/21 às 19h45min58.png)
2. Navegue até `Processar reconciliação de pagamento` doctype
3. Selecione Empresa, Parte e Conta a Receber/Pagar para a qual a Reconciliação deve ser feita. Salvar e enviar
4. O documento terá o status `Em fila`. ![Screenshot 2023 04 21 às 19h14.42](/files/Screenshot 2023-04-21 às 19h14.42.png)
5. Um trabalho em segundo plano executado a cada 15 minutos coletará documentos `enfileirados` e iniciará a reconciliação. Se necessário, o trabalho pode ser acionado imediatamente usando o botão `Iniciar/Continuar`.
6. Isso criará um registro `Processar registro de reconciliação de pagamento` com detalhes sobre o número total de alocações que serão processadas e as entradas reconciliadas com êxito. ![Screenshot 2023 04 21 às 19h54.12](/files/Screenshot 2023-04-21 às 19h54.12.png)


## Tópicos Relacionados


1. [Reconciliação de pagamentos](/docs/pt/accounts/payment-reconciliation)



