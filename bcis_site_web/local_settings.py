DEBUG = False
TEMPLATE_DEBUG = DEBUG
STATIC_SERVE = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':'/var/www/bcis_site_cms/project.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '', 
        'PORT': '',   
    }
}

