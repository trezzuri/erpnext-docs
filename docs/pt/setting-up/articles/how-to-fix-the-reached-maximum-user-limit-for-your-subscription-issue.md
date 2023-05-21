# Problema de limite máximo de usuários


Sua assinatura do ERPNext depende do número de Usuários do Sistema que você assina. Depois de ultrapassar esse limite, o sistema não permitirá que você crie mais nenhum número de usuários. Por exemplo, você se inscreveu para 10 usuários. Se você já criou 10 usuários do sistema em sua conta, o sistema não permitirá que você crie o 11º usuário do sistema e você receberá a mensagem abaixo.

  


![](/files/oP3RzNx.png)

  


Para corrigir isso, você terá que:

1) Compre novos usuários ou

2) Desative os usuários atuais

  


No entanto, às vezes, você ainda pode enfrentar esse problema mesmo quando não esgotou o número de usuários do sistema de acordo com seu plano de assinatura. Por exemplo, você tem um limite de 5 usuários do sistema e criou apenas 3 usuários. No entanto, ao criar o quarto usuário, você recebe a mensagem acima. A razão para isso pode ser que, para alguns dos usos, o campo de "Sessões Simultâneas" seja maior que 1.

  


Cada sessão simultânea é considerada como 1 Usuário do Sistema. Por exemplo, se você criou 3 usuários e um deles tem "Sessão Simultânea" definida como 3, você tem um total de 5 usuários, ou seja, 3 + 1 + 1 = 5 sessões simultâneas/usuários do sistema.

  


Para permitir que o sistema permita criar mais usuários, você terá que reduzir as sessões simultâneas desses usuários. Para tal, aceda ao perfil do Utilizador, em Definições de Segurança, defina/reduza a "Sessão Simultânea" em conformidade.

  


![](/files/YQQ8cHw.png)

  


**Observação:** Você ainda poderá criar Usuários do Site, pois não há limite para isso.