import pandas as pd

unemployment_df = pd.read_csv('./data/unemployment_2016.csv')
type(unemployment_df)

countries = unemployment_df['country']
type(countries)

unemployment_rate = unemployment_df['unemp_rate']

avg_unemployment = unemployment_rate.mean()
print(avg_unemployment)

# unemployment_sorted = unemployment_data.sort_values('unemp_rate')
# lowest_unemployment = unemployment_sorted.head(5)
# print(lowest_unemployment)

# gdp = pd.read_csv('./data/gdp_2016.csv')

# eu_data = pd.merge(unemployment, gdp, how='left', on='country')



# currency_data = pd.read_html('https://flagsworld.org/currencies-europe.html')



# country_data = pd.read_json('./data/eu_member_countries.json')
# print(type(country_data))

# country_data.columns = ['country']

