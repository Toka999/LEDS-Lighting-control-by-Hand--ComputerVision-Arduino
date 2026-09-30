'''.........................pre-programming steps..................................................................
pyfirmata library: 
*its a library that connect arduino with python code
*it operates only with python version 3.7 or less
steps:
1]type in terminal pip3.7 install pyfirmata
2]open arduino ide --->file--->examples--->custom library--->pyfirmata--->standard pyfirmata--->upload to arduino
..................................................................................................................'''

import pyfirmata

comport='COM7'                   #change THE PORT 'COM7' with your port number

board=pyfirmata.Arduino(comport) #assign type of board used with pyfirmata (arduino)

#assign arduino pin number and state
led_1=board.get_pin('d:8:o')     # digital pin, 8,OUTPUT
led_2=board.get_pin('d:9:o')     # digital pin, 9,OUTPUT
led_3=board.get_pin('d:10:o')    # digital pin, 10,OUTPUT
led_4=board.get_pin('d:11:o')    # digital pin, 11,OUTPUT
led_5=board.get_pin('d:12:o')    # digital pin, 12,OUTPUT

#assign a function that tests the value stored in fingerUp to identify the output
def led(fingerUp):
    if fingerUp==[0,0,0,0,0]:
        led_1.write(0)            #digital wirte zero on led1
        led_2.write(0)            #digital wirte zero on led2
        led_3.write(0)            #digital wirte zero on led3
        led_4.write(0)            #digital wirte zero on led4
        led_5.write(0)            #digital wirte zero on led5

    elif fingerUp==[0,1,0,0,0]:
        led_1.write(1)            #digital wirte one on led1
        led_2.write(0)            #digital wirte zero on led2
        led_3.write(0)            #digital wirte zero on led3
        led_4.write(0)            #digital wirte zero on led4
        led_5.write(0)            #digital wirte zero on led5

    elif fingerUp==[0,1,1,0,0]:
        led_1.write(1)            #digital wirte one on led1
        led_2.write(1)            #digital wirte one on led2
        led_3.write(0)            #digital wirte zero on led3
        led_4.write(0)            #digital wirte zero on led4
        led_5.write(0)            #digital wirte zero on led5

    elif fingerUp==[0,1,1,1,0]:
        led_1.write(1)            #digital wirte one on led1
        led_2.write(1)            #digital wirte one on led2
        led_3.write(1)            #digital wirte one on led3
        led_4.write(0)            #digital wirte zero on led4
        led_5.write(0)            #digital wirte zero on led5

    elif fingerUp==[0,1,1,1,1]:
        led_1.write(1)            #digital wirte one on led1
        led_2.write(1)            #digital wirte one on led2
        led_3.write(1)            #digital wirte one on led3
        led_4.write(1)            #digital wirte one on led4
        led_5.write(0)            #digital wirte zero on led5
        
    elif fingerUp==[1,1,1,1,1]:
        led_1.write(1)            #digital wirte one on led1
        led_2.write(1)            #digital wirte one on led2
        led_3.write(1)            #digital wirte one on led3
        led_4.write(1)            #digital wirte one on led4
        led_5.write(1)            #digital wirte one on led5