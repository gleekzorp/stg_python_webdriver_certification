import unittest
from selenium import webdriver


class Challenge_One(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome("../chromedriver")
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def test_challenge_one(self):
        self.driver.get("https://www.google.com")
        self.assertIn("Google", self.driver.title)


if __name__ == "__main__":
    unittest.main()
