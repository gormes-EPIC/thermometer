import time
import requests

# Comment these lines for testing
# import board
# import adafruit_dht
# dhtDevice = adafruit_dht.DHT11(board.D4, use_pulseio=False)

BASE_URL = "http://192.168.110.129:5000"  # replace with your machine's IP
last_email = time.time()
# def get_temp():
#     """
#     Function to get the temperature from a sensor
#     """
#     try:
#         temperature_c = dhtDevice.temperature
#         temperature_c = float(temperature_c)
#         if temperature_c == None:
#             temperature_c = 70
#         temp = temperature_c * (9 / 5) + 32
#         return temp
#     except TypeError:
#         return 70.5
#     except RuntimeError as error:
#         time.sleep(0.5)
#         return 70.5
#     except Exception as error:
#         dhtDevice.exit()
#         raise error
    
#     return 70.5

def get_temp_test():
    """
    Function to get the temperature from a sensor
    """
    return 70.55

def send_email(temp):
    x = requests.post("https://epiccs.daiki-bot.xyz/alert/:"+str(temp)+"/:"+str(80))
    

def get_temp_API():
    """
    Function to get the temperature from a sensor API
    """
    response = requests.get(f"{BASE_URL}/items")
    print("GET /items:", response.json())
    dic = response.json()

    if float(dic[0]["temp"]) > 71:
        if time.time() > (last_email + 5400000):
            send_email(float(dic[0]["temp"]))
            last_email  = time.time()
    return float(dic[0]["temp"])


# # GET all items
# response = requests.get(f"{BASE_URL}/items")
# print("GET /items:", response.json())

# # POST a new item
# new_item = {"name": "Test Item"}
# response = requests.post(f"{BASE_URL}/items", json=new_item)
# print("POST /items:", response.json())

# # GET the newly created item
# item_id = response.json()["id"]
# response = requests.get(f"{BASE_URL}/items/{item_id}")
# print(f"GET /items/{item_id}:", response.json())

# # PUT to update the item
# updated_item = {"name": "Updated Test Item"}
# response = requests.put(f"{BASE_URL}/items/{item_id}", json=updated_item)
# print(f"PUT /items/{item_id}:", response.json())

# # DELETE the item
# response = requests.delete(f"{BASE_URL}/items/{item_id}")
# print(f"DELETE /items/{item_id}:", response.status_code)
