# import serial
# import sys
# from time import sleep
#
# try:
#   ser = serial.Serial("COM7", 9600,timeout=0, parity=serial.PARITY_NONE,
#                         stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)
# except:
#   sys.exit("Error connecting device")
#
# while True:
#   queue = ser.inWaiting()
#   if queue > 0:
#     data = ser.read(1000)
#     print(data)
#   sleep(0.2)

import serial
import sys
from time import sleep
import serial.tools.list_ports
ports = serial.tools.list_ports.comports()

for port, desc, hwid in sorted(ports):
        print("{}: {} [{}]".format(port, desc, hwid))
try:
    ser = serial.Serial("COM10", 9600, timeout=1, parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)
except serial.SerialException as e:
    sys.exit(f"Error connecting device: {e}")

while True:
    try:
        if ser.in_waiting:
            data = ser.read(ser.in_waiting)
            print(f"Received data: {data}")
    except serial.SerialException as e:
        print(f"Error reading data: {e}")

    sleep(0.1)
