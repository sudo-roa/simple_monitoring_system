from dotenv import load_dotenv
import os
load_dotenv()

MQTT_CLIENT = os.getenv("MQTT_CLIENT")
MQTT_PORT = os.getenv("MQTT_PORT")

