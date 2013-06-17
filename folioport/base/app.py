from django.conf.urls import patterns


class Application(object):
    name = None
    
    def __init__(self, app_name=None, **kwargs):
        self.app_name = app_name
        for key, value in kwargs.iteritems():
            setattr(self, key, value)
    
    def get_urls(self):
        """
        To be implemented in the subclass
        """
        return patterns('')

    @property
    def urls(self):
        # Set the application and instance namespace here
        return self.get_urls(), self.app_name, self.name


application = Application()