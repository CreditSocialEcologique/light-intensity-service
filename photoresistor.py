from datetime import datetime
import serial
import asyncio
import aiohttp

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
    arduino_port = '/dev/ttyACM0'
    baud_rate = 9600
    base_url = "http://intensif05.ecole.ensicaen.fr:8080/"
    route_low_light = "api/light/reduceScore"
    id_device = "1"
    low_light_threshold = 100  # Threshold for low light

    try:
        arduino = serial.Serial(arduino_port, baud_rate, timeout=1)
        print(f"Connected to {arduino_port} at {baud_rate} baud")

        while True:
            try:
                sensor_value = int(arduino.readline().decode('utf-8').strip())
                print(f"Light Level: {sensor_value}")
                if sensor_value < low_light_threshold:
                    print("Low light level detected!")
                    asyncio.run(send_request(base_url + route_low_light, {"id_user": id_device, "message": "Low light level detected!"}))

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
