# Usando o relatório preparado



Muitas vezes, ao gerar um relatório que lida com um grande volume de dados, digamos, um relatório contábil para o ano inteiro, você pode acabar recebendo a seguinte mensagem de erro: **Tempo limite da solicitação esgotado**. Isso ocorre porque há muitos dados a serem processados ​​e apresentados na página do relatório, mas não há recursos de servidor suficientes, resultando em um tempo limite.


Para um melhor processamento de tais relatórios, o ERPNext oferece Relatórios Preparados (desde v11). Quando um relatório é definido como Relatório Preparado, ele é gerado por meio de um plano de fundo  [job](https://frappe.io/docs/v13/user/en/guides/app-development/running-background-jobs) e, quando estiver pronto, estará disponível para visualização pelos usuários.


## Etapas para configurar relatórios preparados


1. Acesse [Permissão de função para página e relatório](/docs/pt/setting-up/users-and-permissions/role-permission-for-page-and-report) .
2. No campo 'Definir função para' selecione **Relatório**.
3. No campo 'Relatório', selecione o relatório para o qual deseja ativar/desativar o relatório preparado.
4. Use a caixa de seleção **Desativar relatório preparado** para ativar/desativar o relatório preparado. Se a opção estiver marcada, a opção de relatório preparado será desativada para o relatório selecionado.
5. Clique em **Atualizar**.


![Configurar relatório preparado](/files/set-prep-report.gif)


## Como usar um relatório preparado


1. Abra o referido relatório (por exemplo, General Ledger) e aplique todos os filtros necessários.
2. Se a opção de relatório preparado estiver ativada para esse relatório, você verá um botão **Gerar relatório**. Clique no mesmo.
![Gerar relatório preparado](/files/prepared-report-generate.png)
3. Você verá uma notificação no canto inferior direito da tela dizendo "Relatório iniciado. Você pode acompanhar seu status *aqui*"
![Relatório preparado iniciado](/files/prepared-report-bg.png)
4. Você pode esperar na tela ou clicar *aqui* na mensagem acima para abrir a página do relatório. Isso abrirá uma nova página para o relatório:
![Relatório preparado na fila](/files/prepared-report-queued.png)
Como você pode ver, a página do relatório tem o status "Na fila". Quando o relatório estiver pronto, você verá um botão **Mostrar relatório** no qual poderá clicar para visualizar o relatório:
 ![Relatório preparado iniciado](/files/prepared-report-page.png)
5. Como o Relatório Preparado também é um tipo de documento, para visualizar a lista de Relatórios Preparados, você pode usar o [Role Permission Manager](/docs/pt/setting-up/users-and-permissions/role-based-permissions) para conceder acesso ao mesmo.



