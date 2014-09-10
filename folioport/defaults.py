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