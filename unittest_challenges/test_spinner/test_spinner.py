import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Test_Spinner(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def test_wait_for_spinner_one(self):
        self.driver.get("https://www.copart.com")
        self.driver.find_element_by_id(
            'input-search').send_keys('Exotic', Keys.ENTER)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//div[@id='serverSideDataTable_processing']")))
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
        #     (By.XPATH, "//div[@id='serverSideDataTable_processing']")))
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(
            (By.XPATH, "//div[@id='serverSideDataTable_processing']")))
        table = self.driver.find_element_by_xpath(
            "*//table[@id='serverSideDataTable']")
        self.assertIn('PORSCHE', table.get_attribute('innerHTML'))

    def test_wait_for_spinner_two(self):
        """
        I think this is my favorite one
        """
        self.driver.get("https://www.copart.com")
        self.driver.find_element_by_id(
            'input-search').send_keys('Exotic', Keys.ENTER)
        spinner = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//div[@id='serverSideDataTable_processing']")))
        # WebDriverWait(self.driver, 10).until(EC.visibility_of(spinner))
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element(spinner))
        table = self.driver.find_element_by_xpath(
            "*//table[@id='serverSideDataTable']")
        self.assertIn('PORSCHE', table.get_attribute('innerHTML'))

    def test_wait_for_spinner_three(self):
        """
        Breaks because it won't ever wait to find the spinner
        """
        self.driver.get("https://www.copart.com")
        self.driver.find_element_by_id(
            'input-search').send_keys('Exotic', Keys.ENTER)
        spinner = self.driver.find_element_by_xpath(
            "//div[@id='serverSideDataTable_processing']")
        # WebDriverWait(self.driver, 10).until(EC.visibility_of(spinner))
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element(spinner))
        table = self.driver.find_element_by_xpath(
            "*//table[@id='serverSideDataTable']")
        self.assertIn('PORSCHE', table.get_attribute('innerHTML'))

    def test_wait_for_spinner_four(self):
        self.driver.get("https://www.copart.com")
        self.driver.find_element_by_id(
            'input-search').send_keys('Exotic', Keys.ENTER)
        spinner = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//div[@id='serverSideDataTable_processing']")))
        # WebDriverWait(self.driver, 10).until(lambda _: spinner.get_attribute('style') == 'display: block;')
        WebDriverWait(self.driver, 10).until(
            lambda _: spinner.get_attribute('style') == 'display: none;')
        table = self.driver.find_element_by_xpath(
            "*//table[@id='serverSideDataTable']")
        self.assertIn('PORSCHE', table.get_attribute('innerHTML'))


if __name__ == "__main__":
    unittest.main()
