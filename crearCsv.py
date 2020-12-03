from tqdm import tqdm
import csv

def salidaArchivoTxt(ArchivoSalidaTxt, dataSalida, encabezadoXlsx):
    try:
        with open(ArchivoSalidaTxt, 'w', newline='') as txt:
            writer = csv.writer(txt, delimiter=';')
            encabezado = ['CRR']
            encabezado += encabezadoXlsx
            writer.writerow(encabezado)
            j = 1
            for llave, registro in tqdm(iterable=dataSalida.items(), total = len(dataSalida), desc='Escribiendo %s' % ArchivoSalidaTxt, unit=' Fila'):
                data = [j]
                data += list(registro.values())
                writer.writerow(data)
                j += 1
        return True
    except Exception as e:
        error = 'Error al escribir archivo: %s | %s' % (ArchivoSalidaTxt, e)
        return error

def salidaLogTxt(ArchivoSalidaTxt, dataSalida):
    try:
        with open(ArchivoSalidaTxt, 'w', newline='') as txt:
            writer = csv.writer(txt, delimiter='\n')
            for rut, x in tqdm(iterable=dataSalida.items(), total = len(dataSalida), desc='Escribiendo LOG', unit='Row'):
                writer.writerow(x.values())
        return True
    except Exception as e:
        raise Exception('Error al escribir archivo: %s | %s' % (ArchivoSalidaTxt, e))