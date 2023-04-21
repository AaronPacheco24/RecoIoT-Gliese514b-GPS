#!/usr/bin/env python3

import time
import serial
ser = serial.Serial('/dev/ttyS8', baudrate=9600, timeout=1)
while True:
    with open('/usr/bin/pythontext.txt','w') as file:
            file.write('')
            file.close
    line = ser.readlin().decod('utf-8')
    if line.startswith('$GNGGA'):
        print(line)
        with open('/usr/bin/pythontext.txt','w') as file:
            file.write(str(days_in_feb(year)))
            file.close
    time.sleep(5)