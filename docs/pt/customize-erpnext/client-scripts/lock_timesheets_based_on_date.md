# Folhas de ponto de bloqueio com base na data


Digamos que você gostaria que todos os funcionários preenchessem as planilhas de horas até sexta-feira de cada semana. E permita que apenas os usuários com função de 'Gerente de Projetos' editem ou adicionem planilhas de horas para os dias anteriores à última sexta-feira. O script personalizado abaixo implementará esse recurso.



```
frappe.ui.form.on("Planilha de Horários", "validar", function(frm) {
    if (frappe.user_roles.indexOf("Gerente de Projetos") == -1) {
        const t = new Date().getDate() + (6 - new Date().getDay() - 1) - 7;
        const últimaSexta = new Data();
        lastFriday.setDate(t);

        deixe dd = lastFriday.getDate();
        deixe mm = lastFriday.getMonth() + 1;
        let aaaa = lastFriday.getFullYear();

        frm.doc.time_logs.forEach(log => {
            if (new Date(log.from_time) <= lastFriday) {
                frappe.throw("Você não pode adicionar quadro de horários para datas antes da última sexta-feira " + dd + "/" + mm + "/" + aaaa + ". Entre em contato com seu gerente de projeto.");
            }
        })
    }
})

```
