#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Cyclic Materials'
SITEURL = '//cyclicmaterials.github.io'
SITENAME = u'Cyclic Materials for Cycle.js'
SITETITLE = u'Cyclic Materials'
SITESUBTITLE = u'A Material Design Components Library Collection for Cycle.js'
SITEDESCRIPTION = u'A Material Design Components Library Collection'

ROBOTS = u'index, follow'

THEME = u'./themes/Flex'
PATH = u'content'
TIMEZONE = u'Atlantic/Reykjavik'
DEFAULT_LANG = u'en'
OG_LOCALE = u'en_US'

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True

PATH_METADATA = '\A(?P<category>[^/]+)/(?P<date>\d{4}/\d{2}/\d{2})-(?P<slug>.*)(.md|.rst)'
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

LINKS = (('Cycle.js', '//cycle.js.org'),)

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

COPYRIGHT_YEAR = 2015

DEFAULT_PAGINATION = 4

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
