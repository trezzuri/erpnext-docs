# Gerando conhecimento de embarque eletrônico



e-Waybill é um conhecimento eletrônico que deve ser gerado no [portal e-Waybill](https://ewaybillgst.gov.in/) para a movimentação de mercadorias. O India Compliance oferece várias maneiras de gerenciar a conformidade do seu conhecimento de embarque eletrônico.


### Configurações do conhecimento eletrônico


Comece com as **Configurações de GST** e defina as configurações do conhecimento de embarque eletrônico de acordo com suas necessidades.


* **Ativar recursos de conhecimento eletrônico**: O conhecimento eletrônico é aplicável ao seu negócio? Você é uma empresa registrada no GST envolvida na movimentação de mercadorias? Você deve ativar os recursos do conhecimento eletrônico aqui.
* **Ativar geração de conhecimento de embarque eletrônico a partir da nota de entrega**: deseja gerar um conhecimento de porte eletrônico a partir da nota de entrega? Você transfere mercadorias para Job Work ou para seu armazém diferente? Você deve ativar a geração de conhecimento de embarque eletrônico a partir da nota de entrega se usar esses recursos.



> 
> O ideal é gerar um conhecimento de embarque eletrônico a partir da fatura de venda. A geração de conhecimento de embarque eletrônico a partir de notas de entrega deve ser restrita apenas à movimentação de mercadorias sem fatura (por exemplo, para trabalho ou transferência de mercadorias para armazéns diferentes)
> 
> 
>
* **Limite de valor da fatura para geração de conhecimento de embarque eletrônico**: é definido como 50.000 por padrão, mas você pode alterá-lo de acordo com as leis aplicáveis ​​ou garantir controles internos mais rígidos. A aplicabilidade do conhecimento eletrônico para fatura de vendas é verificada com base nesta configuração.


A seguir estão as configurações adicionais específicas da API:


* **Gerar automaticamente o conhecimento eletrônico no envio da fatura**: a geração do conhecimento eletrônico será tentada se todos os campos obrigatórios estiverem presentes e o conhecimento eletrônico for aplicável.



> 
> A aplicabilidade do conhecimento eletrônico é verificada com base no limite definido acima. Além disso, pelo menos um item com HSN de **mercadorias** deve estar presente.
> 
> 
>
* **Buscar dados do conhecimento eletrônico após a geração**: Na geração do conhecimento eletrônico, os dados completos do conhecimento eletrônico (conforme Portal NIC) não estão disponíveis. No entanto, isso pode ser necessário para gerar o formato de impressão do conhecimento eletrônico conforme o Portal do conhecimento eletrônico. Solicitação adicional de API é necessária para buscar os dados do conhecimento eletrônico. Se ativado, será atualizado em seus registros.
* **Anexar impressão do conhecimento eletrônico após geração**: a impressão do conhecimento eletrônico será anexada à fatura automaticamente na geração do conhecimento eletrônico (após a busca dos dados). Pode ser usado para e-mails ou registros.


![Configurações do conhecimento eletrônico](/files/e_waybill_settings.png)


### Como gerar um e-Waybill?


Você pode gerar o conhecimento de embarque eletrônico usando o recurso de geração em massa ou as APIs.


Etapas para gerar o conhecimento de embarque eletrônico usando o recurso de geração em massa:


* Envie o documento relevante (por exemplo, fatura de venda).
* Se o conhecimento eletrônico for aplicável ao documento atual, você verá o menu do conhecimento eletrônico--> Selecione Gerar.
* A caixa de diálogo Gerar conhecimento de embarque eletrônico será exibida.
* Atualize os campos de transporte e faça download do JSON.
* Faça login em sua conta de conhecimento eletrônico--> Selecione Gerar conhecimento eletrônico em massa--> Escolha o arquivo JSON e carregue-o--> Clique em Gerar.
* O conhecimento eletrônico será gerado--> Atualize o número do conhecimento eletrônico em sua fatura de venda/nota de entrega.


![Gerar conhecimento de embarque eletrônico a partir de JSON](/files/generate_e_waybill_from_json.gif)


Etapas para gerar JSON de conhecimento eletrônico para mais de um documento (somente para faturas de vendas)


* Selecione as faturas na lista de faturas de vendas para as quais você deseja gerar um JSON de conhecimento de embarque eletrônico.
* Clique em Ações--> baixar JSON do conhecimento de embarque eletrônico.
* Faça upload para o portal e-Waybill e gere o e-Waybill.
>Você não poderá atualizar os campos de transporte enquanto baixa o JSON do conhecimento eletrônico da lista de faturas de vendas


Gerando conhecimento de embarque eletrônico usando APIs


* Ao enviar a fatura de venda, o conhecimento eletrônico será gerado automaticamente (se habilitado nas configurações).
* Você pode acionar manualmente a geração do Conhecimento de Transporte Eletrônico para Nota de Remessa ou onde todos os campos não estavam presentes (no envio). Vá para o menu e-Waybill--> caixa de diálogo Gerar--> Atualizar campos e clique em gerar.


![Gerando conhecimento de embarque eletrônico ao enviar](/files/generating_e_waybill.gif)


### Como posso saber se apenas a Parte A do conhecimento eletrônico será ser gerado?


A caixa de diálogo para gerar campos de conhecimento eletrônico tem seções separadas para a Parte A e a Parte B. Além disso, o botão Ação primária indicará se apenas a Parte A pode ser gerada.


### Como calcular automaticamente a distância para o e-Waybill?


Se a distância for definida como zero (0), o Portal e-Waybill irá sugerir a distância entre os códigos postais. Iremos atualizá-lo para o seu documento onde o conhecimento eletrônico é gerado usando as APIs.



> 
> Em algumas circunstâncias excepcionais, onde a distância entre os códigos postais não estiver disponível no banco de dados do conhecimento de embarque eletrônico, você receberá um aviso. Gere o conhecimento eletrônico novamente após inserir a distância conforme sua estimativa.
> 
> 
> 


### Recursos adicionais específicos da API


A atualização ou cancelamento do conhecimento eletrônico só é possível dentro do período de validade. Estas opções estarão visíveis apenas se você tiver gerado o conhecimento eletrônico usando API e a validade para fazê-lo não tiver expirado.


* **Atualizar detalhes do transportador**: use este recurso para atualizar o GSTIN do transportador para seu conhecimento eletrônico. No menu e-Waybill--> Selecione Atualizar transportador--> Atualizar as informações apropriadas e clique em atualizar.


![Update Transporter](/files/update_transporter.gif)


* **Atualizar informações do veículo**: use esse recurso para atualizar as informações do veículo (por exemplo, número do veículo) em seu conhecimento eletrônico. No menu e-Waybill--> Selecione Atualizar informações do veículo--> Atualizar informações na caixa de diálogo e clique em atualizar.



> 
> Há uma caixa de seleção nas caixas de diálogo acima para `Atualizar impressão/dados do conhecimento de embarque eletrônico`. Se você verificar isso, atualizaremos os anexos do conhecimento de porte eletrônico ou dados relativos ao conhecimento de porte eletrônico de acordo com sua preferência nas configurações de GST para conhecimento de porte eletrônico. Se `Anexar impressão de conhecimento de embarque eletrônico após geração` estiver ativado nas configurações de GST, novos anexos substituirão os anexos antigos.
> 
> 
>


![Atualizar informações do veículo](/files/update_vehicle_info.gif)


* **Imprimir conhecimento eletrônico**: você pode usar isso para imprimir um conhecimento eletrônico se preferir não ter anexos. Funciona de forma semelhante à impressão de qualquer outro documento no ERPNext. Ele irá redirecioná-lo para a respectiva impressão do registro do conhecimento eletrônico e buscar os dados mais recentes do conhecimento eletrônico (do Portal NIC) para impressão, se não estiverem disponíveis.
* **Anexar conhecimento eletrônico**: É um acionador manual para anexar um conhecimento eletrônico a uma fatura de vendas. Um novo anexo substituirá o anexo antigo, se houver.
* **Cancelar conhecimento eletrônico**: Se estiver dentro da validade, você poderá cancelar o conhecimento eletrônico, no menu do conhecimento eletrônico. Especifique o motivo do cancelamento na caixa de diálogo e clique em cancelar para cancelar o conhecimento eletrônico.



> 
> Enquanto você cancela o conhecimento eletrônico, o anexo do conhecimento eletrônico antigo será removido.
> 
> 
>


![Cancelar conhecimento eletrônico](/files/cancel_e_waybill.gif)


* **Registros de Conhecimento Eletrônico**: Neste DocType, o histórico do Conhecimento Eletrônico é mantido. Ele é criado depois que você gera um conhecimento eletrônico usando as APIs. Quaisquer atualizações adicionais ao e-Waybill serão adicionadas aqui como um comentário.



