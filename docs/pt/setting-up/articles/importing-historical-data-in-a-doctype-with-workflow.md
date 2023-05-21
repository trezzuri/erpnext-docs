# Erro de importação devido ao fluxo de trabalho


Quando você importa um documento de um DocType que possui um fluxo de trabalho, você não deve ser capaz de definir workflow\_state para um estado exceto o primeiro.
Por exemplo, seu fluxo de trabalho tem 4 estados: **Rascunho**, **Enviado para aprovação**, **Aprovado**, **Rejeitado**.
Você prepara os registros para importação usando a Ferramenta de importação de dados e define o fluxo de trabalho\_estado de cada registro como **Aprovado**. O sistema não permitirá isso, pois você está passando do estado **Rascunho** para **Aprovado**, o que não é uma transição válida de acordo com seu fluxo de trabalho.
A solução é desabilitar o fluxo de trabalho, importar seus dados e habilitar o fluxo de trabalho novamente.