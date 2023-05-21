# Voucher de custo de importação


Para criar um **voucher de custo de importação** no ERPNext: Você deve criá-lo contra um **recibo de compra** e uma **fatura de compra**.
Ao criar contra **Fatura de compra**: Na Fatura de compra --> **Atualizar estoque** deve ser verificado.
![](/files/z3sBK9F.png)
 Se este campo estiver desmarcado, as Notas Fiscais de Compra não serão buscadas no Comprovante Landed Cost
Ao criar contra **Recibo de compra**: O item selecionado deve ter **Manter estoque** marcado.
![](/files/vEwpm61.png)
 Se este campo não estiver marcado, os Itens não serão exibidos quando você clicar em **Obter itens do recibo de compra.**
Ao criar um Voucher de custo no destino, custos adicionais podem ser adicionados aos itens até que cheguem ao nosso Inventário.
Essas cobranças adicionais, uma vez adicionadas, são adicionadas à **Taxa de avaliação do item** e atualizam a Taxa do item.
Você pode rastrear esse efeito de cobrança adicional no razão contábil em **Recibo de compra --> Exibir --> Razão contábil**
Se as taxas adicionais tiverem que ser pagas contra o Voucher de despesas de importação, você pode:1. Você pode criar uma **Entrada de Pagamento** diretamente para concluir o pagamento das despesas adicionais do Item e, em seguida, criar uma **Fatura de Compra** com **Está Pago** marcado --> [Neste caso, a Fatura de Compra é não obrigatório, a menos que você queira que o efeito contábil seja visto. ]
2. Você pode criar uma **Fatura de Compra** para um **Fornecedor** para o qual as **Despesas Adicionais** são incorridas, desta forma você pode ver o efeito Contábil das despesas de acordo com o Voucher de Despesas de Destino, então criar uma entrada de pagamento contra ele.