from tqdm import tqdm
import csv

from variablesConfiguracion import POLIZA_CONFIG, CODIGOS_GAGU_CONFIG, CUOTA_CONFIG, AGENTE_CONFIG, COLUMNAS_ENCABEZADO, PATH_ARCHIVOS

from crearRegistro import *

def leerCargaIcom(archivoConsolidado, configuracionXml:[]):

    salidaUfmesXlsx = dict()
    salidaPolizaXlsx = dict()
    salidaAgenteXlsx = dict()
    salidaCuotaXlsx = dict()
    salidaCodigosGaguXlsx = dict()
    columnasXlsx = COLUMNAS_ENCABEZADO
    salidaArchivo = {'UF_MES': 0, 'POLIZA': 1, 'AGENTE': 2, 'CUOTA': 3, 'CODIGOS_GAGU': 4}

    datoFuente = configuracionXml[0]
    variableIcom = configuracionXml[1]
    inicioVariableIcom = configuracionXml[2]
    nombreArchivoTxt = configuracionXml[3]

    cantidadRegistrosCsv = sum(1 for line in open(archivoConsolidado))
    with open(archivoConsolidado) as archivoCsv:
        registroArchivo = csv.reader(archivoCsv, delimiter=';')
        for fila in tqdm(iterable= registroArchivo, total= cantidadRegistrosCsv, desc='Registro ICOM' , unit=' Fila'):

            varIcomXls = fila[columnasXlsx['VARIABLE_ICOM']]
            valorVarIcomXls = fila[columnasXlsx['VALOR_VARIABLE']]
            rut = fila[columnasXlsx['RUT']]
            poliza = fila[columnasXlsx['POLIZA']]
            agencia = fila[columnasXlsx['AGENCIA']]
            unidad = fila[columnasXlsx['UNIDAD']]
            recibo = fila[columnasXlsx['RECIBO']]
            cuota = fila[columnasXlsx['CUOTA']]

            for controlSalida in range(0,len(variableIcom)):

                resultadoBusqueda = variableIcom[controlSalida].get(varIcomXls)
                if resultadoBusqueda is not None:

                    if controlSalida == salidaArchivo['UF_MES']:

                        salidaUfmesXlsx[rut] = crearRegistroUfmes(inicioVariableIcom[controlSalida], varIcomXls, valorVarIcomXls)

                    elif controlSalida == salidaArchivo['POLIZA']:

                        pk = fila[POLIZA_CONFIG['PK']['POLIZA']]
                        dimensiones = {'RUT': rut, 'AGENCIA': agencia, 'UNIDAD': unidad}
                        if salidaPolizaXlsx.get(pk):
                            salidaPolizaXlsx[pk] = actualizarRegistroPoliza(dimensiones, varIcomXls, valorVarIcomXls, salidaPolizaXlsx[pk])
                        else:
                            salidaPolizaXlsx[pk] = crearRegistroPoliza(poliza, dimensiones, inicioVariableIcom[controlSalida], varIcomXls, valorVarIcomXls)

                    elif controlSalida == salidaArchivo['AGENTE']:

                        pk = fila[AGENTE_CONFIG['PK']['RUT']]
                        dimensiones = {'AGENCIA': agencia, 'UNIDAD': unidad}
                        if salidaAgenteXlsx.get(pk):
                            salidaAgenteXlsx[pk] = actualizarRegistroAgente(dimensiones, varIcomXls, valorVarIcomXls, salidaAgenteXlsx[pk])
                        else:
                            salidaAgenteXlsx[pk] = crearRegistroAgente(rut, dimensiones, inicioVariableIcom[controlSalida], varIcomXls, valorVarIcomXls)

                    elif controlSalida == salidaArchivo['CUOTA']:

                        pk = fila[CUOTA_CONFIG['PK']['POLIZA']] + '_' + fila[CUOTA_CONFIG['PK']['RECIBO']] + '_' + fila[CUOTA_CONFIG['PK']['CUOTA']]
                        dimensiones = {'RECIBO': recibo, 'POLIZA': poliza, 'CUOTA': cuota}
                        if salidaCuotaXlsx.get(pk):
                            salidaCuotaXlsx[pk] = actualizarRegistroCuota(varIcomXls, valorVarIcomXls, salidaCuotaXlsx[pk])
                        else:
                            salidaCuotaXlsx[pk] = crearRegistroCuota(dimensiones, inicioVariableIcom[controlSalida], varIcomXls, valorVarIcomXls)

                    elif controlSalida == salidaArchivo['CODIGOS_GAGU']:

                        pk = fila[CODIGOS_GAGU_CONFIG['PK']['RUT']] + '_' + fila[CODIGOS_GAGU_CONFIG['PK']['AGENCIA']] + '_' + fila[CODIGOS_GAGU_CONFIG['PK']['UNIDAD']]
                        dimensiones = {'AGENCIA': agencia, 'UNIDAD': unidad}
                        if salidaCodigosGaguXlsx.get(pk):
                            salidaCodigosGaguXlsx[pk] = actualizarRegistroCodigosG(varIcomXls, valorVarIcomXls, salidaCodigosGaguXlsx[pk])
                        else:
                            salidaCodigosGaguXlsx[pk] = crearRegistroCodigosG(rut, dimensiones, inicioVariableIcom[controlSalida], varIcomXls, valorVarIcomXls)

    # Encabezado POLIZA
    encabezadoArchivoUfmes = datoFuente[salidaArchivo['UF_MES']]
    # Encabezado POLIZA
    encabezadoArchivoPoliza = datoFuente[salidaArchivo['POLIZA']]
    encabezadoArchivoPoliza.extend(['RUT', 'POLIZA', 'AGENCIA', 'UNIDAD'])
    # Encabezado AGENTE
    encabezadoArchivoAgente = datoFuente[salidaArchivo['AGENTE']]
    encabezadoArchivoAgente.extend(['RUT', 'AGENCIA', 'UNIDAD'])
    # Encabezado CUOTA
    encabezadoArchivoCuota = datoFuente[salidaArchivo['CUOTA']]
    encabezadoArchivoCuota.extend(['RECIBO', 'POLIZA', 'CUOTA'])
    # Encabezado CODIGOS_GAGU
    encabezadoArchivoCodigoG = datoFuente[salidaArchivo['CODIGOS_GAGU']]
    encabezadoArchivoCodigoG.extend(['RUT', 'AGENCIA', 'UNIDAD'])

    dataGenerarTxt = [
        {'NOMBRE_ARCHIVO': nombreArchivoTxt[salidaArchivo['UF_MES']], 'DATA': salidaUfmesXlsx, 'ENCABEZADO': encabezadoArchivoUfmes},
        {'NOMBRE_ARCHIVO': nombreArchivoTxt[salidaArchivo['POLIZA']], 'DATA': salidaPolizaXlsx, 'ENCABEZADO': encabezadoArchivoPoliza},
        {'NOMBRE_ARCHIVO': nombreArchivoTxt[salidaArchivo['AGENTE']], 'DATA': salidaAgenteXlsx, 'ENCABEZADO': encabezadoArchivoAgente},
        {'NOMBRE_ARCHIVO': nombreArchivoTxt[salidaArchivo['CUOTA']], 'DATA': salidaCuotaXlsx, 'ENCABEZADO': encabezadoArchivoCuota},
        {'NOMBRE_ARCHIVO': nombreArchivoTxt[salidaArchivo['CODIGOS_GAGU']], 'DATA': salidaCodigosGaguXlsx, 'ENCABEZADO': encabezadoArchivoCodigoG}
    ]
    return dataGenerarTxt