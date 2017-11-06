"""
Django settings for travelapp project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import django
#import dj_database_url
import mimetypes
#from importlib import import_module   # for social_auth - not works
#from django.utils.module_loading import import_module # social_auth - not works


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#print("BASE_DIR:",BASE_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'nd!n#7j4j0clmf_pmayl(sh3-2codjso_ud9g8ey(5$txzp5n^'


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
    'django.contrib.staticfiles',
    'geoposition',
    'easy_maps',
    'placeslist',
    'geopositioning',
#    'googlemaps.waypoints',
#    'weatherstations','django.contrib.gis',
    'placesdata',
    'django_tables2',
    'leaflet',
    'djgeojson',
#    'mushrooms',
    'contactus',
    'analysis',
    'rest_framework',
    'blog',
    'polls',
    'geomaps',
    'opinions',
    'fortune',
    'infographicsresume',
    # 'floppyforms',
    #'social_auth',   # old
    'social_django',  # only gihub used as of now..
    'django.contrib.sites', # for allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.twitter',

]

# # social auth
# SOCIAL_AUTH_GITHUB_KEY = '9d3ba67271e7a8035a2a'
# SOCIAL_AUTH_GITHUB_SECRET = 'a718092fa0aa0b96346501a5afeb337382208610'
# ### Auth callback URI: http://localhost:8000/oauth/complete/github/   # works!!
# SOCIAL_AUTH_TWITTER_KEY = ' YRBvW89OxoC6RI7EqRAITiW54'
# SOCIAL_AUTH_TWITTER_SECRET = 'JXTfC5wn4p9SAqahj6MJdma1NPquSEeZewFxKaPCc6JPxwsXK7'
# ### Auth callback URI : 'localhost' doesnt work:
# # http://127.0.0.1:8000/complete/twitter/            #### still pending

# for all_auth
#SITE_ID = 1 # for example site from website..and
# https://stackoverflow.com/questions/14019017/django-allauth-no-facebook-app-configured-please-add-a-socialapp-using-the-djan
SITE_ID=2
#SOCIALACCOUNT_PROVIDERS = {'facebook': {},'google':{}, 'twitter':{}}
SOCIALACCOUNT_PROVIDERS =  {'facebook':
                               {'METHOD': 'oauth2',
                                'SCOPE': ['email'],
                                'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
                                'LOCALE_FUNC': lambda request: 'en_US',
                                'VERSION': 'v2.4'
                               },
                            'google':{ 'SCOPE': ['email'],
                               'AUTH_PARAMS': { 'access_type': 'online' }
                             },
                            'twitter':{}
                           }



REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',
    ],
    'PAGE_SIZE': 10
}

mimetypes.add_type("text/css", ".css", True)

GEOPOSITION_MAP_OPTIONS = {
    'minZoom': 3,
    'maxZoom': 15,
}

GEOPOSITION_MARKER_OPTIONS = {
    'cursor': 'move'
}

fillPath = lambda x: os.path.join(os.path.dirname(__file__), x)
GEOPOSITION_GOOGLE_MAPS_API_KEY = 'AIzaSyCHYjIn-8XQ_C0X8PfCrgNiRR-BgNBB0Vs'
#EASY_MAPS_GOOGLE_MAPS_API_KEY = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ___0123456789'
EASY_MAPS_GOOGLE_MAPS_API_KEY = 'AIzaSyCHYjIn-8XQ_C0X8PfCrgNiRR-BgNBB0Vs'
EASY_MAPS_CENTER = (27, 88)
#EASY_MAPS_GEOCODE = 'example.custom_geocode'
#GDAL_LIBRARY_PATH = '/home/ubuntu/anaconda3/envs/web1/lib/libgdal.so'
#GDAL_LIBRARY_PATH='/usr/lib/libgdal.so.1'
#GDAL_LIBRARY_PATH='/usr/lib/ogdi/libgdal.so'
GDAL_LIBRARY_PATH='/home/ubuntu/anaconda3/pkgs/libgdal-2.2.1-0/lib/libgdal.so'    # '/usr/lib/ogdi/libgdal.so'  on aws
#SPATIALITE_LIBRARY_PATH = 'mod_spatialite'
SECRET_KEY = '_omc6hxq40u11no0uvi&g__lzj2n^4-dk#l#i+7+vgng!-bb^)'    # for django-leaflet
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    #'django.middleware.csrf.CsrfResponseMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',

]

ROOT_URLCONF = 'travelapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(os.path.dirname(__file__), 'templates'),fillPath('templates'),os.path.join(BASE_DIR, 'templates','admin'),
os.path.join(BASE_DIR,'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',

            ],
        },
    },
]


SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    'social_core.pipeline.social_auth.associate_by_email',
)


#print("templates dir:",TEMPLATES[0]['DIRS'])

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'admin_tools.template_loaders.Loader',
    'django.template.loaders.cached.Loader',
    'apptemplates.Loader',
)

WSGI_APPLICATION = 'travelapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
'''
DATABASES = {
    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': BASE_DIR + '/traveldb.postgresql',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'traveldb',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

SOCIAL_AUTH_URL_NAMESPACE = 'social'
AUTHENTICATION_BACKENDS = (
    'social_core.backends.open_id.OpenIdAuth',
    'social_core.backends.google.GoogleOpenId',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.google.GoogleOAuth',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.yahoo.YahooOpenId',
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
)
# allauth
EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'  # for allauth
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
#   works and sends email verifications : ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_USERNAME_REQUIRED = False


LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'homepage'
LOGOUT_REDIRECT_URL = 'homepage'  #
APPEND_SLASH = False


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/


STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
#print("static_root:",STATIC_ROOT, "static_url:",STATIC_URL)

LEAFLET_CONFIG = {'SPATIAL_EXTENT': (4.0, 44.0, 7.5, 46)}
