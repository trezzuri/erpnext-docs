# Componente salarial



**Os salários são pagos pelas organizações aos seus funcionários em troca dos serviços por eles prestados. Os diferentes componentes que compõem a Estrutura Salarial são chamados de Componentes Salariais.**


O salário pago aos funcionários é composto por diversos componentes diferentes, como salário base, abonos, atrasos, etc. O Frappe HR permite definir esses Componentes Salariais e também especificar seus diversos atributos.


Para acessar o Componente Salarial, acesse:
> Home > Recursos Humanos > Folha de Pagamento > Componente Salarial


## 1. Como criar um componente salarial


Para criar um novo componente salarial:


1. Vá para a lista de componentes salariais e clique em Novo.
2. Insira o nome e a abreviatura.
3. Insira a descrição do componente salarial (opcional).
4. Insira o nome da empresa e a conta padrão do componente salarial na tabela Contas.
5. Salvar.


![Componente salarial](/files/salary-component1.png)


## 2. Recursos


Além dos campos obrigatórios mencionados acima, alguns dos recursos adicionais do Componente Salarial são fornecidos abaixo:


### 2.1 Condição e Fórmula


Nesta seção podem ser especificadas a Condição e a Fórmula necessárias para o cálculo da Componente Salarial. Para especificar a fórmula, ative a caixa de seleção "Valor baseado na fórmula".


![Componente salarial](/files/salary-component2.png)


Caso o Componente Salarial seja baseado em um valor pré-definido, o Frappe HR permite inserir o valor diretamente no campo Valor (desativar a caixa de seleção 'Valor com base na fórmula').


Você também pode usar algumas funções matemáticas/de data ao escrever fórmulas.



```
# Considere um componente `basic` com valor 1220,32 como exemplo:

# int-lança o valor como int
int(batico) # avalia como 1220

# flt-lança o valor como flt
flt(batico, 1) # avalia como 1220,3

# round-arredonda o valor
round(batico) # avalia como 1220

# ceil-arredonda o número para o número inteiro mais próximo
ceil(batico) # avalia como 1221

# floor-arredonda o número para o número inteiro mais próximo
floor(batico) # avalia como 1220

# getdate/date-converte o valor `start_date` em um objeto `datetime.date`
# por exemplo: o imposto profissional é de 300 em fevereiro e 200 em meses alternados. `start_date` ocupa o valor da `start_date` do comprovante de salário
# Nesse caso, a condição pode ser escrita conforme abaixo:

300 se getdate(data_inicial).mês == 2 senão 200

```

> **Nota:** Esta configuração acima é opcional. Você também pode definir o valor e a fórmula/condição para um componente salarial diretamente na estrutura salarial. Caso estejam especificados no próprio documento do Componente Salarial, as informações serão buscadas diretamente na Estrutura Salarial quando o Componente for selecionado.


### 2.2 Propriedades Adicionais


Alguns dos atributos adicionais do componente Salário que podem ser ativados usando caixas de seleção são os seguintes:


* **É pagável:** selecione esta opção se o componente salarial for pagável.
* **Depende dos dias de pagamento:** Se esta caixa de seleção estiver marcada, o componente salarial será calculado com base no número de dias úteis.
* **Os impostos são aplicáveis:** Esta caixa de seleção é aplicável a componentes de ganhos. Marcar esta caixa de seleção permite que o imposto seja aplicado sobre este componente salarial.
* **Deduzir Imposto Integral na Data Selecionada da Folha de Pagamento:** Se marcado e o componente for usado em Salário Adicional, o valor do imposto aplicável sobre o valor adicional será deduzido no mês específico da folha de pagamento. Caso não seja assinalado, o imposto será distribuído pelos meses restantes do período consignado. Por exemplo, se um bônus for concedido em um determinado mês usando Salário Adicional, você poderá deduzir o valor total do imposto somente no mesmo mês.
* **Arredondar para o número inteiro mais próximo:** marcar esta caixa de seleção permite arredondar o valor deste componente salarial para o número inteiro mais próximo.
* **Componente Estatístico:** Se selecionado, o valor especificado ou calculado neste componente não contribuirá para os rendimentos ou deduções. Porém, seu valor pode ser referenciado por outros componentes que podem ser somados ou deduzidos. Se você definir um Componente Salarial como um componente Estatístico, não será necessário definir a Conta Padrão para o mesmo. Além disso, você não poderá definir esse componente como um benefício flexível.
* **Não incluir no total:** marcar esta caixa de seleção garante que o componente salário não seja incluído no salário total. É usado para definir o componente que faz parte do CTC mas não é pagável (por exemplo, Uso de Carros da Empresa).
* **Variável com base no salário tributável:** o componente é calculado automaticamente sobre o lucro tributável com base na tabela de imposto de renda aplicável (por exemplo, TDS ou imposto de renda).
* **Isento de Imposto de Renda:** Se marcado, o valor total será deduzido do lucro tributável antes do cálculo do imposto de renda sem qualquer [declaração](/docs/pt/human-resources/employee-tax-exemption-declaration) ou [prova submissão](/docs/pt/human-resources/employee-tax-exemption-proof-submission). Por exemplo, o imposto profissional na Índia é deduzido do lucro tributável antes do cálculo do imposto de renda.
* **Desativado:** Esta caixa de seleção pode ser selecionada para desativar este Componente Salarial. Um componente salarial desabilitado não pode ser usado na estrutura salarial.


### 2.3 Benefícios flexíveis


Esta seção é mostrada se o Componente Salarial for um Componente de Remuneração. Os planos de benefícios flexíveis permitem que os funcionários aproveitem os benefícios que desejam ou precisam de um pacote de programas oferecido por um empregador. Eles podem incluir seguro saúde, planos de pensão, despesas telefônicas, etc. Para definir um Componente Salarial como Benefício Flexível, marque a caixa de seleção 'É Benefício Flexível'.


![Benefício flexível](/files/flexible-ben.png)


Insira o valor anual máximo para este benefício flexível no campo 'Valor máximo do benefício (anual)'. Alguns dos atributos adicionais dos Benefícios Flexíveis que podem ser ativados usando caixas de seleção são os seguintes:


* **Reivindicação de pagamento contra benefício:** marque esta caixa de seleção se quiser pagar esse benefício por meio do [Reivindicação de benefício de funcionário](/docs/pt/human-resources/employee-benefit-claim).
* **Somente impacto fiscal (não pode ser reivindicado, mas parte do lucro tributável):** Se definido, o benefício flexível fará parte do lucro tributável.
* **Criar entrada de pagamento separada para solicitação de benefício:** Se esta caixa de seleção estiver marcada, você poderá criar uma entrada de pagamento separada para solicitação de benefício.


## 3. Tópicos Relacionados


1. [Estrutura salarial](/docs/pt/human-resources/salary-structure)
2. [Atribuição de estrutura salarial](/docs/pt/human-resources/salary-structure-assignment)
3. [Lançamento da folha de pagamento](/docs/pt/human-resources/payroll-entry)
4. [Período da folha de pagamento](/docs/pt/human-resources/payroll-period)



