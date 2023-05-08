import paho.mqtt.client as mqtt
import pymysql.cursors
from datetime import datetime
import re
import config

MQTT_BROKER = config.MQTT_BROKER
MQTT_PORT = int(config.MQTT_PORT)
MQTT_TOPIC = "/PC1/hw/hoge/temp"

def on_connect(client, userdata, flag, rc):
  print("Connected with result code " + str(rc))
  client.subscribe(MQTT_TOPIC)

def on_disconnect(client, userdata, rc):
  if  rc != 0:
    print("Unexpected disconnection.")

def on_message(client, userdata, msg):
  topic = msg.topic
  raw_data = str(msg.payload)
  print(topic)
  print(raw_data)
#   regex = r'[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?'
#   data = re.findall(rf'({regex})', raw_data)
#   set_mysql(topic, data[0][0])

def set_mysql(topic, data):
  connection = pymysql.connect(host= 'localhost',
                                user='grafanaReader',
                                password='grafana',
                                db='grafana_db',
                                charset='utf8',
                                cursorclass=pymysql.cursors.DictCursor)
  with connection.cursor() as cursor:
    sql = "INSERT INTO `pi_table`(type, value, data_time) VALUES (%s, %s, %s)"
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
