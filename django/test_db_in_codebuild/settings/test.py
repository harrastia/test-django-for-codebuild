# -*- coding: utf-8 -*-
import string
from random import choice
from os import environ

# default the test runner to be nose runner unless set in environment
from .base import *

DEBUG = False
TEMPLATE_DEBUG = False

# Opsware tests need admin ui
ENABLE_ADMIN_UI = True

ADMINS = (

)


# Use default as read replica for tests
REPLICA_DB_ALIAS = 'default'

DATABASES = {
    'default': {
        'ENGINE': 'vaultcommon.testutils.test_db_backends.backends.postgresql_psycopg2',
        'NAME': 'test_db',
        'USER': 'test_db_dev',
        'PASSWORD': 'test_db_dev',
        'HOST': '127.0.0.1',
        'PORT': '5432',  
        'ATOMIC_REQUESTS': True,
        'TEST_NAME': "{}_{}".format(
            "".join([choice(string.ascii_letters)
                     for i in xrange(1, 10)]), "test_db_dev"),
        'ATOMIC_REQUESTS': True,
    },
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'CRITICAL',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

NOSE_ARGS = [
    '--with-coverage',
    '--cover-inclusive',
    '--cover-package=test_db_in_codebuild',
    '--with-xunit',
]
NOSE_VERBOSITY = 2
