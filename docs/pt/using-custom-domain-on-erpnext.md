# Usando Domínio Personalizado no ERPNext




Se você se inscreveu em algum dos planos em [ERPNext](https://erpnext.com), você pode solicitar que veiculemos seu site em seu domínio personalizado (por exemplo, em http://exemplo.com). Isso permite que seu site seja veiculado em um domínio personalizado.


Para ativar esse recurso, primeiro você terá que editar as configurações de DNS do seu domínio da seguinte maneira.


* Faça um registro CNAME para um subdomínio (www na maioria dos casos) para {nomedasuaconta}.erpnext.com
* Se você quiser veicular o site em um domínio sem www (ou seja, http://example.com), defina um redirecionamento de URL para http://www.example.com e não um registro CNAME. Fazer um registro CNAME neste caso pode ter consequências inesperadas, incluindo você não poder mais receber e-mails.


Depois de configurar os registros DNS, você terá que abrir um ticket de suporte enviando um e-mail para support@erpnext.com e nós cuidaremos do assunto a partir daí.


**Observação**: não oferecemos suporte a HTTPS em domínios personalizados. HTTPS permite criptografia de ponta a ponta (do seu navegador para o nosso servidor). Embora não seja crítico para o site, não recomendamos fortemente o uso do aplicativo ERPNext em um protocolo não criptografado. Para sua segurança, use sempre o ERP no seu endereço erpnext.com.



