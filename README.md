### Instalación de componentes necesarios:

+ Descargar e instalar una version de [Python 3.7.X](https://www.python.org/downloads/ "Python 3.7.X"), marcar la opción para agregar al PATH la varible de python al sistema.

![](https://i.postimg.cc/MG581vfz/pythonsetup-2.jpg)

+ Despues de finalizada la instalacion de Python abrir el CMD de Windows y para verificar que la instalacion esta correcta y esta configurada la variable de Python en el sistema ingresa el siguiente comando "python" en el CMD y este debera mostrar el interprete de python.

![](https://i.postimg.cc/gj6zBLhs/python1.png)

+ Escribir el comando "exit()" para salir y volver al cursor de la consola, una vez en el cursor de la consola dirigirse al directorio del archivo "requirements.txt" (esta dentro de los archivos de la aplicación) y escribir lo siguiente para instalar las librerias necesarias.

```bash
pip install -r requirements.txt
```

+ Como ultimo paso el archivo que controla la ejecucion es "procesoRegenerarXlsx.py" y para ejecutarlo se debe escribir el siguiente comando en la consola.

```bash
python procesoRegenerarXlsx.py
```

## NOTA

Para los fines de prueba la version actual tiene configurado los parametros de manera manual.
+ El archivo de carga debe estar en la carpeta "INPUTS/" y el mismo debe tener el nombre "CARGA_VARIABLES".
+ Los parametros fechaProceso, rutaArchivoConsolidado (linea 19 y el segundo parametro CARGA_VARIABLE es el nombre del archivo a leer), rutaArchivosGenerados y rutaArchivoXml estan definidos manualmente en el archivo "procesoRegenerarXlsx.py" entre las linas 18 a 21.
![](https://i.postimg.cc/SR3RG2SL/Captura.jpg)