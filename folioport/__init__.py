import os

FOLIOPORT_PARENT_TEMPLATE_DIR = os.path.dirname(os.path.abspath(__file__)) + '/templates'

# Use 'final' as the 4th element to indicate
# a full release

VERSION = (0, 0, 7, 'alpha', 0)
    
def get_short_version():
    return '%s.%s' % (VERSION[0], VERSION[1])

def get_version():
    version = '%s.%s' % (VERSION[0], VERSION[1])
    if VERSION[2]:
        # Append 3rd digit if > 0
        version = '%s.%s' % (version, VERSION[2])
    if VERSION[3:] == ('alpha', 0):
        version = '%s pre-alpha' % version
    elif VERSION[3] != 'final':
        version = '%s %s %s' % (version, VERSION[3], VERSION[4])
    return version