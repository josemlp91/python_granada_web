#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Python Granada Org'
SITENAME = 'Python Granada'
SITEURL = ''

PATH = 'content'

THEME = "themes/buruma"
TIMEZONE = 'Europe/Madrid'
DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["i18n_subsites", "assets"]

JINJA_ENVIRONMENT = {
    "extensions": ["jinja2.ext.i18n"],
}


# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False
SITEURL="https://josemlp91.github.io/python_granada_web"

# Theme config
MENUITEMS_NAVBAR = (("Docs", "#"), ("Info", "#"))
NAVBAR_STYLE = "is-warning"

THEME_LOGO = SITEURL + "/theme/images/logo_grande.svg"
FOOTER= "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec accumsan, ipsum ac faucibus fermentum, lacus est posuere risus, ut varius odio tortor tincidunt est"


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True