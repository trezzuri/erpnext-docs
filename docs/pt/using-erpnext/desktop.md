# Área de Trabalho


**No momento em que um usuário fizer login no sistema, ele poderá ver uma tela inicial na qual todos os módulos e domínios serão listados na forma de cartões.**


Seus cartões são um substituto para os antigos ícones do Módulo que estavam presentes nas versões do ERPNext antes da versão 12.


![Nova área de trabalho](/files/desktop.png)


Estes cartões podem ser classificados em quatro categorias, a saber:


* **Módulos**: São todos os módulos agnósticos de domínio disponíveis no ERPNext que são comuns a todos os tipos de negócios. Módulos como Recursos Humanos, CRM, Compras, Vendas, etc. são colocados nesta categoria.
* **Domínios**: Aqui você encontra todos os módulos específicos do domínio, como Educação e Manufatura. Você pode aprender mais sobre todos os módulos específicos do setor [aqui](/docs/v13/user/manual/en#3-industry-specific-modules).
* **Places**: Places é onde você pode encontrar recursos que não são específicos do setor e não são necessários nas operações diárias de sua empresa. Recursos como Site, Painéis e Marketplace podem ser encontrados aqui.
* **Administração**: Aqui você encontra os módulos relacionados à configuração e administração do seu ERPNext.


Esses cartões permitem uma melhor navegação com itens de atalho no menu suspenso. Você pode personalizar este menu suspenso para adicionar ou remover links para vários DocType desse módulo.


![Desktop-dropdown](/files/desktop-dropdown.png)


Você pode reordenar, bem como mostrar ou ocultar esses cartões de módulo.


![Arrastar e soltar](/files/drag-and-drop.gif)


## Página do módulo


Clicar em qualquer cartão de módulo o levará à página do módulo. Aqui o usuário pode navegar por todos os tipos de documento, relatórios e configurações associadas a um determinado módulo.


Por exemplo, aqui está a aparência da página do módulo Contabilidade.


![Módulo de contas](/files/accounts-module-page.png)


### Navegando na página


Alguns links desses módulos podem estar marcados em cinza, clicar nesses links não abrirá nenhuma nova página. Eles são marcados assim porque há um documento dependente que precisa ser criado primeiro. Por exemplo, você precisará criar uma Nota Fiscal de Venda antes de acessar o registro de vendas. Passar o mouse sobre qualquer um desses links mostrará um pop-up orientando o usuário para o documento dependente.


![Link silenciado na página do módulo](/files/module-link-hover.png)


Você também notará um indicador colorido antes de alguns dos links. Esses indicadores são usados ​​para informar ao usuário se algum documento aberto ou urgente precisa ser consultado.


![Indicadores de cores](/files/color-indicator.png)


* O indicador **vermelho** no exemplo acima indica que há tarefas em aberto ou atrasadas na lista.
* Da mesma forma, um indicador **azul** significaria que não há tarefas abertas.
* Um indicador **laranja** significa que o relatório não foi acessado ou nenhum documento foi criado no tipo de documento correspondente.