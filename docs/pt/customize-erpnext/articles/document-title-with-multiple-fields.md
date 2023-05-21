# Título do documento com vários campos


Já pensou em criar um título de documento com mais de um campo? Por exemplo, digamos que sua fatura de venda deva ter o título do nome do cliente (que está presente por padrão) e seu ID fiscal.


Como você vai fazer isso? Bem, aqui está uma capacidade interessante de customização do framework que pode fazer isso sem a necessidade de scripts.


Aqui estão os passos,


1. Certifique-se de ter um campo que será referenciado para a criação do título do documento.
2. A configuração básica termina adicionando este nome de campo nas configurações de visualização do doctype para o título.
3. Se você quiser adicionar mais,
4. Adicione os links de campo no **padrão** do campo neste formato **{field\_name}**


***Aqui está um exemplo de como fica***


![](/files/Eb81KLe.png)


b. Isso resultará em um título de vários campos para o tipo de documento selecionado.


Isso pode ser estendido para criar um campo personalizado com valores consolidados de diferentes campos e mesclá-los em um campo completamente novo. O melhor caso de uso é criar endereços para doctypes personalizados facilmente, sem nenhum script personalizado.


É assim que a configuração do campo ficará


![](/files/FXuN3dK.png)


Nota: Estamos usando opções para adicionar valores porque atualiza o campo alterando seus campos de origem. (Não funciona com padrões)


Além disso, o tipo de campo não deve ser de dados. (Pode ser somente leitura ou HTML)


Aqui está a saída da configuração acima


![](/files/gHpmXZY.png)