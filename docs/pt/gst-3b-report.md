# Relatório GSTR3B no ERPNext



Para gerar o Relatório GSTR3B no ERPNext navegue até



> 
> **Contabilidade > Imposto sobre Bens e Serviços (GST Índia) > Relatório GSTR 3B**
> 
> 
> 


ou simplesmente pesquise Relatório GSTR 3B na barra incrível.


Clique em Novo para gerar um novo relatório ou selecione um relatório existente para atualizá-lo ou fazer download do JSON.


Insira os seguintes detalhes para gerar o relatório:


1. Nome da empresa
2. Endereço da empresa vinculado ao GSTIN para o qual o relatório será gerado
3. Ano
4. Mês


![Relatório GSTR 3B](/files/gstr-3b-input.png)


Clique em Salvar para gerar o relatório. Um relatório existente também pode ser atualizado/gerado novamente clicando em salvar.


Depois de salvar, você poderá ver a saída JSON no campo de texto abaixo, que também pode ser baixado usando o botão Baixar JSON no canto superior direito, conforme mostrado na imagem abaixo.


![GSTR 3B com JSON](/files/gstr-3b-report.png)


Caso queira imprimir o relatório ele também pode ser impresso e visualizado no Formulário GSTR3B clicando em Visualizar Formulário conforme mostrado abaixo


![Opção de download no GSTR 3B](/files/gstr-3b-download.png)


Observação: para garantir que o relatório seja calculado de maneira precisa e correta, certifique-se do seguinte.


1. Como o GST é um imposto baseado no destino, certifique-se de que todos os clientes e fornecedores indianos tenham o estado de GST (mesmo os não registrados).
2. Itens com classificação nula, isentos ou sem GST têm a caixa de seleção Classificação nula ou Não-GST marcada no cadastro de itens.


![Isento de GST](/files/gst-item.png)


1. Os nomes de conta apropriados são inseridos nas configurações de GST.
2. Elegibilidade adequada para o campo ITC está selecionado. Por exemplo: Todos os outros ITC ou inelegíveis



