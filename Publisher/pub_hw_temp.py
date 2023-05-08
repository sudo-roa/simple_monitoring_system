import paho.mqtt.client as mqtt
from time import sleep
import config

MQTT_BROKER = config.MQTT_BROKER
MQTT_PORT = int(config.MQTT_PORT)
MQTT_TOPIC = "/PC1/hw/hoge/temp"
DATA_PATH = "/sys/class/thermal/thermal_zone4/"

def on_connect(client, userdata, flag, rc):
    print("Connected with result code " + str(rc))

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection.")

def on_publish(client, userdata, mid):
    print("{} : publish to {} [ {} ]".format(mid, MQTT_BROKER, MQTT_TOPIC))

def get_hw_temp():
    # with open(DATA_PATH+"type") as f:
    #     data_type = f.read()
    with open(DATA_PATH+"temp") as f:
        data_temp = f.read()
    return (int(data_temp)/1000)

def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_publish = on_publish

    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_start()
    while True:
        client.publish(MQTT_TOPIC, get_hw_temp())
        sleep(30)

if __name__ == '__main__':
    main()