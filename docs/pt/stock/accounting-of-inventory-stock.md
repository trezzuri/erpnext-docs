# Contabilidade do estoque



O valor do estoque disponível é tratado como Ativo Atual no [Plano de
Contas](/docs/pt/accounts/chart-of-accounts). Para preparar um Balanço Patrimonial, você deve fazer os lançamentos contábeis desses ativos. Geralmente existem dois métodos diferentes de
contabilização do estoque.


## 1. Inventário automático/perpétuo


Neste processo, para cada transação de estoque, o sistema lança os valores relevantes
entradas contábeis para sincronizar o saldo do estoque e o saldo contábil. Isto é o
configuração padrão no ERPNext para novas contas. Por padrão, o inventário permanente está ativado na [Empresa](/docs/pt/setting-up/company-setup#23-stock-settings).


Quando você compra e recebe itens, esses itens são contabilizados como ativos da empresa
(estoque em mãos). Quando você vende e entrega esses itens, um
é contabilizada uma despesa (Custo dos Produtos Vendidos) igual ao custo final dos itens.
As entradas do Razão Geral são criadas após cada transação de estoque. Como resultado,
o valor conforme Stock Ledger permanece sempre o mesmo com a conta relevante
equilíbrio. Isso melhora a precisão do Balanço Patrimonial e dos Lucros e Perdas
declaração.


Leia a [documentação do Inventário Perpétuo](/docs/pt/stock/perpetual-inventory)
para verificar os lançamentos contábeis de uma transação de ações específica.


### 1.2 Vantagens do inventário perpétuo


O sistema de Inventário Perpétuo tornará mais fácil para você manter a precisão dos valores de ativos e despesas da empresa. Os saldos de estoque sempre serão sincronizados com os saldos de contas relevantes, portanto, nenhuma entrada manual periódica precisa ser feita para equilibrá-los.


No caso de novas transações de estoque com data retroativa ou cancelamento/alteração de uma transação existente, todos os lançamentos futuros no razão de estoque e lançamentos contábeis serão
ser recalculado para todos os itens dessa transação. O mesmo é aplicável se
qualquer custo é adicionado ao recibo de compra enviado posteriormente através do Landed
Comprovante de custo.



> 
> Observação: o estoque permanente depende completamente da taxa de avaliação do item.
>  Portanto, você deve ter mais cuidado ao inserir a taxa de avaliação ao fazer qualquer
>  transações de estoque de entrada, como recibo de compra, recebimento de material ou
>  Fabricação/Reembalagem.
> 
> 
> 



## 2. Inventário Periódico


Neste método, os lançamentos contábeis precisam ser criados manualmente para sincronizar o saldo do estoque e o saldo da conta relevante. O sistema não cria
lançamentos contábeis automaticamente para ativos no momento das compras de materiais
ou vendas.


Em um período contábil, quando você compra e recebe itens, uma despesa é contabilizada
em seu sistema contábil. Você vende e entrega alguns desses itens.


No final de um período contábil, o valor total dos itens a serem vendidos precisa
a serem registrados como ativos da empresa, geralmente conhecidos como estoque em mãos.


A diferença entre o valor dos itens restantes a serem vendidos e o
o valor do estoque em mãos do período anterior pode ser positivo ou negativo. Se
positivo, esse valor é retirado das despesas (Custo dos Produtos Vendidos) e é
adicionado ao ativo (estoque em mãos). Se negativo, uma entrada reversa
foi aprovado.


Esse processo completo é chamado de **Inventário Periódico**.


Se você já é um usuário que usa Inventário Periódico e deseja usar o Perpetual
Inventário, você precisa seguir [algumas etapas](/docs/pt/stock/articles/migrate-to-perpetual-inventory) para migrar.


### 3. Tópicos Relacionados


1. [Inventário permanente](/docs/pt/stock/perpetual-inventory)
2. [Migrar para o inventário permanente](/docs/pt/stock/articles/migrate-to-perpetual-inventory)



