#enconding: utf-8
import pandas as pd
import csv


def csvToDict(path):

    df = pd.read_csv(
        path, usecols=['Nombre', 'Final', 'Máximo', 'Mínimo', 'Volumen', 'Efectivo'])
    result = df.to_dict(orient='records')

    return result


def quotesCsv(quotesDict, path):
    del_key_list = ['Final', 'Volumen', 'Efectivo']
    newKey = "Media"

    for item in quotesDict:
        [item.pop(key) for key in del_key_list]
        media = (int(item.get('Mínimo')) + int(item.get('Máximo'))) / 2
        item[newKey] = media

    print(quotesDict)
    keys = quotesDict[0].keys()
    with open(path, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(quotesDict)


quotesDict = csvToDict('cotizacion.csv')
# print(quotesDict)
cotizaciones = quotesCsv(quotesDict, 'resumen.csv')
# print(keys)
