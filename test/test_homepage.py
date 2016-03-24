from django.test import LiveServerTestCase
from django.contrib.auth.models import User

from selenium import webdriver

class HomepageTestCase(LiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()
        super(HomepageTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(HomepageTestCase, self).tearDown()

    def test_create_user(self):
        self.selenium.get(
            '%s%s' % (self.live_server_url,  "/")
        )

        self.assertIn("Welcome to my blog", self.selenium.title)