import numpy as np
import cv2
from pyzbar.pyzbar import decode
import datetime
import time

# open camera and scan the qr code
imgCap = cv2.VideoCapture(0)
imgCap.set(3, 640)
imgCap.set(4, 480)
camera = True
while camera == True:
    success, frame = imgCap.read()
    for code in decode(frame):
        personalData = code.data.decode("utf-8")
        time.sleep(3) #indicates when qr code is scanned
    cv2.imshow('Please Scan QR Code Here', frame)
    if cv2.waitKey(1) == ord("q"): #press q when done scanning
        break

# writing the file
qrData = personalData.split(" ", 1)
file = "".join(qrData[0].split())
# naming the file with the first word in the data so that it can scan another qr code w/o problem
qrFile = open(file + ".txt", "w")
qrFile.write(personalData + "\n")
# formatting and writing the date and time into the file
date = datetime.datetime.now()
qrFile.write("date and time accessed: " + date.strftime("%y-%m-%d %H:%M:%S"))
qrFile.close

cv2.destroyAllWindows
