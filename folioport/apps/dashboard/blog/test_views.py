from django_dynamic_fixture import G

from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from django.test import TestCase, Client

from folioport.apps.blog.models import Post


class DashboardBlogViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = G(get_user_model())
        self.user.set_password('1')
        self.user.save()
        self.client.login(email=self.user.email, password='1')

    def test_creation_of_post(self):
        response = self.client.get(reverse('folioport:dashboard:blog:post-create'))
        self.assertEqual(200, response.status_code)

        self.assertEqual(Post.objects.all().count(), 0)

        response = self.client.post(reverse('folioport:dashboard:blog:post-create'), {
            'title': '1',
            'release_date': '10/10/2014',
            }, follow=True)

        self.assertEqual(200, response.status_code)
        self.assertEqual(Post.objects.all().count(), 1)
        post = Post.objects.all()[0]
        self.assertEqual(post.user, self.user)
        self.assertEqual(post.site, self.user.site)

