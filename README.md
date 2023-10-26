Automatización de la verificación de disponibilidad de servidores MySQL

Este proyecto automatiza la verificación de disponibilidad de servidores MySQL. El proceso se realiza de la siguiente manera:

Se verifica la disponibilidad de cada servidor MySQL en la lista de hosts.
Si un servidor no está disponible, se envía un correo electrónico de alerta a los destinatarios especificados.
Se registra la información del proceso en las tablas de historial de las bases de datos especificadas.
Requisitos

Python 3.11.3 o superior
Las bibliotecas mysql.connector, datetime, csv y win32com.client
Instalación

Instala las dependencias:
pip install -r requirements.txt
Uso

Modifica los parámetros de conexión a MySQL en el archivo config.py.
Ejecuta el script principal:
python main.py
Explicación del código

El código se divide en las siguientes partes:

Importación de librerías
Función de validación de disponibilidad de MySQL
Parámetros de conexión a MySQL
Ciclo para verificar disponibilidad de servidores
Guardado de historial en las tablas correspondientes
Guardado de los mensajes de log
Función de validación de disponibilidad de MySQL

Esta función intenta establecer una conexión con el servidor MySQL especificado. Si la conexión se establece correctamente, se devuelve True. De lo contrario, se devuelve False y se envía un correo electrónico de alerta.

Ciclo para verificar disponibilidad de servidores

Este ciclo recorre la lista de hosts y llama a la función de validación de disponibilidad de MySQL para cada uno.

Guardado de historial en las tablas correspondientes

Si un servidor no está disponible, se registra la información del proceso en las tablas de historial de las bases de datos especificadas.

Guardado de los mensajes de log

Los mensajes de log se guardan en un archivo CSV.

Mejoras potenciales

Agregar más información al archivo CSV de mensajes de log.
Implementar un sistema de alertas más robusto.
Extender el proceso para verificar la disponibilidad de otros componentes de la infraestructura.

