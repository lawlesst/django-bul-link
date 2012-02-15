import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "django-bul-link",
    version = "1",
    url = 'https://github.com/lawlesst/django-bul-link',
    description = "An interface to the Serial Solutions 360 Link API.",
    long_description = read('README'),

    author = 'Ted Lawless',
    author_email = 'lawlesst@gmail.com',

    packages = find_packages('src'),
    package_dir = {'': 'src'},
    
    install_requires = ['setuptools'],

    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
