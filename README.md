# Quick Share-Social-Media-Project-Using-Django
 Quick Share social media project one of my best project using django. Where i used django as a framework. Using some core and custom function it's made like insta clone project, where user can signup, login and post their photos with captions and also follow others user and user also can like and comment followers and foillowing users posts.


![Quick-Share-Profile](https://github.com/NowshadRuhan/Quick-Share-Social-Media-Project-Using-Django/blob/master/Quick-Share%20Profile.png?raw=true) 

## About Project:
**In this project i used  two apps, media folder, static folder, templates and others pip library/packages.**

## About Crispy forms in python:
Django-crispy-forms supports several frontend frameworks, such as Twitter Bootstrap (versions 2, 3, and 4), Uni-form and Foundation. You can also easily adapt your custom company's one, creating your own, see the docs for more information. You can easily switch among them using CRISPY_TEMPLATE_PACK setting variable.

### Installing django-crispy-forms:

**Install latest stable version into your python environment using pip:**
- pip install django-crispy-forms

**If you want to install development version (unstable), you can do so doing:**
- pip install git+git://github.com/django-crispy-forms/django-crispy-forms.git@dev#egg=django-crispy-forms

**Once installed add crispy_forms to your INSTALLED_APPS in settings.py:**
```
INSTALLED_APPS = (
    ...
    'crispy_forms',
)
```
**For add template packs within django-crispy-forms: **

```
#bootstrap, bootstrap3, bootstrap4, uni-from
CRISPY_TEMPLATE_PACK = 'bootstrap4'
```
### About Media Files in Django:
In Django, files which are uploaded by the user are called Media or Media Files. Here are some examples:
1. A user uploaded image, pdfs, doc files etc while publishing a post.
2. Images of products in an e-commerce site.
3. User's profile image. etc...

**Just as with static files, to serve media files we have do add some configurations in our settings.py file.**

#### Media Files Configurations:
Media files depend upon two configurations,
1. MEDIA_ROOT,
2. MEDIA_URL

**In settings.py file:**
```
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_ROOT  = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```
**In the main project urls.py file: **
```
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```


### About Static File in Django:
In static folder we store our all of css, js, bootstrap file to use those file in our project.

**Settings added**
```
from django.conf import settings
```
**static and static_url added**
```
from django.conf.urls.static import static
```
**for load static folder in templates**
```
{% load static %}
```

# About Project Apps:
 
   **In this project i used two web-app this are App_login & App_Post .**
   **And database i used in this project is sqlite-3.**
   
   1. App-login :
      - In app login i create one custom model which is connected to Django provided User model in One-To-One connection. And this model used for signup and user- profile part also. The model name is UserProfile.
      - And then also create another model which is follow. This model control peoples follower and following part .
      - #### App-login forms :
            - I used two django provided forms those are UserCreationForm and AuthenticationForm.
            - Using this two forms and my UserProfile model i create three forms for app-login.
            - Those are CreateNewUser, UserLoginForm and UserProfileForm.
   
