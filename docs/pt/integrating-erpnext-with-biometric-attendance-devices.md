# Integração do ERPNext com dispositivos de atendimento biométrico



## Plano de fundo


Os registros de presença do dispositivo biométrico são registros de entrada e saída de um funcionário. O ERPNext permite armazenar esses logs em um documento chamado Employee Checkin.


A presença pode então ser marcada com base nos registros de [Check-in de funcionário](/docs/pt/human-resources/employee_checkin) e no [Tipo de turno](/docs/pt/human-resources/shift_type) do funcionário usando [Atendimento automático](/docs/pt/human-resources/auto-attendance )


Portanto, a integração do seu dispositivo biométrico (*ou qualquer sistema de controle de acesso que colete registros de entrada/saída*) pode ser feita seguindo as seguintes etapas:


### 1. Configurando o Atendimento Automático para marcar presença no Check-in do Funcionário


Antes de importar/sincronizar os registros de Check-in e Check-out dos funcionários em seu sistema ERPNext, você terá que configurar os funcionários e seus turnos para poder gerar atendimento usando o recurso Atendimento Automático no ERPNext.
Consulte o link a seguir para configurar o atendimento automático: [Configurar atendimento automático](/docs/pt/human-resources/auto-attendance)
Depois de configurar o cadastro de funcionários e atribuir turnos aos funcionários, você estará pronto para prosseguir para a próxima etapa.


### 2. Preenchendo os Registros Biométricos de Perfurações no Check-in de Funcionários do ERPNext


Dependendo do seu sistema biométrico e de seus recursos, pode haver várias maneiras de preencher os logs do Punch no ERPNext:


1. **Use a ferramenta de importação de dados do ERPNext**:


	* A solução mais simples possível (em termos de complexidade de implementação) seria gerar um Excel/CSV do Check-in/Check-out e usar a ferramenta de importação de dados integrada no ERPNext para importar periodicamente os logs para o seu Funcionário Documento de check-in
	* Por favor consulte a [Documentação do ERPNext sobre Ferramenta de Importação de Dados](/docs/pt/setting-up/data/data-import) para saber mais sobre como fazer isso .
2. **Integração de API**:


	* Você pode automatizar o processo de sincronização dos Punch Logs Biométricos integrando-os com a API disponível no ERPNext.
	* Este método requer algum conhecimento técnico e você provavelmente deve entrar em contato com seu implementador ERPNext ou fornecedor de sistema biométrico.
	* Etapas:
		1. Primeiro você precisará criar um [user](/docs/pt/setting-up/users-and-permissions/adding-users#1-how-to-create-a-new-user) em sua instância do ERPNext que seria usado para criar logs, já que este método de API requer login. Certifique-se de que este usuário tenha todas as permissões necessárias para criar o Employee Checkin.
		2. [Gerar chave de API e segredo de API](/docs/pt/setting-up/users-and-permissions/adding-users#210-api-access) para o usuário que será usado para autenticação.
		3. Certifique-se de ter definido o  [ID do dispositivo de presença (ID de etiqueta biométrica/RF)](/docs/pt/human-resources/auto-attendance#3-setup-attendance-device-id-field-in-employee) para os funcionários com base no seu dispositivo biométrico.
		4. Os detalhes da implementação da API podem ser encontrados [aqui](https://github.com/frappe/erpnext/blob/develop/erpnext/hr/doctype/employee_checkin/employee_checkin.py#L49-L78) e a API podem ser acessadas em: `/api/method/erpnext.hr.doctype.employee_checkin.employee_checkin.add_log_based_on_employee_field`.
		5. Você pode escrever um script para enviar uma solicitação POST para a API. Este endpoint encontra o Funcionário relevante usando o valor do campo do funcionário e cria um Check-in do Funcionário. Detalhes do endpoint da API:
			+ URL: `/api/method/erpnext.hr.doctype.employee_checkin.employee_checkin.add_log_based_on_employee_field`
			+ Método: `POST`
			+ Parâmetros:
				- `employee_field_value`: o valor a ser procurado no campo funcionário. Este será o ID do dispositivo de presença encontrado em seus registros biométricos e também definido no registro do funcionário.
				- `timestamp`: o timestamp do Log. Atualmente esperado no seguinte formato como uma string: '2022-04-08 10:48:08.000000'
				- `device_id`: (opcional) Localização/ID do dispositivo. Uma string curta é esperada.
				- `log_type`: (opcional) Direção do punção, se disponível (ENTRADA/SAÍDA).
				- `skip_auto_attendance`: (opcional) o campo Pular frequência automática será definido para este registro (0/1)
				- `employee_fieldname`: (Padrão: `attendance_device_id`) Nome do campo em Employee DocType com base em qual pesquisa de funcionário ocorrerá.
			+ Resposta: Retorna um objeto de documento Employee Checkin que foi inserido.
3. **Configure um script python no seu computador para integrar o ZKTeco ou dispositivos semelhantes**:


	* Este método funciona apenas para ZKTeco ou dispositivos similares que usam o ZKProtocol para se comunicar por TCP/IP.
	* Este script está disponível em: [github:frappe/push-biometric-erpnext](https://github.com/frappe/push-biometric-erpnext).
	* Siga as instruções fornecidas na página do script para configurá-lo em seu computador.
	* Este script extrai registros biométricos de um dispositivo compatível e usa a API mencionada na etapa acima para enviar os dados para o ERPNext.


## Perguntas frequentes


### 1. Como seleciono um dispositivo biométrico compatível com ERPNext?


Se você estiver usando o método 1 ou 2, não precisa se preocupar com compatibilidade. 


No entanto, para o terceiro método, o aplicativo biométrico push usa internamente um script compatível com os dispositivos listados [aqui](https://github.com/fananimi/pyzk#compatível-devices). Normalmente, qualquer ZKTeco ou dispositivo semelhante que use o ZKProtocol para se comunicar por TCP/IP deve funcionar. No que diz respeito à compra do dispositivo, sugerimos que você opte por uma avaliação do dispositivo com o fornecedor, se possível, onde o dispositivo pode ser testado com a ferramenta de sincronização, pois depende de vários fatores no que diz respeito à compatibilidade.


### 2. Como posso saber qual método usar para integrar meu dispositivo biométrico ao ERPNext?


O método 1 é viável em qualquer situação, mas exige que você importe manualmente os logs periodicamente. Os métodos 2 e 3 precisam de algum monitoramento e trabalho para uma configuração única para que a sincronização de logs seja automatizada.


**Para configuração de um único local:**


Na abordagem Push Biometric Device, a ferramenta precisa ser capaz de se comunicar com seu dispositivo biométrico via TCP/IP. Portanto, geralmente ele precisa ser executado na mesma rede LAN que o dispositivo biométrico. Para sincronizar esses logs obtidos com sua instância do ERPNext, ele usa acesso à API. Isso funciona melhor quando você tem um único local configurado.


**Para uma configuração em vários locais:**


Neste caso, geralmente recomendamos o método 2, onde a maioria dos fornecedores de biometria fornece serviços para sincronizar os logs de dispositivos biométricos de vários locais para o ERPNext através de acesso à API. O método 3 (ferramenta de atendimento biométrico push) também pode funcionar neste caso se você tiver algum conhecimento de rede.







