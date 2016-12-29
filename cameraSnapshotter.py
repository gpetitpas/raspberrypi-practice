# Created 11/16/15

import os
import time

from twilio.rest import TwilioRestClient

# 1. Wait 1 minute
# 2. Take 1 picture every 30 seconds for 30 minutes
# 2a. Name every picture differently and put them in a separate folder
# 3. Stop the program

pictureCounter = "2"
osPictureCommand = "fswebcam snapshot" + pictureCounter + ".jpg"
#Takes a picture with the webcam
#os.system("fswebcam snapshot.jpg")
#os.system(osPictureCommand)

time.sleep(60)

for thirtySec in range(1, 60):
	osPictureCommand = "fswebcam snapshot" + str(thirtySec) + ".jpg"
	os.system(osPictureCommand)
	time.sleep(30)

print "Ending program"

# terminate the script (this might be unncessary)
quit()

