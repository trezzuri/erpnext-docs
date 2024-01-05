# Dimensão do inventário




> Introduzido na versão 14
> 
> 

As dimensões de inventário no ERPNext são usadas para rastrear um inventário com múltiplos parâmetros. Por padrão, o ERPNext permite rastrear um inventário usando armazéns, lotes e números de série. Se os usuários quiserem rastrear o inventário com parâmetros personalizados, eles poderão configurá-lo usando o recurso Dimensão de inventário. O usuário tem a opção de selecionar a Dimensão do Estoque nos respectivos documentos de estoque, bem como no razão de estoque e no relatório de saldo de estoque. Com esse recurso, você pode visualizar o razão de estoque e relatórios de saldo de estoque por dimensão.

Para acessar a lista Dimensão de estoque, vá para:


> Estoque > Configurações > Dimensão de estoque 
> 
> 

## Criar dimensão de inventário

![nova dimensão de inventário](/files/new-inventory-dimension.png)![]()

* Crie um novo registro e selecione o documento de referência que deseja usar como dimensão de inventário personalizada.
* Você pode selecionar qualquer documento não secundário no documento de referência.
* Em seguida, o usuário deve colocar o nome da dimensão na qual o sistema criará um campo de link personalizado nos Documentos Aplicáveis.

## Aplicável a documentos

### Aplicar a todos os documentos de inventário

![dimensão de inventário aplicável a todos os documentos de inventário](/files/inventory-dimension-applicable-for-all-inventory-documents.png)![]()  


* Será usado para selecionar a dimensão personalizada nos documentos relacionados ao inventário.
* Por exemplo, o usuário criou a dimensão de inventário com o nome "Prateleira" e ativou "Aplicar a todos os tipos de documentos de inventário". Em seguida, o sistema criará o campo de link personalizado com o nome "Prateleira" nos documentos de inventário onde existem os campos Nº do lote e Nº de série.

### Aplicar ao documento específico

![dimensão de inventário aplicável para](/files/inventory-dimension-applicable-for.png)![]()  


* Se o usuário quiser adicionar a dimensão de inventário a um documento específico, ele terá que desabilitar a caixa de seleção "Aplicar a todos os tipos de documentos de inventário" e selecionar o respectivo documento no campo "Aplicável ao documento".
* Também se você deseja adicionar dimensão de inventário para uma condição específica, como para o tipo de entrada de estoque, você deseja uma dimensão separada como "Da prateleira" e o tipo de entrada de estoque Recebimento de material, você deseja uma dimensão separada como "Para a prateleira", então isso pode ser possível usando "Condição aplicável"
* A condição aplicável só pode ser visível se "Aplicar a todos os tipos de documentos de inventário" estiver desabilitado
* Você também pode usar o "Tipo de transação" com opções como Entrada ou Saída para uma condição.

## Uso da dimensão de estoque

![dimensão de estoque na transação](/files/inventory-dimension-on-transaction.png)![]()  


* Depois que a dimensão de inventário for criada, o sistema criará o campo personalizado nos respectivos documentos
* O usuário terá uma opção para selecionar a Dimensão de Estoque na respectiva transação.
* Por exemplo, se o usuário adicionou a Dimensão de Estoque como "Prateleira" no documento Detalhes de Entrada de Estoque. Então, na entrada de estoque, o usuário da tabela filho tem a opção de selecionar a prateleira (veja a imagem acima). Após o envio do sistema de entrada de estoque, serão criados os livros de estoque com as dimensões de estoque selecionadas.

## Validar estoque negativo

![](/files/fqvxY3m.png)![]()  


 Caso o usuário tenha habilitado a caixa de seleção "Validar Estoque Negativo" na dimensão de estoque, o sistema não permitirá realizar transações de estoque caso a respectiva dimensão possua estoque negativo no respectivo armazém. Se o usuário tentou criar a transação de estoque com estoque negativo para a dimensão de estoque, o sistema gerará o erro abaixo

  


![](/files/OKgkIqS.png)![]()  


## Relatório de saldo de estoque e razão de estoque

* Os usuários podem filtrar o relatório de saldo de estoque e razão de estoque usando a dimensão de estoque
* Com esse recurso, os usuários podem ver a quantidade disponível da dimensão do estoque

### Relatório de saldo de estoque

![saldo de estoque da dimensão de estoque](/files/inventory-dimension-stock-balance.png)![]()  


### Relatório de razão de estoque

![dimensão de estoque razão de estoque](/files/inventory-dimension-stock-ledger.png)![]()  
  


Observação:

O usuário só pode usar a reconciliação de estoque com dimensões de estoque para inserir valores de abertura e eles não podem usar a reconciliação de estoque para modificar o estoque disponível ou a avaliação. Como não estamos mantendo a taxa de avaliação sábia das dimensões do estoque, não faz sentido permitir a modificação da taxa de avaliação por meio da reconciliação de estoque. caso eles tentem atualizar a quantidade ou taxa de avaliação por meio da reconciliação de estoque, o sistema gerará o erro abaixo

  


![](/files/cTOHcyI.png)![]()  






