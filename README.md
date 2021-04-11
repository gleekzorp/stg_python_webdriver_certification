# STG Certificate

I originally did these challenges during the autobots meetup.  I wanted a refresher and decided to start over to see what improvments I could have with my new knowledge.  I also thought it would be fun to try to build it out with unittest and pytest.  I was originally going to use pyleniumio but while setting everything up I decided to directly use selenium.

- https://stgconsulting.com/
- http://bitly.com/STGpythonwebdriver

## Setup
- You will need python, if you need help installing it you can read my setup instruction at https://gleek-dan.gitbook.io/dev-info/python/install
- You will also need to setup a virtual environment, if you need help you can read my instructions at https://gleek-dan.gitbook.io/dev-info/python/virtual-environments
- Install all the packages.  `(venv) $ pip install -r requirements.txt`
- Make sure you have a chrome driver in your path.  The easiest way is with brew.  `$ brew cask install chromedriver` or `$ brew install --cask chromedriver`.
  - If you don't have brew or your are using windows, please manually download your chrome driver at https://sites.google.com/a/chromium.org/chromedriver/downloads

## Running tests

### Unittest
- Setup your code editor to run tests.
  - For vscode head over to https://code.visualstudio.com/docs/python/testing#_enable-a-test-framework
    - Make sure you pick unittest
    - It is a good idea to reload your window after setting this up
  - For pycharm go into your `preferences/settings` and under the `python integrated tools` you will see a spot for default test runner, go ahead and choose `unittest`.
- You can now either use the cool new `play/run` icons or run the following command in your terminal.  Make sure you're in the correct folder when you run this command.
```
(venv) $ python test_01_challenge.py
```

### Pytest
- Setup your code editor to run tests.
  - For vscode head over to https://code.visualstudio.com/docs/python/testing#_enable-a-test-framework
    - Make sure you pick pytest
    - It is a good idea to reload your window after setting this up
  - For pycharm go into your `preferences/settings` and under the `python integrated tools` you will see a spot for default test runner, go ahead and choose `pytest`.
- You can now either use the cool new `play/run` icons or run the following command in your terminal.
```
(venv) $ python -m pytest
(venv) $ python -m pytest --help
```

## vscode settings.json

### unittest
```json
{
  "python.testing.unittestArgs": [
    "-v",
    "-s",
    "./unittest_challenges",
    "-p",
    "test_*.py"
  ],
  "python.testing.pytestEnabled": false,
  "python.testing.nosetestsEnabled": false,
  "python.testing.unittestEnabled": true
}
```

### pytest
```json
{
  "python.testing.pytestEnabled": true,
  "python.testing.nosetestsEnabled": false,
  "python.testing.unittestEnabled": false,
  "python.testing.pytestArgs": [
    "pytest_challenges"
  ]
}
```
