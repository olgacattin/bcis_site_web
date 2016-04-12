DEBUG = False
TEMPLATE_DEBUG = DEBUG
STATIC_SERVE = False
ADMINS = [('Olga', 'olga.cattin@vaubantechnologies.com'), ('Claude', 'claude@2xlibre.net')]

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

