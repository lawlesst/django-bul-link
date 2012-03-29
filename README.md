django-bul-link
================

A basic interface to the Serial Solutions 360 Link API.  This is intended to 
provide an example of how to use the API and to get a Django App that uses it
up and running quickly.  You will probably want to subclass these views in a
separate app to meet your needs. 

* Setup a Django project or use an existing project
* Install django-link360 using pip:
 * pip install git+git://github.com/lawlesst/django-bul-link.git
* Add the django-link360 views to your projects urls.py
* Add your Serial Solutions API key to settings.py as
 * BUL_LINK_SERSOL_KEY = 'key'
* Start the Django development server
* Begin testing
 * Go to http://localhost:8000/?id=pmid:20133564 to see a sample citation  

Features
--------
* Front-end to the standard 360 Link interface
* Permalinks for OpenURL requests
* Caching
* More in development


