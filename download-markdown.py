from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
from pprint import pprint
from googletrans import Translator  #  pip3 install googletrans==3.1.0a0
import os
import markdownify
import requests

# cuidado ao usar o translate, pois pode ter correções manuais direto nos arquivos
def main(translate=False):

    filesurl = "https://docs.erpnext.com"
    basepath = "./docs"
    translator = Translator()

    # abre arquivo txt para armazenar as urls processadas e não processar novamente no caso de erro.
    url_processadas = open(os.path.join("./", "urls.txt"), "a", encoding="utf-8")
   
    for page in pages():
        md = None

        # url já processada pula.
        if page in open("urls.txt", "r", encoding="utf-8").read():
            continue
        
        file_folder = "/" + page.split("/manual/en/")[-1] # pastas e nome do arquivo.
        path = "/".join(file_folder.split("/")[:-1]) # retira o nome do arquivo.
        
        if not os.path.exists(basepath + "/en" + path):
            os.makedirs(basepath + "/en" + path)
        if not os.path.exists(basepath + "/pt" + path):
            os.makedirs(basepath + "/pt" + path)

        # trata páginas com erro HTTP
        try:
            html = urlopen(page).read()
            soup = BeautifulSoup(html, features="html.parser")
            md = soup.find('div',{'class':'from-markdown'}) # obtem a tag com o conteudo markdown
        except HTTPError as e:
            print("Página: " + str(page) + " Erro HTTP:", e)

        # se não tiver class from-markdown ou md não estiver sido definido, pula iteração
        if not md:
            url_processadas.write(page + "\n") # não processa novamente
            continue

        title = md.find('div',{'class':'align-items-center'}).contents[1] # obtem o titulo do texto que está em um div
        md.find('div',{'class':'align-items-center'}).replace_with(title) # substitui o div pelo seu conteudo
        md.find('div', {'class': 'modal revisions-modal fade'}).decompose() # remove a div de versões anterior

        # em alguns casos tem esse input, remove para não interferir na tradução.
        input = md.find('input', {'class': 'd-none', 'name': 'wiki-page-name', 'value': '1ea1f51ff5'})
        if input is not None:
            input.decompose()
        
        # busca e download das imagens 
        for img in md.findAll('img'):
            if 'src' in img.attrs:
                imgname = img['src'].split("/")[-1] # obtem o nome do arquivo
                if imgname and not os.path.exists("./files/" + imgname):
                    # cria a pasta de files.
                    if not os.path.exists("./files/"):
                        os.makedirs("./files/")
                    try:
                        img_data = requests.get(filesurl + img['src']).content
                    except:
                        print(img['src'] + ' falhou no download')
                    else:
                        img['src'] = "/files/" + imgname # troca o local da imagem
                        with open("./files/" + imgname, 'wb') as handler:
                            handler.write(img_data)

        content_en = md.decode_contents()
        content_en = markdownify.markdownify(content_en, heading_style="ATX") # converte html para markdown     
        content_en = content_en.replace("/docs/v13/user/manual/en/", "/docs/en/") # substitui os links da documentação original
        content_en = content_en.replace("/docs/v14/user/manual/en/", "/docs/en/") # substitui os links da documentação original
        content_en = content_en.replace("/docs/v13/user/videos/", "https://docs.erpnext.com/docs/v13/user/videos/")
        content_en = content_en.replace("/docs/v14/user/videos/", "https://docs.erpnext.com/docs/v14/user/videos/")
        #content_en = content_en.replace("ERPNext", "SOMA")
        #content_en = content_en.replace("ERPnext", "SOMA")
        content_en = content_en.replace("{{", "&lcub;&lcub;") # substitui as chaves pois senão dá erro no markdown quando instalado no frappe
        
        fname = basepath + "/en" + file_folder + ".md"

        f = open(fname, "w")
        f.write(content_en)
        f.close()

        if translate:
            content_pt = md.decode_contents()

            # conteudo > 10000 precisa dividir para traduzir
            if len(content_pt) > 10000:
                fechamento = content_pt[:10000].rfind('>') # primeiro fechamento de tag
                texto1 = content_pt[:fechamento + 1]  # +1 para incluir o ">"
                texto1 = translator.translate(texto1, src='en', dest='pt').text
                texto2 = content_pt[fechamento + 1:] 
                texto2 = translator.translate(texto2, src='en', dest='pt').text
                content_pt = texto1 + texto2
            else:
                content_pt = translator.translate(content_pt, src='en', dest='pt').text # traduz para portugues 

            # correções devido o tradutor.
            content_pt = content_pt.replace("< ", "<")
            content_pt = content_pt.replace("< /", "</") 
            content_pt = content_pt.replace(" p>", "</p>")
            content_pt = content_pt.replace(". png", ".png")
            content_pt = content_pt.replace(" .png", ".png")  
            content_pt = content_pt.replace(" .jpg", ".jpg")
            content_pt = content_pt.replace(". jpg", ".jpg")
            content_pt = content_pt.replace(". gif", ".gif")
            content_pt = content_pt.replace(" .gif", ".gif")
            content_pt = content_pt.replace("- ", "-")
            content_pt = content_pt.replace(" -", "-")  
            content_pt = content_pt.replace(" /", "/")
            content_pt = content_pt.replace("/ ", "/")
            content_pt = content_pt.replace(" )", ")")
            content_pt = content_pt.replace("< br", "<br")
            content_pt = content_pt.replace("< a", "<a")
            content_pt = content_pt.replace("Screenshot de", "Screenshot from")
            content_pt = content_pt.replace("Captura de tela", "Screenshot")
            content_pt = content_pt.replace("em class=", "class=")
            content_pt = content_pt.replace("/erpnext/arquivos", "/erpnext/files")
            content_pt = content_pt.replace("/privado/arquivos", "/private/files")
            content_pt = content_pt.replace("docs. erpnext", "docs.erpnext")
            content_pt = content_pt.replace("erpnext .com", "erpnext.com")
            content_pt = content_pt.replace("<código>", "<code>")
            content_pt = content_pt.replace("</código>", "</code>")
            content_pt = content_pt.replace("\_", "_")
            content_pt = content_pt.replace("< /span>", "</span>")
            ###

            content_pt = markdownify.markdownify(content_pt, heading_style="ATX") # converte html para markdown 
            content_pt = content_pt.replace("/docs/v13/user/manual/en/", "/docs/pt/") # substitui os links da documentação original
            content_pt = content_pt.replace("/docs/v14/user/manual/en/", "/docs/pt/") # substitui os links da documentação original
            content_pt = content_pt.replace("/docs/v13/user/videos/", "https://docs.erpnext.com/docs/v13/user/videos/")
            content_pt = content_pt.replace("/docs/v14/user/videos/", "https://docs.erpnext.com/docs/v14/user/videos/")
            content_pt = content_pt.replace("{{", "&lcub;&lcub;") # substitui as chaves pois senão dá erro no markdown quando instalado no frappe

            # lines = content_pt.strip().split('\n')  # divide em linhas e remove espaços em branco
            # title = lines[0].lstrip('#').strip()  # remove '#' do título e espaços em branco extras
            # block_content = "\n".join(lines[1:])  # obtém o restante do conteúdo

            # content_pt_jinja = (
            # "{% extends 'templates/web.html' %}\n"
            # "{%- block title -%}"+title+"{%- endblock -%}\n"
            # "{% block navbar %}\n"
            # "<div style='position: fixed; left: 0; top: 0; bottom: 0; width: 250px; background-color: #f2f2f2; padding: 10px; overflow-y: scroll;'>\n"
            # "{index}\n"  
            # "</div>\n"
            # "{% endblock %}\n"
            # "{% block page_content %}\n"
            # + "\n# " + title + "\n"
            # + block_content
            # + "\n{next}\n"  
            # "{% endblock %}\n"
            # )

            fname = basepath + "/pt" + file_folder + ".md"
            f = open(fname, "w")
            f.write(content_pt)
            f.close()

        # adiciona a url no arquivo txt para controle, ao fim do código pois se der erro não deve adicionar.
        url_processadas.write(page + "\n")


def pages(translate=False):

    # adiciona no vetor todas as urls através do sitemap.xml
    sitemap_url = "https://docs.erpnext.com/sitemap.xml"
    response = requests.get(sitemap_url)
    pages = []

    if response.status_code >= 400:
        print("Requisição para sitemap.xml falhou. Status:" + str(response.status_code))
        return

    soup = BeautifulSoup(response.text, "html.parser")
    loc_tags = soup.find_all("loc")

    for loc in loc_tags:
        if "/manual/en" in loc.text: #  somente urls com /manual/en
            pages.append(loc.text)
   
    return pages

main(True) # cuidado ao usar o translate, pois pode ter correções manuais direto nos arquivos