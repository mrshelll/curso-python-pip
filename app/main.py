import utils
import read_csv
import charts
import pandas as pd

def run():
  '''
  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda item: item['Continent'].lower() == 'South America'.lower(), data))
  countries = list(map(lambda item: item['Country/Territory'], data))
  percentages = list(map(lambda item: float(item['World Population Percentage']), data))
  charts.generate_pie_chart(countries, percentages)
  '''

  df = pd.read_csv('data.csv')
  df = df[df['Continent'] == 'Africa']
  countries = df['Country/Territory'].values
  percentages = df['World Population Percentage'].values
  charts.generate_pie_chart(countries, percentages)

  data = read_csv.read_csv('data.csv')
  country = input('Type Country => ')
  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)
  
if __name__ == '__main__':
  run()