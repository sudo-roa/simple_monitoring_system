import paho.mqtt.client as mqtt
from time import sleep
import config

MQTT_CLIENT = config.MQTT_CLIENT
MQTT_PORT = int(config.MQTT_PORT)
MQTT_TOPIC = "/PC1/mem/rate"
DATA_PATH = "/proc/meminfo"

def on_connect(client, userdata, flag, rc):
    print("Connected with result code " + str(rc))

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection.")

def on_publish(client, userdata, mid):
    print("{} : publish to {} [ {} ]".format(mid, MQTT_CLIENT, MQTT_TOPIC))

def calc_mem_use_rate():
    with open(DATA_PATH) as f:
        for line in f:
            if("MemTotal" in line):
                mem_total = int(line.split()[1])
            if("MemAvailable" in line):
                mem_available = int(line.split()[1])
    return ((mem_total - mem_available) / mem_total)

def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_publish = on_publish

    client.connect(MQTT_CLIENT, MQTT_PORT, 60)
    client.loop_start()

    while True:
        client.publish(MQTT_TOPIC, calc_mem_use_rate())
        sleep(30)

if __name__ == '__main__':
    main()