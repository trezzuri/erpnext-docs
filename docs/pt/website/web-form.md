# Formulários da Web



As partes interessadas que não fazem parte da sua organização podem precisar interagir com
sua instância do ERPNext. Você pode autorizar clientes, fornecedores, candidatos a empregos,
alunos e responsáveis ​​acessem determinadas informações ou até mesmo criem determinados
transações. Por exemplo, você pode permitir que qualquer pessoa crie uma conta no seu site
(criado com ERPNext) e candidatar-se a um emprego. Você pode permitir que seus clientes vejam o
detalhes das reclamações que registraram. Isso pode ser feito usando Web Forms.


> Existem dois tipos de interfaces integradas disponíveis no ERPNext. O
> *Visualização de mesa* e *Visualização da Web*. Desk é para usuários que interagem regularmente
> com instância ERPNext, como funcionários da sua organização.


> Web View é para usuários que precisam interagir ocasionalmente com uma instância do ERPNext.
> Os formulários da Web são semelhantes aos formulários que você geralmente preenche em vários sites da Web.
>internet. Webforms fazem parte da interface *Web View* no ERPNext.


Para criar um novo **Formulário Web** vá para:


> Página inicial > Site > Site > Formulário da Web


![Novo formulário web](/files/new-web-form-1.png)
*Novo formulário da web*


Selecione o **DocType** com base no qual você deseja construir seu formulário web. O
A **Rota** será definida com base no **Título** do seu Formulário Web. Você também pode adicionar
um texto de introdução para mostrar uma mensagem amigável acima do seu formulário.


Adicione campos ao seu formulário web. Estes são os campos do DocType que você possui
selecionado. Você pode alterar o rótulo desses campos. Tente manter o número de
os campos devem ser mínimos, pois formulários longos são complicados de preencher.


![Campos de formulário da Web](/files/new-web-form-2.png)
*Campos do formulário da Web*


Clique em **Ver no site** na barra lateral para visualizar seu formulário da web.
![Formulário Web](/files/web-form.png)
*Formulário Web*


Aqui está uma explicação de cada uma das caixas de seleção à direita.


1. **Publicado**: o formulário da Web só estará acessível se estiver ativado.
2. **Login obrigatório**: O usuário só poderá preencher o formulário da Web se estiver logado.
Quando Login obrigatório estiver marcado,
3. **Link do Caminho para o Sucesso**: acesse o Link do Sucesso depois que o formulário for enviado.
4. **Permitir edição**: se esta opção estiver desmarcada, o formulário se tornará somente leitura quando for
salvo.
5. **Permitir múltiplos**: permite que o usuário crie mais de um registro.
6. **Mostrar como grade**: mostra registros em formato de tabela.
7. **Permitir exclusão**: permite que o usuário exclua os registros que possui
criado.
8. **Permitir comentários**: permite que o usuário adicione comentários no formulário criado.
9. **Permitir impressão**: permite que o usuário imprima o documento no formato de impressão selecionado.
10. **Permitir formulários incompletos**: permite que o usuário envie o formulário com dados parciais.


## 2. Recursos


### 2.1 Barra lateral


Você também pode mostrar links contextuais em uma barra lateral do seu formulário web. Configure em
**Configurações da barra lateral**.


![Barra lateral do formulário da Web](/files/web-form-sidebar.png)
*Barra lateral do formulário da Web*


![Formulário Web com barra lateral](/files/web-form-with-sidebar.png)
*Formulário Web com barra lateral*


### 2.2 Criando formulários web com tabela filho


Você pode adicionar tabelas filhas aos seus formulários da web, assim como os formulários normais.


![Formulário Web Grid](/files/grid-in-webform.png)


### 2.3 Integração do gateway de pagamento


Agora você pode adicionar um gateway de pagamento ao formulário da web para solicitar aos usuários que
pague em um formulário da web. Um bom exemplo disso é um ingresso de conferência.


![Pagamento por formulário da Web](/files/payment-in-webform.png)


### 2.4 Usuário do portal


Também introduzimos funções para usuários do site. Antes da versão 11, se você
atribuisse qualquer 'Função' a ​​um usuário, ele teria acesso à 'Visualização da mesa'. Da versão
11, você pode atribuir uma 'Função', mas ainda assim proibir o acesso à 'Visualização da área de trabalho',
desmarcando 'Acesso à mesa' em Função.


![Proibir acesso à mesa](/files/disallow_desk_access.png)


Nas Configurações do Portal, você pode definir uma função para cada item de menu para que somente os usuários
com essa função poderão ver esse item.


![configurações do portal](/files/portal-settings.png)


### 2.5 Script personalizado


Você pode escrever scripts personalizados para seu formulário da Web para validar seu
entradas, valores de preenchimento automático, exibição de uma mensagem de sucesso ou qualquer
ação.


Para aprender como escrever scripts personalizados para seus Web Forms, leia
[Documentação de scripts personalizados](https://frappeframework.com/docs/user/en/web-forms#client-script).


### 2.6 CSS personalizado


Você pode personalizar a aparência do seu formulário da Web escrevendo seu próprio formulário personalizado
CSS. Inspecione os elementos na página para ver para quais classes estão disponíveis
estilo. Saiba mais sobre CSS [aqui](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics).


### 2.7 Ações


Você pode adicionar o texto no campo 'Mensagem de sucesso' e esse texto será mostrado para
usuário assim que ele enviar o formulário da web com sucesso. E o usuário é redirecionado para
o URL fornecido em 'URL de sucesso' quando clicado no botão 'Continuar'. Isto é apenas
aplicável a webforms acessíveis sem o login do usuário (webforms com 'Login
Caixa de seleção Obrigatório' desmarcada).


![Mensagem de sucesso](/files/success_message.png)


### 2.8 Resultado


Quando um usuário do site envia o formulário, os dados serão armazenados no
document/doctype para o qual o formulário da web é criado.


### 2.9 Personalização


Para personalizar formulários web, consulte [Frappe Web
Documentação de formulários](https://frappeframework.com/docs/user/en/web-forms)



