from dotenv import load_dotenv
import os
load_dotenv()

MQTT_BROKER = os.getenv("MQTT_BROKER")
MQTT_PORT = os.getenv("MQTT_PORT")

SQL_HOST = os.getenv("SQL_HOST")
SQL_USER = os.getenv("SQL_USER")
SQL_PASSWORD = os.getenv("SQL_PASSWORD")
SQL_DB = os.getenv("SQL_DB")

# print(MQTT_BROKER, MQTT_PORT, SQL_HOST, SQL_USER, SQL_PASSWORD, SQL_DB)