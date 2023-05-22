# Erro de importação devido ao fluxo de trabalho


Ao importar um documento de um DocType que possui um fluxo de trabalho, você não deve ser capaz de definir o workflow\_state para um estado exceto o primeiro.   
Por exemplo, seu fluxo de trabalho tem 4 estados: **Rascunho**, **Enviado para aprovação**,  **Aprovado**, **Rejeitado**.  
Você prepara registros para importar usando a ferramenta de importação de dados e define o workflow\_state de cada registre como **Aprovado**. O sistema não permitirá isso, pois você está passando do estado **Rascunho** para **Aprovado**, o que não é uma transição válida de acordo com seu fluxo de trabalho.< br/>A solução é desabilitar o workflow, importar seus dados e depois habilitar o workflow novamente.  
