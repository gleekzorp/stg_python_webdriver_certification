# Spinner

The spinner is a tricky one and I still have more work on this.  I want to go ahead and dive deeper into the Page Object in order to clean up the tests and have all the crazy spinner stuff hidden away.

# Some of the research:

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

http://allselenium.info/working-with-expected-conditions-explicit-wait-part-2/

- During autobots I brought up the idea that I was struggling with the spinner and this is what we came up with while exploring.

```java
public class Challenge1 {
  public WebDriver driver;
  public WebDriverWait wait;

  @BeforeSuite
  public void startSuite() throws Exception {
    System.setProperty("webdriver.chrome.driver", "src/main/resources/drivers/chromedriver");
    driver = new ChromeDriver();
    driver.manage().window().maximize();
    driver.manage().timeouts().implicitlyWait(20, SECONDS);
    wait = new WebDriverWait(driver, 10);
  }

  @AfterSuite
  public void stopSuite() throws Exception {
    System.out.println("All done!!!");
  }

  @AfterClass
  public void stopClass(){
    driver.quit();
  }

  @Test()
  public void verifyListOfExoticCardsHasPorsche() {
    driver.get("https://www.copart.com");
    WebElement searchBarTbx = driver.findElement(By.id("input-search"));
    WebElement searchBtn = driver.findElement(By.xpath("//button[@data-uname='homepageHeadersearchsubmit']"));

    searchBarTbx.sendKeys("exotics");
    searchBtn.click();
    Assert.assertTrue(driver.getCurrentUrl().contains("exotics"));

    // WebElement spinner = wait.until(ExpectedConditions.presenceOfElementLocated(By.xpath("//div[@id='serverSideDataTable_processing']")));
    // wait.until(ExpectedConditions.attributeToBe(spinner, "style", "display: block;"));
    // wait.until(ExpectedConditions.attributeToBe(spinner, "style", "display: none;"));

    // WebElement spinner = wait.until(ExpectedConditions.presenceOfElementLocated(By.xpath("//div[@id='serverSideDataTable_processing']")));
    // wait.until(ExpectedConditions.invisibilityOfElementLocated(By.xpath("//div[@id='serverSideDataTable_processing']")));

    WebElement spinner = wait.until(ExpectedConditions.presenceOfElementLocated(By.xpath("//div[@id='serverSideDataTable_processing']")));
    wait.until(ExpectedConditions.invisibilityOf(spinner));

    List<WebElement> exotics = driver.findElements(By.xpath("//span[@data-uname='lotsearchLotmake']"));
    List<String> exoticCars = new ArrayList<>();
    for (WebElement element : exotics) {
      exoticCars.add(element.getText());
    }
    Assert.assertTrue(exoticCars.contains("PORSCHE"));
  }
}
```
