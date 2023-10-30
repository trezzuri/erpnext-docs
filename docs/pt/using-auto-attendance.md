# Usando atendimento automático



Nosso sistema permite marcar presença automaticamente dependendo dos registros de check-in do funcionário. Há algumas coisas que você precisa saber:


A. Crie ou importe Check-in de funcionário:


![](/files/zTTsnRA.png)


1. Defina o horário com cuidado para o tipo de registro **IN** e **OUT.**
2. Para o tipo de registro **IN** o horário deve ser maior que o **Hora de início do tipo de turno-comece o check-in antes do horário do turno**
3. Para o tipo de registro **OUT** o tempo deve ser menor que o **horário de término do tipo de turno + permitir check-out após o horário de término do turno.**
4. Então apenas Shift seria mapeado corretamente e seu Checkin será válido.


B.Verifique seu tipo de turno:


![](/files/ant5ZYn.png)


1. Definir **processar comparecimento após** (o comparecimento será marcado somente após esta data)
2. Definir **Última Sincronização de Checkins** (É o horário antes do qual todos os check-ins serão considerados. Observação: Se for menor que o horário de término do turno, não será considerado aquele dia de check-in porque significa essa mudança ainda não acabou)


C.Clique em Marcar atendimento automático para verificar se está funcionando


Nota: Nosso agendador executará o processo para marcar presença automaticamente a cada hora. Porém, após fazer upload ou criar check-ins, você precisa verificar seu **Participação no processo após e última sincronização de check-ins** em **Tipo de turno**.



