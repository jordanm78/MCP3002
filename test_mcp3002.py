from __future__ import division
from mcp3002 import MCP3002
from random import random


class Test_MCP3002(MCP3002): #The test_MCP3002 class is an MCP3002

    def __init__(self, referenceVoltage = 5.0, SPIChannel = 0):
        super().__init__(referenceVoltage, SPIChannel)
        

    def readData(self, singleEnded = 1, channel = 0):

        #Generate and return a random number between 0 and 5
        return 5*random()


if __name__ == '__main__':
    tmcp = Test_MCP3002()
    print(tmcp.readChannel0())

