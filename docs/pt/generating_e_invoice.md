# Gerando fatura eletrônica



e-Invoice é uma fatura eletrônica que deve ser gerada no [portal e-Invoice](https://einvoice1.gst.gov.in/) para todas as faturas, exceto para suprimentos feitos para clientes não cadastrados. Para cumprir o mesmo, a India Compliance oferece uma solução fácil, rápida e confiável para gerar fatura eletrônica.



> 
> Seriam necessárias APIs para usar esses recursos. Isso é necessário para empresas com bom volume de transações e, portanto, é recomendado o uso com APIs.
> 
> 
> 


### Configurações da fatura eletrônica


Comece com as **Configurações de GST** e defina as configurações da fatura eletrônica de acordo com seus requisitos.



> 
> Primeiro você precisa ativar a API para acessar as configurações da fatura eletrônica
> 
> 
> 


* **Ativar a fatura eletrónica**: a fatura eletrónica é aplicável a si? Você pode ativar os recursos de faturamento eletrônico aqui.
* **Gerar fatura eletrônica automaticamente no envio da fatura**: a fatura eletrônica será gerada automaticamente, se aplicável, no envio da fatura de vendas.



> 
> A fatura eletrônica é gerada automaticamente para todas as faturas, exceto para suprimentos para pessoas não registradas ou suprimentos não GST.
> 
> 
>
* **Fatura eletrônica aplicável a partir de**: Faturas eletrônicas serão geradas somente para faturas geradas após esta data. Você pode pré-configurar isso se for aplicável posteriormente.


![Configurações de fatura eletrônica](/files/e_invoice_settings.png)


### Geração de fatura eletrônica


A fatura eletrônica será gerada automaticamente no momento do envio da fatura, se for aplicável a você.


Caso queira acionar a geração manualmente, poderá fazê-lo após o envio da Nota Fiscal. As opções do menu da fatura eletrônica aparecerão. Depois de clicar no botão Gerar, a geração da fatura eletrônica será acionada.


![Gerando fatura eletrônica](/files/generating_e_invoice.gif)


### Cancelamento da fatura eletrônica


Você pode cancelar a fatura eletrônica nas opções do menu da fatura eletrônica se estiver dentro do período de validade.


Clique no menu da fatura eletrônica--> Clique no botão Cancelar--> Forneça os motivos do cancelamento na caixa de diálogo--> e confirme o cancelamento da fatura eletrônica.


![Cancelamento da fatura eletrônica](/files/cancelling_e_invoice.gif)


### e-Invoice e e-Waybill ambos são aplicáveis ​​a nós. Como essas configurações interagem entre si?


Temos uma integração perfeita para você, onde ambos são aplicáveis ​​a você. Os pontos a seguir ajudarão você a entender o mesmo em detalhes.


* Se a configuração `Gerar fatura eletrônica automaticamente no envio de fatura` estiver ativada por você, `Gerar fatura eletrônica automaticamente no envio de fatura` será uma configuração obrigatória para você .
* Ao gerar a fatura eletrônica, o conhecimento de embarque eletrônico será gerado automaticamente se aplicável e os campos obrigatórios (Detalhes do Transporte) estiverem presentes. Caso os dados não estejam disponíveis e o conhecimento eletrônico não seja gerado ou apenas a Parte A do conhecimento eletrônico seja gerada, você poderá gerar ou atualizar o conhecimento eletrônico a partir dos itens do menu do conhecimento eletrônico.
* Para cancelamento da fatura eletrônica, o conhecimento de embarque eletrônico precisa ser cancelado primeiro. Nós ajudamos você aqui. Enquanto você cancela a fatura eletrônica, e se o conhecimento de embarque eletrônico estiver disponível e válido, tanto a fatura eletrônica quanto o conhecimento de porte eletrônico serão cancelados simultaneamente.


### E se gerarmos o e-Waybill antes da e-Invoice?


O e-Invoice foi projetado para automatizar seu processo de GSTR-1 e e-Waybill. Você deve primeiro criar uma fatura eletrônica e depois gerar um conhecimento de embarque eletrônico somente se ela não for gerada junto com a fatura eletrônica.


### O que devemos fazer se a validade da fatura eletrônica expirou e ainda assim gostaríamos de cancelá-la?


e-Invoice é um registro legal. Cancelar sua fatura (embora a fatura eletrônica não seja cancelável) devido a atualizações, erros ou devoluções não é uma boa prática nesses casos.


Você deve ajustar a diferença com uma nota de crédito ou débito além desta fatura.



