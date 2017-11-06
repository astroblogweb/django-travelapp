import os
if os.environ.get('DJANGO_DEVELOPMENT') is not None:
    from settings_development import *
    print("in development mode")
else:
    from settings_production import *
    print("in production mode")


