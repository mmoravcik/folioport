from django_dynamic_fixture import G

from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from django.test import TestCase, Client

from folioport.apps.page.models import Page


class DashboardPageViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = G(get_user_model())
        self.user.set_password('1')
        self.user.save()
        self.client.login(email=self.user.email, password='1')

    def test_creation_of_content_page(self):
        response = self.client.get(reverse('folioport:dashboard:page:create'))
        self.assertEqual(200, response.status_code)

        self.assertEqual(Page.objects.all().count(), 0)

        response = self.client.post(
            reverse('folioport:dashboard:page:create'),
            {'title': '1', 'type': Page.CONTENT_PAGE,},
            follow=True
        )

        self.assertEqual(200, response.status_code)
        self.assertEqual(Page.objects.all().count(), 1)
        page = Page.objects.all()[0]
        self.assertEqual(page.user, self.user)
        self.assertEqual(page.site, self.user.site)

    def test_edit_of_page(self):
        page = G(Page, user=self.user, site=self.user.site, type=Page.LANDING_PAGE)
        response = self.client.get(reverse('folioport:dashboard:page:edit',
                                           args=(page.id,)))
        self.assertEqual(200, response.status_code)
        self.assertContains(response, page.title)

        response = self.client.post(
            reverse('folioport:dashboard:page:edit', args=(page.id,)),
            {'title': 'new', 'type': Page.LANDING_PAGE,},
            follow=True
        )
        self.assertEqual(200, response.status_code)
        page = Page.objects.all()[0]
        self.assertEqual(page.title, 'new')
        self.assertEqual(page.user, self.user)
        self.assertEqual(page.site, self.user.site)

    # TODO perhaps make this nicer...
    def test_not_possible_to_have_two_active_landing_pages(self):
        # Create the first landing page
        self.client.post(
            reverse('folioport:dashboard:page:create'),
            {'title': '1', 'type': Page.LANDING_PAGE, 'active': 'on'},
            follow=True
        )
        self.assertEqual(Page.objects.all().count(), 1)
        landing_page_1 = Page.objects.all()[0]

        # Now create second one - should not be possible...
        response = self.client.post(
            reverse('folioport:dashboard:page:create'),
            {'title': '2', 'type': Page.LANDING_PAGE, 'active': 'on'},
            follow=True
        )
        self.assertIn('type', response.context['form'].errors)
        self.assertEqual(Page.objects.all().count(), 1)

        # I should be able to create inactive one though
        self.client.post(
            reverse('folioport:dashboard:page:create'),
            {'title': '1', 'type': Page.LANDING_PAGE,},
            follow=True
        )
        self.assertEqual(Page.objects.all().count(), 2)
        landing_page_2 = Page.objects.all()[1]

        # Edit the first page, ok = as it is active
        self.client.post(
            reverse('folioport:dashboard:page:edit', kwargs={'pk': landing_page_1.pk}),
            {'title': '1new', 'type': Page.LANDING_PAGE, 'active': 'on'},
            follow=True
        )
        self.assertEqual('1new', Page.objects.get(pk=landing_page_1.pk).title)

        # Set page 2 as active won't work
        self.client.post(
            reverse('folioport:dashboard:page:edit', kwargs={'pk': landing_page_2.pk}),
            {'title': '2new', 'type': Page.LANDING_PAGE, 'active': 'on'},
            follow=True
        )
        self.assertIn('type', response.context['form'].errors)

        # I can set page1 to inactive and then set page 2 to active
        self.client.post(
            reverse('folioport:dashboard:page:edit', kwargs={'pk': landing_page_1.pk}),
            {'title': '1new', 'type': Page.LANDING_PAGE},
            follow=True
        )
        self.client.post(
            reverse('folioport:dashboard:page:edit', kwargs={'pk': landing_page_2.pk}),
            {'title': '2new2', 'type': Page.LANDING_PAGE, 'active': 'on'},
            follow=True
        )
        self.assertEqual('2new2', Page.objects.get(pk=landing_page_2.pk).title)

        # I can create/edit content (in) active pages
        self.client.post(
            reverse('folioport:dashboard:page:create'),
            {'title': '3', 'type': Page.CONTENT_PAGE, 'active': 'on'},
            follow=True
        )
        self.assertEqual(Page.objects.all().count(), 3)

        self.client.post(
            reverse('folioport:dashboard:page:create'),
            {'title': '4', 'type': Page.CONTENT_PAGE, 'active': 'on'},
            follow=True
        )
        self.assertEqual(Page.objects.all().count(), 4)

        content_page_1 = Page.objects.all()[2]
        self.client.post(
            reverse('folioport:dashboard:page:edit', kwargs={'pk': content_page_1.pk}),
            {'title': '3new', 'type': Page.CONTENT_PAGE, 'active': 'on'},
            follow=True
        )
        self.assertEqual('3new', Page.objects.get(pk=content_page_1.pk).title)