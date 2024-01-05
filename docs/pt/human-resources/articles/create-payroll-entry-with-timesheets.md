# Criar entrada de folha de pagamento com planilhas de horas



**Caso de uso:** As horas extras de um funcionário são registradas usando planilhas de horas, e o funcionário precisa ser compensado pelas mesmas durante a folha de pagamento, além de seu salário normal.  
 **Etapas:**1) Criar um funcionário.  
2) Criar um componente salarial denominado "Horas extras" do tipo Ganhos.  
![](/files/IKY5KnC.png)   
3) Crie uma Estrutura Salarial e inclua “Horas extras” com valor definido como 0.  
4) No Estrutura salarial em si, marque a caixa de seleção "Recibo de salário com base no quadro de horários", selecione Componente salarial como "Horas extras" e insira a taxa horária.  
![](/files/RSBGOUP.png)  
5) Envie a estrutura salarial e atribua esta estrutura salarial a um funcionário por meio da atribuição de estrutura salarial.  
![](/files/qj9KVAu.png)  
6) Criar Quadros de horários para este funcionário por meio do DocType do quadro de horários.  
![](/files/xtdKq6i.png)![](/files/W7vYYWt.png)  
No exemplo mostrado acima, o Funcionário trabalhou horas extras por um total de 8 horas no mês de janeiro.  
7) Crie um novo lançamento de folha de pagamento para o mês de janeiro e selecione "Recibo de salário com base no quadro de horários" caixa de seleção. Salvar. Clique no botão "Obter funcionários". Em seguida, clique em "Criar recibos de salário".  
O recibo de salário do funcionário irá buscar todas as planilhas de horas (se houver) desse funcionário criadas para aquele determinado mês e calcule o componente de horas extras no recibo de salário de acordo.  
![](/files/oZ1rr5x.png)![](/files/1QoJVGc.png)  


