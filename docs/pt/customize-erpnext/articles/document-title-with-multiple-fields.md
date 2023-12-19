# Título do documento com vários campos



Já pensou em criar um título de documento com mais de um campo? Por exemplo, digamos que sua fatura de venda deva ter o título do nome do cliente (que está presente por padrão) e seu ID fiscal.


Como você fará isso? Bem, aqui está uma capacidade interessante de customização do framework que pode fazer isso sem a necessidade de scripts.


Aqui estão as etapas,


1. Certifique-se de ter um campo que será referenciado para criar o título do documento.
2. A configuração básica termina adicionando este nome de campo nas configurações de visualização do tipo de documento para o título.
3. Se você quiser adicionar mais,
4. Adicione os links de campo no **padrão** do campo neste formato **{field\_name}**


***Aqui está um exemplo de como fica***


![](/files/Eb81KLe.png)


         b. Isso resultará em um título multicampo para o tipo de documento selecionado.


Isso pode ser estendido para criar um campo personalizado com valores consolidados de diferentes campos e mesclá-los em um campo completamente novo. O melhor caso de uso é criar endereços para tipos de documentos personalizados facilmente, sem nenhum script personalizado.


Esta é a aparência da configuração do campo


![](/files/FXuN3dK.png)


Observação: estamos usando opções para adicionar valores porque isso atualiza o campo alterando seus campos de origem. (Funciona com padrões)


Além disso, o tipo de campo não deve ser dados. (Pode ser somente leitura ou HTML)


Aqui está o resultado da configuração acima


![](/files/gHpmXZY.png)



