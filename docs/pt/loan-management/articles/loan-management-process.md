# Processo de gerenciamento de empréstimos



**ERPNext fornece o recurso de gerenciamento de empréstimos para gerenciar empréstimos concedidos pela empresa aos funcionários**.  
O sistema de gerenciamento de empréstimos no ERPNext Envolve vários passos a seguir:  
1. Para isso, primeiro você precisa criar o tipo de empréstimo onde deverá preencher os campos obrigatórios, ou seja, Nome do Empréstimo, Taxa de juros (%) Anual. Aqui você também pode definir o valor máximo do empréstimo e a descrição, se houver.  
  
![](/files/kVkSATB.gif)  
2. Feito isso, o Funcionário pode solicitar um empréstimo. Para solicitar um empréstimo, preencha Tipo de solicitante, Solicitante, Tipo de empréstimo, Valor do empréstimo e Método de reembolso.  
  
 ![](/files/B6hlWnR.gif)  
  
3. Agora, o Aprovador de Empréstimo precisa criar um Empréstimo para o respectivo aplicativo de Empréstimo. Ele/ela deve preencher Data de Início do Reembolso, Forma de Pagamento, Conta de Pagamento, Conta de Empréstimo, Conta de Receita de Juros e alguns campos obrigatórios. Inicialmente, o status do empréstimo é sancionado. Há uma caixa de seleção 'Reembolsar do salário' que oferece ao funcionário a opção de reembolsar o valor do empréstimo com seu salário.  
  
![](/files/P5g11nV.gif)  
Após enviar o documento, ele cria o Cronograma de Reembolso do Empréstimo conforme mostrado abaixo:   
![](/files/wDPuhRR.png)  
 4. Agora, você precisa criar a Entrada de Desembolso. Ao clicar no botão 'Criar entrada de desembolso; no canto superior direito do Documento de Empréstimo. Isso cria um lançamento contábil manual para desembolso do empréstimo.  
![](/files/xoPxquv.gif)

