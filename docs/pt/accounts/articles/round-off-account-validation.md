# Mensagem final de validação da conta



**Pergunta**


Ao enviar uma fatura, por que ela solicita uma conta de arredondamento? Como atualizá-lo?


![Arredondar conta na fatura de compra](/files/round-off-message-in-purchase-invoice.png)


**Responder**


Na fatura de compra, o total geral é calculado com base em vários cálculos, como:


* Quantidade \* Taxa = Valor
* Impostos e outros encargos aplicados a cada item
* Desconto aplicado a alguns ou todos os itens
* Multiplicação com taxa de câmbio, no caso de múltiplas moedas


Como resultado de vários cálculos, pode haver alguma perda de arredondamento no valor final. Esta perda de arredondamento é geralmente muito marginal, como 0,034. Mas para a exatidão contábil, tem que ser lançado nas contas. Portanto, é necessário definir uma conta de arredondamento padrão no cadastro da empresa na qual o valor aproveitado em decorrência da perda de arredondamento possa ser contabilizado.


Você precisa criar uma conta de arredondamento no plano de contas e atualizar no cadastro da empresa. Etapas aqui.


* Contas > Plano de contas
* No Plano de Conta, marque ou crie uma nova Conta em Despesa > Despesa Direta. Ignorar se a conta para esta finalidade já existir
* Venha para o mestre da empresa
Conta > Empresa
* Empresa aberta na qual a conta Round-Off deve ser atualizada.
* No cadastro da empresa, vá até Configurações de contas e selecione Conta de arredondamento e centro de custo.
![Arredondar conta na empresa](/files/round-off-account-in-company.png)


Depois que a conta de arredondamento for atualizada no cadastro da empresa, tente enviar a fatura de compra novamente.



