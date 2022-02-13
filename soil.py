import time
import board
import adafruit_sht31d

# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()
sensor = adafruit_sht31d.SHT31D(i2c)

# loopcount = 0
# while True:
#     print("\nTemperature: %0.1f C" % sensor.temperature)
#     print("Humidity: %0.1f %%" % sensor.relative_humidity)
#     loopcount += 1
#     time.sleep(2)
#     # every 10 passes turn on the heater for 1 second
#     if loopcount == 10:
#         loopcount = 0
#         sensor.heater = True
#         print("Sensor Heater status =", sensor.heater)
#         time.sleep(1)
#         sensor.heater = False
#         print("Sensor Heater status =", sensor.heater)


while True:
    print("\nTemperature: %0.1f C" % sensor.temperature)
    print("Humidity: %0.1f %%" % sensor.relative_humidity)
    sensor.heater = True
    print("Sensor Heater status =", sensor.heater)
    time.sleep(1)




        

# import RPi.GPIO as GPIO
# import time
 
# #GPIO SETUP
# channel = 21
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(channel, GPIO.IN)
 
# def callback(channel):
#         if GPIO.input(channel):
#                 print ("Water Detected!")
#         else:
#                 print ("Water Detected!")
 
# GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=100)  # let us know when the pin goes HIGH or LOW
# GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change
 
# # infinite loop
# while True:
#         time.sleep(1)