from .base import *
import envvars

env = envvars.get('DJANGO_ENV')

if env == 'production':
    from .prod import *
elif env == 'test':
    from .test import *
else:
    from .dev import *
