import board
import time
import busio
import datetime
from datetime import datetime

import pymongo
import certifi
from pymongo import MongoClient


import adafruit_tca9548a
import adafruit_sht4x

import adafruit_sgp30

import adafruit_sht31d

import adafruit_scd30

#################Soil Moisture sensor2#################

import RPi.GPIO as GPIO 
channel =21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel,GPIO.IN)
#################Soil Moisture sensor2#################

# Create I2C bus as normal
i2c = board.I2C()  # uses board.SCL and board.SDA


# Create the TCA9548A object and give it the I2C bus
tca = adafruit_tca9548a.TCA9548A(i2c)

#tsl1= adafruit_sgp30.Adafruit_SGP30(tca[0])
tsl1= adafruit_sht4x.SHT4x(tca[0])
tsl2= adafruit_sht4x.SHT4x(tca[1])
tsl3= adafruit_sht31d.SHT31D(tca[2])
 
tsl4= adafruit_scd30.SCD30(tca[3])

#################SGP30#################
tsl5= adafruit_sgp30.Adafruit_SGP30(tca[4])

print("SGP30 serial #", [hex(i) for i in tsl5.serial])

tsl5.iaq_init()
tsl5.set_iaq_baseline(0x8973, 0x8AAE)

elapsed_sec = 0

#################SGP30#################


#################SHT40#################
tsl1.mode = adafruit_sht4x.Mode.NOHEAT_HIGHPRECISION
tsl2.mode = adafruit_sht4x.Mode.NOHEAT_HIGHPRECISION
# Can also set the mode to enable heater
# sht.mode = adafruit_sht4x.Mode.LOWHEAT_100MS
print("Current mode is: ", adafruit_sht4x.Mode.string[tsl1.mode])
print("Current mode is: ", adafruit_sht4x.Mode.string[tsl2.mode])
#################SHT40#################

#################Soil Moisture sensor2#################
def callback(channel):
    if channel.input(channel):
        print("No water Detected")
    else:
        print("Water Detected")
GPIO.add_event_detect(channel,GPIO.BOTH,bouncetime=300)
GPIO.add_event_callback(channel,callable)
#################Soil Moisture sensor2#################



connection = MongoClient("mongodb+srv://subham:1234@cluster0.t4iwt.mongodb.net/testdb?retryWrites=true&w=majority",tlsCAFile=certifi.where())
db=connection["testdb"]
collection=db["test"]




while True:
    #################SHT40#################
    temperature1, relative_humidity1 = tsl1.measurements
    temperature2, relative_humidity2 = tsl2.measurements
    print("Temperature1: %0.1f C" % temperature1)
    print("Humidity1: %0.1f %%" % relative_humidity1)
    print("Temperature2: %0.1f C" % temperature2)
    print("Humidity2: %0.1f %%" % relative_humidity2)
    print("")
    #################SHT40#################


    #################Soil Sensor#################
    # print("\nTemperature: %0.1f C" % tsl3.temperature)
    print("Humidity: %0.1f %%" % tsl3.relative_humidity)
    tsl3.heater = True
    print("Sensor Heater status =", tsl3.heater)
    #################Soil Sensor#################

    #################SCD30#################
    if tsl4.data_available:
        print("Data Available!")
        print("CO2: %d PPM" % tsl4.CO2)
        # print("Temperature: %0.2f degrees C" % scd.temperature)
        # print("Humidity: %0.2f %% rH" % scd.relative_humidity)
        # print("")
        # print("Waiting for new data...")
        # print("")
    #################SCD30#################



    #################SGP30(VOC)#################

    print("eCO2 = %d ppm \t TVOC = %d ppb" % (tsl5.eCO2, tsl5.TVOC))
    time.sleep(1)
    elapsed_sec += 1
    if elapsed_sec > 10:
        elapsed_sec = 0
        print(
            "**** Baseline values: eCO2 = 0x%x, TVOC = 0x%x"
            % (tsl5.baseline_eCO2, tsl5.baseline_TVOC)
        )



    tsl1.measurements1 ={
    "timestamp":datetime.now().strftime('%y-%m-%d,%H:%M:%S,'),
    "temperature1":("Temperature1: %0.1f C" % temperature1),
    "Humidity1":("Humidity1: %0.1f %%" % relative_humidity1),
    "temperature2":("Temperature2: %0.1f C" % temperature2),
    "Humidity2":("Humidity2: %0.1f %%" % relative_humidity2),
    "Soil Mositure":("Humidity: %0.1f %%" % tsl3.relative_humidity),
    "TVOC":("TVOC = %d ppb" % tsl5.TVOC),
    "CO2":("CO2: %d PPM" % tsl4.CO2)
    }
    deviceId=1
    
    collection.update_one({'deviceId': deviceId,'nsamples':{'$lt':200}},
    {
        '$push':{'samples':tsl1.measurements1},
        '$inc':{'nsamples':1}
    },
    upsert=True

    )


    time.sleep(1)





    
