# Configurar autenticação de dois fatores



## Ativar autenticação de dois fatores (2FA)


Ative a autenticação de dois fatores executando o comando.


`bench--site [sitename] set-config enable_two_factor_auth true`


Especifique o seguinte nas configurações do sistema


* O método de validação OTP (OTP App = TOTP usando Soft ou Hard Token enquanto Email/SMS = HOTP usando Email ou SMS
* O prazo de validade do QR Code no servidor se o aplicativo OTP for especificado
* O nome do emissor OTP.


![Ativar autenticação de dois fatores](/files/twofactor-1.png)


Na ativação do 2FA na configuração, ele também é ativado para a função "Todos". Desta forma, todos os utilizadores incluindo o Administrador têm que realizar uma autenticação de 2º nível com um token. Ao desmarcar a caixa de seleção "Autenticação de dois fatores" na função "Todos" e ativá-la em outras funções, a necessidade de fazer login com um token pode ser limitada a funções específicas. 2FA não se aplica ao login de usuários da Web e ao login da API


![Role Enable Two Factor Auth](/files/twofactor-2.png)


Se estiver usando autenticação por SMS, certifique-se de que suas configurações de SMS estejam atualizadas


![Configurações de SMS](/files/twofactor-3.png)


Se estiver usando e-mail, certifique-se de que as configurações da sua conta de e-mail de saída estejam atualizadas


![Configurações de e-mail](/files/twofactor-4.png)


Quando o novo usuário tenta fazer login pela primeira vez em um sistema que possui a autenticação de dois fatores habilitada e que possui a opção de autenticação como OTP App, é enviado um e-mail contendo um link para o QR Code.

 >
![Notificação por e-mail de dois fatores](/files/twofactor-5.png)
![Página de código QR](/files/twofactor-6.png)


A leitura do QR Code com um aplicativo de autenticação como o Google Authenticator registra o acesso do usuário e automaticamente começa a gerar tokens que podem ser usados ​​para fazer login


![Aplicativo de verificação de dois fatores](/files/twofactor_app.jpeg)


Se qualquer um dos e-mails/SMS for usado como método de autenticação, você também receberá notificações


![E-mail e SMS](/files/twofactor-8.png)


### Perguntas frequentes (FAQ)


Q. Não consigo fazer login mesmo depois de seguir todo o processo. 


Resposta: Frappe usa algoritmo OTP baseado em TOTP, que depende da hora do sistema do seu dispositivo. Por favor, certifique-se de que o dispositivo que você está usando tenha o mesmo horário definido como o seu servidor ERPNext. 



