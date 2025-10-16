from unittest import TestCase
from paleofuturistic_python_project import hello


class TestSmoke(TestCase):
    def test_sanity(self):
        self.assertTrue(True)

    def test_integration(self):
        self.assertEqual("Hello from paleofuturistic_python_project!", hello())
