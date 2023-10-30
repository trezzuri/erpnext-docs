
# Twitter Settings




> Note: This integration doesn't work anymore due to Twitter's API changes. This has been removed from ERPNext starting from v15.
> 
> 

Twitter related settings like OAuth can be configured here. ERPNext needs access to the API through which the post is shared and achieved using OAuth 2.0 Authentication Protocol.

## 1. How to set up Twitter App

You must have Twitter App for your company. ERPNext interacts with this App for sharing Tweet.

### 1.1 Create Twitter Developer App

Create App by link `https://developer.twitter.com/` and check that the App has **Read and write** Access permission. ![Twitter App Permission](/files/twitter-app-permission.png)  


### 1.2. Configure Callback URL

1. Select your App and go to **App Details**.
2. Then go to **Edit** and click **Edit Details**.
3. Add your website URL in **Callback URLs** like: `https://{yoursite}/api/method/erpnext.crm.doctype.twitter_settings.twitter_settings.callback`
4. Click **Save** to make changes.

![Twitter App Callback URL](/files/twitter-callback-url.png)  


## 2. How to set up Twitter Settings

To access Twitter Settings, go to:


> Home > CRM > Settings > Twitter Settings
> 
> 

![Twitter Settings](/files/twitter-settings.png)  


### 2.1 API Key and API Key Secret

You get **API Key** and **API Key Secret** from your Twitter Developer account go to:


> `https://developer.twitter.com/` > My Apps > `{Your App}` > Keys and tokens
> 
> 

![Twitter Keys Tokens](/files/twitter-key-token.png)  


Once you save the doc by filling **API Key** and **API Key Secret** it will redirect to Twitter's sign-in page by providing valid Twitter credentials and clicking **Authorize app**, the member approves your application's request to access their member data and interact with Twitter. ![Twitter Authorize App](/files/twitter-authorize-app.png)  





