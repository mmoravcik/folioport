FOLIOPORT_CONTENT_TYPES = [
        ('ItemImage', 'Image'),
        ('ItemRichText', 'Text'),
        #('ItemText', 'Plain text'),
        ('ItemHeading', 'Heading'),
        ('ItemRandomImage', 'Random Image'),
        ('ItemEmbed', 'Video/Audio embed'),
        ('ItemGallery', 'Gallery'),
    ]

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
           ['Bold','Italic','Underline','StrikeThrough','-','Undo','Redo','-','Cut','Copy','Paste','Find','-','Outdent','Indent'],
           ['Styles','Format','FontSize'],
           '/',
           ['NumberedList','BulletedList','-','JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock'],
           ['Table','-','Link','TextColor','BGColor','-','Print','Source']
        ],
        'height': 600,
        'width': '70%',
        },
    }

DATE_FORMAT = 'j N Y'

AUTH_USER_MODEL = 'account.FolioportUser'

CRISPY_TEMPLATE_PACK = 'bootstrap3'
CRISPY_FAIL_SILENTLY = False

ENDLESS_PAGINATION_PER_PAGE = 5

THUMBNAIL_DEBUG = False

MAIN_DOMAIN = 'heyhey.io'

ALLOWED_HOSTS = ['.' + MAIN_DOMAIN]
