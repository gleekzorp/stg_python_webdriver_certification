# Challenge
- For this challenge, look through the different ways to do assertions.
- go to copart.com,
- search for exotics
- verify porsche is in the list of cars.
- Use the hard assertion for this challenge. 


# Elements

- Search Input `id = input-search`
- Search Button `*//button[@data-uname='homepageHeadersearchsubmit']`
- Table `*//table[@id='serverSideDataTable']`
- Spinner `*//div[@id='serverSideDataTable_processing']`
- query_params = `https://www.copart.com/lotSearchResults/?free=true&query=exotics`

# Ideas
- Spinner
  - https://stackoverflow.com/questions/26086965/wait-until-loader-disappears-python-selenium/40903207
```python
from selenium.common.exceptions import TimeoutException
def spinner(self):
    SHORT_TIMEOUT  = 5   # give enough time for the loading element to appear
    LONG_TIMEOUT = 30  # give enough time for loading to finish
    LOADING_ELEMENT_XPATH = "*//div[@id='serverSideDataTable_processing']"
    try:
        # wait for loading element to appear
        # - required to prevent prematurely checking if element
        #   has disappeared, before it has had a chance to appear
        WebDriverWait(self.driver, SHORT_TIMEOUT
            ).until(EC.presence_of_element_located((By.XPATH, LOADING_ELEMENT_XPATH)))

        # then wait for the element to disappear
        WebDriverWait(self.driver, LONG_TIMEOUT
            ).until_not(EC.presence_of_element_located((By.XPATH, LOADING_ELEMENT_XPATH)))

    except TimeoutException:
        # if timeout exception was raised - it may be safe to 
        # assume loading has finished, however this may not 
        # always be the case, use with caution, otherwise handle
        # appropriately.
        pass 
```

```python
WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "*//div[@id='serverSideDataTable_processing']")))
WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.ID, "*//div[@id='serverSideDataTable_processing']")))
table = self.driver.find_element_by_xpath("*//table[@id='serverSideDataTable']")
```