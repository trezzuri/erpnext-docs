# Série de nomes da empresa


Suponha que você tenha uma configuração multiempresarial e precise criar diferentes séries de nomenclatura para documentos pertencentes a diferentes empresas. Por exemplo, você tem três empresas:* Empresa A
* Empresa B
* Empresa C

A A necessidade é criar uma série de nomenclatura específica da empresa para documentos como Nota Fiscal de Venda, Pedido de Compra, etc. Por exemplo, no caso de Nota Fiscal de Venda, para a Empresa A, a série de nomenclatura será SINV-A-0001 e para a Empresa B , a série de nomenclatura será SINV-B-0001. Isso pode ser facilmente obtido por meio da personalização seguindo as etapas abaixo:  
1) Primeiro, vá até o DocType para o qual você deseja séries diferentes com base na empresa e abra seu Formulário Personalizado. Nesse caso, selecionaremos o tipo como fatura de venda.  
2) Em seguida, abaixo do campo Empresa, adicione outro campo e nomeie-o 'Abbr'. Adicione `empresa.abbr` em sua entrada Fetch From.  
![](/files/3mLkrQs.png)  
Além disso, kmantenha este campo oculto (se necessário).  
![](/files/w6DS7FY.png)  
  
3) Agora, no próprio Custom Form, vá até a linha Naming Series e expanda-a. Na caixa Opções, adicione outra entrada na nova linha (tomando a Fatura de venda como exemplo) `SINV-.abbr.-.####` e defina como padrão.  
![](/files/WAE0FQA.png)   
  
![](/files/2GJ5YLM.png)  
  
Feito isso, clique em Atualizar.  
Agora vá em Nota Fiscal de Venda e crie um. Selecione a empresa e a série de nomes será atualizada automaticamente com base na abreviatura da empresa.  
![](/files/PrEgDa7.png)< /div>