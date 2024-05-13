from machine import Pin # type: ignore
import time
import database

last_pulse_time = 0
debounce_interval1 = 30
debounce_interval2 = 60

def count_pulse(pin):
    global last_pulse_time
    current_millis = time.ticks_ms()
    if current_millis - last_pulse_time > debounce_interval1:
        if current_millis - last_pulse_time > debounce_interval2:
            count = database.get_count() + 1
            database.update_count(count)
            last_pulse_time = current_millis

def init_pulse_counter(sensor_pin):
    sensor = Pin(sensor_pin, Pin.IN, Pin.PULL_UP)
    sensor.irq(trigger=Pin.IRQ_FALLING, handler=count_pulse)
