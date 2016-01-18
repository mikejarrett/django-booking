#!/usr/bin/env python

from django.conf import settings, global_settings

if not settings.configured:
    settings.configure(
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
            }
        },
        INSTALLED_APPS=[
            'booking'
        ],
        ROOT_URLCONF='',
        DEBUG=False,
        SITE_ID=1,
    )


import sys
from os.path import dirname, abspath
from optparse import OptionParser

try:
    # Django >= 1.8
    from django.test.runner import DiscoverRunner
    django_gte_18 = True
except ImportError:
    # Django < 1.8
    from django.test import DjangoTestSuiteRunner as DiscoverRunner
    django_gte_18 = False

if django_gte_18:
    import django
    django.setup()


def runtests(*test_args, **kwargs):
    if not test_args:
        test_args = ['tests']

    parent = dirname(abspath(__file__))
    sys.path.insert(0, parent)
    test_runner = DiscoverRunner(
        verbosity=kwargs.get('verbosity', 1),
        interactive=kwargs.get('interactive', False),
        failfast=kwargs.get('failfast')
    )
    failures = test_runner.run_tests(test_args)
    sys.exit(failures)

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option(
        '--failfast',
        action='store_true',
        default=False,
        dest='failfast'
    )

    (options, args) = parser.parse_args()

    runtests(failfast=options.failfast, *args)

# """
# This script is a trick to setup a fake Django environment, since this reusable
# app will be developed and tested outside any specifiv Django project.

# Via ``settings.configure`` you will be able to set all necessary settings
# for your app and run the tests as if you were calling ``./manage.py test``.

# """
# import sys

# from django.conf import settings

# import test_settings

# from django_nose import NoseTestSuiteRunner

# # import django
# # django.setup()

# # import os

# # os.environ['DJANGO_SETTINGS_MODULE'] = 'booking.tests.test_settings'

# # if not settings.configured:
# #     settings.configure(**test_settings.__dict__)


# from django.conf import settings, global_settings

# if not settings.configured:
#     settings.configure(
#         DATABASES={
#             'default': {
#                 'ENGINE': 'django.db.backends.sqlite3',
#             }
#         },
# 		CACHES = {
# 			'default': {
# 				'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
# 			}
# 		},
#         LOGGING_CONFIG = {},
#         INSTALLED_APPS=[
#             'booking',
#             # 'tests',
#         ],
#         ROOT_URLCONF='',
#         DEBUG=False,
#         SITE_ID=1,
#     )

# class NoseCoverageTestRunner(NoseTestSuiteRunner):
#     """Custom test runner that uses nose and coverage"""
#     pass


# def runtests(*test_args):
#     failures = NoseCoverageTestRunner(
#         verbosity=2,
#         interactive=True
#     ).run_tests(test_args)

#     sys.exit(failures)


# if __name__ == '__main__':
#     runtests(*sys.argv[1:])
