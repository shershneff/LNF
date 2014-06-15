#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from pelican.readers import BaseReader

AUTHOR = u'ЛНТ'
SITENAME = u'Лаборатория неравновесных течений'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'ru'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS =  (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ["images","pdf","mytheme"]
#THEME = "/home/Antony/Site/pelican-themes-master/Just-Read"
THEME = "mytheme"

ARTICLE_DIR = 'news'
ARTICLE_URL = 'news/{slug}.html'
ARTICLE_SAVE_AS = 'news/{slug}.html'


PAGE_DIR = 'pages'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

AUTHOR_SAVE_AS = False
CATEGORY_SAVE_AS = 'news/category/{slug}.html'
CATEGORY_URL = 'news/category/{slug}.html'
TAG_SAVE_AS = 'news/tag/{slug}.html'
TAG_URL = 'news/tag/{slug}.html'

DIRECT_TEMPLATES = (('index',))
#DIRECT_TEMPLATES = (('index', 'news/tags', 'news/categories', 'news/archives', 'news/index'))
PAGINATED_DIRECT_TEMPLATES = (('index', 'news/index', ))

DEFAULT_PAGE_SLUG = 'about'




