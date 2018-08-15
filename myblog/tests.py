from django.test import TestCase
from myblog.models import Post

# Create your tests here.
from django.contrib.auth.models import User


class PostTestCase(TestCase):
    fixrures = ['myblog_test_fixture.json', ]

    def setUp(self):
        self.user = User.objects.get(pk=1)

    def test_string_representation(self):
        expected = "This is a title"
        p1 = Post(title=expected)
        actual = str(p1)
        self.assertEqual(expected, actual)
