import time

# Comment these lines for testing
import board
import adafruit_dht
dhtDevice = adafruit_dht.DHT11(board.D4, use_pulseio=False)

def get_temp():
    """
    Function to get the temperature from a sensor
    """
    try:
        temperature_c = dhtDevice.temperature
        temperature_c = float(temperature_c)
        if temperature_c == None:
            temperature_c = 70
        temp = temperature_c * (9 / 5) + 32
        return temp
    except TypeError:
        return 70.5
    except RuntimeError as error:
        time.sleep(0.5)
        return 70.5
    except Exception as error:
        dhtDevice.exit()
        raise error
    
    return 70.5

def get_temp_test():
    """
    Function to get the temperature from a sensor
    """
    return 70.5