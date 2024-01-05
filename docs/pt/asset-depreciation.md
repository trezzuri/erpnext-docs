# Depreciação de ativos



O sistema cria automaticamente um cronograma de depreciação com base no `Método de depreciação`, `Número total de depreciações`, etc., e outras entradas relacionadas, como `Disponível para usar a data` no registro do ativo. Também é possível criar vários cronogramas de depreciação para diferentes livros financeiros. Você precisa marcar a caixa de seleção `Calcular Depreciação` ao criar um ativo se quiser que o sistema crie o cronograma de depreciação.

![Asset](/files/depreciation-schedule.png)![]()

## Diferentes métodos de depreciação no ERPNext:

* **Linha reta**: Neste método, o valor de um ativo é reduzido uniformemente ao longo de sua vida útil até atingir seu valor residual. Por exemplo: se o ativo valer 1.000 e seu valor residual for 500 após 5 anos, o método linear depreciaria o ativo em 100 a cada mês/ano. Este método é útil quando não existe um padrão específico de como a depreciação ocorre durante um período de tempo. Você pode usar a opção `Depreciar com base na proporção diária` se desejar que o valor da depreciação varie dependendo do número de dias em um período de calendário. Você pode usar a opção `Depreciar com base em turnos` para definir o número de turnos que o ativo executaria em um período para depreciá-lo adequadamente. Você precisa primeiro definir os nomes dos turnos com seus fatores de deslocamento no tipo de documento `Asset Shift Factor` (por exemplo: "half": 0,5, "single": 1, "double": 1,5 e "triple" : 2) e defina um padrão. Posteriormente, se você quiser alterar os turnos de um ativo para um determinado período, poderá fazê-lo usando o [Alocação de turnos de ativos](https://docs.erpnext.com/docs/user/manual/en/asset-shift-allocation ) e os turnos restantes são ajustados automaticamente.
* **Declínio duplo Saldo**: também é conhecido como saldo decrescente de 200%. Este método é útil quando o ativo se deprecia rapidamente no início e desacelera mais tarde. Por exemplo: se o ativo vale 1.00.000 e seu valor residual é 11.000 após 8 anos, o cronograma de depreciação seria:



| Valor atual | Depreciação | Valor reservado |
| --- | --- | --- |
| 1.00.000,00 | 25.000,00 | 75.000,00 |
| 75.000,00 | 18.750,00 | 56.250,00 |
| 56.250,00 | 14.063,00 | 42.187,50 |
| 42.187,50 |  10.547,00 | 31.640,62 |
| 31.640,62 | 7.910,00 | 23.730,46 |
| 23.730,46 | 5.933,00 | 17.797,84 |
| 17.797,84 | 4.449,00 13.348,38 | |
| 13.348,38 | 2.348,00 | 11.000,00 |
* **Valor anotado**: Em Com esse método, você pode definir uma `taxa de depreciação` específica ou deixar o sistema calcular a `taxa de depreciação` com base no valor de compra do ativo, valor residual e vida útil. A `taxa de depreciação` é aplicada ao valor atual anotado do ativo para calcular o valor da depreciação para cada ano. Este método é útil para ativos que apresentam maior depreciação nos anos iniciais. Por exemplo: se o valor de compra do ativo for 1.000 e a `taxa de depreciação` for 10% ao longo de 5 anos, o cronograma de depreciação seria:



|  Valor Atual | Depreciação | Valor reservado |
| --- | --- | --- |
| 1.000,00 | 100,00 | 900,00 |
| 900,00 | 90,00 | 810,00 |
| 810,00 | 81,00 | 729,00 |
| 729,00 | 72,90 | 656,10 |
| 656,10 | 65,61 | 590,49 |
* **Manual**: Neste método, primeiro um cronograma de depreciação gerado pelo sistema seria criado para sua conveniência com base nos detalhes de depreciação definidos, e você pode então editar as datas do cronograma e os valores de depreciação manualmente para qualquer período de acordo com suas necessidades.

## Lançamentos automáticos de depreciação

Você pode ativar o registro de lançamento de depreciação automaticamente em [Configurações de contas](/docs/pt/contas/configurações de contas). Isso criará lançamentos de depreciação automaticamente nas datas programadas. Caso contrário, você terá que criar o lançamento contábil manualmente clicando no botão "Fazer lançamento de depreciação" na linha correspondente do Cronograma de depreciação.

![Asset](/files/depreciation-entry.png)![]()  


## Lançamentos contábeis sobre depreciação

No lançamento de depreciação:

* "Conta de depreciação acumulada" é creditada e
* "Conta de Despesas de Depreciação" é debitada.

As contas relacionadas podem ser definidas na Categoria de Ativos ou Empresa.

## Gráfico de valores de ativos

Para melhor compreensão, o valor líquido do ativo em diferentes datas de depreciação é mostrado em um gráfico de linhas.

![Asset](/files/asset-submit.png)![]()  


## Tópicos relacionados

1. [Manutenção de ativos](/docs/pt/asset/asset-maintenance)
2. [Ajuste do valor do ativo](/docs/pt/asset/asset-value-adjustment)
3. [Descarte de um ativo](/docs/pt/asset/scrapping-an-asset)


