import os
from selenium import webdriver


def test_challenge_three():
    driver = webdriver.Chrome()
    driver.get("https://www.copart.com")
    popularMakes = driver.find_elements_by_xpath(
        "//*[@ng-if='popularSearches']//a")
    for make in popularMakes:
        if make.get_attribute('innerHTML') != "More...":
            print(f"{make.get_attribute('innerHTML')} - {make.get_attribute('href')}")


def test_challenge_three_write_to_file(project_root):
    driver = webdriver.Chrome()
    driver.get("https://www.copart.com")
    popularMakes = driver.find_elements_by_xpath(
        "//*[@ng-repeat='popularSearch in popularSearches']//a")
    f = open(os.path.join(project_root,
             'test_results/test_challenge_three.txt'), "w")
    for make in popularMakes:
        innerHTML = make.get_attribute('innerHTML')
        href = make.get_attribute('href')
        f.write(f"{innerHTML} - {href}\n")
    f.close()
