#!/usr/bin/python

import os
import sys

# if no environment settings use the jenkins settings by default
os.environ.setdefault(
	'DJANGO_SETTINGS_MODULE', 
	'test_db_in_codebuild.settings.test')

VAULT_MODULES = (
    'test_db_in_codebuild/test_db_testing',)


def runtests(*args, **kwargs):
    fail = os.system(
        'django-admin test %s --noinput --verbosity=2 --testrunner="django_nose.NoseTestSuiteRunner"'
        % ' '.join(VAULT_MODULES))
    sys.exit(fail >> 8)


if __name__ == '__main__':
    runtests()
