properties = [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
              {'año': 2012, 'metros': 60, 'habitaciones': 2,
                  'garaje': True, 'zona': 'B'},
              {'año': 1980, 'metros': 120, 'habitaciones': 4,
               'garaje': False, 'zona': 'A'},
              {'año': 2005, 'metros': 75, 'habitaciones': 3,
                  'garaje': True, 'zona': 'B'},
              {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]
budget = 100000


def get_prop_price(prop):
    precio = (prop['metros'] * 1000 + prop['habitaciones'] * 5000 +
              int(prop['garaje']) * 15000) * (1 - (2020 - prop['año']) / 100)
    if prop['zona'] == 'B':
        precio *= 1.5
    prop['precio'] = precio
    return prop


def search_properties(properties, budget):
    properties_found = []
    for prop in properties:
        properties_found.append(get_prop_price(prop))

    return [d for d in properties_found if d['precio'] <= budget]


print(search_properties(properties, budget))
