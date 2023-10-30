# Série de nomes de empresas



Suponha que você tenha uma configuração multiempresa e precise criar séries de nomenclatura diferentes para documentos pertencentes a empresas diferentes. Por exemplo, você tem três empresas:* Empresa A
* Empresa B
* Empresa C

A A necessidade é criar séries de nomenclatura específicas da empresa para documentos como Nota Fiscal de Venda, Pedido de Compra, etc. Por exemplo, no caso de Nota Fiscal de Venda, para a Empresa A, a série de nomenclatura será SINV-A-0001 e para a Empresa B , a série de nomenclatura será SINV-B-0001. Isso pode ser facilmente alcançado por meio da personalização seguindo as etapas abaixo:  
1) Primeiro, vá até o DocType para o qual deseja diferentes séries com base na empresa e abra seu Formulário Personalizado. Neste caso, selecionaremos o tipo de fatura de vendas.  
2) Em seguida, abaixo do campo Empresa, adicione outro campo e nomeie-o como 'Abbr'. Adicione `company.abbr` na entrada Fetch From.  
![](/files/3mLkrQs.png)  
Além disso, kmantenha este campo oculto (se necessário).  
![](/files/w6DS7FY.png)  
  
3) Agora, no próprio formulário personalizado, vá para a linha Naming Series e expanda-a. Na caixa Opções, adicione outra entrada em uma nova linha (tomando a fatura de vendas como exemplo) `SINV-.abbr.-.####` e defina-o como padrão.  
![](/files/WAE0FQA.png)   
  
![](/files/2GJ5YLM.png)  
  
Uma vez feito isso, clique em Atualizar.  
Agora, vá para Fatura de Venda e crie um. Selecione a Empresa e a Série de Nomenclatura será atualizada automaticamente com base na abreviatura da empresa.  
![](/files/PrEgDa7.png)

