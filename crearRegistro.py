def validarVacio(valorAnterior, valor):
    if valorAnterior is '':
        return valor
    return valorAnterior

#  CREAR REGISTROS UF MES
def crearRegistroUfmes(keyIcom, varIcomXls, valorVarIcomXls):

    salidaTxt = dict()
    salidaTxt.update(keyIcom)
    salidaTxt[varIcomXls] = valorVarIcomXls
    return salidaTxt

#  CREAR REGISTROS AGENTES
def crearRegistroAgente(rut, dimensiones:dict(), keyIcom, varIcomXls, valorVarIcomXls):

    salidaTxt = dict()
    salidaTxt.update(keyIcom)
    salidaTxt.setdefault('RUT', rut)
    salidaTxt.setdefault('AGENCIA', dimensiones['AGENCIA'])
    salidaTxt.setdefault('UNIDAD', dimensiones['UNIDAD'])
    salidaTxt[varIcomXls] = valorVarIcomXls
    return salidaTxt

def actualizarRegistroAgente(dimensiones:dict(), varIcomXls, valorVarIcomXls, salidaTxt):

    salidaTxt[varIcomXls] = valorVarIcomXls
    salidaTxt['AGENCIA'] = validarVacio(salidaTxt['AGENCIA'], dimensiones['AGENCIA'])
    salidaTxt['UNIDAD'] = validarVacio(salidaTxt['UNIDAD'], dimensiones['UNIDAD'])
    return salidaTxt

#  CREAR REGISTROS POLIZA
def crearRegistroPoliza(poliza, dimensiones:dict(), keyIcom, varIcomXls, valorVarIcomXls):

    salidaTxt = dict()
    salidaTxt.update(keyIcom)
    salidaTxt.setdefault('RUT', dimensiones['RUT'])
    salidaTxt.setdefault('POLIZA', poliza)
    salidaTxt.setdefault('AGENCIA', dimensiones['AGENCIA'])
    salidaTxt.setdefault('UNIDAD', dimensiones['UNIDAD'])
    salidaTxt[varIcomXls] = valorVarIcomXls
    return salidaTxt

def actualizarRegistroPoliza(dimensiones:dict(), varIcomXls, valorVarIcomXls, salidaTxt):

    salidaTxt[varIcomXls] = valorVarIcomXls
    salidaTxt['RUT'] = validarVacio(salidaTxt['RUT'], dimensiones['RUT'])
    salidaTxt['AGENCIA'] = validarVacio(salidaTxt['AGENCIA'], dimensiones['AGENCIA'])
    salidaTxt['UNIDAD'] = validarVacio(salidaTxt['UNIDAD'], dimensiones['UNIDAD'])
    return salidaTxt

#  CREAR REGISTROS CUOTA
def crearRegistroCuota(dimensiones, keyIcom, varIcomXls, valorVarIcomXls):

    salidaTxt = dict()
    salidaTxt.update(keyIcom)
    salidaTxt.setdefault('RECIBO', dimensiones['RECIBO'])
    salidaTxt.setdefault('POLIZA', dimensiones['POLIZA'])
    salidaTxt.setdefault('CUOTA', dimensiones['CUOTA'])
    salidaTxt[varIcomXls] = valorVarIcomXls
    return salidaTxt

def actualizarRegistroCuota(varIcomXls, valorVarIcomXls, salidaTxt):

    salidaTxt[varIcomXls] = valorVarIcomXls
    return salidaTxt

#  CREAR REGISTROS CODIGOS_GAGU
def crearRegistroCodigosG(rut, dimensiones, keyIcom, varIcomXls, valorVarIcomXls):

    salidaTxt = dict()
    salidaTxt.update(keyIcom)
    salidaTxt.setdefault('RUT', rut)
    salidaTxt.setdefault('AGENCIA', dimensiones['AGENCIA'])
    salidaTxt.setdefault('UNIDAD', dimensiones['UNIDAD'])
    salidaTxt[varIcomXls] = valorVarIcomXls
    return salidaTxt

def actualizarRegistroCodigosG(varIcomXls, valorVarIcomXls, salidaTxt):

    salidaTxt[varIcomXls] = valorVarIcomXls
    return salidaTxt
