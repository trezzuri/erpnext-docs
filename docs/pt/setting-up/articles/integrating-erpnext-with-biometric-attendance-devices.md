# Integrando o SOMA com dispositivos biométricos de atendimento


## Fundo


Os registros de ponto de atendimento do dispositivo biométrico são registros de check-in e check-out de um funcionário. O SOMA tem uma provisão para armazenar esses logs em um documento chamado Employee Checkin.


A frequência pode ser marcada com base nos registros [Check-in do funcionário](/docs/pt/human-resources/employee_checkin) e nos [Tipo de turno](/docs /v14/user/manual/en/human-resources/shift_type) do funcionário usando [Atendimento automático](/docs/pt/human-resources/auto-atendimento )


Portanto, a integração do seu dispositivo biométrico (*ou qualquer sistema de controle de acesso que colete registros de ENTRADA/SAÍDA*) pode ser feita usando as seguintes etapas:


### 1. Configurando o Atendimento Automático para marcar presença no Check-in do Funcionário


Antes de importar/sincronizar os registros de Check-in e Check-out dos funcionários em seu sistema SOMA, você terá que configurar os funcionários e seus turnos para poder gerar presença usando o recurso de Atendimento Automático no SOMA.


Consulte o seguinte link para configurar o atendimento automático: [Configurar atendimento automático](/docs/pt/human-resources/auto-attendance)


Depois de configurar o cadastro de funcionários e atribuir turnos aos funcionários, você está pronto para prosseguir para a próxima etapa.


### 2. Preenchendo os registros biométricos de pontos no check-in do funcionário do SOMA


Dependendo do seu sistema biométrico e de seus recursos, pode haver várias maneiras de preencher os logs do Punch no SOMA:


1. **Use a ferramenta de importação de dados do SOMA**:


	* A solução mais simples possível (em termos de complexidade de implementação) seria gerar um Excel/CSV do Check-in/Check-out e usar a ferramenta de importação de dados embutida no SOMA para importar periodicamente os logs para o seu Funcionário Documento de check-in
	* Consulte [Documentação do SOMA sobre ferramenta de importação de dados](/docs/pt/setting-up/data/data-import) para saber mais sobre como fazer isso .
2. **Integração de API**:


	* Você pode automatizar o processo de sincronização dos Logs de Punch Biométricos integrando-o com a API disponível no SOMA.
	* Este método requer algum conhecimento técnico e você provavelmente deve entrar em contato com o implementador do SOMA ou com o fornecedor do sistema biométrico.
	* Etapas:
		1. Você primeiro precisará criar um [usuário](/docs/pt/setting-up/users-and-permissions/adding-users#1-how-to-create-a- new-user) em sua instância do SOMA que seria usado para criar logs, pois esse método de API requer login. Certifique-se de que este usuário tenha todas as permissões necessárias para criar Check-in de funcionário.
		2. [Gerar chave de API e segredo de API](/docs/pt/setting-up/users-and-permissions/adding-users#210-api-access) para o usuário que será usado para autenticação.
		3. Certifique-se de ter definido o  [ID do dispositivo de atendimento (ID biométrico/identificador de RF)](/docs/pt/human-resources/auto-attendance#3-setup-attendance-device-id-field-in-employee) para os funcionários com base em seu dispositivo biométrico.
		4. Os detalhes da implementação da API podem ser encontrados [aqui< /a> e a API pode ser acessada em: `/api/method/erpnext.hr.doctype.employee_checkin.employee_checkin.add_log_based_on_employee_field`.](https://github.com/frappe/erpnext/blob/develop/erpnext/hr/doctype/employee_checkin/employee_checkin.py#L49-L78)
		5. Você pode escrever um script para enviar uma solicitação POST à ​​API. Este endpoint encontra o funcionário relevante usando o valor do campo do funcionário e cria um check-in do funcionário. Detalhes do endpoint da API:
			+ URL: `/api/method/erpnext.hr.doctype.employee_checkin.employee_checkin.add_log_based_on_employee_field`
			+ Método: `POST`
			+ Parâmetros:
				- `employee_field_value`: o valor a ser procurado no campo do funcionário. Este será o ID do dispositivo de atendimento encontrado em seus registros biométricos e também definido no registro do funcionário.
				- `timestamp`: O timestamp do Log. Atualmente esperado no seguinte formato como uma string: '2022-04-08 10:48:08.000000'
				- `device_id`: (opcional) Local / ID do dispositivo. Uma string curta é esperada.
				- `log_type`: (opcional) Direção do soco, se disponível (IN/OUT).
				- `skip_auto_attendance`: (opcional) Ignorar o campo de atendimento automático será definido para este log (0/1)
				- `employee_fieldname`: (Padrão: `attendance_device_id`) Nome do campo em Employee DocType com base em qual pesquisa de funcionário ocorrerá.
			+ Resposta: Retorna um objeto de documento Check-in do funcionário que foi inserido.
3. **Configure um script python em seu computador para integrar o ZKTeco ou dispositivos semelhantes**:


	* Este método funciona apenas para dispositivos ZKTeco ou similares que usam o ZKProtocol para se comunicar por TCP/IP.
	* Este script está disponível em: [github:frappe/push-biometric-erpnext](https://github.com/frappe/push-biometric-erpnext).
	* Siga as instruções fornecidas na página do script para configurá-lo em seu computador.
	* Este script extrai registros biométricos de um dispositivo compatível e usa a API mencionada na etapa acima para enviar os dados para o SOMA.


## Perguntas frequentes


### 1. Como seleciono um dispositivo biométrico compatível com o SOMA?


Se você estiver usando o método 1 ou 2, não precisa se preocupar com a compatibilidade. 


No entanto, para o terceiro método, o aplicativo biométrico push usa internamente um script compatível com os dispositivos listados [aqui< /a>. Normalmente, qualquer dispositivo ZKTeco ou similar que use o ZKProtocol para se comunicar por TCP/IP deve funcionar. No que diz respeito à compra do dispositivo, sugerimos que você opte por uma avaliação do dispositivo com o fornecedor, se possível, onde o dispositivo pode ser testado com a ferramenta de sincronização, pois depende de vários fatores quando se trata de compatibilidade.](https://github.com/fananimi/pyzk#functional-devices)


### 2. Como sei qual método usar para integrar meu dispositivo biométrico com o SOMA?


O método 1 é viável em qualquer situação, mas exige que você importe manualmente os logs periodicamente. Os métodos 2 e 3 precisam de algum monitoramento e funcionam para uma configuração única para que a sincronização de log seja automatizada.


**Para configuração de um único local:**


Na abordagem Push Biometric Device, a ferramenta precisa ser capaz de se comunicar com seu dispositivo biométrico via TCP/IP. Portanto, geralmente é necessário que ele seja executado na mesma rede LAN do dispositivo biométrico. Para sincronizar esses logs buscados com sua instância do SOMA, ele usa o acesso à API. Isso funciona melhor quando você tem um único local configurado.


**Para uma configuração de vários locais:**


Nesse caso, geralmente recomendamos o método 2, no qual a maioria dos fornecedores biométricos fornece serviços para sincronizar os logs do dispositivo biométrico de vários locais para o SOMA por meio de acesso à API. O método 3 (ferramenta de atendimento biométrico push) também pode funcionar neste caso se você tiver algum conhecimento de rede.

