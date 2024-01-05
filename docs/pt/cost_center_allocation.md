# Alocação de centro de custo



## Alocação de centro de custo


Alocação de centro de custo é um recurso que permite dividir o lançamento contábil em um centro de custo em vários centros de custo. No documento Alocação de Centro de Custo você pode definir percentuais de alocação dos centros de custo filhos.


Em um negócio em crescimento, torna-se necessário analisar as receitas/despesas de cada unidade de negócio da organização. E para isso, precisamos tratar cada unidade de negócio como um centro de custo e contabilizar receitas/despesas em relação ao centro de custo. Mas se precisarmos sempre dividi-lo manualmente no nível da transação, isso se tornará muito difícil. É aí que o recurso de Alocação de Centro de Custo vem em socorro.


No ERPNext, só precisamos definir a alocação entre múltiplos centros de custo (unidades de negócios) em relação a um centro de custo mestre/principal específico. Então, sempre que registramos uma fatura ou transação de despesa no centro de custo principal, o sistema a divide automaticamente com base na alocação e lança lançamentos contábeis em cada centro de custo filho.


### 1. Como criar uma Alocação de Centro de Custo?


1. Acesse a visualização de lista Alocação de centro de custo e crie uma nova Alocação de centro de custo.
2. Insira o **Centro de Custo Principal** que será utilizado na transação.
3. Insira **Válido de** e **Válido até** para rastrear a validade da alocação.
4. Na tabela secundária, insira os **centros de custo secundários e sua porcentagem**
5. Salve e envie o documento.


![Alocação do centro de custo](/files/cost-center-allocation5d3d2d.png)


### 2. Lançamentos contábeis contra transação


Ao reservar qualquer transação no centro de custo principal, o sistema divide automaticamente a entrada contábil e lança várias entradas contábeis com base no registro de alocação do centro de custo aplicável.



![Entrada GL baseada na alocação do centro de custo](/files/general-ledger-based-on-cost-center-allocation.png)
(As entradas contábeis de uma fatura de vendas foram divididas com base na alocação do centro de custo)




