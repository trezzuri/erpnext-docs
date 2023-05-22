# Voucher de custo de importação


Para criar um **voucher Landed cost** no ERPNext: Você deve criá-lo contra um **Recibo de Compra** e  **Fatura de Compra.**   
Ao criar contra **Fatura de compra**: Na fatura de compra --> **Atualizar estoque** deve ser verificado.  
![](/files/z3sBK9F.png)  
 Se este campo estiver desmarcada, as Faturas de Compra não serão buscadas no Voucher de Despesas de Desembarque  
Ao criar contra **Recibo de Compra**: O Item selecionado deve marque **Manter estoque**.  
![](/files/vEwpm61.png)  
 Se este campo não estiver marcado, os Itens não serão exibidos quando você clicar em **Obter itens do Recibo de Compra.**   
Ao criar um Voucher de custo no destino, custos adicionais podem ser adicionados aos itens até que cheguem ao nosso Inventário.  
Essas cobranças adicionais, uma vez adicionadas, são adicionadas à **taxa de avaliação do item** e atualizam a taxa do item.  
< /div>Você pode rastrear esse efeito de cobrança adicional no razão contábil em **Recibo de compra --> Exibir --> Razão contábil**  
Se as cobranças adicionais tiverem que ser pagas com o Voucher de despesas de importação, você pode:1. Você pode criar uma **Entrada de pagamento** diretamente para concluir o pagamento das despesas adicionais do Item e, em seguida, crie uma **Fatura de compra** com **Está pago** marcado --> [Neste caso, a Fatura de compra não é obrigatória a menos que você queira que o efeito contábil seja visto. ]
2. Você pode criar uma **Fatura de Compra** para um **Fornecedor** para o qual as **Despesas Adicionais** são incorridos, desta forma você pode ver o efeito contábil para as despesas de acordo com o Voucher Landed Cost e, em seguida, criar uma entrada de Pagamento contra ele.

  
