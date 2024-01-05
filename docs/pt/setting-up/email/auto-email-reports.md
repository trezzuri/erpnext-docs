# Relatórios automáticos por e-mail



**O Auto Email Reports envia automaticamente relatórios para o documento selecionado.**


Você pode configurar o **Relatório automático por e-mail** para enviar relatórios em intervalos regulares. Devem ser relatórios salvos de qualquer tipo (Report Builder, Script ou Query Report).


Você pode encontrar o Relatório automático por e-mail em:


> Página inicial > Configurações > Relatório automático por e-mail


## 1. Como criar um relatório automático por e-mail


1. Vá para a lista Relatório automático por e-mail e clique em Novo.
2. Selecione o relatório para o qual deseja gerar e-mails.
3. Selecione o usuário para o qual você deseja criar este relatório (as permissões serão aplicadas a este usuário).
4. Defina os endereços de e-mail para os quais você deseja que este relatório seja enviado por e-mail e a frequência do relatório. Os e-mails serão enviados à meia-noite. A data será repetida em caso de frequência semanal/mensal/anual. Por exemplo, se a data selecionada for 7 e a frequência for mensal, o e-mail será enviado no dia 7 de cada mês.


![Com filtros](/files/auto-email-2.png)
5. Salvar.


Você pode testar o relatório clicando em "Baixar" ou "Enviar agora". Aqui está um exemplo do e-mail que você receberá para um relatório de contabilidade:


![Relatório por e-mail](/files/auto-email-4.png)


## 2. Recursos


### 2.1 Filtrar dados


* **Enviar apenas se houver dados**: se ativado, os e-mails não serão enviados se não houver dados no relatório.
* **Enviar apenas registros atualizados nas últimas X horas**: se definido como 24, um e-mail conterá apenas registros atualizados nas últimas 24 horas.
* **Nº de linhas**: O número de linhas a serem enviadas no email. O máximo é 500.


### 2.2 Filtros de relatório


Se o seu relatório tiver filtros, você poderá vê-los. Clique na tabela para editá-la:


![Editar filtros](/files/auto-email-3.png)


Por exemplo, se o e-mail estiver no relatório 'Resumo do faturamento do projeto', selecione o Projeto. O período aqui é o período do 'Resumo do faturamento do projeto'.


### 2.3 Mensagem


Uma mensagem também pode ser adicionada para ser enviada com o relatório por e-mail. Por exemplo, 'Este é o seu relatório mensal de resumo do faturamento do projeto:'


Você também pode alterar o formato do arquivo no qual o relatório é criado. As opções disponíveis são HTML, XLSX e CSV.


### 2. Tópicos Relacionados


1. [Resumo por e-mail](/docs/pt/setting-up/email/email-digest)
2. [Acompanhamento de documento](/docs/pt/setting-up/email/document-follow)



