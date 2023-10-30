# Inspeção de qualidade



No ERPNext, você pode marcar seus produtos recebidos ou enviados para Inspeção de Qualidade.

Para acessar esse recurso vá em: > Home > Estoque > Ferramentas > Inspeção de Qualidade

## 1. Pré-requisitos

Antes de criar e usar uma Inspeção de Qualidade, é aconselhável que você faça primeiro o seguinte:

* **Crie um** [**Item**](/docs/pt/stock/item).
* **Ativar critérios de inspeção de qualidade no mestre de itens**. Ao ativar qualquer uma das caixas de seleção, o **envio** de um documento de entrega/recebimento de estoque será permitido somente após uma Inspeção de Qualidade ser realizada: ![Ativar Inspeção de Qualidade](/files/quality-inspection-pre-requisite.png)![]()
* (Opcional) **Crie um modelo de inspeção de qualidade**. Você pode adicionar parâmetros de inspeção e critérios de aceitação no modelo, que podem ser facilmente obtidos em qualquer Inspeção de Qualidade. Depois de salvar o modelo, você pode configurá-lo no Item Master (conforme mostrado acima). ![Modelo de inspeção de qualidade](/files/quality-inspection-template.png)![]()

## 2. Como criar uma nova Inspeção de Qualidade

1. A partir de um **Rascunho** de Recibo de Compra/Subcontratação ou Nota de Entrega, acesse o campo Inspeção de Qualidade da tabela Item e clique em Criar uma nova inspeção de qualidade. Você também pode criar uma Inspeção de Qualidade para Cartão de Trabalho para monitorar a qualidade dos itens em processo. Neste caso, você pode criar uma Inspeção de Qualidade para o Item de Produção no Cartão de Trabalho.
2. Selecione o tipo de inspeção: Entrada (Compra), Saída (Vendas) ou Em Processo (Fabricação).
3. Selecione o tipo de documento de referência, seja Recibo de compra, Fatura de compra, Nota de entrega, Fatura de venda, Entrada de estoque ou Cartão de trabalho.
4. Selecione o Item e defina o tamanho da amostra que será inspecionada. Observe que apenas os itens com critérios de inspeção habilitados no cadastro de itens serão buscados.
5. O modelo de inspeção de qualidade definido no cadastro de itens será buscado.
6. Você pode alterar quem é inspecionado e também adicionar quem é verificado.
7. Qualquer observação adicional sobre a inspeção pode ser adicionada.

- Salvar. Defina o status. Enviar.

![Inspeção de qualidade](/files/quality-inspection-1.png)![]()  


## 3. Recursos

Uma única inspeção de qualidade consiste em muitas verificações de qualidade (parâmetros) dentro dela. Cada uma dessas verificações pode ser [Numérica](#31-numeric-quality-checks), [Não numérico](#32-non-numeric-value-based-quality-checks) ou [Baseado em fórmulas](#33-formula-based-quality-checks).

### 3.1 Verificações de qualidade numérica

As verificações de qualidade numéricas incluem todas as verificações que exigem leituras baseadas em números e critérios de aceitação. 

Ex. verificar se uma leitura está em um determinado intervalo.

Por padrão, as verificações são numéricas. Existem dois campos: **Valor Mínimo** e **Valor Máximo**, para definir um intervalo em que **cada** leitura deve estar. Esses campos podem ser definidos no campo Modelo de inspeção de qualidade uma vez e simplesmente obtido na inspeção de qualidade.

![Verificação de qualidade numérica](/files/quality-inspection-numeric-reading.png)![]()  


Se alguma das leituras inseridos não estão dentro deste intervalo, o status na linha será definido como 'Rejeitado' automaticamente ao salvar.

### 3.2 Verificações de qualidade não numéricas (baseadas em valor)

Não-numéricas (baseadas em valor)Não-numéricas (baseadas em valor) As verificações de qualidade numéricas incluem verificações que exigem valores alfabéticos ou aquelas que não exigem cálculos matemáticos.

Por exemplo, verificar se a cor é branca em uma verificação de qualidade de cor, valores Sim/Não para determinados parâmetros, etc.

Para verificações não numéricas, ative a caixa de seleção 'Não numérico'. Você notará que o campo **Valor dos Critérios de Aceitação** e a seção **Inspeção Baseada em Valor** estão visíveis.

Insira o campo Valor de Leitura. O valor dos critérios de aceitação pode ser definido no modelo de inspeção de qualidade uma vez e depois obtido na inspeção de qualidade.

![Verificação de qualidade não numérica](/files/quality-inspection-non-numeric-reading.png)![]()  
Se o valor de leitura não corresponder ao valor dos critérios de aceitação, o status na linha será definido como 'Rejeitado' automaticamente ao salvar.

### 3.3 Verificações de qualidade baseadas em fórmulas

As verificações de qualidade baseadas em fórmulas são úteis para cenários mais complexos onde apenas especificar um intervalo ou um valor de aceitação não é suficiente.

Por exemplo: verificar se o grau de um material é A/B/C, verificar se a média de algumas leituras está dentro de um determinado intervalo, etc.

As verificações de qualidade baseadas em fórmulas são aplicáveis ​​à qualidade numérica e não numérica Verificações.

Ative a caixa de seleção 'Critérios Baseados em Fórmula' para realizar uma Verificação de Qualidade Baseada em Fórmula. Você notará então um campo chamado **Fórmula de critérios de aceitação** onde você pode especificar uma fórmula que determina se um determinado cheque é aceito ou rejeitado. Esta fórmula pode ser definida uma vez no modelo de inspeção de qualidade e depois ser buscada na inspeção de qualidade.

![Fórmula de critérios de aceitação](/files/acceptance-criteria-formula.png)![]()  


 Esta fórmula depende dos vários campos de leitura na tabela Leituras.

Para leituras numéricas, `reading_1`, `reading_2` e assim por diante são aceitos na fórmula. 

Para leituras não numéricas, apenas `reading_value` é aceito na fórmula.

Aqui estão alguns exemplos de fórmulas:


```
# Numérico
(leitura_1 + leitura_2) &lt; 10 # soma de ambas as leituras é menor que 10
(leitura_1 + leitura_2) &lt;= 10 # soma de ambas as leituras é menor ou igual a 10
significa &lt; 15 # média de leituras numéricas não vazias é menor que 15
(leitura_1 * 2) &lt; 20 # Ler 1 multiplicado por 2 é menor que 20
(leitura_1)/2 &lt; 20 # Ler 1 dividido por 2 é menor que 20

# Não numérico
valor_leitura em ("A", "B", " C") # O valor de leitura é A/B/C
reading_value != "Vermelho" # O valor de leitura não é igual ao vermelho
  

```
Atualize as leituras e salve. O campo Status nas linhas da tabela Leituras é definido automaticamente com base na fórmula de aceitação.

### 3.3 Inspeção manual

Até agora, todas as verificações de qualidade têm aceitação/rejeição automática ao salvar. No mundo real, pode haver casos em que um cheque é rejeitado, mas ainda assim será aceito porque há alguma tolerância.

Esses casos exigirão que o usuário determine o status no nível da linha. Para evitar qualquer interferência do sistema nessas verificações, ative a caixa de seleção “Inspeção Manual”. Agora você pode definir o status manualmente e ele permanecerá intacto ao salvar.

![Inspeção manual](/files/quality-inspection-manual-reading.png)![]()  


Aqui a leitura 1 é fora do intervalo definido, esta verificação seria rejeitada. Mas, como não está muito longe de 0,153, nós o aceitamos manualmente.

O status de toda a Inspeção de Qualidade pode então ser decidido pelo usuário.

## 4. Vídeo

### 5. Tópicos relacionados

1. [Recibo de compra](/docs/pt/stock/purchase-receipt)
2. [Nota de entrega](/docs/pt/stock/delivery-note)
3. [Entrada de estoque](/docs/pt/stock/stock-entry)
4. [Fatura de vendas](/docs/pt/accounts/sales-fatura)
5. [Fatura de compra](/docs/pt/accounts/purchase-invoice)
6. [Cartão de trabalho](/docs/pt/manufacturing/job-card)






