# Importar las librerias necesarias para que se ejecute el proceso
import mysql.connector
from datetime import datetime
import csv
import win32com.client as win32

# Lista para almacenar los mensajes de print
log_messages = []

# Funcion de validacon del servidor si esta arriba o no
def verificar_disponibilidad_mysql(host, user, password):
    try:
        # Intenta establecer una conexión con los parámetros proporcionados
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )

        # La conexión se estableció correctamente
        message = f"La instancia de MySQL en {host} está disponible."
        log_messages.append(message)  # Agrega el mensaje a la lista
        connection.close()
        return True
    except mysql.connector.Error as error:
        # Ocurrió un error al intentar establecer la conexión
        message = f"No se puede conectar a la instancia de MySQL en {host}: {error}"
        log_messages.append(message)  # Agrega el mensaje a la lista



        # Envio del Corrreo al destinatarios
        outlook=win32.Dispatch("Outlook.Application")

        mail= outlook.CreateItem(0)

        # Correo destinatarios
        mail.To= "cesar.almeciga@groupcos.com.co; sebastian.avila@groupcos.com.co; juan.aya@groupcos.com.co; jose.suarez@groupcos.com.co;"

        # Copia (CC)
        # mail.CC = 'oscar.rios@groupcos.com.co;raphael.h@cos.com.co;'  # Agrega la dirección de correo para copia

        # Asunto del correo 
        mail.Subject='Alerta Indiponibilidad Servidor ' + host

        # Cuerpo del correo
        mail.Body= f'Cordial Saludo, \n \nLa sigiuiente es para reportar la indisponibilidad del servidor {message}. \n \n \n \n Quedo Atento, Cualquier inquietud o Solicitud.'

        mail.Send()


        return False
    
# Parámetros de conexión a MySQL
hosts = ["172.25.7.5","172.66.7.111","172.60.7.110","172.30.7.12","172.25.7.5","172.25.7.14","172.16.7.130","172.70.7.19","172.70.7.30","172.50.7.140","172.16.7.41","172.60.7.100","172.66.7.179","172.70.7.40","172.70.7.50","172.80.7.217","172.80.7.210"]  # Lista de hosts
users="areareporting"
passwords="O*998dQM8*sQ"

# Parámetros de conexión a las bases de datos de historial
historial_configs = [
    {
        'host': '172.70.7.61',  # Cambia esto al host correcto
        'user': 'juanaya6582',  # Cambia esto al usuario correcto
        'password': 'gZ%vsFWmf6%ANuU8',  # Cambia esto a la contraseña correcta
        'database': 'bbdd_groupcos_dba'  # Cambia esto al nombre de la base de datos correcta
    },
    {
        'host': '172.70.7.60',  # Cambia esto al host correcto
        'user': 'juanaya6582',  # Cambia esto al usuario correcto
        'password': 'gZ%vsFWmf6%ANuU8',  # Cambia esto a la contraseña correcta
        'database': 'bbdd_groupcos_dba'  # Cambia esto al nombre de la base de datos correcta
    }
]

# Ciclo para repetir el proceso para cada conjunto de host, usuario y contraseña
for host in hosts:
    # Verificar disponibilidad de MySQL
    disponibilidad = verificar_disponibilidad_mysql(host, users, passwords)

    # Guardar historial en las tablas correspondientes
    estado = '1' if disponibilidad else '0'
    now = datetime.now()

    for historial_config in historial_configs:
        connection_historial = mysql.connector.connect(**historial_config)
        cursor_historial = connection_historial.cursor()
        query_historial = "INSERT INTO tb_validacion_servidores (fecha, estado, ips) VALUES (%s, %s, %s)"
        values_historial = (now, estado, host)
        cursor_historial.execute(query_historial, values_historial)
        connection_historial.commit()
        cursor_historial.close()
        connection_historial.close()



# Guardar los mensajes en un archivo CSV
with open('log_messages.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Log Messages'])
    for message in log_messages:
        writer.writerow([message])

print("Se han exportado los mensajes de log a log_messages.csv.")        