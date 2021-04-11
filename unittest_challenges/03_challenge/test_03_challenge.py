import unittest
from selenium import webdriver


class Challenge_Two(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def test_challenge_three(self):
        self.driver.get("https://www.copart.com")
        popularMakes = self.driver.find_elements_by_xpath(
            "//*[@ng-if='popularSearches']//a")
        for make in popularMakes:
            if make.get_attribute('innerHTML') != "More...":
                print(
                    f"{make.get_attribute('innerHTML')} - {make.get_attribute('href')}")


if __name__ == "__main__":
    unittest.main()
