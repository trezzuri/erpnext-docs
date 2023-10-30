# Custo da lista técnica em moeda diferente



O usuário pode alterar a moeda na BOM *antes* de enviar. O sistema calcula o custo com base na moeda da Lista de Preços. Você pode verificar o custo de fabricação em uma moeda específica alterando a moeda na lista técnica.


Considere que você importa plattico como matéria-prima do Japão e as faturas de vendas estão na moeda iene. A moeda da sua empresa é INR, mas você deseja que o custo da lista técnica seja feito em ienes. Ao definir 'Taxa de materiais com base em' para 'Lista de preços', as matérias-primas utilizadas na lista técnica também terão taxas definidas em ienes. Essas taxas são obtidas na Lista de Preços que você cria para o Japão. Neste caso, trata-se de uma Lista de Preços de compra denominada 'Importar Japão'.


![BOM em moeda diferente](/files/bom-currency.png)


Se você selecionar 'Taxa de materiais com base em' para 'Taxa de avaliação' ou 'Taxa de última compra', os preços serão obtidos do cadastro de itens ou da fatura de vendas, respectivamente. No caso do item mestre, você precisará inserir a taxa de avaliação na **sua** moeda. Na BOM, a Taxa de avaliação será convertida para a moeda definida na BOM.


![BOM em moeda diferente](/files/bom-currency-1.png)



