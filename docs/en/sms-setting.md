
# SMS Settings



**You can subscribe to an SMS provider to send SMS to mobile numbers.**


To integrate SMS in ERPNext, approach an SMS Gateway Provider who provides HTTP
API. They will create an account for you and will provide a unique username
and password.


To access SMS settings, go to:
> Home > Settings > SMS Settings


To configure SMS Settings in ERPNext, find out their HTTP API (a document
which describes the method of accessing their SMS interface from 3rd party
applications). In this document, you will get a URL which is used to send the
SMS using HTTP request. Using this URL, you can configure SMS Settings in
ERPNext.


Example SMS Gateway URL:



```
http://instant.smses.com/web2sms.php?username=&lt;username&gt;&amp;password;=&lt;password&gt;&amp;to;=&lt;mobilenumber&gt;&amp;sender;=&lt;senderid&gt;&amp;message;=&lt;message&gt;

```

![SMS Setting 2](/files/sms-settings2.jpg)


> Note: For SMS Gateway URL, only include the string before the "?".


Example:



```
http://instant.smses.com/web2sms.php?username=abcd&amp;password;=abcd&amp;to;=9900XXXXXX&amp;sender;
=DEMO&amp;message;=THIS+IS+A+TEST+SMS

```

The above URL will send SMS from account abcd to mobile number 9900XXXXXX with
sender ID as DEMO with a text message as "THIS IS A TEST SMS".


Note that some parameters in the URL are static. You will get static values
from your SMS Provider like username, password, etc. These static values should
be entered in the Static Parameters table.


![SMS Setting](/files/sms-settings1.png)


## How to configure ERPNext with Voip.ms


The first step is to login to voip.ms account. Then go **Main menu**, **SOAP and REST/JSON API**.
Enable the API, set a password and whitelist your server ip address.


Then go to DIDs and enable SMS on the number SMS will be sent from.


Set SMS Gateway to **https://voip.ms/api/v1/rest.php**


Set Message Parameter to **message**


Receiver Parameter to **dst**


Create 4 new Static Parameters:


* **api\_username** (voip.ms account username
* **api\_password** (the API password configured few minutes ago)
* **method** set value to **sendSMS**
* **did** (the 10 digits DID that will be used to send the sms)


![Voip.MS Setting](/files/voipms sms settings.jpg)


Then go to SMS Center to test if everything works properly.


### Related Topics


1. [Email Account](/docs/en/setting-up/email/email-account)
2. [Notifications](/docs/en/setting-up/notifications)
</message></senderid></mobilenumber></password></username>




