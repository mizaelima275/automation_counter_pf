from umqtt.simple import MQTTClient # type: ignore
import network # type: ignore

wifi = None
client = None

def connect_wifi(ssid, password):
    global wifi
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.connect(ssid, password)
    while not wifi.isconnected():
        pass

def connect_mqtt(broker, client_id, user, password):
    global client
    client = MQTTClient(client_id, broker, user=user, password=password)
    client.connect()
