import paho.mqtt.client as mqtt
import pymysql.cursors
from datetime import datetime
import config

MQTT_BROKER = config.MQTT_BROKER
MQTT_PORT = int(config.MQTT_PORT)
MQTT_TOPIC = "/PC1/hw/hoge/temp"
SQL_HOST = config.SQL_HOST
SQL_USER = config.SQL_USER
SQL_PASSWORD = config.SQL_PASSWORD
SQL_DB = config.SQL_DB

def on_connect(client, userdata, flag, rc):
  print("Connected with result code " + str(rc))
  client.subscribe(MQTT_TOPIC)

def on_disconnect(client, userdata, rc):
  if  rc != 0:
    print("Unexpected disconnection.")

def on_message(client, userdata, msg):
  topic = msg.topic
  raw_data = str(msg.payload)
  data = raw_data.replace("b","").replace("'","")
  print("[", topic, "]", data)
  set_mysql(topic, data)

def set_mysql(topic, data):
  connection = pymysql.connect(host = SQL_HOST, user = SQL_USER, password = SQL_PASSWORD, db = SQL_DB, charset='utf8', cursorclass=pymysql.cursors.DictCursor)
  with connection.cursor() as cursor:
    sql = "INSERT INTO `hw_temp`(data_topic, data_value, data_time) VALUES (%s, %s, %s)"
    r = cursor.execute(sql, (topic, float(data), datetime.now().strftime( '%Y-%m-%d %H:%M:%S' )))
    connection.commit()

def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_forever()

if __name__ == "__main__":
    main()
