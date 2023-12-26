import serial
from loguru import logger
import time


class Satelite:
    system = ""
    id = 0
    CN0 = 0



def send_command(string):
    cmd = '"' + string+"\r" + '"'
    ser.write(cmd.encode())
    time.sleep(0.1)
    ser.readline()
    response = ser.readline().decode()
    if response == "OK\r\n":
        logger.info(f"Command {string} accepted")
    else:
        logger.error(f"Command {string} encountered error")

def read_sentence():
    data = ""
    while True:
        char = ser.read().decode()
        if char == "$":
            data += char
            while True:
                char = ser.read().decode()
                data += char
                if char == "\n":
                    return data
    
def decode_header():
    code = ""
    for i in range (3,5):
        code += i
    if code == "GSV":
        pass


    

    

try:
    ser = serial.Serial('COM5', 9600, 8, 'N', 1, timeout=0)
    if ser.is_open:
        logger.info("Connected to comPort")
except:
    logger.error("Cannot open the port")


send_command("AT")  #test cmd
send_command("AT+CGNSPWR=1")    #turn on GNSS module
send_command("AT+CGNSTST=1,1")  #show NMEA data once
while True:
    tmp = read_sentence()
    print(tmp)

ser.close()


