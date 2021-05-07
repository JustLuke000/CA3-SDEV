# CA3-SDEV
## DT282 Software for the Global Market 2 – Final Report

Student Number: C19300696

Student Name: Luke O’Shea Scanlan

Group Name: Luke O’Shea Scanlan and Igor Alekhnovych

## My Django Application
http://localhost:8000/en/appone/

## Changing the language 

 

Changing the language (and inadvertently changing the template) is shown above. The languages are presented in their own language regardless of current region to help users navigate to a page they would be more familiar with.
Indicating progress  
Above you can see the Achievement template display the progress from scrolling down the page. 
An Attempt was made to include a buffering circle as the page loaded but this was later omitted from both websites for one of two reasons, the website loaded too quickly for me to see the buffering or alternatively the buffering circle did not work. Below you can see the code implementation as well as what it would have looked like.

Code - CSS
```CSS
.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}
.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #fff;
  border-color: #fff transparent #fff transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}
```
Code - HTML
```html
<div class="lds-dual-ring"></div>
```
What It Looked Like
  
These above “Loader” assets (HTML , CSS and photo) were taking from https://loading.io/css/
And were released under CC0 License

The decision to only include a progress loader on the Achievement template was because how typically members from that cultural dimension have a preference to track their own progress (2017, Aubrey Daniels ) .

## Layout

 
Achievement (Left) - Ascription (Right)
As you can see above the websites were able to follow the templates and wireframes from CA2 quite closely. The most noticeable difference is the navigation bar. 

For Achievement, users do not usually mind navigating a page to find something for themselves and having a fixed navigation bar (Assuming the information is stored in a relevant and intuitive structure – i.e., Addresses and phone numbers in on a “Contact us” page). 

For Ascription, my “what is what” concept discussed in previous submissions returns to play a large role in this design as it greatly alters the visual aspect of this page. The fixed navigation bar allows the user to jump to a different page immediately. It also acts a “servant” to the user, the bar is “showing respect to people in authority [the user]”  (2012, Mind Tools Content Team) by always being by the users side and moving with their actions.

## Interaction
 
Above you can see the feedback given to the user, the image itself is quite self-explanatory implying where the user is with a full white colour, the hovered colour is slightly more grey than white and then the unselected tab is the darkest shade of grey.





## Managing navigation
 
Breadcrumbs were included in the Ascription and Omitted from the Achievement Site. Referencing the Ascription wireframe from previous submissions, the breadcrumbs were particularly more vibrant and an important part of the website. I have found from my own research and browsing of websites in Ireland (a primarily Achievement Culture) there is a considerable lack of breadcrumbs across a majority of large corporate and professional websites.

Setting up Django for Internationalization and Localization
[Adapted from SGM2-Practical Class 5 - Instructions Part TWO]
Create Folder “locale” in project directory and add path in settings.py:
```py
import os
LOCALE_PATHS = (
    os.path.join(os.path.dirname(__file__), "locale"),
)
```

Add highlighted line to Middleware (in settings.py):

```py
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

Add highlighted line to Templates (in settings.py):
```py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['CA3Project/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

Now that you have set up the pathing and implementation for Internationalization and Localization ensure that you have the following set to true (in settings.py):
```py
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
```



Now set your language codes for locale (in settings.py):
```py
from django.utils.translation import ugettext_lazy as _
LANGUAGE = (
    ('fr', _('French')),
    ('en', _('English')),
    ('uk', _('Ukrainian')),
)
```

If all the above have been done correctly you should now be able to type (in terminal) to retrieve tagged text:
```
python manage.py makemessages -l fr
python manage.py makemessages -l ua
```
 
This creates the respective “language_code” directory and .po file.
Using POedit (mentioned later) you can now translate the text enclose in {% trans “” %}.
 
Be sure to hit save and a .mo file will be created for Django to interpret.














## Folder Structure
 



## Identifying text requiring translation within your application 
Code
<li class="nav-item">
<a class="nav-link active" href="#">
{% trans "Our Story" %}
</a></li>

## Extracting text requiring translation
Gettext
“GNU gettext is an important step for the GNU Translation Project, as it is an asset on which we may build many other steps” , (1998, GNU Operating System). Gettexts’ library supports the cataloguing of languages and can be utilised efficiently in Django and POEdit.

Code
```
{% get_language_info for LANGUAGE_CODE as lang %}
```

## Making translated text accessible within your application & Managed the loading/display of resources to support resources needed for culturalization.

Code – Found At the beginning of all HTML files
```
{% load i18n %}
{% load static %}
{% load change_lang %}
```
 
“The fastest and most convenient way to translate apps & sites with gettext” , (2021, Václav Slavík).
This program utilises the GNU gettext mentioned above in this python project to retrieve “msgid” and returns the “msgstr”, in other words, finds the text enclosed with {% trans “” %} in the HTML, translates it and then displays the translated text.


## Handling the date
```html
<pid="local-date">{%now"DATE_FORMAT"%}-{%now"TIME_FORMAT"%}</p>
```


|Python Version:| 3.9 |


| Packages Installed | Versions |
|-----------|-----------|
| Django | 3.2.2 |
| asgiref | 3.3.4 |
| pip | 21.1.1 |
| pytz | 2020.5 |
| setuptools | 56.0.0 |
| ssqlparse | 0.4.1 |


## Photographs

Photographs which were used in the main body of the websites are my own (photo (*).jpg filenames). All other photographs are from Lucian Potlog  a Dublin based photographer.


## Content
Since the target website has shut down, I was unable to retrieve information for the “Our Story” section of the website. “Timemachine” and archive websites which take snapshots of other websites also did not include this page, most of which, only including the home page it any page at all. As a result, I have filled the text with lorem ipsum filler text.
