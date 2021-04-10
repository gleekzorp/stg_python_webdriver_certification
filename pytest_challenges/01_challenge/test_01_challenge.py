from selenium import webdriver


def test_challenge_one():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    assert 'Google' in driver.title
