AUTHOR = 'FIAB Cosenza Ciclabile'
SITENAME = 'FIAB CosenzaCiclabile'
SITEURL = ""

PATH = "content"
OUTPUT_PATH = 'output'

TIMEZONE = 'Europe/Rome'
THEME = 'themes/fiab'
DEFAULT_LANG = 'it'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight', 'guess_lang':False,},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.smarty': {},
        'markdown.extensions.sane_lists': {},
    },
    'output_format': 'html5',
}

CATEGORIES_SAVE_AS = 'blog/index.html'
CATEGORY_URL = '/{slug}/'
CATEGORY_SAVE_AS = '/{slug}/index.html'

DELETE_OUTPUT_DIRECTORY = True

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 25

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
