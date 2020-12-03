import os.path
import sys

from leerCargaIcomXLSX import leerCargaIcom
from leerXml import configuracionXmlArchivos

from variablesConfiguracion import PATH_ARCHIVOS
from crearCsv import salidaArchivoTxt, salidaLogTxt

PROCESO_LOG = dict()

try:
    if len(sys.argv) == 1:
        # fechaProceso = sys.argv[1]
        # rutaArchivoConsolidad = sys.argv[2]
        # rutaArchivosGenerados = sys.argv[3]
        # rutaArchivoXml = sys.argv[4]
        fechaProceso = '202010'
        rutaArchivoConsolidado = '%s%s.csv' % (PATH_ARCHIVOS['ENTRADA_CSV'], 'CARGA_VARIABLES')
        rutaArchivosGenerados = PATH_ARCHIVOS['SALIDA_TXT']
        rutaArchivoXml = 'Variables2020.xml'

        if not os.path.isfile(rutaArchivoConsolidado):
            raise Exception('Error archivo: %s no encontrado' % rutaArchivoConsolidado)
        if not os.path.isfile(rutaArchivoXml):
            raise Exception('Error archivo: %s no encontrado' % rutaArchivoXml)

        configuracionXml = list(configuracionXmlArchivos(rutaArchivoXml))
        # LOG
        PROCESO_LOG.setdefault('LECTURA_ARCHIVO_XML', {len(PROCESO_LOG)+1: 'Lectura del archivo: %s Ok' % rutaArchivoXml})

        dataArchivosAgentes = leerCargaIcom(rutaArchivoConsolidado, configuracionXml)
        # LOG
        PROCESO_LOG.setdefault('LECTURA_ARCHIVO_CONSOLIDADO', {len(PROCESO_LOG)+1: 'Lectura del archivo: %s Ok' % rutaArchivoConsolidado})
        PROCESO_LOG.setdefault('INICIO_ARCHIVOS_SALIDA', {len(PROCESO_LOG)+1: 'Iniciando escritura de: %s archivo(s)' % len(dataArchivosAgentes)})

        archivosEscritos = 0
        for archivo in range(0,len(dataArchivosAgentes)):
            archivoTxt, separador, extension = str(dataArchivosAgentes[archivo]['NOMBRE_ARCHIVO']).partition('yyyymm')
            salidaTxt = rutaArchivosGenerados + archivoTxt + fechaProceso + '_CAR' + extension
            escribirTxt = salidaArchivoTxt(salidaTxt, dataArchivosAgentes[archivo]['DATA'], dataArchivosAgentes[archivo]['ENCABEZADO'])
            if escribirTxt is not str:
                PROCESO_LOG.setdefault('ESCRITURA_ARCHIVO_TXT_%s' % archivo, {len(PROCESO_LOG)+1: 'Escritura del archivo: %s, registros escritos: %s' % (salidaTxt, len(dataArchivosAgentes[archivo]['DATA'])+1)})
                archivosEscritos += 1
            else:
                PROCESO_LOG.setdefault('ESCRITURA_ARCHIVO_TXT%s' % archivo, {len(PROCESO_LOG)+1: 'Error al escribir archivo: %s | %s' % (salidaTxt, escribirTxt)})
        PROCESO_LOG.setdefault('PROCESO_PRINCIPAL', {len(PROCESO_LOG)+1: 'Fin del proceso de lectura de: %s y escritura de: %s archivo(s)' % (rutaArchivoConsolidado, archivosEscritos)})
    else:
        PROCESO_LOG.setdefault('PROCESO_PRINCIPAL', {len(PROCESO_LOG)+1: 'Error el proceso necesita: 4 parametros para iniciar'})
except Exception as e:
    PROCESO_LOG.setdefault('ERROR', {len(PROCESO_LOG)+1: e})
finally:
    pathLogSalida = 'PROCESO_LOG/test_log.txt'
    if salidaLogTxt(pathLogSalida, PROCESO_LOG):
        print("Archivo: %s creado !!" % pathLogSalida)

