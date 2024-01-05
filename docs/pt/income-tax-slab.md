# Laje de Imposto de Renda



**A Placa de Imposto de Renda é um documento que define as alíquotas do imposto de renda com base nas diferentes placas de rendimento tributável.**


Em muitos países, o imposto sobre o rendimento é cobrado dos contribuintes individuais com base num sistema de lajes onde diferentes taxas de imposto foram prescritas para diferentes lajes e tais taxas de imposto continuam a aumentar com o aumento da laje de rendimentos. No Frappe HR, você pode definir várias placas de imposto de renda e vinculá-las à estrutura salarial individual do funcionário por meio da atribuição de estrutura salarial.


Para acessar a Placa do Imposto de Renda, acesse:
> Home > Recursos Humanos > Folha de Pagamento > Placa de Imposto de Renda


## 1. Como criar uma Laje de Imposto de Renda


Para criar uma nova tabela de imposto de renda:


1. Insira um nome para a placa de TI, empresa e a data a partir da qual ela entrará em vigor.
2. Ative a caixa de seleção "Permitir isenção de impostos", se aplicável.
3. Salvar e enviar.


## 2. Recursos


### 2.1 Placas fiscais


Na tabela Tax Slab, você pode definir a alíquota para diferentes faixas de renda. Para definir a laje, deve-se inserir From Amount e To Amount. Para a primeira laje, From Amount é opcional e para a última laje, To Amount é opcional. Ambos os valores são inclusivos na avaliação do imposto com base no lucro tributável.


![Income Tax Slab](/files/income-tax-slab.png)


A tabela tributária pode ser aplicável com base em condições específicas. As condições podem ser escritas usando todos os nomes de campo dos documentos Funcionário, Estrutura Salarial, Atribuição de Estrutura Salarial e Comprovante de Salário.


Exemplos:



```
//Aplicar imposto se funcionário nascido entre 31-12-1937 e 01-01-1958 (Colaboradores com idade entre 60 e 80 anos)
data_de_nascimento> data(1937, 12, 31) e data_de_nascimento < data(1958, 01, 01)

//Aplicar imposto por sexo do funcionário
gênero == "Masculino"

//Aplica imposto por componente salarial
básico> 10.000

//O lucro tributável anual é superior a 5 lakhs
ganho_tributável_anual > 500.000

```

### 2.2 Outros impostos e taxas sobre o imposto de renda


Se outros impostos forem aplicáveis ​​ao imposto de renda calculado, você poderá inseri-los usando esta tabela. Você também pode definir o valor tributável mínimo e máximo ao qual este imposto será aplicável.
Por exemplo, a Taxa de Saúde e Educação é aplicada adicionalmente ao imposto de renda para todos na Índia.


![Outros Cobrados sobre Imposto de Renda](/files/other-taxes-on-income-tax.png)


### 2.3 Outras propriedades


* **Permitir isenções fiscais:** isenções fiscais podem ser permitidas para uma tabela de imposto de renda específica. Se ativado, ao calcular os impostos com base nesta tabela fiscal, a Declaração de Isenção de Imposto do Funcionário e o Envio de Comprovante serão considerados para o cálculo do lucro tributável.
* **Valor Padrão de Isenção de Imposto:** Se a isenção for permitida, o Valor Padrão de Isenção de Imposto definido pelo governo pode ser adicionado aqui. Esta isenção geralmente não necessita de qualquer tipo de comprovação documental e é aplicável a todos os funcionários vinculados a esta laje de imposto de renda.


## 3. Tópicos Relacionados


1. [Componente salarial](/docs/pt/human-resources/salary-component)
2. [Estrutura salarial](/docs/pt/human-resources/salary-structure)
3. [Atribuição de estrutura salarial](/docs/pt/human-resources/salary-structure-assignment)
4. [Lançamento da folha de pagamento](/docs/pt/human-resources/payroll-entry)
5. [Declaração de isenção fiscal do funcionário](/docs/pt/human-resources/employee-tax-exemption-declaration)
6. [Envio de comprovante de isenção fiscal de funcionário](/docs/pt/human-resources/employee-tax-exemption-proof-submission)



