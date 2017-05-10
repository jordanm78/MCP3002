from __future__ import division
import spidev



class MCP3002(object): #The MCP3002 class inherits from the object class

    def __init__(self, referenceVoltage = 5.0, SPIChannel = 0):
        #A subclass will read a config file and extract all relevant information

        self.SPIChannel = SPIChannel
        self.referenceVoltage = referenceVoltage
        

    def readChannel0(self):
        return(self.readData(1,0))

    def readChannel1(self):
        return(self.readData(1,1))

    def readDifferential(self):
        return(self.readData(0,0))


    def readData(self, singleEnded = 1, channel = 0):
        # This code is based on a program written by coderanger,
        # as well as a comment by Robert Mash, found at:
        # http://raspberry.io/projects/view/reading-from-a-mcp3002-analog-to-digital-converter/
        conn = spidev.SpiDev(0, self.SPIChannel)
        conn.max_speed_hz = 1200000 # 1.2 MHz
        

        #The first bit of the command is the start bit, it must always be 1
        #The second bit of the command is the single ended bit: 1 means single ended, 0 means pseudo-differential
        #The third bit of the command is the channel bit.  0 to read channel 0, 1 to read channel 1.
        cmd = 0b10000000 + 0b01000000*singleEnded + 0b00100000*channel

        
        reply_bytes = conn.xfer2([cmd, 0])
        reply_bitstring = ''.join(__bitstring(n) for n in reply_bytes)
        reply = reply_bitstring[5:15]  #reply is a number between 0 and 1023, where 0 represents 0 volts and 1023 represents the reference (supply) voltage.


        #To get a voltage, multiply the reply by the supply voltage, then divide by 1023
        #The int(string, base) interprets string as an integer with the specified base.
        return self.referenceVoltage*int(reply, 2) / 1023



    def __bitstring(n):
        s = bin(n)[2:]
        return '0'*(8-len(s)) + s

"""
if __name__ == '__main__':
    print readChannel0()
"""
