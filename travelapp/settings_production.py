
SECRET_KEY = 'nd!n#7j4j0clmf_pmayl(sh3-2codjso_ud9g8ey(5$txzp5n^'  # for django leaflet

DEBUG = False

ALLOWED_HOSTS = ['54.165.36.179','localhost','127.0.0.1']


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
    # 'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.twitter',

]

SITE_ID=3

fillPath = lambda x: os.path.join(os.path.dirname(__file__), x)
GEOPOSITION_GOOGLE_MAPS_API_KEY = 'AIzaSyCHYjIn-8XQ_C0X8PfCrgNiRR-BgNBB0Vs'
GOOGLE_API_KEY = 'AIzaSyCHYjIn-8XQ_C0X8PfCrgNiRR-BgNBB0Vs'
EASY_MAPS_GOOGLE_MAPS_API_KEY = 'AIzaSyCHYjIn-8XQ_C0X8PfCrgNiRR-BgNBB0Vs'
#################GDAL_LIBRARY_PATH='/usr/lib/ogdi/libgdal.so'   #'/home/ubuntu/anaconda3/pkgs/libgdal-2.2.1-0/lib/libgdal.so'
#SPATIALITE_LIBRARY_PATH = 'mod_spatialite'
SECRET_KEY = '_omc6hxq40u11no0uvi&g__lzj2n^4-dk#l#i+7+vgng!-bb^)'    # for django-leaflet
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

