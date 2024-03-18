import csv, json

counter = 0
first_cities = []
l = []

with open('list.csv') as f:
  settlements = csv.DictReader(f)
  first_cities = [settlement for settlement in settlements if settlement['Country'] == "United States"]

with open('uscities.csv') as f2:
  cities = list(csv.DictReader(f2))  # Load into a list

for fcity in first_cities:
  for city in cities:  # Now you can iterate over cities multiple times
    if fcity['Settlement'].strip().lower() == city['city'].strip().lower() and fcity['Subdivision'] == city['state_name']:
      o = {
        "city": fcity['Settlement'],
        "state": fcity['Subdivision'],
        "state_id": city['state_id'],
        "lat": city['lat'],
        "lng": city['lng'],
        "year": fcity['Year'],
      }
      l.append(o)
      counter += 1
      break

print(f"Total: {counter}")

with open('output.json', 'w') as f:
  f.write(json.dumps(l, indent=2))