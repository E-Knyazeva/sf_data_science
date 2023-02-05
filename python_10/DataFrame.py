import pandas as pd

countries_df = pd.DataFrame(
    {'country':['England', 'Canada', 'USA','Russia','Ukraine','Belarus','Kazakhstan'],
     'population':[56.29, 38.05,322.28,146.24,45.5,9.5,17.04],
     'square': [133396, 9984670, 9826630, 17125191, 603628, 207600, 2724902]})
countries_df.index=['UK','CA', 'US','RU','UA','BY','KZ']
print(countries_df)

countries_df1 = pd.DataFrame(
    data = [
        ['England', 56.29,133396],
        ['Canada',38.05,9984670],
        ['USA', 322.28,9826630],
        ['Russia', 146.24,17125191],
        ['Ukraine',45.5,603628],
        ['Belarus',9.5,207600],
        ['Kazakhstan',17.04,2724902]        
    ],
    columns= ['country', 'population', 'square'],
    index = ['UK','CA','US', 'RU','UA','BY','KZ']
)
print(countries_df1)

print(countries_df.mean(axis=0))
print(countries_df.mean(axis=1))

print(countries_df.population)
print(type(countries_df.population))
print(countries_df['square'])

print(countries_df.loc['UK','square'])
print(countries_df.loc['RU',['population','square']])
print(countries_df.loc[['UA','BY','KZ'],['population','square']])
print(countries_df.iloc[4:8, 1:3])


countries_df.to_csv('D:\курс по data science\IDE\python_10\data/countries.csv', index=False, sep=';')
countries_data = pd.read_csv('D:\курс по data science\IDE\python_10\data\countries.csv', sep=';')
print(countries_data)

data = pd.read_csv('https://raw.githubusercontent.com/esabunor/MLWorkspace/master/melb_data.csv')
print(data)