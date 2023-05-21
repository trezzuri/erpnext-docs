# Buscando dados de um mestre vinculado


**Pergunta:** Como adicionar termos e condições no formulário do motorista?
**Passos:**
1. Vá para o tipo de documento onde deseja adicionar os termos e condições.
2. Vá para Menu > Personalizar

![](/files/c6WTMJQ.png)
1. Você verá uma tabela com uma lista de campos. Estes são os campos na sua página de driver.
2. Role para baixo até a seção/campo após o qual deseja adicionar termos e condições.
3. Clique no pequeno ícone no lado direito. Isso expandirá o campo selecionado.
4. Você pode adicionar um novo campo acima ou abaixo clicando em *Insert Above/Below*.![](/files/AsJWH8L.png)
5. Adicione um novo campo conforme mostrado abaixo:![](/files/YGEuBrn.png)Para mais detalhes sobre como adicionar um campo de link personalizado, consulte [este link](https://erpnext.com/docs/user/manual /en/customize-erpnext/articles/creating-custom-link-field).
6. Adicione um segundo campo abaixo deste:![](/files/LoWglZL.png)Como isso funciona? Em Fetch from, estamos adicionando os seguintes detalhes: doctype.field. No doctype Terms and Conditions, o campo onde adicionamos os termos chama-se *terms* e é do tipo: Editor de Texto. Para *fetch from*to work, os dados devem estar no seguinte formato: link*field*name.field*to*fetch
7. Feito isso, clique em **Atualizar** e volte para sua lista. Clique em Ctrl + Shift + R para recarregar.
8. Ao selecionar o modelo de termos no driver, o sistema buscará as condições do modelo selecionado:![](/files/b7hVL7Y.png)