from xml.etree import ElementTree

def configuracionXmlArchivos(archivo):
    try:
        with open(archivo, 'rt') as archivo:
            archivoXml = ElementTree.parse(archivo)

        valorSalidaIcom = dict()
        datoFuenteExportar = []
        variableIcomExportar = []
        inicioVariableIcom = []
        archivoSalidaTxt = []

        for archivoVariable in archivoXml.iter('archivo-carga'):
            # TAG <archivo-carga>
            archivoSalida = archivoVariable.attrib.get('patron')
            archivoSalidaTxt.append(archivoSalida)
            variablesIcomXml = dict()
            inicioIcomXml = dict()
            datoFuenteKey = []
            # TAG <dato-fuente>
            for datoFuente in archivoVariable.iter('dato-fuente'):
                valorDatoFuente = datoFuente.attrib.get('nombre')
                datoFuenteKey.append(valorDatoFuente)
                # TAG <variable-icom>
                for variableIcom in datoFuente.iter('variable-icom'):
                    valorVariableIcom = variableIcom.attrib.get('nombre')
                    variablesIcomXml.setdefault(valorVariableIcom, 0)
                    inicioIcomXml.setdefault(valorVariableIcom, None)

            datoFuenteExportar.append(datoFuenteKey)
            variableIcomExportar.append(variablesIcomXml)
            inicioVariableIcom.append(inicioIcomXml)
        return datoFuenteExportar, variableIcomExportar, inicioVariableIcom, archivoSalidaTxt
    except Exception as e:
        error = 'Error al leer archivo: %s | %s' % (archivo, e)
        return error