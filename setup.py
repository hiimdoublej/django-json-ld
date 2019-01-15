import os
import re

from setuptools import setup, find_packages


def rel(*parts):
    '''returns the relative path to a file wrt to the current directory'''
    return os.path.abspath(os.path.join(os.path.dirname(__file__), *parts))


README = open('README.md', 'r').read()

with open(rel('django_json_ld', '__init__.py')) as handler:
    INIT_PY = handler.read()

VERSION = re.findall("__version__ = '([^']+)'", INIT_PY)[0]

setup(
    name='django-json-ld',
    packages=find_packages(),
    include_package_data=True,
    version=VERSION,
    description='Django template tag for json-ld',
    long_description=README,
    long_description_content_type="text/markdown",
    author='Johnny Chang',
    author_email='hiimdoublej.pi@gmail.com',
    #  download_url = 'https://github.com/owais/django-webpack-loader/tarball/{0}'.format(VERSION),
    url='https://github.com/hiimdoublej/django-json-ld',  # use the URL to the github repo
    keywords=['django', 'webpack', 'assets'],  # arbitrary keywords
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Framework :: Django',
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
    ],
)
