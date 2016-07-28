#  Import statements
import subprocess
import RPi.GPIO as GPIO
import time
import string

#  Assign GPIO pins to BCM numbering format
GPIO.setmode(GPIO.BCM)
#  Asign individual pins to compressor, fans, etc...
relayCompressor = 21
relayIndoorFanH = 26
relayIndoorFanL = 20

executed = 0 # A variable to count how often the script is executed)
sleep = 0  # Interval between readings in Seconds
setpointCool = 25 # Cooling setpoint in Celsius
setpointHeat = 22 # Heating setpoint in Celsius
coolingMode = 0 # Cooling mode On or Off in Boolean
heatingMode = 0 # Heating mode On or Off in Boolean
indoorFanOn = 0 # Manual mode for indoor fan On or Off in Boolean

while 1: #While loop, always evaluates to true to run process in infinite loop
	proc = subprocess.Popen(["/home/pi/Downloads/Adafruit_Python_DHT-master/examples/AdafruitDHT.py","11","16"],stdout=subprocess.PIPE)
	procS = proc.stdout.read()
	split = procS.split(' ')
	temp = split[0].split('=')
	
	humidity = split[2].split('=')
	print "Temperature: " + temp[1]
	print "Humidity: " + humidity[1]
	temp[1] = str(temp[1]).replace('*','')
	
	# Check if temperature is higher or lower than cooling set point
	# If temperature is above, engage cooling, if below, disengage
	if float(temp[1]) > setpointCool:
		print ("Temp greater than cooling setpoint " + str(setpointCool))
		coolingMode = 1
		GPIO.setup(relayCompressor,GPIO.OUT)
		GPIO.output(relayCompressor,GPIO.LOW)
		print ("Compressor engaged")
	else:
		print ("Temp not greater than cooling setpoint " + str(setpointCool))
		coolingMode = 0
		GPIO.setup(relayCompressor,GPIO.OUT)
		GPIO.output(relayCompressor,GPIO.HIGH)
		print ("Compressor disengaged")

	# Check if cooling mode/compressor or indoor fan switch is on
	# If so engage indoor fan
	if coolingMode == 1 or indoorFanOn == 1:
		if coolingMode == 1:
			GPIO.setup(relayIndoorFanH,GPIO.OUT)
			GPIO.output(relayIndoorFanH,GPIO.LOW)
			print ("Compressor on, indoor fan engaged")
		else:
			GPIO.setup(relayIndoorFanH,GPIO.OUT)
			GPIO.output(relayIndoorFanH,GPIO.LOW)
			print ("Indoor fan is switched on, indoor fan engaged")
	else:
		print ("Neither compressor nor fan switch is on")
		GPIO.setup(relayIndoorFanH,GPIO.OUT)
		GPIO.output(relayIndoorFanH,GPIO.HIGH)
		print ("Indoor fan disengaged")

	# Check if temperature is below heating set point
	# If so engage heating/fan
	if float(temp[1]) < setpointHeat:
		print ("Temperature below heating set point")
		GPIO.setup(relayIndoorFanL,GPIO.OUT)
		GPIO.output(relayIndoorFanL,GPIO.LOW)
		print ("Heating engaged")
		print ("Indoor fan engaged")
	else:
		print ("Temperature above heating set point")
		GPIO.setup(relayIndoorFanL,GPIO.OUT)
		GPIO.output(relayIndoorFanL,GPIO.HIGH)
		print ("Heating disengaged")
		print ("Indoor fan disengaged")

	executed = executed + 1	
	print ("Executed: " + str(executed) + " times\n")
	if sleep > 0:
		time.sleep(sleep)
