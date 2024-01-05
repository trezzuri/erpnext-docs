
# Installing RediSearch to enable super fast E-commerce Search




> 
> **Experimental**
> 
> 
> 


The E-Commerce module of ERPNext optionally uses RediSearch to enable superfast search functionality which is configurable via **E Commerce Settings**.


Once installed and configured, RediSearch will be used to super charge the search functionality of the E-Commerce website. This includes features like fuzzy-word searching, autocomplete, results ranking and customizable field indexing.


### Pre-requisites


1. Frappe Framework + ERPNext Setup
2. Redis 6+


### Installation Instructions



```
$ git clone --recursive https://github.com/RediSearch/RediSearch.git
$ cd RediSearch
$ sudo make setup # Remove `sudo` on macOS
$ make build

```

On successful completion of the above instructions, a `redisearch.so` binary file will be generated in the `RediSearch/build` directory.


Move this binary to the `/etc` directory and restart your Frappe Server:



```
sudo mv build/redisearch.so /etc/

```

Now, open the `redis_cache.conf` file located in the `config` directory (inside the bench directory). Add the following line before the `save ""` line and then restart bench server:



```
loadmodule /etc/redisearch.so

```

This will load the redisearch module at startup. You can check if the module was loaded successfully by running the following command in the `redis-cli`:



```
> MODULE LIST

```

and `search` should be one of the modules.


You can also load the module on a running redis instance by running the following command in the `redis-cli`:



```
> MODULE LOAD /etc/redisearch.so

```


> 
> We placed the `redisearch.so` module in the `/etc` directory, but it can be placed anywhere in the file system. We have used this directory because in the future the `loadmodule` line will be populated in the config file automatically and it will assume the binary is in the `/etc` directory.
> 
> 
> 



> 
> More detailed instructions can be found [here](https://oss.redislabs.com/redisearch/Quick_Start/#building_and_running_from_source).
> 
> 
> 




