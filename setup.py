# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

import booking as app

dependency_links = [
    'https://github.com/mikejarrett/django-international/tarball/master'
]

def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''

setup(
    name="django-booking",
    version=app.__version__,
    description=read('DESCRIPTION'),
    long_description=read('README.rst'),
    license='The MIT License',
    platforms=['OS Independent'],
    keywords='django, app, reusable, booking',
    author='Daniel Kaufhold',
    author_email='daniel.kaufhold.com',
    url="https://github.com/bitmazk/django-booking",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=1.7.0',
        'django-hvad',
        'django-libs>=1.35',
        # 'django-international==0.0.7',
    ],
    dependency_links=dependency_links,
)
