import RPi.GPIO as gpio
import time
#gpio.setmode(gpio.BOARD)
#gpio.setup(19,gpio.IN)

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setwarnings(False)
    gpio.setup(7,gpio.OUT)
    gpio.setup(11,gpio.OUT)
    gpio.setup(13,gpio.OUT)
    gpio.setup(15,gpio.OUT)
    gpio.setup(19,gpio.IN)    
    print "Gpio Initialized"

def forward(t):
    init()
    gpio.output(7,False)
    gpio.output(11,True)
    gpio.output(13,True)
    gpio.output(15,False)
    time.sleep(t)
    gpio.cleanup()

def reverse(t):
    init()
    gpio.output(7,True)
    gpio.output(11,False)
    gpio.output(13,False)
    gpio.output(15,True)
    time.sleep(t)
    gpio.cleanup()

def turn_right(t):
    init()
    gpio.output(7,False)
    gpio.output(11,False)
    gpio.output(13,False)
    gpio.output(15,True)
    time.sleep(t)
    gpio.cleanup()

def turn_left(t):
    init()
    gpio.output(7,True)
    gpio.output(11,True)
    gpio.output(13,True)
    gpio.output(15,False)
    time.sleep(t)
    gpio.cleanup()

def pivot_left(t):
    init()
    gpio.output(7,True)
    gpio.output(11,False)
    gpio.output(13,True)
    gpio.output(15,False)
    time.sleep(t)
    gpio.cleanup()

def pivot_right(t):
    init()
    gpio.output(7,False)
    gpio.output(11,True)
    gpio.output(13,False)
    gpio.output(15,True)
    time.sleep(t)
    gpio.cleanup()



while True:
      init()
#     if ( gpio.input(19) == True ):
#        forward(1)
#        print "here"
      command = raw_input("Enter command")
      if command == "w":
         print "test"
         forward(1)
         gpio.cleanup()
         continue
