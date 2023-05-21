# Integração do ERPNext com dispositivos biométricos de atendimento


## Fundo


Os registros de ponto de atendimento do dispositivo biométrico são registros de check-in e check-out de um funcionário. O ERPNext possui uma provisão para armazenar esses logs em um documento chamado Check-in do Funcionário.


A frequência pode ser marcada com base nos registros de [Check-in do funcionário](/docs/v14/user/manual/en/human-resources/employee_checkin) e no [Tipo de turno](/docs/v14/user/manual/en/human -resources/shift_type) do funcionário usando [Atendimento automático](/docs/v14/user/manual/en/human-resources/auto-atendimento)


Assim, a integração do seu Dispositivo Biométrico (*ou qualquer sistema de controle de acesso que colete registros de ENTRADA/SAÍDA*) pode ser feita seguindo os seguintes passos:


### 1. Configurando o Atendimento Automático para marcar presença no Check-in do Funcionário


Antes de importar/sincronizar os registros de Check-in e Check-out dos funcionários em seu sistema ERPNext, você terá que configurar os funcionários e seus turnos para poder gerar atendimento usando o recurso de Atendimento Automático no ERPNext.


Consulte o seguinte link para configurar o atendimento automático: [Configurar o atendimento automático](/docs/v14/user/manual/en/human-resources/auto-atendimento)


Depois de configurar o cadastro de funcionários e atribuir turnos aos funcionários, você está pronto para prosseguir para a próxima etapa.


### 2. Preenchendo os Registros de Perfuração Biométricos no Check-in do Funcionário do ERPNext


Dependendo do seu sistema biométrico e de seus recursos, pode haver várias maneiras de preencher os logs do Punch no ERPNext:


1. **Utilize a Ferramenta de Importação de Dados do ERPNext**:


* A solução mais simples possível (em termos de complexidade de implementação) seria gerar um Excel/CSV do Check-in/Check-out e utilizar a ferramenta de importação de dados embutida no ERPNext para importar periodicamente os logs para o seu Documento de Check-in do Funcionário
* Consulte a [Documentação do ERPNext sobre ferramenta de importação de dados](/docs/v14/user/manual/en/setting-up/data/data-import) para saber mais sobre como fazer isso.
2. **Integração de API**:


* Você pode automatizar o processo de sincronização dos Logs de Perfuração Biométricos integrando-o com a API disponível no ERPNext.
* Este método requer algum conhecimento técnico e você provavelmente deve entrar em contato com o implementador do ERPNext ou com o fornecedor do sistema biométrico.
* Passos:
1. Primeiro, você precisará criar um [usuário](/docs/v14/user/manual/en/setting-up/users-and-permissions/adding-users#1-how-to-create-a-new- user) em sua instância do ERPNext que seria usado para criar logs, pois esse método de API requer login. Certifique-se de que este usuário tenha todas as permissões necessárias para criar Check-in de funcionário.
2. [Gerar API Key e API Secret](/docs/v14/user/manual/en/setting-up/users-and-permissions/adding-users#210-api-access) para o usuário que será usado para autenticação.
3. Certifique-se de ter definido o [ID do dispositivo de atendimento (ID da etiqueta biométrica/RF)](/docs/v14/user/manual/en/human-resources/auto-attendance#3-setup-attendance-device-id- field-in-employee) para os funcionários com base em seu dispositivo biométrico.
4. Os detalhes da implementação da API podem ser encontrados [aqui](https://github.com/frappe/erpnext/blob/develop/erpnext/hr/doctype/employee_checkin/employee_checkin.py#L49-L78) e a API pode ser acessado em: `/api/method/erpnext.hr.doctype.employee_checkin.employee_checkin.add_log_based_on_employee_field`.
5. Você pode escrever um script para enviar uma solicitação POST à ​​API. Este endpoint encontra o funcionário relevante usando o valor do campo do funcionário e cria um check-in do funcionário. Detalhes do endpoint da API:
+ URL: `/api/method/erpnext.hr.doctype.employee_checkin.employee_checkin.add_log_based_on_employee_field`
+ Método: `POST`
+ Parâmetros:
- `employee_field_value`: O valor a ser procurado no campo empregado. Este será o ID do dispositivo de atendimento encontrado em seus registros biométricos e também definido no registro do funcionário.
- `timestamp`: O timestamp do Log. Atualmente esperado no seguinte formato como uma string: '2022-04-08 10:48:08.000000'
- `device_id`: (opcional) Local / ID do dispositivo. Uma string curta é esperada.
- `log_type`: (opcional) Direção do punção se disponível (IN/OUT).
- `skip_auto_attendance`: (opcional) Ignorar o campo de atendimento automático será definido para este log (0/1)
- `employee_fieldname`: (Padrão: `attendance_device_id`) Nome do campo em Employee DocType com base no qual a pesquisa do funcionário acontecerá.
+ Resposta: Retorna um objeto de documento Check-in do Funcionário que foi inserido.
3. **Configure um script python em seu computador para integrar o ZKTeco ou dispositivos similares**:


* Este método funciona apenas para dispositivos ZKTeco ou similares que utilizam o ZKProtocol para comunicação via TCP/IP.
* Este script está disponível em: [github:frappe/push-biometric-erpnext](https://github.com/frappe/push-biometric-erpnext).
* Siga as instruções fornecidas na página do script para configurá-lo em seu computador.
* Este script extrai logs biométricos de um dispositivo compatível e usa a API mencionada na etapa acima para enviar os dados para o ERPNext.


## Perguntas frequentes


### 1. Como seleciono um Dispositivo Biométrico compatível com o ERPNext?


Se você estiver usando o método 1 ou 2, não precisa se preocupar com a compatibilidade.


No entanto, para o terceiro método, o aplicativo biométrico push usa internamente um script compatível com os dispositivos listados [aqui](https://github.com/fananimi/pyzk#functional-devices). Normalmente, qualquer dispositivo ZKTeco ou similar que use o ZKProtocol para se comunicar por TCP/IP deve funcionar. No que diz respeito à compra do dispositivo, sugerimos que você opte por uma avaliação do dispositivo com o fornecedor, se possível, onde o dispositivo pode ser testado com a ferramenta de sincronização, pois depende de vários fatores quando se trata de compatibilidade.


### 2. Como sei qual método usar para integrar meu dispositivo biométrico com o ERPNext?


O método 1 é viável em qualquer situação, mas exige que você importe manualmente os logs periodicamente. Os métodos 2 e 3 precisam de algum monitoramento e funcionam para uma configuração única para que a sincronização de log seja automatizada.


**Para configuração de um único local:**


Na abordagem Push Biometric Device, a ferramenta precisa ser capaz de se comunicar com seu dispositivo biométrico via TCP/IP. Portanto, geralmente é necessário que ele seja executado na mesma rede LAN do dispositivo biométrico. Para sincronizar esses logs buscados com sua instância do ERPNext, ele usa o acesso à API. Isso funciona melhor quando você tem um único local configurado.


**Para uma configuração em vários locais:**


Nesse caso, geralmente recomendamos o método 2, no qual a maioria dos fornecedores biométricos fornece serviços para sincronizar os logs do dispositivo biométrico de vários locais para o ERPNext por meio de acesso à API. O método 3 (ferramenta de atendimento biométrico push) também pode funcionar neste caso se você tiver algum conhecimento de rede.