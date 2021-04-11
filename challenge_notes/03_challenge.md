# Challenge

- Go to copart
- Print a list of all the “Popular Items” of vehicle Make/Models on the home page and the URL/href for each type.
- Example:

```
IMPREZA - https://www.copart.com/popular/model/impreza
CAMRY - https://www.copart.com/popular/model/camry
ELANTRA - https://www.copart.com/popular/model/elantra
```

# Elements

- trendingTab = `id = tabTrending`
- popularMakes = `//*[@ng-if='popularSearches']//ul//a`
- popularMakes = `//*[@ng-repeat='popularSearch in popularSearches']//a`

# Pytest Printing

In order to print to the console with pytest run the following command

```
(venv) $ python -m pytest pytest_challenges/03_challenge/test_03_challenge.py --capture=no
```
