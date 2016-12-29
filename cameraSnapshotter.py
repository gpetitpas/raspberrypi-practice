# Created 11/16/15

import os
import time

from twilio.rest import TwilioRestClient

# 1. Wait 10 minutes
# 2. Take 1 picture every 30 seconds for 30 minutes
# 2a. Name every picture differently and put them in a separate folder
# 3. Stop the program

pictureCounter = "2"
osPictureCommand = "fswebcam snapshot" + pictureCounter + ".jpg"
#Takes a picture with the webcam
#os.system("fswebcam snapshot.jpg")
os.system(osPictureCommand)

