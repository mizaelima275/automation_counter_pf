# Contador de Pulsos IoT

Este é um projeto de contador de pulsos IoT que faz a conversão levando em conta o debounce para contabilizar a entrada de água no edifício, a cada 10L é contabilizado 1 pulso.

## Funcionalidades

- **Detecção de Pulsos**: O projeto utiliza um contador de pulsos para detectar pulsos em um pino específico.
- **Conexão Wi-Fi**: O dispositivo se conecta a uma rede Wi-Fi para comunicação com o servidor MQTT.
- **Publicação via MQTT**: O número de pulsos detectados é publicado em um tópico MQTT para monitoramento remoto.

## Pré-requisitos

- Dispositivo compatível com MicroPython, como ESP32.
- Contador de pulsos conectado a um pino específico.
- Acesso à rede Wi-Fi.
- Configurações do servidor MQTT, incluindo endereço, porta, usuário e senha.

## Instalação e Configuração

1. Conecte o contador de pulsos ao dispositivo, especificando o pino correto no arquivo `config.py`.
2. Configure as variáveis de configuração no arquivo `config.py`, incluindo SSID e senha da rede Wi-Fi, detalhes do servidor MQTT e ID do cliente.
3. Carregue o código Python para o dispositivo.

## Uso

O dispositivo iniciará a detecção de pulsos assim que for ligado. O número de pulsos detectados será exibido a cada segundo e publicado no tópico MQTT especificado.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests para melhorar este projeto.
