import board
import time
import busio
import adafruit_tca9548a
import adafruit_sht4x

import adafruit_sgp30

import adafruit_sht31d

import adafruit_scd30

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


    time.sleep(1)





    
