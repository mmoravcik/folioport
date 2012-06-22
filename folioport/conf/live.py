DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'illustration_martinapaukova',                      # Or path to database file if using sqlite3.
        'USER': 'illustration_dev',                      # Not used with sqlite3.
        'PASSWORD': 'illustration_dev',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

MEDIA_ROOT = '/var/www/static_files/thisisoko/dev/'