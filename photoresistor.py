from datetime import datetime
import serial
import asyncio
import aiohttp

# Méthode permettant de faire une requete sur le web asynchrone. L'échec de la requete ne génère pas d'exception.
async def send_request(url, data):
    try:
        async with aiohttp.ClientSession() as session:
            print(f"Sending request to {url}")
            async with session.post(url, data=data) as response:
                print(f"Request sent to {url}")
    except:
        print(f"Request to {url} failed")

def main():
    # Replace 'COM3' with your Arduino port
    arduino_port = '/dev/ttyACM0' # Le port peut changer. Sur Windows, cela sera probablement COM3
    baud_rate = 9600 # Le nombre de symbole par seconde (un arduino est par défaut configuré sur 9600)
    base_url = "http://intensif05.ecole.ensicaen.fr:8080/" # L'url de l'api
    route_low_light = "api/light/reduceScore" # La route a appelé
    id_device = "1" # correspond à l'id de l'utilisateur
    low_light_threshold = 100  # Détermine la valeur maximale qui déclenche une diminution du score de l'utilisateur

    try:
        arduino = serial.Serial(arduino_port, baud_rate, timeout=1) # Se connecte à l'arduino
        print(f"Connected to {arduino_port} at {baud_rate} baud")

        while True:
            try:
                sensor_value = int(arduino.readline().decode('utf-8').strip()) # Lit ce que l'arduino envoie
                print(f"Light Level: {sensor_value}")
                if sensor_value < low_light_threshold: # La valeur envoyé va de 0 (très lumineux) à 1023 (sombre)
                    print("Low light level detected!")
                    asyncio.run(send_request(base_url + route_low_light, {"id_user": id_device, "message": "Low light level detected!"})) # Crée une tache asynchrone qui va lancer la requete web

            except ValueError:
                # Handle the case where the sensor value is not an integer
                continue

    except serial.SerialException as e:
        print(f"Error: {e}")

    finally:
        if arduino.is_open:
            arduino.close()
            print("Connection closed.")

if __name__ == "__main__":
    main()
