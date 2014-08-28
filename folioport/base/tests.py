from django.test import TestCase

from folioport.base.utils import get_solr_thumbnail_geometry


class UtilTests(TestCase):
    def test_thumbnail_geometry_width_only(self):
        fixtures = (
            ("12", get_solr_thumbnail_geometry(12)),
            ("13", get_solr_thumbnail_geometry(13, 0)),
        )
        for fixture in fixtures:
            self.assertEqual(fixture[0], fixture[1])

    def test_thumbnail_geometry(self):
        fixtures = (
            ("12x14", get_solr_thumbnail_geometry(12, 14)),
            ("13x15", get_solr_thumbnail_geometry(13, 15)),
            ("x0", get_solr_thumbnail_geometry(0, 0)),
        )
        for fixture in fixtures:
            self.assertEqual(fixture[0], fixture[1])

    def test_thumbnail_geometry_height_only(self):
        fixtures = (
            ("x12", get_solr_thumbnail_geometry(0, 12)),
            ("x13", get_solr_thumbnail_geometry(0, 13)),
        )
        for fixture in fixtures:
            self.assertEqual(fixture[0], fixture[1])