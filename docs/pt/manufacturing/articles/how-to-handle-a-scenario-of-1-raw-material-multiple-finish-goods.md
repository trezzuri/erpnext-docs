# Vários produtos acabados com uma única matéria-prima



Em muitas indústrias de manufatura lidam com um cenário em que usam uma RM (matéria-prima) e produzem vários produtos finais. Na maioria das indústrias de fabricação de produtos químicos você pode encontrar esse caso de uso de negócios. Agora, como você pode mapear esse caso de uso no ERPNext? Vejamos um exemplo da indústria petrolífera, onde a partir do petróleo bruto são produzidos vários produtos, como gasolina, gás, diesel, querosene, etc.  
* Primeiro crie um Mestre de itens onde o petróleo bruto será RM e gasolina, gás, diesel, querosene etc. será o seu FG. Aqui cada produto também pode ter uma UOM diferente.

  
* Após a criação do item mestre, crie uma BOM para qualquer um dos FG que você estiver indo para produzir a partir de petróleo bruto (RM). Aqui criei BOM de Gasolina para 25 litros onde vou utilizar Petróleo Bruto (RM) de quantidade. 100 litros. Resto do FG, como Gás, Diesel e Querosene, adicionei na seção Sucata.

  
  
 ![](/files/1VHaiPf.png)  
![](/files/mg68Dbr.png)   
* Ao criar uma lista técnica, você também pode adicionar operações e executar seu ciclo de produção (ordem de serviço) de acordo.

  
* Após a conclusão da ordem de serviço no momento da entrada de backflush, sua matéria-prima será consumida e você terá vários produtos acabados.




