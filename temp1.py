import time
import board
import adafruit_tca9548a
import adafruit_sht4x
import datetime
from datetime import datetime
import csv


import pymongo
import certifi
from pymongo import MongoClient

i2c = board.I2C()  # uses board.SCL and board.SDA
tca = adafruit_tca9548a.TCA9548A(i2c)
tsl1= adafruit_sht4x.SHT4x(tca[0])

print("Found SHT4x with serial number", hex(tsl1.serial_number))

tsl1.mode = adafruit_sht4x.Mode.NOHEAT_HIGHPRECISION
# Can also set the mode to enable heater
# sht.mode = adafruit_sht4x.Mode.LOWHEAT_100MS
print("Current mode is: ", adafruit_sht4x.Mode.string[tsl1.mode])



connection = MongoClient("mongodb+srv://subham:1234@cluster0.t4iwt.mongodb.net/testdb?retryWrites=true&w=majority",tlsCAFile=certifi.where())
db=connection["testdb"]
collection=db["test"]






# def store_data(time,temperature,Humidity):
#     append=[time,temperature,Humidity]
#     with open('sensors_output.csv','a') as csvFile:
#         writer=csv.writer(csvFile)
#         writer.writerow(append)
    
#     csvFile.close()




# while True:
#     temperature, relative_humidity = {tsl1.measurements}
#     print("Temperature: %0.1f C" % temperature})
#     print("Humidity: %0.1f %%" % relative_humidity)
#     print("")
#     store_data(datetime.now().strftime('%y-%m-%d,%H:%M:%S,'),temperature,relative_humidity)
#     time.sleep(1)


while True:

    
    temperature, relative_humidity = tsl1.measurements
    tsl1.measurements1 ={
    "temperature":("Temperature: %0.1f C" % temperature),
    "Humidity":("Humidity: %0.1f %%" % relative_humidity),
    "timestamp":datetime.now().strftime('%y-%m-%d,%H:%M:%S,')

    
    }
    deviceId=1
    
    collection.update_one({'deviceId': deviceId,'nsamples':{'$lt':200}},
    {
        '$push':{'samples':tsl1.measurements1},
        '$inc':{'nsamples':1}
    },
    upsert=True

    )

    print("Temperature: %0.1f C" % temperature)
    print("Humidity: %0.1f %%" % relative_humidity)
    # print("")
    # store_data(datetime.now().strftime('%y-%m-%d,%H:%M:%S,'),temperature,relative_humidity)
    time.sleep(1)
