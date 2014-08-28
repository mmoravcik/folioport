def get_solr_thumbnail_geometry(width, height=0):
    if height > 0 and width > 0:
        return '%dx%d' % (width, height)
    if width > 0:
        return '%d' % width
    return 'x%d' % height
