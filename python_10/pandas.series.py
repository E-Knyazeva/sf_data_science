import pandas as pd
countries = pd.Series(data = ['England', 'Canada', 'USA', 'Ukraine', 'Russia', 'Belarus', 'Kazakhstan'], index = ['UK', 'CA', 'US','UA','RU', 'BY','KZ'], name = 'countries')
print(countries)

countries = pd.Series({'Uk': 'England', 'RU':'Russia', 'US':'USA'}, name = 'countries')
print(countries)