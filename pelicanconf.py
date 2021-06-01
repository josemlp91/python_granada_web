#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from pelican_jupyter import markup as nb_markup

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
PLUGINS = ["i18n_subsites", "assets", nb_markup]

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
MENUITEMS_NAVBAR = (("Asociación", f"{SITEURL}/pages/about.html"),)
NAVBAR_STYLE = "is-primary"
THEME_LOGO = f"{SITEURL}/theme/images/logo_grande.svg"
FOOTER= "Made with ❤️ with Python from Granada. Under construction 🚧"

# Pelican jupyter integration

IGNORE_FILES = [".ipynb_checkpoints"]
# IPYNB_SKIP_CSS=True
IPYNB_FIX_CSS = True
IPYNB_SKIP_CSS = False

IPYNB_STOP_SUMMARY_TAGS = [('div', ('class', 'input')), ('div', ('class', 'output')), ('h2', ('id', 'Header-2'))]
IPYNB_GENERATE_SUMMARY = True
# dir_path = os.path.dirname(os.path.realpath(__file__))
# IPYNB_EXPORT_TEMPLATE =  "minimal_xy_theme/templates/basic_jupyter.html"