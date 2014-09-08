GOOGLE_ANALYTICS_ACCOUNT = 'test'

FOLIOPORT_CONTENT_TYPES = [
    'ItemImage',
    'ItemText',
    'ItemHeading',
    'ItemRandomImage',
    'ItemRichText',
    'ItemEmbed',
    'ItemGallery',
    ]

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Basic',
        'height': 600,
        'width': '70%',
        },
    }

AUTH_USER_MODEL = 'account.FolioportUser'