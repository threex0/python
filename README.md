# rpi-thermostat
HVAC/Thermostat Simulator for the Raspberry Pi

Ideally this program is to be used in tandem with an arduino 4-port relay, as well as an arduino thermostat/barometer, both of which can be interfaced into the Raspberry Pi's GPIO pins.

Configuration:
The script sets the GPIO pins to BCM mode, strictly a preference, but can be changed at the top of the file.
At the same point in the file the individual GPIO pins are set for the relays containing the following circuits in your closed cooling system:
- Compressor
- Indoor fan, high
- Indoor fan, low (on the same circuit as a heating element)

This script will run until quit, in order to constantly check the temperature of the room/area that it's in and adjust accordingly.  The script keeps track of how many iterations it has went through. You can also configure how often the script checks the temperature in a seconds-based interval in the config lines (defaulted to the maximum of every second).

Currently cooling and heating setpoints, and manual engagement of the fan part of the relay are set manually in the config at the top.  The long term vision is to be able to configure these via an SSH, command line argument, GUI, and ultimately also via web server with a website interface from a network, possibly also bluetooth/via web app.  The heating and cooling setpoints are in degrees celsius and that is specifically called out in the variable names and comments.  A current limitation of the prototype we are testing with, is that it uses the DHT-11 arduino sensor which has low accuracy on humidity and is only able to read a whole number in celsius.  Our next prototype (and what we recommend using if deploying this code) is a DHT-22 sensor (note to self, change line 23 of the code to make it a config and not hard-coded to allow changing the type of sensor and also allowing setting GPIO pins for temp sensor), the DHT-22 sensor has more accuarte humidity reading and allows for floating point precision on the temperature readings.

Currently this simulator uses AdafruitDHT.py which is a python wrapper for a C back-end that accesses the temperature from these sensors.  Due to their real-time nature they can't be accessed in python strictly (at least not in a timely manner leading to ocassional timeouts).

If the temperature is above the cooling setpoint, two relays are activated.
One relay is hooked up to a compressor for cooling, the second relay is hooked up to a fan to circulate the cold air.
If the temperature is below the cooling setpoint, the compressor and fan are disengaged UNLESS
The fan switch is also manually set to the on mode (as you often see on thermostats or AC's)

This script does constantly output feedback of the current temperature, humidy, whether or not the temperature is above or below the cooling setpoint or heating setpoint, which fans are on, if the heating element is on, and how many iterations the program has run through so far.

If the temperature is below the heating setpoint, the heating element and the low fan mode come on.  With both the compressor and the heating element, it is important the fan be inexorably linked, especially so with the heating element to prevent burnout or fires.  Due to this we have constructed our prototype so that the low fan is forced to be on the same relay/circuit as the heating element.

Our prototype used 110v power through three circuits.  Two circuits were run through a contactor that was wired into corresponding raspberry pi relays, and the heating element was wired just directly into a relay.  We also needed a couple step-down transformers to pull this off exactly as envisioned.

Our prototype works perfectly, using the Raspberry Pi as a stand-in for a complex HVAC circuit, using two fan motors and a lightbulb.  We were able to successfully change the temperature and the cooling setpoints manually and have the pieces of the HVAC circuit we built behave accordingly.

Here is our proof of concept:  https://www.youtube.com/watch?v=XtYMyyDnxeE&feature=youtu.be  
This is out-dated in that what we have now is an actual working prototype ready to plugin to a compressor, fan and heating element.  Currently I'm working on making this code have any kind of user interface, which will have a web front-end soon and will require installing LAMP on the Pi.  More to come.
