from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_wait_for_spinner_one():
    driver = webdriver.Chrome()
    driver.get("https://www.copart.com")
    driver.find_element_by_id(
        'input-search').send_keys('Exotic', Keys.ENTER)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, "//div[@id='serverSideDataTable_processing']")))
    WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(
        (By.XPATH, "//div[@id='serverSideDataTable_processing']")))
    table = driver.find_element_by_xpath(
        "*//table[@id='serverSideDataTable']")
    assert 'PORSCHE' in table.text


def test_wait_for_spinner_two():
    """
    I think this is my favorite one
    """
    driver = webdriver.Chrome()
    driver.get("https://www.copart.com")
    driver.find_element_by_id(
        'input-search').send_keys('Exotic', Keys.ENTER)
    spinner = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, "//div[@id='serverSideDataTable_processing']")))
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element(spinner))
    table = driver.find_element_by_xpath(
        "*//table[@id='serverSideDataTable']")
    assert 'PORSCHE' in table.text


def test_wait_for_spinner_three():
    """
    Breaks because it won't ever wait to find the spinner
    """
    driver = webdriver.Chrome()
    driver.get("https://www.copart.com")
    driver.find_element_by_id(
        'input-search').send_keys('Exotic', Keys.ENTER)
    spinner = driver.find_element_by_xpath(
        "//div[@id='serverSideDataTable_processing']")
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element(spinner))
    table = driver.find_element_by_xpath(
        "*//table[@id='serverSideDataTable']")
    assert 'PORSCHE' in table.text


def test_wait_for_spinner_four():
    driver = webdriver.Chrome()
    driver.get("https://www.copart.com")
    driver.find_element_by_id(
        'input-search').send_keys('Exotic', Keys.ENTER)
    spinner = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, "//div[@id='serverSideDataTable_processing']")))
    WebDriverWait(driver, 10).until(
        lambda _: spinner.get_attribute('style') == 'display: none;')
    table = driver.find_element_by_xpath(
        "*//table[@id='serverSideDataTable']")
    assert 'PORSCHE' in table.text
