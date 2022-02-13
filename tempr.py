import time
import board
import adafruit_sht4x
import busio
import adafruit_sgp30

i2c = board.I2C()  # uses board.SCL and board.SDA
sht = adafruit_sht4x.SHT4x(i2c)
print("Found SHT4x with serial number", hex(sht.serial_number))

i2c = busio.I2C(board.SCL, board.SDA, frequency=100000) #SGP30
sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)

sht.mode = adafruit_sht4x.Mode.NOHEAT_HIGHPRECISION
# Can also set the mode to enable heater
# sht.mode = adafruit_sht4x.Mode.LOWHEAT_100MS
print("Current mode is: ", adafruit_sht4x.Mode.string[sht.mode])

while True:
    #SHT40
    temperature, relative_humidity = sht.measurements
    print("Temperature: %0.1f C" % temperature)
    print("Humidity: %0.1f %%" % relative_humidity)
    print("")


    #SGP30
    print("eCO2 = %d ppm \t TVOC = %d ppb" % (sgp30.eCO2, sgp30.TVOC))
    elapsed_sec += 1
    if elapsed_sec > 10:
        elapsed_sec = 0
        print(
            "**** Baseline values: eCO2 = 0x%x, TVOC = 0x%x"
            % (sgp30.baseline_eCO2, sgp30.baseline_TVOC)
        )





    time.sleep(1)


