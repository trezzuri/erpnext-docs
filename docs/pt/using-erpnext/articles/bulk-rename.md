# Renomear em massa


Usando a ferramenta Bulk Rename, você pode optar por retificar/alterar vários IDs de documentos de uma só vez. Esta ferramenta só é acessível ao usuário que tem a função de gerente do sistema atribuída.


### Ferramenta de renomeação


Você pode renomear IDs de até 500 registros por vez. A seguir estão as etapas para renomear registros em massa. Vamos supor que estamos renomeando IDs de funcionários para os funcionários existentes.


#### Passo 1: Abra o Arquivo Excel


Em um arquivo de planilha, insira IDs de funcionários antigos na primeira coluna, IDs de novos funcionários na segunda coluna e se esse registro deve ser mesclado com um existente (falso por padrão). Salve o arquivo de planilha em um formato CSV sem o cabeçalho.




| Nome antigo | Novo nome | Mesclar |
| --- | --- | --- |
| HR-EMP-00001 | EMP0001 | FALSO |
| HR-EMP-00002 | EMP0002 | FALSO |
| HR-EMP-00003 | EMP0003 | FALSO |
| HR-EMP-00004 | EMP0004 | FALSO |
| HR-EMP-00005 | EMP0005 | FALSO |
| HR-EMP-00006 | EMP0006 | FALSO |


#### Etapa 2: Carregar Arquivo de Dados


Para carregar o arquivo de dados, vá para,



>
> Configurações > Dados > Renomear em massa
>
>
>


Selecione DocType que você deseja renomear. Aqui, DocType será Item. Em seguida, navegue e carregue o arquivo de dados.


![Dados de upload](/files/using-bulk-rename-2.gif)