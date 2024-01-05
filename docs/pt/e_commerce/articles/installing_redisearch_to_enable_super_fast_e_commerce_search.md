# Instalando o RediSearch para permitir uma pesquisa de comércio eletrônico super rápida




> 
> **Experimental**
> 
> 
> 


O módulo de comércio eletrônico do ERPNext usa opcionalmente RediSearch para ativar a funcionalidade de pesquisa super rápida que pode ser configurada através de **Configurações de comércio eletrônico**.


Depois de instalado e configurado, o RediSearch será usado para turbinar a funcionalidade de pesquisa do site de comércio eletrônico. Isso inclui recursos como pesquisa de palavras difusas, preenchimento automático, classificação de resultados e indexação de campos personalizáveis.


### Pré-requisitos


1. Estrutura Frappe + Configuração do ERPNext
2. Redis 6+


### Instruções de instalação



```
$ git clone--recursive https://github.com/RediSearch/RediSearch.git
$ cd RediSearch
$ sudo make setup # Remova `sudo` no macOS
$ fazer construir

```

Após a conclusão bem-sucedida das instruções acima, um arquivo binário `redisearch.so` será gerado no diretório `RediSearch/build`.


Mova este binário para o diretório `/etc` e reinicie seu servidor Frappe:



```
sudo mv build/redisearch.so/etc/

```

Agora, abra o arquivo `redis_cache.conf` localizado no diretório `config` (dentro do diretório do bench). Adicione a seguinte linha antes da linha `save ""` e reinicie o servidor bench:



```
loadmodule/etc/redisearch.so

```

Isso carregará o módulo de nova pesquisa na inicialização. Você pode verificar se o módulo foi carregado com sucesso executando o seguinte comando no `redis-cli`:



```
> LISTA DE MÓDULOS

```

e `search` devem ser um dos módulos.


Você também pode carregar o módulo em uma instância do redis em execução executando o seguinte comando no `redis-cli`:



```
> MODULE LOAD/etc/redisearch.so

```


> 
> Colocamos o módulo `redisearch.so` no diretório `/etc`, mas ele pode ser colocado em qualquer lugar do sistema de arquivos. Usamos este diretório porque no futuro a linha `loadmodule` será preenchida automaticamente no arquivo de configuração e assumirá que o binário está no diretório `/etc`.
> 
> 
> 



> 
> Instruções mais detalhadas podem ser encontradas [aqui](https://oss.redislabs.com/redisearch/Quick_Start/#building_and_running_from_source).
> 
> 
> 



