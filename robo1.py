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
    gpio.setup(22,gpio.IN)
    gpio.setup(21,gpio.IN)
    gpio.setup(23,gpio.IN)    
    print "Gpio Initialized"

def forward(t):
    gpio.output(7,False)
    gpio.output(11,True)
    gpio.output(13,True)
    gpio.output(15,False)
    time.sleep(t)
    gpio.cleanup()
    init()
    clean_gpio()

def reverse(t):
    gpio.output(7,True)
    gpio.output(11,False)
    gpio.output(13,False)
    gpio.output(15,True)
    time.sleep(t)
    gpio.cleanup()
    init()
    clean_gpio()
   
def turn_right(t):
    gpio.output(7,False)
    gpio.output(11,False)
    gpio.output(13,False)
    gpio.output(15,True)
    time.sleep(t)
    gpio.cleanup()
    init()
    clean_gpio()

def turn_left(t):
    gpio.output(7,True)
    gpio.output(11,True)
    gpio.output(13,True)
    gpio.output(15,False)
    time.sleep(t)
    gpio.cleanup()
    init()
    clean_gpio()

def pivot_left(t):
    gpio.output(7,True)
    gpio.output(11,False)
    gpio.output(13,True)
    gpio.output(15,False)
    time.sleep(t)
    gpio.cleanup()
    init()
    clean_gpio()

def pivot_right(t):
    gpio.output(7,False)
    gpio.output(11,True)
    gpio.output(13,False)
    gpio.output(15,True)
    time.sleep(t)
    gpio.cleanup()
    init()
    clean_gpio()

def clean_gpio():
    gpio.output(7,False)
    gpio.output(11,False)
    gpio.output(13,False)
    gpio.output(15,False)

init()
while True:
      #init()
      if ( gpio.input(19) == True ):
         forward(0.2)
         print "forward here"
      elif (gpio.input(21) == True):
         reverse(0.2)
         print "reverse"
      elif (gpio.input(23) == True):
         turn_left(0.2)
         print "left"
      elif (gpio.input(22) == True):
         turn_right(0.2)
         print "right"   
#    continue 
