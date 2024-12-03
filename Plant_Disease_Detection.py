import cv2
import numpy as np
import tflite_runtime.interpreter as tflite
import drivers
import RPi.GPIO as GPIO
import time
display = drivers.Lcd()

#loading model
interpreter = tflite.Interpreter(model_path='/home/eg1004/Desktop/leaf_link/model_updated.tflite')
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

#setting up camera
cap =cv2.VideoCapture(0)
if not cap.isOpened():
	print("Error: Camera could not be opened")

#capturing video and making predictions
while True:
	ret, frame = cap.read()
	if not ret:
		break
	
	#preprocessing
	image = cv2.resize(frame, (225, 225)) # resizing to image size of model
	image = image.astype(np.float32)/255.0 # normalizing images to [0,1]
	image = np.expand_dims(image, axis=0) # adding batch dimension
	
	#setting input
	interpreter.set_tensor(input_details[0]['index'], image)
	
	#run inferenece and get preditions
	interpreter.invoke()
	predictions = interpreter.get_tensor(output_details[0]['index'])
	predicted_class = np.argmax(predictions)

	#printing prediction on LCD
	if predicted_class ==1:
		display.lcd_display_string('Healthy', 1)
	elif predicted_class == 2:
		display.lcd_display_string('Powdery', 1)
	elif predicted_class == 3:
		display.lcd_display_string('Rust', 1)

	#print prediciton and captured image
	cv2.putText(frame, f'Predicted Class; {predicted_class}', (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
	cv2.imshow('Plant Disease Detection', frame)

	#stops program if 'q' is pressed on keyboard
	if cv2.waitKey(0):
		break

cap.release()
cv2.destroyAllWindows()

	
		
	
