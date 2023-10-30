# Relatório de rentabilidade do projeto



O Relatório de Rentabilidade do Projeto mostra a Rentabilidade e a Utilização de cada funcionário com base nos Quadros de Horários gerados.


Para visualizar este relatório, você pode acessar:


> Home > Projetos > Relatórios > Rentabilidade do Projeto


Este relatório mostra a Rentabilidade do Projeto com os seguintes dados:


* Quadro de horas
* Comprovante de salário gerado através do quadro de horários
* Fatura de vendas gerada usando o quadro de horários


![](/files/profitability-report.gif)


### Cálculo da utilização


A utilização do funcionário é calculada usando o total de horas faturadas do quadro de horários, os dias úteis do comprovante de salário e o horário de trabalho padrão das configurações de RH.


A fórmula para Utilização é a seguinte,



```
Utilização = Total de Horas Faturadas/(Dias Úteis * Horário de Trabalho Padrão)

```

### Cálculo do lucro


O lucro é calculado usando o pagamento bruto do comprovante de salário, o total geral da fatura de vendas e a utilização.


A fórmula do lucro é a seguinte,



```
Lucro = Total Geral-Salário Bruto * Utilização

```

### Cálculo do custo fracionário


O custo fracionário é calculado usando o pagamento bruto do comprovante de salário e utilização.


A fórmula para Custo Fracionário é a seguinte,



```
Custo fracionário = Salário bruto * Utilização

```


