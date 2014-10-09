from django_dynamic_fixture import G

from django.conf import settings
from django.test import TestCase
from django.contrib.sites.models import Site

from folioport.apps.account.models import FolioportUser


class FolioportUserTests(TestCase):

    def test_new_user_will_have_site_assigned(self):
        self.assertEqual(1, Site.objects.all().count())

        user = G(FolioportUser, subdomain='a1', site=None)
        self.assertEqual(2, Site.objects.all().count())

        site = Site.objects.all().order_by('pk')[1]
        self.assertEqual('a1.' + settings.MAIN_DOMAIN, site.domain)
        self.assertEqual(user.site, site)