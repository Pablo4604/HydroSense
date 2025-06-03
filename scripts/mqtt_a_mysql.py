import paho.mqtt.client as mqtt
import mysql.connector

# Configuración de la base de datos MySQL
db = mysql.connector.connect(
    host="localhost",        # Cambiar según el host de tu MySQL
    user="root",        # Cambiar por el usuario de MySQL
    password="P@blo33225",   # Cambiar por la contraseña
    database="mqtt_data"      # Base de datos creada anteriormente
)

cursor = db.cursor()

# Función para guardar datos en MySQL
def guardar_datos_en_mysql(topic, mensaje):
    sql = "INSERT INTO sensor_data (topic, message) VALUES (%s, %s)"
    val = (topic, mensaje)
    cursor.execute(sql, val)
    db.commit()
    print(f"Datos guardados: {cursor.rowcount} fila(s) afectada(s)")

# Callback cuando se recibe un mensaje
def on_message(client, userdata, msg):
    print(f"Mensaje recibido en el topic {msg.topic}: {msg.payload.decode()}")
    
    # Aquí puedes transformar el mensaje si es necesario (por ejemplo, si es JSON)
    try:
        mensaje = msg.payload.decode()  # Decodifica el mensaje
        # Si esperas un JSON, puedes cargarlo con json.loads(mensaje)
        
        # Guardar en MySQL
        guardar_datos_en_mysql(msg.topic, mensaje)
        
    except Exception as e:
        print(f"Error al procesar el mensaje: {e}")

# Callback para la conexión exitosa al broker
def on_connect(client, userdata, flags, rc):
    print(f"Conectado con código de resultado {rc}")
    client.subscribe("esp32/agua")  # Cambia esto al topic que desees

# Configurar cliente MQTT
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Conectarse al broker EMQX
client.connect("broker.hivemq.com", 1883, 60)  # Cambiar si el broker no está en localhost

# Mantener el script en funcionamiento para recibir mensajes
client.loop_forever()
