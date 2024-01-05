
# E-commerce Search



All Product Listing pages contain a **Search bar** that lets users quickly search for Website Items or Item Groups. It also stores recent searches that you can click on and reuse.


![Search](/files/e-commerce-search.png)


## RediSearch



> 
> **Experimental**: Requires Redis 6+
> 
> 
> 


By default ERPNext performs a simple DB search but you can **optionally** choose to use [RediSearch](https://redis.com/modules/redis-search/) for super fast search instead. You can refer to RediSearch's [installation documentation](/docs/en/e_commerce/articles/installing_redisearch_to_enable_super_fast_e_commerce_search).



> 
> Go to > **E Commerce Settings** > **Item Search Settings** > Check **Enable Redisearch**
> 
> 
> 


![Item Search Settings with RediSearch](/files/item-search-settings-enabled.png)


#### Settings without RediSearch


If RediSearch is not installed, this is what the **Item Search Settings** will look like:
![Item Search Settings without RediSearch](/files/item-search-settings.png)


#### Configurable Fields


Along with fast search you get the option to configure fields that you want search to consider. Add comma separated fields in the **Search Index Fields** text box to make them searchable.


E.g. Adding **brand** to these fields makes it searchable. Typing a brand, e.g. 'Apple', should give results where the brand is 'Apple'.


The results will be based on values in all the fields mentioned in the **Search Index Fields** text box.



> 
> Fields of the foll.g types are supported: **Link**, **Table MultiSelect**, **Data**, **Small Text**, **Text Editor**
> 
> 
> 




