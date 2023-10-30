# Pacote serial e em lote



> Introduzido na versão 15


Na versão 15, introduzimos o pacote serial e em lote. Este recurso será usado para vincular números de série/lote nas transações de estoque.


Antes da versão 15, o campo Serial No era um campo Small Text. O que significava que uma coluna continha mais de um número de série. Por causa desse design, houve muitos problemas de integridade de dados. Então, para resolver isso, alteramos o campo Serial No de Small Text para Link na versão 15. Como não podemos adicionar uma tabela filho dentro de uma tabela filho, adicionamos um novo tipo de documento "Serial and Batch Bundle" para selecionar/despachar vários números de série/lote.


![pacote serial e em lote](/files/serial-and-batch-bundle.png)


## Como isso funciona?


Você precisa que um pacote de série e lote seja criado e vinculado a transações de estoque sempre que precisar lidar com números de série/lote. O usuário precisa criar um "pacote serial e em lote" separado para cada transação e não pode vincular o mesmo "pacote serial e em lote" a várias transações. 


### Criação automática de pacote serial e em lote para entrada interna


Se o usuário quiser criar um "Pacote de Série e Lote" automático para a entrada interna, ele deverá certificar-se de que 'Série de Número de Série' foi definida para o item Item de Série e a caixa de seleção 'Criar Novo Lote Automaticamente' com 'Série de número de lote' definida para o item de lote.


#### Para número de série


![Serial sem configuração](/files/auto-serial-creation.png)


#### Para lote nº


![Lote sem configuração](/files/auto-batch-creation.png)


Após a configuração quando o usuário cria o Recibo de Compra ou Entrada de Estoque com o Tipo "Recebimento de Material", o sistema criará o "Pacote de Série e Lote" para entrada automaticamente no envio do registro.


![Pacote de lote serial automático para dentro](/files/auto-create-serial-batch-for-inward.gif)


### Criação automática de pacote serial e em lote para entrada externa


Se o usuário quiser criar um "pacote serial e em lote" automático para a entrada externa, ele deverá ativar a caixa de seleção "Criar automaticamente pacote serial e em lote para saída" nas configurações de estoque. O usuário também pode definir "Selecionar serial/lote com base em" como "FIFO/LIFO/Expiração" nas configurações de estoque.


![Configuração externa do pacote de lote serial automático](/files/auto-outward-configuration.png)


Após a configuração quando o usuário cria a Nota de Remessa ou Entrada de Estoque com o Tipo "Emissão de Material", o sistema criará o "Pacote de Série e Lote" para saída automaticamente no envio do registro.


![Pacote de lote serial automático para fora](/files/auto-create-serial-batch-for-outward.gif)


### Criação manual de pacote serial e em lote para entrada interna


Para o "Pacote Serial e Lote", tanto serial/lote não precisa estar presente primeiro no sistema. Assim, com a opção manual o usuário deve primeiro criar os números de série/lote no sistema. O usuário deve usar a opção de importação de CSV para fazer números de série/lote. O modelo CSV em branco pode ser baixado usando o seletor de série e lote.


![Configuração interna do pacote de lote serial manual](/files/create-using-csv.png)


O GIF completo para criação manual de pacote serial e em lote para entrada interna é o seguinte


![Pacote de lote serial manual para dentro](/files/manually-create-serial-no-inward.gif)


### Criação manual de pacote serial e em lote para entrada externa


Usando o Seletor de Série e Lote, o usuário pode escolher os Números de Série/Lote com base no método "FIFO/LIFO/Expiração".


![Configuração externa manual do pacote de lote serial](/files/serial-batch-selector-outward.png)


O GIF completo para criação manual de pacote serial e em lote para entrada externa é o seguinte


![Pacote de lote serial manual para fora](/files/manually-create-serial-no-outtward.gif)


## Histórico de números de série


Para verificar o histórico dos números de série, consulte o relatório "Serial No Ledger"


![Serial No Ledger](/files/serial-no-ledger-report.png)



