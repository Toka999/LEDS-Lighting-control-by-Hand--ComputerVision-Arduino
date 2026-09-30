#import pyfirmata
#comport='COM7'
#board=pyfirmata.Arduino(comport)
'''import serial
ser = serial.Serial('COM7', 9600)

ledone=ser.write('d:2:o')
ledtwo=ser.write('d:3:o')
ledthree=ser.write('d:4:o')
ledfour=ser.write('d:5:o')
ledfive=ser.write('d:6:o')

ledone=board.get_pin('d:2:o')
ledtwo=board.get_pin('d:3:o')
ledthree=board.get_pin('d:4:o')
ledfour=board.get_pin('d:5:o')
ledfive=board.get_pin('d:6:o')

def led(fingers):
    if fingers==[0]:
        ledone.write('L')
        ledtwo.write('L')
        ledthree.write('L')
        ledfour.write('L')
        ledfive.write('L')
    elif fingers==[1]:
        ledone.write('H')
        ledtwo.write('L')
        ledthree.write('L')
        ledfour.write('L')
        ledfive.write('L')
    elif fingers==[2]:
        ledone.write('H')
        ledtwo.write('H')
        ledthree.write('L')
        ledfour.write('L')
        ledfive.write('L')
    elif fingers==[3]:
        ledone.write('H')
        ledtwo.write('H')
        ledthree.write('H')
        ledfour.write('L')
        ledfive.write('L')
    elif fingers==[4]:
        ledone.write('H')
        ledtwo.write('H')
        ledthree.write('H')
        ledfour.write('H')
        ledfive.write('L')
    elif fingers==[5]:
        ledone.write('H')
        ledtwo.write('H')
        ledthree.write('H')
        ledfour.write('H')
        ledfive.write('H')'''
import serial.tools.list_ports
ports=serial.tools.list_ports.comports()
serialINST=serial.Serial()
portsList=[]
for onePort in ports:
    portsList.append(str(onePort))
    print(str(onePort))
val= input("select port: COM")
for x in range(0,len(portsList)):
    if portsList[x].startswith("COM"+str(val)):
        portVar='COM'+str(val)
        print(portVar)
serialINST.baudrate=9600
serialINST.port=portVar
serialINST.open()