# Regra de gratuidade



> Este recurso foi introduzido na versão 13, que fará parte de um módulo de folha de pagamento separado.


**Regras de gratificação são um conjunto de regras definidas pela Central ou Estado usadas durante o cálculo do valor da gratificação**


No Frappe HR, você pode definir diferentes regras de gorjeta com base em diferentes regiões.


Para acessar a Regra de Gratificação, acesse:


> Página inicial > Folha de pagamento > Regra de gratificação


## 1. Pré-requisitos


Antes de criar uma regra de gorjeta, é aconselhável criar o seguinte:


1. [Funcionário](/docs/pt/human-resources/employee)
2. [Componente salarial](/docs/pt/human-resources/salary-component)


## 2. Como criar regra de gratuidade


1. Regra de gratificação > Nova
2. Selecione Componentes Aplicáveis. Esses componentes salariais contribuem durante o cálculo da gratificação.
3. Selecione "Calcular o valor da gratificação com base em"
4. Definir regra de gratificação
5. Salvar


![Regra de gratuidade](/files/gratuity-rule.png)


## 3. Propriedades Adicionais


Alguns dos atributos adicionais usados ​​durante o cálculo da gorjeta são definidos abaixo.


### 3.1 Método de cálculo de experiência profissional:


O Frappe HR fornece dois métodos diferentes para cálculo da experiência profissional.


1. Método de conclusão da experiência profissional Complete sua experiência atual. Por exemplo, se o funcionário tiver experiência total de 3 anos e 6 meses, será tratado como experiência de 4 anos.
2. Pegue o ano completo exato.


### 3.2 Calcular o valor da gratificação com base em:


Vamos considerar o exemplo a seguir para entender o cálculo.


![gratuity-rule-example](/files/gratuity-rule-example.png)


1. **Laje Atual:** Se o cálculo do Valor da Gratificação for baseado na Laje Atual, o valor será o produto da Experiência Profissional (em anos), Fração de Rendimentos Aplicáveis ​​e somatório dos Componentes de Rendimentos Aplicáveis. Com base nas Regras/laje de Gratificação acima, se o funcionário tiver experiência de 5 anos, ele cai na terceira laje. O cálculo do Valor da Gratificação será o seguinte:


> Valor da gratificação = 5 \* 0,467 \* (Atrasado + Batico)


2. **Soma de todas as lajes anteriores:** Se o cálculo do valor da gratificação for baseado na soma de todas as lajes anteriores, o valor será a soma do produto de lajes individuais até o ano de experiência e a soma dos Aplicáveis Componente de ganhos. Com base nas Regras/placa de gratificação acima, se um funcionário tiver uma experiência de 5 anos, o cálculo do valor da gratificação será o seguinte:


> Valor da gorjeta = [(1 \* 0) + (2 \* 0,233) + (2 \* 0,467)]\*(Atrasado + Batico)



