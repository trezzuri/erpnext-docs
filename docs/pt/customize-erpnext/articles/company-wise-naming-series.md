# Série de nomes da empresa


Suponha que você tenha uma configuração multiempresarial e precise criar diferentes séries de nomenclatura para documentos pertencentes a diferentes empresas. Por exemplo, você tem três empresas:* Empresa A
* Empresa B
* Empresa C

A necessidade é criar séries de nomenclatura específicas da empresa para documentos como Nota Fiscal, Pedido de Compra, etc. Por exemplo, no caso de Nota Fiscal de Venda, para Empresa A, a série de nomenclatura será SINV-A-0001 e para Empresa B, a série de nomenclatura será SINV-B-0001. Isso pode ser facilmente alcançado por meio da personalização, seguindo as etapas abaixo:
1) Primeiro, vá para o DocType para o qual você deseja séries diferentes com base na empresa e abra seu Formulário Personalizado. Nesse caso, selecionaremos o tipo como fatura de venda.
2) A seguir, abaixo do campo Empresa, adicione outro campo e nomeie-o 'Abbr'. Adicione `company.abbr` em sua entrada Fetch From.
![](/files/3mLkrQs.png)
Além disso, mantenha esse campo oculto (se necessário).
![](/files/w6DS7FY.png)
  
3) Agora, no próprio Formulário Personalizar, vá até a linha Naming Series e expanda-a. Na caixa Opções, adicione outra entrada na nova linha (tendo como exemplo a Nota Fiscal de Venda) `SINV-.abbr.-.####` e defina isso como padrão.
![](/files/WAE0FQA.png)
  
![](/files/2GJ5YLM.png)
  
Feito isso, clique em Atualizar.
Agora, vá para Fatura de Vendas e crie uma. Selecione a empresa e a série de nomes será atualizada automaticamente com base na abreviatura da empresa.
![](/files/PrEgDa7.png)