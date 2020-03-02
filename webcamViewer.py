import cv2
import datetime

print("This is a webcam viewer...")



# Open the device at the ID 2

cap = cv2.VideoCapture(2)

#Check whether user selected camera is opened successfully.

if not (cap.isOpened()):

	print("Could not open video device")


while(True):

	# Capture frame-by-frame

	ret, frame = cap.read()

	# Display the resulting frame

	cv2.imshow("preview",frame)

	#Waits for a user input to quit the application
	key = cv2.waitKey(1)

	if key == ord('q'):

		break
	if key == ord('s'):

		#Get a timestamp
		myTime = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
		print(myTime)
		fileName = "capture_{}.jpeg".format(myTime)
		print(fileName)		
		cv2.imwrite(fileName,frame)

# When everything done, release the capture

cap.release()

cv2.destroyAllWindows()
