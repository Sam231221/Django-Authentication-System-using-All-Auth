import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_@j651u)$nuc5v=73@4#e$7&4(m8fxc*aer5v0&6qh)#4r++7u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',  #needed for all auth
    'django.contrib.staticfiles',
    
    'MAllAuthForm.apps.MallauthformConfig',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
     'allauth.socialaccount.providers.google',
     'allauth.socialaccount.providers.facebook',
  #  'social_django',
]
 
SITE_ID = 1   #needed since we use sites app


# Additional configuration settings
SOCIALACCOUNT_QUERY_EMAIL = True
ACCOUNT_LOGOUT_ON_GET= True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_REQUIRED = True

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

]



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'AConfig.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR.joinpath('templates'))],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                
                # `allauth` needs this from django
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                 
                'social_django.context_processors.backends',  # <-- Here
                'social_django.context_processors.login_redirect', # <-- Here
                 
                 
            ],
        },
    },
]

LOGIN_REDIRECT_URL = 'home'

#SMTP CONFIGURATION
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
#THIS IS YOUR LOGIN INFO FOR GMAIL ADDRESS
EMAIL_HOST_USER = 'dimensionalassistanceteam37@gmail.com'
EMAIL_HOST_PASSWORD = '123@gmailcom'

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    },
    'facebook': {
        'METHOD': 'oauth2',
        'SDK_URL': '//connect.facebook.net/{locale}/sdk.js',
        'SCOPE': ['email', 'public_profile'],

    }
}
WSGI_APPLICATION = 'AConfig.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
"""
When you define a model in Django without specifying a primary key, Django will automatically create a primary key for you. The primary key is set to be an integer. If you want to override the field type, you can do so on a per model basis.

Starting in Django 3.2, you can now customise the type of the automatically created primary key in your settings.

Starting new projects in Django 3.2, the default type for primary keys is set to a BigAutoField which is a 64 bit integer. However, earlier versions set the type of implicit primary keys to be integers.

This means that when you upgrade to 3.2, you will start to see warnings about the fact that you do not have an explicitly defined primary key type. Satisfying Django's requirements for an explicitly set primary key type is easy enough, but you also need to choose whether or not you want to upgrade your primary key field types from integer to 64 bit integer.

There are a few ways to fix this. Broadly speaking they fall into two categories

Configure DEFAULT_AUTO_FIELD in settings

Open your project's settings.py and add a new line at the bottom of the file

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
Setting on a per app basis

If you prefer to set your field type on a per app basis rather than for the whole project, you can specify this in apps.py.

            from django.apps import AppConfig

            class MyappConfig(AppConfig):
                default_auto_field = 'django.db.models.AutoField'
                name = 'Myapp'
            Set AutoField or BigAutoField on a per model basis
            
            

If you prefer even more fine grained control, you can set a per model id field.

            class Model1(models.Model):
                id = models.BigAutoField(primary_key=True)
    
    
allauth.EmailAddress: (models.W042) Auto-created primary key used when not defining a primary key type, by 
default 'django.db.models.AutoField'.
        HINT: Configure the DEFAULT_AUTO_FIELD setting or the AppConfig.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.
allauth.EmailConfirmation: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
        HINT: Configure the DEFAULT_AUTO_FIELD setting or the AppConfig.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.
"""