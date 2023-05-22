# Vídeo


**Os vídeos podem ser adicionados do Vimeo e do YouTube, usando o Video DocType.**


Você pode adicionar vídeos com seus URLs, descrições, miniaturas, etc. Alguns de seus usos são para manter o material educacional do curso e rastrear o envolvimento pessoal com vídeos do YouTube.


Para acessar os Vídeos, acesse:



> 
> Página inicial > Ferramentas > Vídeo
> 
> 
> 


## 1. Como criar um novo vídeo


1. Vá para a lista de vídeos e clique em Novo.
2. Digite o título do vídeo.
3. Selecione o provedor. O provedor de vídeo padrão é o YouTube.
4. Insira o URL para acessar o vídeo.
5. Opcionalmente, você pode adicionar uma data de publicação e a duração do vídeo em dias-horas-minutos-segundos.
6. Você também deve adicionar alguma descrição para ele.
7. Salvar.


Depois de salvar, você receberá uma provisão para adicionar uma imagem/miniatura para o vídeo.
![Video](/files/video-after-save.png)


Você também pode assistir ao vídeo no próprio documento depois de salvá-lo.
![Video](/files/video-watch.gif)


## 2. Recursos


### 2.1 Acompanhamento de análise de vídeo via YouTube


As estatísticas de vídeos do YouTube podem ser rastreadas e analisadas. Isso é útil para rastrear a contagem de visualizações e engajamento de um vídeo que você publicou.


Para isso, você deve primeiro ativar o rastreamento do YouTube em **Configurações de vídeo**:



> 
> Configurações de vídeo > Ativar rastreamento do YouTube
> 
> 
> 


Depois de habilitar isso, os campos **API Key** e **Frequency** ficarão visíveis.
![Video](/files/video-settings.png)


**Chave de API**: você pode gerar uma chave de API em seu [Google Developers Console](https://console.developers.google.com/). Você pode consultar a [Documentação da API de dados do YouTube](https://developers.google.com/youtube/v3/getting-started) para ver as etapas para gerar o mesmo.


**Frequência**: Você pode escolher com que frequência o sistema deve atualizar automaticamente suas estatísticas. As opções disponíveis são a cada 30 minutos, 1 hora, 6 horas e Diariamente (uma vez por dia).


Além da atualização automática, as estatísticas são atualizadas ao salvar. Assim, todos os vídeos criados/atualizados **após** habilitar o rastreamento do YouTube, terão estatísticas atualizadas ao salvar.
![Video](/files/video-stats.png)


### 2.2 Relatório de interações do YouTube


O relatório de interações do YouTube fornece uma visão consolidada de todos os engajamentos dos vídeos. O gráfico de barras fornece uma análise visual de curtidas x visualizações.


Você pode filtrar os dados do relatório pelo intervalo de datas de publicação.
![Video](/files/youtube-interactions.png)



> 
> **Observação**: a cota para o número de solicitações **não faturáveis** para a API de dados do YouTube é de 10.000 solicitações em setembro de 2020. O SOMA atualiza automaticamente até 50 vídeos em 1 solicitar. Da mesma forma, para 100 vídeos seriam necessárias 2 solicitações.  
> 
>  Supondo que 100 vídeos sejam atualizados **a cada hora** (frequência = 1 hora):  
> 
> 
> 
> * 2 solicitações serão enviadas por hora
> * 48 solicitações serão enviadas por dia
> 
> 
> 



> 
> Defina a frequência de acordo.
> 
> 
> 

