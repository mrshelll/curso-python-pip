def get_population(country_dict):
  data = {
    '1970': int(country_dict['1970 Population']),
    '1980': int(country_dict['1980 Population']),
    '1990': int(country_dict['1990 Population']),
    '2000': int(country_dict['2000 Population']),
    '2010': int(country_dict['2010 Population']),
    '2015': int(country_dict['2015 Population']),
    '2020': int(country_dict['2020 Population']),
    '2022': int(country_dict['2022 Population'])
  }
  
  return data.keys(), data.values()

def population_by_country(data, country):
  result = list(filter(lambda item: item['Country/Territory'].lower() == country.lower(), data))
  return result