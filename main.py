import time
import pulse_counter
import wifi_mqtt
import database
import config

# Inicializa o contador de pulsos
pulse_counter.init_pulse_counter(config.SENSOR_PIN)

# Conectar ao Wi-Fi
wifi_mqtt.connect_wifi(config.WIFI_SSID, config.WIFI_PASSWORD)

# Conectar ao broker MQTT
wifi_mqtt.connect_mqtt(config.MQTT_BROKER, config.CLIENT_ID, config.MQTT_USER, config.MQTT_PASSWORD)

# Loop principal
while True:
    # Exibir o número de pulsos a cada segundo
    time.sleep(1)
    pulse_count = database.get_count()
    print("Pulsos detectados:", pulse_count)
    
    # Publica o número de pulsos no tópico MQTT
    wifi_mqtt.client.publish(config.TOPIC, str(pulse_count))
