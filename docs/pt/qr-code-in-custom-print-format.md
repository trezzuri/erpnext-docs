# QR Code em formato de impressão personalizado



Depois de atualizar da versão 13 para a versão 14, os códigos QR da fatura eletrônica em seu formato de impressão personalizado não funcionarão mais. Este guia ajudará você a adicionar códigos QR em formatos de impressão personalizados.


### Etapa 1: Crie um modelo web para QR Code


Primeiro você terá que criar um Web Template para o QR Code, para ir para a lista de modelos da web, procure por Web Template na barra incrível e crie um novo Web Template. Dê um nome como "Código QR da fatura eletrônica", digite como "Componente" e o módulo como "Impressão".


![nomeação de modelo da web](/files/web-template-naming.png)


Após esta cópia, cole o trecho de código mencionado abaixo no campo do modelo



```
![]()

```

Depois de adicionar o modelo, a última etapa é adicionar os campos, adicionar rótulo, nome do campo e tipo de campo conforme mostrado na imagem abaixo e salvar o modelo da web


![campos de modelo da web](/files/web-template-fields.png)


### Etapa 2: adicionar modelo da web ao formato de impressão personalizado


Vá para o formato de impressão personalizado onde deseja adicionar o QR Code, substitua o campo de imagem do QR Code atual por uma seção HTML personalizada e nessa seção HTML personalizado cole o snippet de código mencionado abaixo


`{% if doc.irn %}
{% set e_invoice_log = frappe.db.get_value(
 "Registro de fatura eletrônica", doc.irn, ("invoice_data", "signed_qr_code"), as_dict=True
) %}

{%-definir fatura_data = dict(json.loads(e_invoice_log.invoice_data))-%}

##### **Detalhes da transação**




 {%
 definir detalhes\_da\_transação = {
 "IRN": dados\_fatura.Irn,
 "Ack. Não": fatura\_data.AckNo,
 "Data de confirmação": frappe.utils.format\_datetime(
 fatura\_data.AckDt, "dd/MM/aaaa hh:mm:ss"
 ),
 "Categoria": fatura\_data.TranDtls.SupTyp,
 "Tipo de documento": fatura\_data.DocDtls.Typ,
 "Documento Nº": fatura\_data.DocDtls.No,
 }
 %}
 {% para chave, valor em transaction\_details.items() %}
 
&lcub;&lcub; chave }}
&lcub;&lcub; valor }}

 {% fim para %}


 &lcub;&lcub; web\_block('Código QR da fatura eletrônica', valores={'qr\_text': e\_invoice\_log.signed\_qr\_code }) }}



{% fim se %}`
![print format](/files/print-format.png)


Observação: certifique-se de que o nome mencionado em web\_block corresponda exatamente ao nome do seu modelo da Web, que é "Código QR da fatura eletrônica" aqui



