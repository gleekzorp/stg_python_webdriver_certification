from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_challenge_two():
    driver = webdriver.Chrome()
    driver.get("https://www.copart.com")
    driver.find_element_by_id('input-search').send_keys('Exotic', Keys.ENTER)
    table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "serverSideDataTable")))
    assert 'PORSCHE' in table.text


def test_challenge_two_rows():
    driver = webdriver.Chrome()
    driver.get("https://www.copart.com")
    driver.find_element_by_id('input-search').send_keys('Exotic', Keys.ENTER)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, "*//table[@id='serverSideDataTable']//tr[20]")))
    table = driver.find_element_by_xpath("*//table[@id='serverSideDataTable']")
    assert 'PORSCHE' in table.text
