import adafruit_dht
import board
import time
import RPi.GPIO as GPIO
import drivers

#connecting Raspberry Pi to Water Pump
GPIO.setmode(GPIO.BCM)
Relay_Pin = 17
GPIO.setup(Relay_Pin, GPIO.OUT)

#defining function for pump on and off
def pump_on():
	print("pump is on")
	GPIO.output(Relay_Pin, GPIO.HIGH)
def pump_off():
	print("pump off")
	GPIO.output(Relay_Pin, GPIO.LOW)


while True:
    dht_device = adafruit_dht.DHT11(board.D4)

    try:
	#initializing variables 
        humidity, temperature = dht_device.humidity, dht_device.temperature
        if humidity is not None and temperature is not None:
            print(f"Temp=({temperature})C Humidity=({humidity})")
	#if humidiity is less than 60 turns pump on, else the pump is off
            if humidity < 60:
                pump_on()
		
            else:
                pump_off()
		
		
        else:
            print("Sensor failure. Check wiring.");
    except Exception as e:
        print("failed",e)
    dht_device.exit()
    time.sleep(2)

