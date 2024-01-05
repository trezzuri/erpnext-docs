# Voucher de custo final



Para criar um **voucher de custo final** no ERPNext: Você deve criá-lo em relação a um **Recibo de Compra** e uma **Fatura de Compra.**   
Ao criar com base na **Fatura de Compra**: Na Fatura de Compra--> **Atualizar Estoque** deve ser verificado.  
![](/files/z3sBK9F.png)  
 Se este campo estiver desmarcado, as faturas de compra não serão buscadas no comprovante de custo final  
Ao criar com base no **Recibo de compra**: o item selecionado deve marque **Manter estoque**.  
![](/files/vEwpm61.png)  
 Se este campo não estiver marcado, os Itens não serão exibidos quando você clicar em **Obter itens do Recibo de Compra.**   
Ao criar um voucher de custo no destino, custos adicionais podem ser adicionados para os itens até que eles cheguem ao nosso inventário.  
Essas cobranças adicionais, uma vez adicionadas, são adicionadas à **taxa de avaliação do item** e atualizam a taxa do item.  
Você pode rastrear esse efeito de cobrança adicional no razão contábil em **Recibo de compra--> Visualizar--> Razão contábil**  
Se os encargos adicionais precisarem ser pagos com base no Voucher de custo final, você pode:1. Você pode criar uma **Entrada de pagamento** diretamente para concluir o pagamento de despesas adicionais do Item e então criar uma **Fatura de Compra** com **Está Pago** marcado--> [Neste caso, a Fatura de Compra não é obrigatória a menos que você queira que o efeito contábil seja visto. ]
2. Você pode criar uma **Fatura de Compra** para um **Fornecedor** para o qual as **Despesas Adicionais** são incorridos, desta forma você pode ver o efeito contábil das despesas de acordo com o comprovante de despesas no destino e, em seguida, criar um lançamento de pagamento contra ele.

  


