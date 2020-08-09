import cv2


cap=cv2.VideoCapture(0)
eyes_cascade=cv2.CascadeClassifier("./Train/third-party/frontalEyes35x16.xml")
nose_cascade=cv2.CascadeClassifier("./Train/third-party/Nose18x15.xml")
while True:
	ret, frame = cap.read()

	if ret==False:
		continue


	eyes=eyes_cascade.detectMultiScale(frame,1.3,5)
	nose=nose_cascade.detectMultiScale(frame,1.3,5)
	for (x,y,w,h) in nose:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
	for (x,y,w,h) in eyes:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),2)
	cv2.imshow("Video Frame", frame)

	key_pressed = cv2.waitKey(1) & 0xFF
	if key_pressed == ord('q'):
		break


cap.release()
cv2.destroyAllWindows()