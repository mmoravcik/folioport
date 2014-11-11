from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.sites.models import Site
from django.conf import settings
from django.contrib.sites.managers import CurrentSiteManager


class FolioportUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        user = self.model(
            email=email
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class SiteFolioportUserManager(FolioportUserManager, CurrentSiteManager):
    pass


class SocialMedia(models.Model):
    title = models.CharField(max_length=128)
    code = models.CharField(max_length=3, unique=True)
    script_code = models.TextField(default='', blank=True)
    html_code = models.TextField(default='', blank=True)

    def __unicode__(self):
        return "%s" % (self.title)


class AbstractFolioportUser(AbstractBaseUser):
    email = models.EmailField(blank=True, unique=True)
    subdomain = models.CharField(max_length=100, unique=True)

    site_name = models.CharField(max_length=128, blank=True,
                                 default='', help_text='e.g. John Doe')
    site_catch_phrase = models.CharField(max_length=128, blank=True,
                                         default='', help_text='e.g. Illustrator')

    social_media = models.ManyToManyField(SocialMedia, blank=True)

    use_system_blog = models.BooleanField('Use blog', default=True)
    own_blog_link = models.URLField(default='', blank=True,
        help_text='In case you have your own blog already running, please '
                  'enter the address including http://, '
                  'e.g. http://wwww.myblog.com')

    google_analytics_code = models.CharField(max_length=30, blank=True, default='')

    site_logo = models.ImageField(
        null=True, blank=True, upload_to='images/site_logos')
    logo_width = models.IntegerField(default=120, blank=True)

    site = models.ForeignKey(Site, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        abstract = True

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __unicode__(self):
        return "%s - %s - %s" % (self.email, self.subdomain, self.site.id)

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    def save(self, *args, **kwargs):
        if not self.site:
            domain = '%s.%s' % (self.subdomain, settings.MAIN_DOMAIN)
            site, created = Site.objects.get_or_create(domain=domain, name=domain)
            self.site = site
        return super(AbstractFolioportUser, self).save(*args, **kwargs)

    objects = FolioportUserManager()
    site_objects = SiteFolioportUserManager()