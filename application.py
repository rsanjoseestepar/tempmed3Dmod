"""
WSGI config for h3d project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
#extra para deplyment en eb
os.environ["DJANGO_SETTINGS_MODULE"] = "med3Dmodel.settings"



#termina el extra
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "med3Dmodel.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()