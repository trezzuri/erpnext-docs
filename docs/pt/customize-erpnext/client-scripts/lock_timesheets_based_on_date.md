# Bloquear planilhas de horas com base na data



Digamos que você gostaria que todos os funcionários preenchessem planilhas de ponto até sexta-feira de cada semana. E permita que apenas os usuários com função de 'Gerente de Projetos' editem ou adicionem planilhas de horas dos dias anteriores à última sexta-feira. O script personalizado abaixo implementará esse recurso.



```
frappe.ui.form.on("Timesheet", "validate", function(frm) {
    if (frappe.user_roles.indexOf("Gerenciador de Projetos") ==-1) {
        const t = new Date().getDate() + (6-new Date().getDay()-1)-7;
        const última sexta-feira = new Data();
        última sexta-feira.setDate(t);

        deixe dd = lastFriday.getDate();
        deixe mm = lastFriday.getMonth() + 1;
        deixe aaaa = lastFriday.getFullYear();

        frm.doc.time_logs.forEach(log => {
            if (nova data(log.from_time) <= última sexta-feira) {
                frappe.throw("Você não pode adicionar planilha de horas para datas anteriores à última sexta-feira " + dd + "/" + mm + "/" + aaaa + ". Entre em contato com seu gerente de projeto.");
            }
        })
    }
})

```


