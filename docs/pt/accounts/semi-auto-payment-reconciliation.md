# Reconciliação de pagamento semi-automática


Se houver um grande número de faturas que precisam ser reconciliadas rapidamente sem alocação manual, o tipo de documento 'Process Payment Reconciliation' pode ser usado.


## Passos:


1. Primeiro, esse recurso deve ser ativado por meio da configuração de contas. Habilite `Reconciliar pagamentos automaticamente` nas configurações de contas. ![Captura de tela 2023 21/04 às 19h45/58](/private/files/Captura de tela 21/04/2023 às 19h45/58.png)
2. Navegue até o tipo de documento "Process Payment Reconciliation"
3. Selecione Empresa, Parte e Conta a Receber/Pagar para a qual a Conciliação deve ser feita. Guardar e submeter
4. O documento terá o status 'Queued'. ![Captura de tela 2023 21/04 às 19h14/1942](/private/files/Captura de tela 21/04/2023 às 14/07/42.png)
5. Uma tarefa em segundo plano executada a cada 15 minutos selecionará os documentos `Queued` e iniciará a reconciliação. Se necessário, o trabalho pode ser acionado imediatamente usando o botão 'Iniciar / Continuar'.
6. Isso criará um registro 'Process Payment Reconciliation Log' com detalhes sobre o número total de alocações que serão processadas e as entradas reconciliadas com sucesso. ![Captura de tela 2023 21/04 às 19h54/12](/private/files/Captura de tela 21/04/2023 às 19h54/12.png)


## Tópicos relacionados


1. [Reconciliação de pagamento](/docs/v14/user/manual/en/accounts/payment-reconciliation)