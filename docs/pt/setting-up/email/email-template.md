# Modelo de e-mail


Cada e-mail enviado é diferente, mas alguns e-mails podem ser padronizados, geralmente conhecidos como modelo de e-mail ou resposta padrão.


Para acessar a lista de modelos de e-mail, acesse:



> 
> Página inicial > Configurações > E-mail > Modelo de e-mail
> 
> 
> 


## 1. Como criar um modelo de e-mail


1. Vá para a lista de modelos de e-mail e clique em Novo.
2. Digite um nome para este modelo de e-mail.
3. Insira um assunto para este modelo de e-mail.
4. Resposta é o conteúdo padrão do e-mail que fará parte deste modelo.
5. Salvar.


![Modelo de e-mail](/files/email-template-example.png)


**DocType Associated:** (opcional) O DocType associado a este modelo.


### 1.1 Como usar o modelo de e-mail


Você pode usar este modelo de e-mail nos e-mails enviados do SOMA no campo "CC, BCC e modelo de e-mail" da seção de e-mail do documento. O SOMA buscará o assunto e a resposta de acordo com o modelo selecionado.


Você pode definir um modelo de e-mail padrão para cada tipo de documento em [Personalizar formulário](/docs/pt/customize-erpnext/customize-form).


### 1.2 Como obter nomes de campos


Os nomes de campo que você pode usar em seu modelo de e-mail são os campos do documento a partir do qual você está enviando o e-mail. Você pode descobrir os campos de qualquer documento via [Personalizar formulário](/docs/pt/customize-erpnext/customize-form) e selecionar o tipo de documento (por exemplo, Pedido de venda )


### 1.3 Usando HTML para construir o modelo


Há uma verificação `Usar HTML` que você pode alternar para alternar do editor de texto para um editor de código. Isso permite um controle mais preciso sobre o corpo do e-mail e facilita o uso de recursos como loops em Jinja.


### 1.4 Modelagem


Os modelos são compilados usando o Jinja. Para saber mais sobre Jinja, [visite esta página](https://jinja.palletsprojects.com/en/2.10.x/).


## 2. Tópicos Relacionados


1. [Conta de e-mail](/docs/pt/setting-up/email/email-account)
2. [Caixa de entrada de e-mail](/docs/pt/setting-up/email/email-inbox)
