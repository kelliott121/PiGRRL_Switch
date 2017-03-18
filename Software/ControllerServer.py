import serial
from uinput import *

class Controller:
	"""docstring for Controller"""

	NumButtons = 8

	def __init__(self, devName, devKeys):
		self.devPath = "/dev/" + devName
		try:
			print "Connecting to " + self.devPath
			self.serial = serial.Serial(self.devPath, 9600, timeout=10)
		except Exception as inst:
			print type(inst)     # the exception instance
			print inst.args      # arguments stored in .args
			print inst 
			print "Connection to " + self.devPath + " failed!"
			self.connected = False
		else:
			print "Connection to " + self.devPath + " successful!"
			self.connected = True

		self.devKeys = devKeys
		self.device = Device(devKeys)

ValidKeys = [	KEY_A, KEY_B, KEY_C, KEY_D, KEY_E, KEY_F, KEY_G, KEY_H, KEY_I, KEY_J,
				KEY_K, KEY_L, KEY_M, KEY_N, KEY_O, KEY_P, KEY_Q, KEY_R, KEY_S, KEY_T,
				KEY_U, KEY_V, KEY_W, KEY_X, KEY_Y, KEY_Z,]
ControllerNames = ["rfcomm0"]

Controllers = []

controllerNum = 0
for controllerName in ControllerNames:
	Controllers.append(Controller(controllerName, ValidKeys[controllerNum:((controllerNum*Controller.NumButtons) - 1)]))
	Controllers[controllerNum].serial.reset_input_buffer()
	controllerNum = controllerNum + 1

PrevPacket = {}
PrevPacket['K'] = '1' * Controller.NumButtons

while True:
	controllerNum = 0
	for controller in Controllers:
		line = controller.serial.readline()
		print line

		packet = line.split(':')
		if packet[0] == 'K':
			charNum = 0
			for char, prevChar in zip(packet[1], PrevPacket['K']):
				if (char == '0') and (prevChar == '1'):
					controller.device.emit(controller.devKeys[(controllerNum*Controller.NumButtons) + charNum], 1)
				elif (char == '1') and (prevChar == '0'):
					controller.device.emit(controller.devKeys[(controllerNum*Controller.NumButtons) + charNum], 0)
				charNum = charNum + 1
			PrevPacket['K'] = packet[1]
		elif packet[0] == 'A':
			pass
		elif packet[0] == 'B':
			pass

		controllerNum = controllerNum + 1
 
