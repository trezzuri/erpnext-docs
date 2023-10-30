# Configurações educacionais



**As Configurações de Educação permitirão que você faça uma configuração batica para o seu Instituto, onde você pode definir o Ano Acadêmico, o Período Acadêmico e outros padrões para sua conta ERPNext.**


Essas definições de configuração terão impacto em todo o módulo.


Para acessar o período acadêmico, acesse:



> 
> Página inicial > Educação > Configurações > Configurações educacionais
> 
> 
> 


## 1. Etapas para definir as configurações educacionais


1. Selecione o ano letivo atual. Este se tornará o ano letivo padrão em toda a sua conta.
2. Selecione o período acadêmico atual. Este se tornará o Período Acadêmico padrão em toda a sua conta.
3. Selecione a data de congelamento de participação. Qualquer participação capturada após a Data de Congelamento de Participação não será válida.
4. Selecione como deseja que os Registros do Instrutor sejam criados, usando Nome Completo, usando Série de Nomenclatura ou usando Número de Funcionário.
5. **Registro do Instrutor a ser criado por**: Você pode selecionar como deseja que os Registros do Instrutor sejam criados em seu sistema ERPNext, se deve ser por Nome Completo, por Série de Nomenclatura ou por Código do Funcionário.


![Configurações educacionais](/files/education-seetings-1.png)


### 1.1. Configurando Propriedades


* **Validar Lote para Alunos no Grupo de Alunos**: Ao adicionar alunos a um grupo de alunos via Lote, o sistema irá verificar se o aluno pertence ou não àquele lote, e se o mesmo não aconteceu, um erro será mostrado ao salvar o grupo de alunos.
* **Validar Lote de Alunos no Grupo de Alunos**: Ao adicionar alunos em um grupo de alunos via Curso, o sistema irá verificar se o aluno está matriculado naquele curso ou não, e se o mesmo não aconteceu , um erro será mostrado ao salvar o Grupo de Alunos.
* **Tornar o período acadêmico obrigatório**: quando ativada, esta opção garantirá que, ao criar uma inscrição no programa por meio do [Ferramenta de Inscrição no Programa](/docs/pt/education/program-matricula-tool), o usuário deverá informar o Período Acadêmico.
* **Ignorar criação de usuário para novo aluno**: sempre que um novo aluno é criado, por padrão, um usuário é criado para ele. Se esta opção estiver ativada, nenhum novo usuário será criado quando um novo aluno for criado.


### 1.2. Configurações do LMS


O módulo Educação vem com um Sistema de Gerenciamento de Aprendizagem (LMS) pronto para uso. Isso permite que os institutos publiquem seus programas em seus sites. Os programas podem conter artigos em rich text, vídeos e até questionários. O progresso de cada aluno pode ser acompanhado tanto na mesa quanto no portal.


Depois de habilitar o LMS para seu módulo ERPNext Education, as seguintes configurações estarão disponíveis para configuração:


1. **Título do LMS**: insira o título do seu LMS. Pode ser o nome do seu instituto.
2. **Descrição**: você pode adicionar a descrição do curso ao seu LMS.


![Configurações educacionais](/files/education-seetings-1.png)


Você também pode acessar [Atividade do LMS](/docs/pt/education/setting-up-lms) para adicionar cursos, artigos ou questionários ao seu LMS . Para acessar seu portal LMS, você pode acessar o URL {seunomedodomínio}.erpnext.com/lms



