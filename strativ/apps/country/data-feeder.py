import requests

url = 'https://restcountries.eu/rest/v2/all'
print(url)

response = requests.get(url)
country = response.json()
'name, alphacode2, capital, population, timezone, flag, languages , neighbouring_countries'
data = {}
for key, line in enumerate(country):
    if key == 3:
        break
    data['name'] = line["name"]
    data['alpha2Code'] = line["alpha2Code"]
    data['alpha3Code'] = line["alpha3Code"]
    data['capital'] = line['capital']
    data['population'] = line['population']
    data['timezones'] = line['timezones']
    data['flag'] = line['flag']
    data['neighbouring_countries'] = line['borders']
    print(data)
    #print(key, line)

