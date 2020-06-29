"""
WSGI config for netdelta project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""
import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/home/iantibble/jango/netdelta_11115/local/lib/python2.7/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('/home/iantibble/netdelta_sites/ndwww/')
sys.path.append('/home/iantibble/netdelta_sites/ndwww/ndwww')

os.environ['DJANGO_SETTINGS_MODULE'] = 'ndwww.settings'

# Activate your virtual env
# activate_env=os.path.expanduser("/home/iantibble/jango/netdelta_11115/bin/activate_this.py")
# execfile(activate_env, dict(__file__=activate_env))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

