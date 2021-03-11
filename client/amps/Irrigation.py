import gpiozero
from gpiozero import DigitalOutputDevice
import time


#   IRGMainPump, IRGWtrPump, IRGTrnsPump, IRGNutrPump ,
            # IRGlvl1Sol, IRGlvl2Sol, IRGlvl3Sol, IRGlvl4Sol, IRGlvl5Sol



class Irrigation():
    def __init__(self,gpioMainPump, gpioWtrPump,gpioTrnsPump, gpioNutrPump,
                gpiolvl1Sol, gpiolvl2Sol, gpiolvl3Sol, gpiolvl4Sol, gpiolvl5Sol): #add level sensor GOPIO and level Sensor Input



        self.IRGMainPump = DigitalOutputDevice(gpioMainPump)
        self.IRGWtrPump = DigitalOutputDevice(gpioWtrPump)
        self.IRGTrnsPump = DigitalOutputDevice(gpioTrnsPump)
        self.IRGNutrPump = DigitalOutputDevice(gpioNutrPump)
        self.IRGlvl1Sol = DigitalOutputDevice(gpiolvl1Sol)
        self.IRGlvl2Sol = DigitalOutputDevice(gpiolvl2Sol)
        self.IRGlvl3Sol = DigitalOutputDevice(gpiolvl3Sol)
        self.IRGlvl4Sol = DigitalOutputDevice(gpiolvl4Sol)
        self.IRGlvl5Sol = DigitalOutputDevice(gpiolvl5Sol)
        self.IRGPumps = [self.IRGMainPump,self.IRGWtrPump,self.IRGTrnsPump,self.IRGNutrPump]

    def waterCycle(self, cycleTime):
        self.IRGMainPump.on()
        time.sleep(1)
        self.IRGWtrPump()
        time.sleep(1)
        for pump in self.IRGPumps:
            pump.on()
            time.sleep(cycleTime)
            pump.off()
        time.sleep(1)
        self.IRGWtrPump.off()
        time.sleep(1)
        self.IRGMainPump.off()

    def nutrientCycle(self,cycleTime):
        self.IRGMainPump.on()
        time.sleep(1)
        self.IRGNutrPump()
        time.sleep(1)
        for pump in self.IRGPumps:
            pump.on()
            time.sleep(cycleTime)
            pump.off()
        time.sleep(1)
        self.IRGNutrPump.off()
        time.sleep(1)
        self.IRGMainPump.off()




Wtring =Irrigation(gpioMainPump=14, gpioWtrPump=15,gpioTrnsPump=18, gpioNutrPump=23,
                gpiolvl1Sol=24, gpiolvl2Sol=25, gpiolvl3Sol=8, gpiolvl4Sol=7, gpiolvl5Sol=1)

Wtring.waterCycle(0.1)