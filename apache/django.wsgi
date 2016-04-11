# -*- coding: utf-8 -*-
import os
import sys
import site

UPGRADING = False

project_dir = '/var/www/bcis_site_cms'
#site.addsitedir('/var/www/virtualenvs/bcis_site_cms_test/lib/python2.7/site-packages')
# Prepend path so as mptt in virtualenv take precedence over system one
#sys.path.insert(0, '/var/www/virtualenvs/bcis_site_cms_test/lib/python2.7/site-packages')
#sys.path.append('/var/www')
#sys.path.append(project_dir)

def upgrade_in_progress(environ, start_response):
    upgrade_file = os.path.join(project_dir, 'templates', '503.html')
    if os.path.exists(upgrade_file):
        response_headers = [('Content-type','text/html')]
        response = open(upgrade_file).read()
    else:
        response_headers = [('Content-type','text/plain')]
        response = "Mise à jour de l'application en cours... revenez dans quelques minutes."

    if environ['REQUEST_METHOD'] == 'GET':
        status = '200 OK'
    else:
        status = '403 Forbidden'
    start_response(status, response_headers)
    return [response]

if UPGRADING:
    application = upgrade_in_progress
else:
    os.environ['DJANGO_SETTINGS_MODULE'] = 'bcis_site_web.settings'
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
 
    #import django.core.handlers.wsgi
    #application = django.core.handlers.wsgi.WSGIHandler()

