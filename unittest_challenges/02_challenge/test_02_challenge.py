import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Challenge_Two(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def test_challenge_two(self):
        self.driver.get("https://www.copart.com")
        self.driver.find_element_by_id(
            'input-search').send_keys('Exotic', Keys.ENTER)
        table = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "serverSideDataTable"))
        )
        self.assertIn('PORSCHE', table.get_attribute('innerHTML'))

    def test_challenge_two_table_rows(self):
        self.driver.get("https://www.copart.com")
        self.driver.find_element_by_id(
            'input-search').send_keys('Exotic', Keys.ENTER)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "*//table[@id='serverSideDataTable']//tr[20]")))
        table = self.driver.find_element_by_xpath(
            "*//table[@id='serverSideDataTable']")
        self.assertIn('PORSCHE', table.get_attribute('innerHTML'))


if __name__ == "__main__":
    unittest.main()
