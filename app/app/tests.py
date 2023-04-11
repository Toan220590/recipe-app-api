from django.test import SimpleTestCase
from app import cacl


class calcTest(SimpleTestCase):

    def test_add_numbers(self):
        res = cacl.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        res = cacl.subtract(10, 15)
        self.assertEqual(res, 5)
