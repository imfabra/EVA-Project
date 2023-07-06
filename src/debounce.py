import time
import RPi.GPIO as GPIO

# Variables de configuración
DEBOUNCE_TIME = 0.1  # Tiempo de debounce en segundos
STABLE_HIGH_COUNT = 3  # Número de flancos en valor alto para la estabilización
PINS = [18, 23, 24]  # Lista de pines de las entradas digitales

# Variables globales
last_states = {}
last_times = {}
high_counts = {}
stable_highs = {}

def debounce_callback(channel):
    global last_states, last_times, high_counts, stable_highs

    current_time = time.time()
    pin = channel

    if (current_time - last_times[pin]) < DEBOUNCE_TIME:
        return

    # Lectura del estado lógico de la entrada digital
    state = GPIO.input(pin)

    if state != last_states[pin]:
        # El estado ha cambiado después del tiempo de debounce
        last_states[pin] = state
        last_times[pin] = current_time

        if state == GPIO.HIGH:
            high_counts[pin] += 1
            if high_counts[pin] >= STABLE_HIGH_COUNT:
                stable_highs[pin] = True
        else:
            high_counts[pin] = 0
            stable_highs[pin] = False

        if stable_highs[pin]:
            # Acción a realizar cuando se alcanza la estabilización de tres flancos en valor alto
            print(f"¡Estabilización de tres flancos en valor alto alcanzada en el pin {pin}!")

# Configuración de los pines de GPIO
GPIO.setmode(GPIO.BCM)
for pin in PINS:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    last_states[pin] = GPIO.input(pin)
    last_times[pin] = time.time()
    high_counts[pin] = 0
    stable_highs[pin] = False

# Configuración de interrupción por cambio en los pines
for pin in PINS:
    GPIO.add_event_detect(pin, GPIO.BOTH, callback=debounce_callback, bouncetime=10)

# Bucle principal
try:
    while True:
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
