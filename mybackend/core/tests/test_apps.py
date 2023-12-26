from django.test import TestCase
from django.apps import apps
from core.apps import CoreConfig

class CoreConfigTest(TestCase):
    def test_app_config(self):
        app_config = apps.get_app_config('core')
        self.assertIsInstance(app_config, CoreConfig)
        self.assertEqual(app_config.name, 'core')
        self.assertEqual(app_config.default_auto_field, 'django.db.models.BigAutoField')
