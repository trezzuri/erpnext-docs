# Usando domínio personalizado no SOMA



Se você se inscreveu em qualquer um dos planos em [SOMA](https://erpnext.com), pode solicitar que veiculemos seu site em seu domínio personalizado (por exemplo, em http: //exemplo.com). Isso permite que seu site seja exibido em um domínio personalizado.


Para habilitar esse recurso, primeiro você terá que editar as configurações de DNS do seu domínio da seguinte maneira.


* Faça um registro CNAME para um subdomínio (www na maioria dos casos) para {youraccountname}.erpnext.com
* Se você deseja exibir o site em um domínio sem www (ou seja, http://example.com), defina um redirecionamento de URL para http://www.example.com e não um registro CNAME. Fazer um registro CNAME neste caso pode ter consequências inesperadas, incluindo você não conseguir mais receber e-mails.


Depois de configurar os registros DNS, você terá que abrir um tíquete de suporte enviando um e-mail para support@erpnext.com e nós cuidaremos disso a partir daí.


**Observação**: não oferecemos suporte a HTTPS em domínios personalizados. O HTTPS permite a criptografia de ponta a ponta (do seu navegador para o nosso servidor). Embora não seja crítico para o site, recomendamos fortemente o uso do aplicativo SOMA em um protocolo não criptografado. Para estar seguro, use sempre o ERP em seu endereço erpnext.com.

