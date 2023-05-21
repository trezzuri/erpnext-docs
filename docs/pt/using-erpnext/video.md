# Vídeo


**Os vídeos podem ser adicionados do Vimeo e do YouTube, usando o Video DocType.**


Você pode adicionar vídeos com seus URLs, descrições, miniaturas, etc. Alguns de seus usos são para manter o material educacional do curso e rastrear o envolvimento pessoal com vídeos do YouTube.


Para acessar os vídeos, acesse:



>
> Início > Ferramentas > Vídeo
>
>
>


## 1. Como criar um novo vídeo


1. Vá para a lista de vídeos e clique em Novo.
2. Digite o título do vídeo.
3. Selecione o Provedor. O provedor de vídeo padrão é o YouTube.
4. Digite a URL para acessar o vídeo.
5. Opcionalmente, você pode adicionar uma data de publicação e duração do vídeo em dias-horas-minutos-segundos.
6. Você também deve adicionar alguma descrição para ele.
7. Salve.


Depois de salvar, você receberá uma provisão para adicionar uma imagem/miniatura para o vídeo.
![Vídeo](/files/video-after-save.png)


Você também pode assistir ao vídeo no próprio documento depois de salvá-lo.
![Vídeo](/files/video-watch.gif)


## 2. Características


### 2.1 Rastreamento de análise de vídeo via YouTube


As estatísticas de vídeo do YouTube podem ser rastreadas e analisadas. Isso é útil para rastrear a contagem de visualizações e o engajamento de um vídeo que você publicou.


Para isso, você deve primeiro ativar o rastreamento do YouTube em **Configurações de vídeo**:



>
> Configurações de vídeo > Ativar rastreamento do YouTube
>
>
>


Depois de habilitá-lo, os campos **API Key** e **Frequency** ficarão visíveis.
![Vídeo](/files/video-settings.png)


**Chave de API**: você pode gerar uma chave de API em seu [Google Developers Console](https://console.developers.google.com/). Você pode consultar a [documentação da API de dados do YouTube](https://developers.google.com/youtube/v3/getting-started) para obter as etapas para gerar o mesmo.


**Frequência**: Você pode escolher com que frequência o sistema deve atualizar automaticamente suas estatísticas. As opções disponíveis são a cada 30 minutos, 1 hora, 6 horas e Diariamente (uma vez por dia).


Além da atualização automática, as estatísticas são atualizadas ao salvar. Assim, todos os vídeos criados/atualizados **após** habilitar o rastreamento do YouTube, terão estatísticas atualizadas ao salvar.
![Vídeo](/files/video-stats.png)


### 2.2 Relatório de interações do YouTube


O relatório de interações do YouTube fornece uma visão consolidada de todos os engajamentos dos vídeos. O gráfico de barras fornece uma análise visual de curtidas x visualizações.


Você pode filtrar os dados do relatório pelo intervalo de datas de publicação.
![Vídeo](/files/youtube-interactions.png)



>
> **Observação**: a cota para o número de solicitações **não faturáveis** para a API de dados do YouTube é de 10.000 solicitações em setembro de 2020. O ERPNext atualiza automaticamente até 50 vídeos em 1 solicitação. Da mesma forma, para 100 vídeos seriam necessários 2 pedidos.
>
> Supondo que 100 vídeos sejam atualizados **a cada hora** (frequência = 1 hora):
>
>
>
> * 2 solicitações serão enviadas por hora
> * 48 solicitações serão enviadas por dia
>
>
>



>
> Por favor, defina a frequência de acordo.
>
>
>