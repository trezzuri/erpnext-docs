# Arredondar mensagem de validação de conta


**Pergunta**


Ao enviar uma fatura, por que ela pede uma Conta Redonda? Como atualizá-lo?


![Arredondar conta na fatura de compra](/files/round-off-message-in-purchase-invoice.png)


**Responder**


Na Fatura de Compra, o Total Geral é calculado com base em vários cálculos como:


* Qtd \* Taxa = Valor
* Impostos e outros encargos aplicados a cada item
*Desconto aplicado a alguns ou a todos os artigos
* Multiplicação com taxa de câmbio, no caso de várias moedas


Como resultado de vários cálculos, pode haver alguma perda de arredondamento no valor final. Esta perda de arredondamento é geralmente muito marginal como 0,034. Mas para o rigor contabilístico, tem de ser lançado nas contas. Portanto, você precisa definir uma conta de arredondamento padrão no mestre da empresa na qual o valor aproveitado como resultado de perda de arredondamento pode ser registrado.


Você precisa criar Conta Arredondada no Plano de Contas e atualizar no cadastro da Empresa. Passos aqui.


* Contas > Plano de contas
* No Plano de Contas, marque ou crie uma nova Conta em Despesas > Despesas Diretas. Ignorar se a conta para esta finalidade já existe
* Venha para o mestre da empresa
Conta > Empresa
* Empresa aberta em que a conta Round-Off deve ser atualizada.
* No mestre da Empresa, vá até Configurações de Contas e selecione Conta de Arredondamento e Centro de Custo.
![Arredondar conta na empresa](/files/round-off-account-in-company.png)


Depois que a conta de arredondamento for atualizada no mestre da empresa, tente enviar a fatura de compra novamente.