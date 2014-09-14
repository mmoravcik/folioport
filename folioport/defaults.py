GOOGLE_ANALYTICS_ACCOUNT = 'test'

FOLIOPORT_CONTENT_TYPES = [
        ('ItemImage', 'Image'),
        ('ItemText', 'Plain text'),
        ('ItemHeading', 'Heading'),
        ('ItemRandomImage', 'Random Image'),
        ('ItemRichText', 'Rich Text'),
        ('ItemEmbed', 'Video/Audio embed'),
        ('ItemGallery', 'Gallery'),
    ]

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
           ['Styles','Format','FontSize'],
           '/',
           ['Bold','Italic','Underline','StrikeThrough','-','Undo','Redo','-','Cut','Copy','Paste','Find','-','Outdent','Indent'],
           ['NumberedList','BulletedList','-','JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock'],
           ['Table','-','Link','TextColor','BGColor','-','Print','Source']
        ],
        'height': 600,
        'width': '70%',
        },
    }

AUTH_USER_MODEL = 'account.FolioportUser'

CRISPY_TEMPLATE_PACK = 'bootstrap3'
CRISPY_FAIL_SILENTLY = False
