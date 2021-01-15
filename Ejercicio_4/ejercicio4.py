import pandas as pd
import csv


def generate_report(path):
    value_type = ['FA', 'FB', 'FC', 'FI']
    report = []
    colunms = ['FECHA', 'TIPO VALOR', 'EMISORA',
               'SERIE', 'PRECIO LIMPIO', 'PRECIO SUCIO',
               'INTERESES ACUMULADOS', 'CUPON ACTUAL', 'SOBRETASA', 'NOMBRE COMPLETO', 'SECTOR',
               'MONTO EMITIDO', 'MONTO EN CIRCULACION', 'FECHA EMISION', 'PLAZO EMISION', 'FECHA VCTO',
               'VALOR NOMINAL', 'MONEDA EMISION', 'SUBYACENTE', 'REND. COLOCACION', 'ST COLOCACION',
               'FREC. CPN', 'TASA CUPON', 'DIAS TRANSC. CPN', 'REGLA CUPON', 'CUPONES EMISION',
               'CUPONES X COBRAR', 'HECHO DE MKT', 'FECHA U.H.', 'PRECIO TEORICO', 'POST COMPRA',
               'POST VENTA', 'YIELD COMPRA', 'YIELD VENTA', 'SPREAD COMPRA', 'SPREAD VENTA', 'MDYS',
               'S&P', 'BURSATILIDAD', 'LIQUIDEZ', 'CAMBIO DIARIO', 'CAMBIO SEMANAL', 'PRECIO MAX 12M',
               'PRECIO MIN 12M', 'SUSPENSION', 'VOLATILIDAD', 'VOLATILIDAD 2', 'DURACION', 'DURACION MONET.',
               'CONVEXIDAD', 'VAR', 'DESVIACION STAND', 'VALOR NOMINAL ACTUALIZADO', 'CALIFICACION FITCH',
               'FECHA PRECIO MAXIMO', 'FECHA PRECIO MINIMO', 'SENSIBILIDAD', 'DURACION MACAULAY',
               'TASA DE RENDIMIENTO', 'HR RATINGS', 'DURACION EFECTIVA', 'ISIN', 'CALIFICACION VERUM',
               'CALIFICACION DBRS']
    df = pd.read_csv(
        path, usecols=colunms)
    array_obj = df.to_dict(orient='records')

    _filter = [d for d in array_obj if d['TIPO VALOR']
               in value_type and d['SECTOR'] == 'DERIVADOS' and int(d['FECHA EMISION'][-4:]) >= 2020]

    for item in _filter:
        item_reporte = {'TICKER': item['TIPO VALOR'] + '_' + item['EMISORA'] + '_' + item['SERIE'],
                        'PRECIO': item['PRECIO LIMPIO'], 'MONEDA': item['MONEDA EMISION'], 'VAR': item['VAR']}
        report.append(item_reporte)
    keys = report[0].keys()
    with open(path, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(report)
    return 'holi'


print(generate_report('VectorAnalitico24H.csv'))

# print(busca_piso(pisos, 100000))
